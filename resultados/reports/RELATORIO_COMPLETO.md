# 📊 RELATÓRIO COMPLETO DE FAIRNESS - ENEM 2024

**Data de Geração**: 2025-11-05 12:55:42

---

## 📈 RESUMO EXECUTIVO

### Dados Analisados
- **Total de participantes completos**: 2,302,906
- **Registros na análise**: 2,274,981 (100% dos dados - sem amostragem)
- **Critério**: Presença em todas as provas + redação corrigida + não-treineiro

### Estatísticas Gerais
- **Nota Média Geral**: 547.59 ± 84.03
- **Taxa de Aprovação (≥600)**: 26.81%
- **Taxa de Alta Performance (≥700)**: 4.60%
- **Taxa de Excelência (≥750)**: 1.02%

---

## 1️⃣ ANÁLISE POR RAÇA/COR

### Disparidades Máximas (max - min)
- **média**: 0.61 pontos
- **mediana**: 0.92 pontos
- **desvio**: 0.40 pontos
- **Q1**: 0.54 pontos
- **Q3**: 0.64 pontos
- **P10**: 0.47 pontos
- **P90**: 2.33 pontos
- **IQR**: 1.13 pontos
- **CV**: 0.00 pontos

### Demographic Parity (Aprovação ≥600)
- **Diferença**: 0.0015 (0.15 pp)
- **Razão**: 0.9944 ✅ PASS

---

## 2️⃣ ANÁLISE POR SEXO

### Disparidades Máximas
- **média**: 0.17 pontos
- **mediana**: 0.20 pontos
- **desvio**: 0.19 pontos
- **Q1**: 0.04 pontos
- **Q3**: 0.30 pontos
- **P10**: 0.16 pontos
- **P90**: 0.52 pontos
- **IQR**: 0.26 pontos
- **CV**: 0.00 pontos

---

## 3️⃣ ANÁLISE POR REGIÃO

### Disparidades Máximas
- **média**: 0.46 pontos
- **mediana**: 0.74 pontos
- **desvio**: 0.24 pontos
- **Q1**: 0.44 pontos
- **Q3**: 0.70 pontos
- **P10**: 0.34 pontos
- **P90**: 0.90 pontos
- **IQR**: 0.86 pontos
- **CV**: 0.00 pontos

---

## 4️⃣ ANÁLISE INTERSECCIONAL

**Gap Máximo (Raça × Sexo)**: 1.90 pontos

---

## 📊 ARQUIVOS GERADOS

### Gráficos (10 visualizações)
1-10. Dashboards, heatmaps, distribuições, extremos, correlações

### Tabelas (7 arquivos CSV)
1-7. Estatísticas completas por atributo sensível e interseccionalidade

---

## 🎯 CONCLUSÕES

### Achados Principais

1. **Disparidades Raciais**: Diferença máxima de 0.61 pontos
2. **Disparidades de Gênero**: Diferença de 0.17 pontos
3. **Disparidades Regionais**: Diferença máxima de 0.46 pontos
4. **Interseccionalidade**: Gap de 1.90 pontos entre extremos

### Melhorias Implementadas
- ✅ 100% dos dados utilizados (sem amostragem)
- ✅ Processamento otimizado com tipos eficientes
- ✅ 10 visualizações completas (vs 6 anteriores)
- ✅ 9 métricas personalizadas Fairlearn
- ✅ Análise de extremos, quartis e decis
- ✅ Organização de arquivos em subpastas

---

**Código-fonte**: `analise_fairness_completa.py`  
**Tempo de execução**: ~13.4 minutos
