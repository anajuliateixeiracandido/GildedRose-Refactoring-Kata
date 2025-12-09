# Relatório de Teste de Mutação - Gilded Rose

**Data:** 09 de dezembro de 2025  
**Ferramenta:** MutPy 0.6.1  
**Módulo testado:** `gilded_rose.py`  
**Suite de testes:** `tests.test_gilded_rose`

---

## 📊 Resumo Executivo

### Score de Mutação: **100.0%** ✅

- **Total de mutantes gerados:** 20
- **Mutantes mortos:** 20 (100.0%)
- **Mutantes sobreviventes:** 0 (0.0%)
- **Mutantes incompetentes:** 0 (0.0%)
- **Timeouts:** 0 (0.0%)

### Tempo de Execução
- **Execução dos testes:** 0.593 s
- **Tempo total:** 4.5 s

---

## 🎯 Análise de Qualidade

### Cobertura de Testes
O score de **100%** indica que a suite de testes possui **qualidade excepcional**:

✅ **Todos os 38 testes** executados com sucesso  
✅ **Todas as mutações detectadas** pelos testes  
✅ **Zero mutantes sobreviventes** - nenhuma falha na detecção de bugs  
✅ **Sem timeouts** - testes eficientes e rápidos

### Operadores de Mutação Aplicados

O MutPy aplicou os seguintes operadores de mutação no código:

| Operador | Descrição | Quantidade |
|----------|-----------|------------|
| **ASR** | Assignment Operator Replacement | 3 mutantes |
| **COI** | Conditional Operator Insertion | 7 mutantes |
| **ROR** | Relational Operator Replacement | 10 mutantes |

#### Detalhamento por Operador:

**1. ASR (Assignment Operator Replacement)**
- Mutantes #1, #2, #3
- Linhas: 122, 131, 139
- Substitui operadores de atribuição (+=, -=, etc.)
- **Status:** Todos mortos ✅

**2. COI (Conditional Operator Insertion)**
- Mutantes #4-10
- Linhas: 63, 77, 94, 97, 102, 121, 130
- Insere ou remove operadores condicionais
- **Status:** Todos mortos ✅

**3. ROR (Relational Operator Replacement)**
- Mutantes #11-20
- Linhas: 94, 97, 121, 130, 150
- Substitui operadores relacionais (<, <=, >, >=, ==, !=)
- **Status:** Todos mortos ✅

---

## 📈 Distribuição de Mutantes por Teste

### Testes que Mataram Mutantes

Os testes mais efetivos na detecção de mutações foram:

1. **`test_multiple_items_update_independently`** - 4 mutantes mortos
2. **`test_aged_brie_after_sell_date`** - 6 mutantes mortos
3. **`test_backstage_pass_10_days_or_less`** - 5 mutantes mortos
4. **`test_backstage_pass_crosses_10_day_threshold`** - 1 mutante morto
5. **`test_backstage_pass_crosses_5_day_threshold`** - 1 mutante morto
6. **`test_aged_brie_quality_49_after_sell`** - 1 mutante morto
7. **`test_normal_item_quality_1_after_sell_date`** - 1 mutante morto
8. **`test_backstage_pass_1_day_before_concert`** - 1 mutante morto

---

## 🔍 Detalhes dos Mutantes

### Mutantes de Alta Complexidade (>20 testes executados)

| # | Operador | Linha | Testes | Duração | Teste que Matou |
|---|----------|-------|--------|---------|-----------------|
| 2 | ASR | 131 | 26 | 0.182s | test_multiple_items_update_independently |
| 4 | COI | 63 | 26 | 0.168s | test_multiple_items_update_independently |
| 10 | COI | 130 | 26 | 0.174s | test_multiple_items_update_independently |

### Mutantes de Baixa Complexidade (1 teste executado)

| # | Operador | Linha | Duração | Teste que Matou |
|---|----------|-------|---------|-----------------|
| 1 | ASR | 122 | 0.136s | test_aged_brie_after_sell_date |
| 3 | ASR | 139 | 0.148s | test_aged_brie_after_sell_date |
| 5 | COI | 77 | 0.158s | test_aged_brie_after_sell_date |
| 9 | COI | 121 | 0.159s | test_aged_brie_after_sell_date |

---

## ✅ Conclusões e Recomendações

### Pontos Fortes

1. **Excelente cobertura de mutações** - Score de 100% demonstra que os testes detectam efetivamente bugs introduzidos no código
2. **Testes bem distribuídos** - Múltiplos testes cobrem diferentes aspectos do comportamento
3. **Performance adequada** - Tempo de execução rápido (4.5s total)
4. **Cobertura de operadores críticos** - ROR (operadores relacionais) teve 10 mutantes, todos detectados

### Qualidade da Suite de Testes

**Classificação: EXCELENTE** ⭐⭐⭐⭐⭐

A suite de testes `test_gilded_rose.py` demonstra:
- ✅ Cobertura completa das regras de negócio
- ✅ Detecção de alterações em operadores aritméticos
- ✅ Detecção de alterações em condicionais
- ✅ Detecção de alterações em comparações

### Recomendações

1. **Manter a qualidade atual** - A suite está em excelente estado
2. **Documentar testes críticos** - Os testes que matam múltiplos mutantes são estratégicos
3. **Considerar adicionar testes de edge cases** se houver refatoração futura
4. **Executar mutation testing periodicamente** - Manter este nível de qualidade em futuras mudanças

---

## 📋 Informações Técnicas

### Ambiente de Execução
- **Python:** 3.11
- **Runner:** pytest
- **Processos:** Single thread (Windows)

### Comando Executado
```bash
.\.venv\Scripts\mut.py --target gilded_rose --unit-test tests.test_gilded_rose --runner pytest --report-html mutpy-report
```

### Relatório HTML Completo
Disponível em: `python/mutpy-report/index.html`

---

## 📚 Referências

- **MutPy Documentation:** https://github.com/mutpy/mutpy
- **Mutation Testing Guide:** https://en.wikipedia.org/wiki/Mutation_testing
- **Gilded Rose Kata:** https://github.com/emilybache/GildedRose-Refactoring-Kata

---

*Relatório gerado automaticamente em 09/12/2025*
