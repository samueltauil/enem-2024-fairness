# 🔧 Solução de Problemas - Download de Dados

## ℹ️ Informações Importantes

### 📁 Estrutura de Diretórios Automática

O projeto utiliza uma abordagem **"repositório limpo"**:

- ✅ **Versionado**: Apenas código-fonte, documentação e configuração
- ❌ **Não versionado**: Dados, resultados e arquivos temporários

**Os diretórios `dados/`, `downloads/` e `resultados/` são criados automaticamente pelos scripts.**

Se você clonou o repositório e não vê estes diretórios, é **normal**! Execute:

```bash
python download_dados.py  # Cria dados/ com todos os subdiretorios
python analise_fairness_completa.py  # Cria resultados/
```

---

## ❌ Problemas Comuns e Soluções

### 1. Erro: "URL do INEP não acessível"

**Causa**: A URL de download do INEP pode ter mudado.

**Solução**:
1. Acesse manualmente: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem
2. Localize o link de download dos **Microdados ENEM 2024**
3. Atualize a variável `ENEM_2024_URL` no arquivo `download_dados.py` (linha 25)

```python
# Atualizar esta linha com a URL correta:
ENEM_2024_URL = "https://download.inep.gov.br/microdados/microdados_enem_2024.zip"
```

---

### 2. Erro: "Dependências faltando (requests, tqdm)"

**Causa**: Bibliotecas de download não instaladas.

**Solução**:
```bash
pip install requests tqdm
```

---

### 3. Erro: "Espaço insuficiente em disco"

**Causa**: O download requer ~2.5 GB temporários + ~2.3 GB finais.

**Solução**:
- Libere pelo menos **5 GB** de espaço em disco
- Ou baixe manualmente e extraia direto em `dados/DADOS/`

---

### 4. Download muito lento ou travando

**Causa**: Conexão instável ou servidor INEP sobrecarregado.

**Soluções**:

**Opção A: Tentar em outro horário**
```bash
# Servidor INEP costuma estar mais rápido entre 22h-6h
python download_dados.py
```

**Opção B: Download manual via navegador**
1. Abra: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem
2. Clique no link **Microdados ENEM 2024** (arquivo ZIP)
3. Aguarde download completo no navegador (mais estável)
4. Extraia manualmente os arquivos CSV para `dados/DADOS/`

**Opção C: Usar gerenciador de downloads**
- Windows: [Free Download Manager](https://www.freedownloadmanager.org/)
- Linux/Mac: `wget` ou `curl`

```bash
# Exemplo com wget
wget https://download.inep.gov.br/microdados/microdados_enem_2024.zip -P downloads/
```

---

### 5. Arquivo ZIP corrompido após download

**Causa**: Download incompleto ou interrompido.

**Solução**:
```bash
# Deletar arquivo corrompido
rm downloads/microdados_enem_2024.zip

# Baixar novamente
python download_dados.py
```

---

### 6. Arquivos CSV não encontrados após extração

**Causa**: Estrutura interna do ZIP pode ter mudado.

**Solução Manual**:

1. Abra o arquivo ZIP manualmente:
   ```
   downloads/microdados_enem_2024.zip
   ```

2. Localize e extraia **apenas** estes arquivos:
   - `PARTICIPANTES_2024.csv`
   - `RESULTADOS_2024.csv`
   - `ITENS_PROVA_2024.csv` (opcional)

3. Copie para:
   ```
   dados/DADOS/
   ```

4. Verifique a estrutura final:
   ```
   dados/
   └── DADOS/
       ├── PARTICIPANTES_2024.csv  (440 MB)
       ├── RESULTADOS_2024.csv     (1.6 GB)
       └── ITENS_PROVA_2024.csv    (opcional)
   ```

---

## ✅ Verificação Manual

Para verificar se os arquivos estão corretos:

```python
import pandas as pd

# Testar carregamento (primeiras 5 linhas)
participantes = pd.read_csv('dados/DADOS/PARTICIPANTES_2024.csv', 
                            sep=';', encoding='latin1', nrows=5)
print("✅ PARTICIPANTES OK")

resultados = pd.read_csv('dados/DADOS/RESULTADOS_2024.csv', 
                         sep=';', encoding='latin1', nrows=5)
print("✅ RESULTADOS OK")

print("\n🎉 Arquivos prontos para análise!")
```

---

## 🆘 Ainda com problemas?

1. **Verifique requisitos mínimos**:
   - Python 3.8+
   - 5 GB de espaço em disco
   - Conexão estável de internet (para download)

2. **Consulte Issues no GitHub**:
   - Abra uma issue descrevendo o problema
   - Inclua mensagem de erro completa
   - Mencione sistema operacional e versão do Python

3. **Alternativa**: Baixar diretamente do INEP via navegador
   - Mais lento, mas mais estável
   - Link direto: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

---

## 📧 Suporte

Para problemas técnicos:
- Abra uma [Issue no GitHub](https://github.com/SEU_USUARIO/enem-2024-fairness/issues)
- Ou consulte a [documentação oficial do INEP](https://www.gov.br/inep/)
