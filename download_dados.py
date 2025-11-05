"""
Script de Download Automático - Microdados ENEM 2024
====================================================

Baixa e extrai automaticamente os microdados do ENEM 2024 do site oficial do INEP.

Fonte: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem
"""

import os
import sys
import time
import zipfile
import requests
from pathlib import Path
from tqdm import tqdm

print("="*80)
print("📥 DOWNLOAD AUTOMÁTICO - MICRODADOS ENEM 2024")
print("="*80)
print("\nFonte: INEP - Instituto Nacional de Estudos e Pesquisas Educacionais")
print("URL: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem")
print("="*80)

# ============================================================================
# CONFIGURAÇÃO
# ============================================================================

# URL direta do arquivo ZIP
ENEM_2024_URL = "https://download.inep.gov.br/microdados/microdados_enem_2024.zip"

# Diretórios
DOWNLOAD_DIR = Path("downloads")
DATA_DIR = Path("dados/DADOS")

# Criar diretórios se não existirem
DOWNLOAD_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

ZIP_FILE = DOWNLOAD_DIR / "microdados_enem_2024.zip"

# ============================================================================
# FUNÇÕES
# ============================================================================

def download_file(url: str, destination: Path, max_retries: int = 3) -> bool:
    """
    Baixa arquivo com barra de progresso e retry automático.
    
    Args:
        url: URL do arquivo
        destination: Caminho de destino
        max_retries: Número máximo de tentativas
        
    Returns:
        True se sucesso, False caso contrário
    """
    for attempt in range(max_retries):
        try:
            print(f"\n📡 Conectando ao servidor INEP... (Tentativa {attempt + 1}/{max_retries})")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            # Primeiro, obter informações sobre o arquivo
            head_response = requests.head(url, headers=headers, timeout=30)
            head_response.raise_for_status()
            total_size = int(head_response.headers.get('content-length', 0))
            
            print(f"📦 Tamanho do arquivo: {total_size / (1024**3):.2f} GB")
            print(f"💾 Salvando em: {destination}")
            
            # Fazer o download
            response = requests.get(url, headers=headers, stream=True, timeout=60)
            response.raise_for_status()
            
            with open(destination, 'wb') as f, tqdm.tqdm(
                desc=f"Baixando (Tentativa {attempt + 1})",
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
            ) as pbar:
                for chunk in response.iter_content(chunk_size=32768):  # Chunks maiores
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))
            
            print(f"✅ Download concluído: {destination.name}")
            return True
            
        except (requests.exceptions.ConnectionError, 
                requests.exceptions.Timeout,
                requests.exceptions.ChunkedEncodingError) as e:
            print(f"⚠️  Erro de conexão na tentativa {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 5  # Espera progressiva: 5s, 10s, 15s
                print(f"🔄 Aguardando {wait_time}s antes da próxima tentativa...")
                time.sleep(wait_time)
                # Remove arquivo parcial se existir
                if destination.exists():
                    destination.unlink()
            else:
                print(f"❌ Falhou após {max_retries} tentativas")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao baixar: {e}")
            return False
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return False


def extract_zip(zip_path: Path, extract_to: Path) -> bool:
    """
    Extrai arquivo ZIP com barra de progresso.
    
    Args:
        zip_path: Caminho do arquivo ZIP
        extract_to: Diretório de destino
        
    Returns:
        True se sucesso, False caso contrário
    """
    try:
        print(f"\n📂 Extraindo arquivos para: {extract_to}")
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            members = zip_ref.namelist()
            
            # Filtrar apenas CSVs relevantes
            csv_files = [m for m in members if m.endswith('.csv') and 
                        ('PARTICIPANTES' in m.upper() or 'RESULTADOS' in m.upper() or 'ITENS_PROVA' in m.upper())]
            
            print(f"📋 Arquivos CSV encontrados: {len(csv_files)}")
            
            for member in tqdm.tqdm(csv_files, desc="Extraindo", unit="arquivo"):
                # Extrair apenas o nome do arquivo (sem subpastas)
                filename = os.path.basename(member)
                
                # Ler e salvar diretamente em DATA_DIR
                source = zip_ref.open(member)
                target = extract_to / filename
                
                with open(target, 'wb') as f:
                    f.write(source.read())
                
                print(f"  ✅ {filename}")
        
        print(f"\n✅ Extração concluída!")
        return True
        
    except zipfile.BadZipFile:
        print(f"❌ Erro: Arquivo ZIP corrompido")
        return False
    except Exception as e:
        print(f"❌ Erro ao extrair: {e}")
        return False


def verify_files() -> bool:
    """
    Verifica se os arquivos essenciais foram extraídos.
    
    Returns:
        True se todos arquivos estão presentes
    """
    print("\n🔍 Verificando arquivos extraídos...")
    
    required_files = [
        'PARTICIPANTES_2024.csv',
        'RESULTADOS_2024.csv',
        'ITENS_PROVA_2024.csv'
    ]
    
    all_present = True
    for filename in required_files:
        filepath = DATA_DIR / filename
        if filepath.exists():
            size_mb = filepath.stat().st_size / (1024**2)
            print(f"  ✅ {filename} ({size_mb:.2f} MB)")
        else:
            print(f"  ❌ {filename} (não encontrado)")
            all_present = False
    
    return all_present


# ============================================================================
# EXECUÇÃO PRINCIPAL
# ============================================================================

def main():
    print("\n🚀 Iniciando download dos Microdados ENEM 2024...\n")
    
    # Verificar se já existe
    if ZIP_FILE.exists():
        print(f"⚠️  Arquivo ZIP já existe: {ZIP_FILE}")
        response = input("Deseja baixar novamente? (s/N): ").strip().lower()
        
        if response != 's':
            print("⏭️  Pulando download...")
        else:
            print("🗑️  Removendo arquivo antigo...")
            ZIP_FILE.unlink()
            
            # Download
            if not download_file(ENEM_2024_URL, ZIP_FILE):
                print("\n❌ Falha no download. Verifique:")
                print("   1. Conexão com a internet")
                print("   2. URL do INEP (pode ter mudado)")
                print("   3. Espaço em disco disponível (~2.5 GB)")
                sys.exit(1)
    else:
        # Download
        if not download_file(ENEM_2024_URL, ZIP_FILE):
            print("\n❌ Falha no download. Verifique:")
            print("   1. Conexão com a internet")
            print("   2. URL do INEP (pode ter mudado)")
            print("   3. Espaço em disco disponível (~2.5 GB)")
            sys.exit(1)
    
    # Extrair
    if not extract_zip(ZIP_FILE, DATA_DIR):
        print("\n❌ Falha na extração.")
        sys.exit(1)
    
    # Verificar
    if not verify_files():
        print("\n⚠️  Alguns arquivos essenciais não foram encontrados!")
        print("   Verifique manualmente em: dados/DADOS/")
        sys.exit(1)
    
    # Limpar (opcional)
    print("\n🗑️  Deseja remover o arquivo ZIP para economizar espaço? (~2.5 GB)")
    response = input("Remover ZIP? (S/n): ").strip().lower()
    
    if response != 'n':
        ZIP_FILE.unlink()
        print(f"✅ Arquivo ZIP removido: {ZIP_FILE}")
    else:
        print(f"📦 Arquivo ZIP mantido: {ZIP_FILE}")
    
    # Sucesso
    print("\n" + "="*80)
    print("✅ CONFIGURAÇÃO CONCLUÍDA!")
    print("="*80)
    print("\n📊 Você já pode executar a análise:")
    print("   python analise_fairness_completa.py")
    print("\n⏱️  Tempo estimado: ~5-8 minutos")
    print("="*80)


if __name__ == "__main__":
    try:
        # Verificar dependências
        try:
            import tqdm
            import requests
        except ImportError:
            print("\n❌ Dependências faltando!")
            print("\nInstale com:")
            print("   pip install requests tqdm")
            sys.exit(1)
        
        main()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Download cancelado pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)
