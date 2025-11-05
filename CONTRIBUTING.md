# 🤝 Guia de Contribuição

Obrigado por considerar contribuir para o projeto **ENEM Fairness Analysis**! 

## 🎯 Como Posso Contribuir?

### 🐛 Reportar Bugs

Se encontrar um bug:
1. Verifique se já não foi reportado nas [Issues](https://github.com/SEU_USUARIO/enem-2024-fairness/issues)
2. Abra uma nova issue com:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs observado
   - Ambiente (Python version, OS, etc.)

### 💡 Sugerir Melhorias

Para sugestões de features:
1. Abra uma issue com label `enhancement`
2. Descreva claramente:
   - O problema que a feature resolveria
   - Como você imagina a solução
   - Possíveis alternativas

### 🔧 Pull Requests

1. **Fork** o repositório
2. **Clone** seu fork: `git clone https://github.com/SEU_USUARIO/enem-2024-fairness.git`
3. **Crie uma branch**: `git checkout -b feature/MinhaFeature`
4. **Faça suas mudanças** seguindo o guia de estilo
5. **Teste** suas mudanças
6. **Commit**: `git commit -m 'feat: Adiciona análise temporal'`
7. **Push**: `git push origin feature/MinhaFeature`
8. **Abra um Pull Request** com descrição detalhada

## 📝 Guia de Estilo

### Código Python

- Siga **PEP 8**
- Use **type hints** quando possível
- Docstrings no formato **Google Style**
- Máximo 100 caracteres por linha
- Nomes descritivos em **português** (variáveis de domínio)

```python
def calcular_disparidade_raca(
    notas: pd.Series,
    raca: pd.Series
) -> Dict[str, float]:
    """
    Calcula disparidade de notas por raça/cor.
    
    Args:
        notas: Série com notas dos candidatos
        raca: Série com raça/cor (1-6)
        
    Returns:
        Dicionário com estatísticas de disparidade
    """
    pass
```

### Commits

Siga [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Apenas documentação
- `style:` Formatação (sem mudança de lógica)
- `refactor:` Refatoração de código
- `perf:` Melhoria de performance
- `test:` Adição de testes
- `chore:` Manutenção (build, CI, etc.)

**Exemplos**:
```
feat: Adiciona análise de DIF por item
fix: Corrige cálculo de demographic parity
docs: Atualiza README com novos gráficos
perf: Otimiza carregamento com dtypes explícitos
```

## 🧪 Testes

Antes de submeter PR:

1. **Teste o script principal**:
   ```bash
   python analise_fairness_completa.py
   ```

2. **Valide os outputs**:
   - 10 gráficos gerados em `resultados/graficos/`
   - 7 tabelas em `resultados/tabelas/`
   - 1 relatório em `resultados/reports/`

3. **Verifique erros de sintaxe**:
   ```bash
   python -m py_compile analise_fairness_completa.py
   ```

## 📚 Áreas Prioritárias

### 🔥 High Priority
- [ ] Análise temporal (2018-2024)
- [ ] Dashboard interativo (Streamlit)
- [ ] Controles socioeconômicos (Q001-Q025)
- [ ] Análise de DIF (Differential Item Functioning)

### 🌟 Medium Priority
- [ ] Análise causal (matching, IV)
- [ ] Testes estatísticos adicionais
- [ ] Comparação com PISA/SAT
- [ ] Análise regional granular (municipal)

### 💡 Low Priority
- [ ] Exportação para formatos alternativos (Excel, Parquet)
- [ ] Múltiplos idiomas (EN, ES)
- [ ] Análise de clusters

## 📊 Dados

Ao trabalhar com dados:

- **Nunca** commite arquivos CSV grandes (>10MB)
- Use `.gitignore` para excluir dados brutos
- Documente fonte e processo de obtenção
- Respeite privacidade (dados já são anonimizados)

## 🤔 Dúvidas?

- Abra uma [Issue](https://github.com/SEU_USUARIO/enem-2024-fairness/issues) com label `question`
- Ou envie email para [SEU_EMAIL]

---

**Obrigado por contribuir! 🎉**
