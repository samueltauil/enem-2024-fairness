# 🚀 Início Rápido

Este projeto utiliza uma abordagem de **repositório limpo** - apenas código e documentação são versionados.

## 📋 Passo a Passo

### 1. Clone o repositório
```bash
git clone https://github.com/samueltauil/enem-2024-fairness.git
cd enem-2024-fairness
```

### 2. Instale dependências
```bash
pip install -r requirements.txt
```

### 3. Baixe os dados (automático)
```bash
python download_dados.py
```
Este script criará:
- `dados/` - Todos os arquivos do INEP (2+ GB)
- `downloads/` - Arquivos temporários (removidos automaticamente)

### 4. Execute a análise
```bash
python analise_fairness_completa.py
```
Este script criará:
- `resultados/graficos/` - Visualizações PNG
- `resultados/tabelas/` - Análises CSV  
- `resultados/reports/` - Relatórios Markdown

## 🔍 Verificação

Após a execução completa, sua estrutura será:
```
enem-2024-fairness/
├── 📁 dados/          # ← Criado por download_dados.py
├── 📁 resultados/     # ← Criado por analise_fairness_completa.py
├── 📜 *.py           # ← Scripts (versionados)
└── 📚 docs/          # ← Documentação (versionada)
```

## ⚠️ Importante

- **Primeira execução**: Execute os scripts na ordem (download → análise)
- **Re-execução**: Pode executar `analise_fairness_completa.py` quantas vezes quiser
- **Limpeza**: Diretórios `dados/` e `resultados/` podem ser removidos sem problemas

---

💡 **Dúvidas?** Consulte [TROUBLESHOOTING.md](TROUBLESHOOTING.md)