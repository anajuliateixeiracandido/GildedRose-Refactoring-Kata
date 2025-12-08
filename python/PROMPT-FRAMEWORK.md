# 🎯 PROMPT COMPLETO PARA GERAR O FRAMEWORK GILDED ROSE
**Target IA**: Claude Sonnet 4.5  
**Linguagem**: Python 3.x

---

## 📋 CONTEXTO E OBJETIVO

Preciso que você crie um **framework de engenharia de prompts modular** para guiar uma IA (Claude) através de um processo sistemático de análise, teste, refatoração e documentação BDD do **Gilded Rose Kata em Python**.

**Diferencial**: Este framework não foca apenas em cobertura de código, mas em **qualidade efetiva de testes** através de:
- Mutation Testing (matar mutantes)
- Test Smells (zero bad practices)
- Test Patterns (Object Mother, Data Builder)
- Clean Code principles
- BDD scenarios

---

## 📚 FUNDAMENTAÇÃO TEÓRICA (CRÍTICO)

Você receberá **arquivos de contexto teórico** que DEVEM ser a base epistemológica do framework:

**INSTRUÇÕES DE EXTRAÇÃO**:
- Leia TODOS os arquivos antes de gerar qualquer conteúdo
- Extraia conceitos-chave, exemplos de código, e referências acadêmicas
- Adapte exemplos da linguagem que estiver para Python 3 idiomático
- Cite autores e anos conforme aparecem nos materiais
- Integre a teoria nos prompts de forma aplicada, não apenas descritiva

---

## 🏗️ ESTRUTURA DE PASTAS REQUERIDA

Crie a seguinte estrutura em `.github/`:

```
.github/
└── gilded-rose-instructions/
    ├── gilded-rose-instructions/
    │   ├── core.md              # Meta-instruções do framework
    │   └── state.md             # Gestão de estado e progresso
    ├── gilded-rose-prompts/
    │   ├── analyze.prompt.md         # Prompt para análise de código
    │   ├── unit-tests.prompt.md      # Prompt para geração de testes
    │   ├── refactor.prompt.md        # Prompt para refatoração
    │   ├── bdd-scenarios.prompt.md   # Prompt para BDD
    │   └── test-quality-guide.md     # Referência completa consolidada
    └── gilded-rose-templates/
        ├── analysis-report.md        # Template de análise
        ├── coverage-report.md        # Template de coverage
        ├── refactoring-report.md     # Template de refatoração
        ├── bdd-scenarios.md          # Template BDD
        ├── FRAMEWORK-SUMMARY.md      # Sumário executivo
        └── README.md                 # Guia rápido de uso
```

---

## 📘 ESPECIFICAÇÃO: `gilded-rose-instructions/core.md`

### Conteúdo Obrigatório:

**1. AI PROCESSING INSTRUCTIONS** (seção inicial)
- Declaração: "You are Claude Sonnet 4.5, an expert AI assistant..."
- Regra crítica: "Always begin responses with `[MODE: MODE_NAME]`"

**2. FRAMEWORK OVERVIEW**
- Workflow linear: ANALYZE → TEST → REFACTOR → BDD
- Diagrama mermaid flowchart mostrando transições

**3. MODES OF OPERATION** (4 modos detalhados)

#### MODE 1: ANALYZE
- **Purpose**: Deep code analysis WITHOUT modifications
- **Command**: `/analyze` ou "ENTER ANALYZE MODE"
- **Permitted**: Read files, identify patterns, document business rules, map complexity
- **Forbidden**: Writing code, making suggestions, creating tests
- **Output**: Begin with `[MODE: ANALYZE]`, structured analysis document
- **Checklist**: Code structure, business rules, complexity, test coverage, tech debt

#### MODE 2: TEST
- **Purpose**: Generate comprehensive unit tests with 100% coverage
- **Command**: `/test` ou "ENTER TEST MODE"
- **Prerequisites**: ANALYZE mode completed
- **Permitted**: Create test files, write unit tests, document coverage
- **Forbidden**: Modifying source code (except tests), refactoring, skipping edge cases
- **Coverage Requirements**:
  - 100% Line Coverage
  - 100% Branch Coverage
  - Boundary testing (min/max, zero, negative)
  - Edge cases (Aged Brie, Sulfuras, Backstage passes, Conjured)
- **Test Principles**:
  - AAA Pattern (Arrange-Act-Assert)
  - Single Responsibility per test
  - Descriptive names
  - No test interdependencies
  - Fast execution
- **Output**: Begin with `[MODE: TEST]`, complete test suite + coverage report

#### MODE 3: REFACTOR
- **Purpose**: Refactor code following Clean Code WITHOUT changing behavior
- **Command**: `/refactor` ou "ENTER REFACTOR MODE"
- **Prerequisites**: TEST mode completed with 100% coverage
- **Permitted**: Refactor source code, extract methods/classes, rename, simplify, apply patterns, run tests after each step
- **Forbidden**: Changing business logic, modifying tests (unless absolutely necessary), breaking coverage, adding features
- **Clean Code Principles**:
  1. Single Responsibility Principle
  2. Meaningful Names
  3. Small Functions
  4. DRY Principle
  5. Command Query Separation
  6. Error Handling
  7. Null Safety
- **Python Best Practices**:
  - ✅ No `(object)` inheritance in Python 3
  - ✅ Use f-strings for formatting
  - ✅ Docstrings for all public methods
  - ✅ No trailing whitespace
  - ✅ Remove unnecessary else after return
  - ✅ Type hints where appropriate
- **Refactoring Strategies**: Replace conditionals with polymorphism, extract strategy pattern, create item-specific classes, factory pattern, simplify conditionals
- **Safety Protocol**: Run tests after EVERY change, commit after each step, rollback if tests fail, document decisions
- **Output**: Begin with `[MODE: REFACTOR]`, refactored code + before/after comparison + confirm tests pass

#### MODE 4: BDD
- **Purpose**: Create behavior-driven development scenarios in Gherkin
- **Command**: `/bdd` ou "ENTER BDD MODE"
- **Prerequisites**: ANALYZE completed (preferably REFACTOR too)
- **Permitted**: Create feature files, write scenarios, define Given-When-Then, scenario outlines, document acceptance criteria
- **Forbidden**: Modifying source code, changing existing tests, skipping scenarios
- **BDD Structure**: Feature/As a/I want/So that + Scenario/Given/When/Then
- **Output**: Begin with `[MODE: BDD]`, complete feature files in Gherkin

**4. MODE TRANSITION RULES**
- Sequential flow enforcement
- Prerequisites validation
- Command reference table

**5. STATE MANAGEMENT INTEGRATION**
- Reference to `state.md` for tracking progress
- Update instructions after mode completion

**6. BEST PRACTICES SECTION**
- Commit frequently during REFACTOR
- Run tests after every change
- Document decisions
- Use version control

---

## 📗 ESPECIFICAÇÃO: `gilded-rose-instructions/state.md`

### Conteúdo Obrigatório:

**1. PROJECT STATE** (variáveis de estado)
```markdown
**CURRENT_MODE**: "NONE"
- Possible values: "NONE", "ANALYZE", "TEST", "REFACTOR", "BDD"

**LANGUAGE**: ""
- Programming language being used (Python expected)

**FRAMEWORK_VERSION**: "1.0.0"

**LAST_UPDATE**: ""
- ISO 8601 timestamp
```

**2. PHASE COMPLETION STATUS** (flags booleanas)
```markdown
**ANALYSIS_COMPLETE**: false
**TESTS_COMPLETE**: false
**REFACTOR_COMPLETE**: false
**BDD_COMPLETE**: false
```

**3. PROGRESS TRACKING** (checklists expandidas)
- Analysis Phase checklist (5 items)
- Test Phase checklist (7+ items por tipo de item)
- Refactor Phase checklist (5 items)
- BDD Phase checklist (4 items)

**4. QUALITY METRICS** (seção de métricas)
```markdown
**COVERAGE_METRICS**:
- Line Coverage: 0%
- Branch Coverage: 0%
- Mutation Score: 0%

**TEST_QUALITY**:
- Total Tests: 0
- Test Smells Detected: []
- Patterns Applied: []
```

---

## 📗 ESPECIFICAÇÃO: `gilded-rose-prompts/analyze.prompt.md`

### Conteúdo Obrigatório:

**1. MODE DECLARATION**: `[MODE: ANALYZE]`

**2. OBJECTIVE**: Comprehensive, systematic analysis without modifications

**3. ANALYSIS CHECKLIST** (7 seções detalhadas):

- **Code Structure Analysis**: Files, classes, methods, dependencies, patterns
- **Business Rules Extraction**: 
  - Normal Items (4 rules)
  - Aged Brie (3 rules)
  - Sulfuras (3 rules)
  - Backstage Passes (5 rules)
  - Conjured Items (1 rule)
- **Code Complexity Analysis**: Cyclomatic complexity, nested levels, LOC, duplication, magic numbers
- **Code Smells Identification**: 10 specific smells (Long Method, Long Parameter List, Large Class, Primitive Obsession, Feature Envy, Data Clumps, Switch Statements, Duplicated Code, Dead Code, Comments as Deodorant)
- **Edge Cases & Risk Areas**: Boundaries, negative values, max values, item name variations, special items interaction, overflow, null handling
- **Current Test Coverage**: Existing tests, gaps, quality issues, percentage
- **Technical Debt Assessment**: Rate 1-10 for Maintainability, Readability, Testability, Extensibility, Overall Score

**4. ANALYSIS OUTPUT FORMAT** (template markdown estruturado)

**5. FORBIDDEN ACTIONS** (lista explícita):
- ❌ Do not suggest solutions
- ❌ Do not propose refactorings
- ❌ Do not write test cases
- ❌ Do not modify any code

**6. ANALYSIS PRINCIPLES**:
- Objective observation only
- Evidence-based conclusions
- Quantitative metrics where possible
- Reference specific line numbers

---

## 📗 ESPECIFICAÇÃO: `gilded-rose-prompts/unit-tests.prompt.md`

### ⭐ ARQUIVO MAIS CRÍTICO - CONTEÚDO DETALHADO:

**1. MODE DECLARATION**: `[MODE: TEST]`

**2. OBJECTIVE** (4 metas quantificáveis):
- 100% code coverage (line and branch)
- Maximum mutation kill rate (>80%)
- Zero test smells
- Test patterns applied

**3. PREREQUISITES** (checklist de 4 items)

**4. THEORETICAL FOUNDATION** (extrair de `mutacao.md`)

#### Mutation Testing Mindset
- Definição: Coverage ≠ Quality
- Princípio: Insert small bugs (mutants), tests must fail
- Goal: Write assertions that kill mutants
- Exemplo completo em Python:
```python
# CODE
if quality > 0:
    quality -= 1

# MUTANT (changes > to >=)
if quality >= 0:
    quality -= 1

# WEAK TEST (doesn't kill mutant)
assert item.quality >= 0  # Still passes!

# STRONG TEST (kills mutant)
assert item.quality == 9  # Fails if logic changes!
```
- Key Insight: Use specific assertions, not generic checks

**5. ANTI-PATTERNS: TEST SMELLS TO AVOID** (extrair de `test smell.md`)

#### 🚫 Critical Test Smells (NEVER DO THIS) - 7 smells detalhados:

**1. Mystery Guest**
- Problem: External data dependencies
- Why bad: Invisible content, brittle, hard to debug
- Exemplo BAD vs GOOD em Python

**2. Fragile Test**
- Problem: Coupled to implementation details
- Why bad: Prevents refactoring, false positives, trust loss
- Exemplo BAD vs GOOD em Python

**3. Conditional Logic in Test**
- Problem: if/for/while in tests
- Why bad: May test nothing, unpredictable, unclear
- Exemplo BAD vs GOOD em Python

**4. Obscure Setup**
- Problem: Setup longer than test
- Why bad: Hard to understand, violates DRY, maintenance nightmare
- Exemplo BAD vs GOOD em Python

**5. Assertion Roulette**
- Problem: Multiple assertions without messages
- Why bad: Can't tell which failed, hard to debug
- Exemplo BAD vs GOOD em Python

**6. The Giant / The Sleeper**
- Problem: Test too long or uses sleep()
- Why bad: Slow, unclear, flaky
- Exemplo BAD vs GOOD em Python

**7. Obscure Test**
- Problem: Unclear intent
- Why bad: Hard to understand purpose
- Exemplo BAD vs GOOD em Python

#### Test Smell Checklist (7 items)

**6. PYTHON 3 MODERN PRACTICES** (5 práticas obrigatórias)

**1. NO Object Inheritance in Python 3**
```python
# ❌ BAD
class TestGildedRose(object):
    pass

# ✅ GOOD
class TestGildedRose:
    pass
```

**2. F-Strings for All String Formatting**
```python
# ❌ BAD
assert item.quality == 10, "Expected %s, got %s" % (10, item.quality)

# ✅ GOOD
assert item.quality == 10, f"Expected 10, got {item.quality}"
```

**3. Docstrings for Test Methods**
**4. No Trailing Whitespace**
**5. Simplified Control Flow** (no else after return)

#### Python Test Quality Checklist (7 items)

**7. TEST PATTERNS TO APPLY** (extrair de `testpattern.md`)

#### Pattern 1: Object Mother
- Purpose: Centralize complex object creation
- When to use: Multiple tests need same setup
- Implementation completa em Python:
```python
class ItemMother:
    @staticmethod
    def create_normal_item():
        return Item("Normal Item", sell_in=5, quality=10)
    
    @staticmethod
    def create_aged_brie():
        return Item("Aged Brie", sell_in=10, quality=20)
    
    @staticmethod
    def create_expired_item():
        return Item("Normal Item", sell_in=-1, quality=10)

# Usage
def test_normal_item_decreases():
    """Test that normal items decrease in quality."""
    item = ItemMother.create_normal_item()
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 9
```

#### Pattern 2: Data Builder (Preferred)
- Purpose: Fluent API for customization
- When to use: Need variations of same object
- Implementation completa em Python:
```python
class ItemBuilder:
    def __init__(self):
        self._name = "Normal Item"
        self._sell_in = 5
        self._quality = 10
    
    @staticmethod
    def an_item():
        return ItemBuilder()
    
    def with_name(self, name):
        self._name = name
        return self
    
    def with_sell_in(self, sell_in):
        self._sell_in = sell_in
        return self
    
    def with_quality(self, quality):
        self._quality = quality
        return self
    
    def build(self):
        return Item(self._name, self._sell_in, self._quality)

# Usage
def test_aged_brie_increases():
    """Test that Aged Brie increases in quality."""
    item = (ItemBuilder.an_item()
            .with_name("Aged Brie")
            .with_quality(20)
            .build())
    
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 21, f"Expected 21, got {item.quality}"
```

#### Pattern 3: Test Doubles (brief mention)

**8. MUTATION OPERATORS** (extrair de `mutacao.md` e adaptar para Python)

#### Arithmetic Operators
- Original: `quality -= 1` → Mutant: `quality += 1`
- Original: `quality *= 2` → Mutant: `quality /= 2`
- Killing assertion: `assert item.quality == 9` (specific value)

#### Relational Operators
- Original: `if quality > 0` → Mutant: `if quality >= 0`
- Original: `if sell_in == 0` → Mutant: `if sell_in != 0`
- Killing assertion: Test boundary exactly

#### Logical Operators
- Original: `and` → Mutant: `or`
- Original: `not x` → Mutant: `x`
- Killing assertion: Test each condition separately

#### Boundary Value Operators
- Original: `range(10)` → Mutant: `range(9)` or `range(11)`
- Original: `0` → Mutant: `1` or `-1`
- Killing assertion: Count exact iterations

#### Python-Specific Operators
- Original: `//` (floor div) → Mutant: `/` (true div) or `%`
- Original: `is` → Mutant: `==`
- Original: `in` → Mutant: `not in`

**9. AAA PATTERN** (estrutura obrigatória)
```python
def test_example():
    """Docstring explaining what is tested."""
    # Arrange
    item = Item("foo", 10, 20)
    gilded_rose = GildedRose([item])
    
    # Act
    gilded_rose.update_quality()
    
    # Assert
    assert item.quality == 19, "Quality should decrease by 1"
```

**10. QUALITY TARGETS** (5 métricas quantificáveis)
- Line coverage: 100% (pytest-cov)
- Branch coverage: 100% (pytest-cov --branch)
- Mutation score: >80% (mutmut)
- Test smells: 0
- Execution time: <5s

**11. TOOLS** (comandos exatos)
```bash
pip install pytest pytest-cov mutmut
pytest --cov=gilded_rose --cov-report=html --cov-report=term
pytest --cov=gilded_rose --cov-branch
mutmut run
mutmut results
mutmut html
```

**12. TEST GENERATION CHECKLIST** (3 seções expandidas)
- Test Framework Setup (4 items)
- Test Organization Strategy (4 items)
- Coverage Requirements (3 subseções)

**13. TEST SCENARIOS BY ITEM TYPE** (5 categorias detalhadas)

#### NORMAL ITEMS (6 tests minimum)
```
✅ Test: Normal item quality decreases by 1 before sell date
   - Arrange: Item("foo", sell_in=5, quality=10)
   - Act: update_quality()
   - Assert: quality == 9

✅ Test: Normal item quality decreases by 2 after sell date
   - Arrange: Item("foo", sell_in=-1, quality=10)
   - Act: update_quality()
   - Assert: quality == 8

✅ Test: Normal item quality never goes negative
   - Arrange: Item("foo", sell_in=5, quality=0)
   - Act: update_quality()
   - Assert: quality == 0

✅ Test: Normal item sellIn decreases by 1
✅ Test: Normal item with quality 0 stays at 0
✅ Test: Normal item quality after multiple days
```

#### AGED BRIE (6 tests minimum)
```
✅ Test: Aged Brie quality increases by 1 before sell date
✅ Test: Aged Brie quality increases by 2 after sell date
✅ Test: Aged Brie quality caps at 50
✅ Test: Aged Brie at quality 50 stays at 50
✅ Test: Aged Brie at quality 49 before sell date
✅ Test: Aged Brie at quality 49 after sell date (caps at 50)
```

#### SULFURAS (4 tests minimum)
```
✅ Test: Sulfuras quality never changes
✅ Test: Sulfuras quality is always 80
✅ Test: Sulfuras sellIn never changes
✅ Test: Sulfuras behavior over multiple days
```

#### BACKSTAGE PASSES (9 tests minimum)
```
✅ Test: Quality +1 when sellIn > 10
✅ Test: Quality +2 when sellIn = 10
✅ Test: Quality +2 when 6 ≤ sellIn ≤ 10
✅ Test: Quality +3 when sellIn = 5
✅ Test: Quality +3 when 1 ≤ sellIn ≤ 5
✅ Test: Quality drops to 0 when sellIn < 0
✅ Test: Quality caps at 50
✅ Test: Quality at 48 with sellIn = 5 (caps at 50)
✅ Test: Quality at 49 with sellIn = 10 (caps at 50)
```

#### CONJURED ITEMS (4 tests minimum, if implemented)
```
✅ Test: Quality decreases by 2 before sell date
✅ Test: Quality decreases by 4 after sell date
✅ Test: Quality never goes negative
✅ Test: Quality at 1 before sell date becomes 0
```

**14. EDGE CASES CHECKLIST** (10+ scenarios)

**15. FORBIDDEN ACTIONS** (lista explícita)
- ❌ Modifying source code (except test files)
- ❌ Skipping edge cases for simplicity
- ❌ Using generic assertions (assert > 0 instead of == 9)
- ❌ Creating tests with conditional logic
- ❌ External file dependencies

**16. OUTPUT REQUIREMENTS**
- Begin with `[MODE: TEST]`
- Create test files following pytest conventions
- Use descriptive test names: `test_<item>_<scenario>_<expected>`
- Group tests by item type (classes or modules)
- Provide coverage summary table
- List mutation testing results

**17. VALIDATION CHECKLIST** (final quality check - 10 items)

---

## 📗 ESPECIFICAÇÃO: `gilded-rose-prompts/refactor.prompt.md`

### Conteúdo Obrigatório:

**1. MODE DECLARATION**: `[MODE: REFACTOR]`

**2. OBJECTIVE**: Refactor code following Clean Code WITHOUT changing behavior

**3. PREREQUISITES**: Tests complete with 100% coverage

**4. REFACTORING THEORY** (extrair de `refatoracao.md`)
- Code smells (Fowler 1999)
- Refactoring techniques catalog
- When to refactor vs rewrite

**5. CLEAN CODE PRINCIPLES** (7 princípios detalhados)
- Cada princípio com explicação e exemplo Python

**6. PYTHON BEST PRACTICES** (mesmo do core.md)

**7. REFACTORING STRATEGIES FOR GILDED ROSE** (específicas)
- Replace conditionals with polymorphism
- Extract strategy pattern for item types
- Create item-specific classes (NormalItem, AgedBrieItem, etc.)
- Use factory pattern for item creation
- Simplify complex conditionals

**8. REFACTORING PROCESS** (step-by-step)
1. Identify code smell
2. Choose refactoring technique
3. Apply refactoring
4. Run tests (must pass)
5. Commit
6. Repeat

**9. SAFETY PROTOCOL**
- ✅ Run tests after EVERY change
- ✅ Commit after each successful step
- ✅ If tests fail, rollback immediately
- ✅ Document refactoring decisions

**10. FORBIDDEN ACTIONS**
- ❌ Changing business logic or behavior
- ❌ Modifying tests (unless absolutely necessary)
- ❌ Breaking existing test coverage
- ❌ Adding new features

**11. OUTPUT REQUIREMENTS**
- Begin with `[MODE: REFACTOR]`
- Present refactored code with clear diffs
- Explain each major refactoring decision
- Confirm all tests still pass (show pytest output)
- Provide before/after complexity comparison
- Show coverage maintained at 100%

**12. REFACTORING CHECKLIST** (8 items)

---

## 📗 ESPECIFICAÇÃO: `gilded-rose-prompts/bdd-scenarios.prompt.md`

### Conteúdo Obrigatório:

**1. MODE DECLARATION**: `[MODE: BDD]`

**2. OBJECTIVE**: Create behavior-driven development scenarios

**3. PREREQUISITES**: ANALYZE completed

**4. BDD THEORY**
- What is BDD (North 2006)
- Benefits of Gherkin syntax
- Given-When-Then structure

**5. GHERKIN SYNTAX GUIDE**
```gherkin
Feature: Feature Name
  As a [role]
  I want [feature]
  So that [benefit]

Scenario: Scenario Name
  Given [context]
  When [action]
  Then [expected result]

Scenario Outline: Parameterized Scenario
  Given <context>
  When <action>
  Then <result>
  
  Examples:
    | context | action | result |
    | ...     | ...    | ...    |
```

**6. PYTHON BDD WITH BEHAVE**
- Installation: `pip install behave`
- File structure: `features/`, `steps/`
- Step definitions example

**7. SCENARIOS TO CREATE FOR GILDED ROSE** (5 features)
- Feature: Normal item quality degradation
- Feature: Aged Brie quality improvement
- Feature: Sulfuras legendary persistence
- Feature: Backstage passes concert approach
- Feature: Conjured items double degradation

**8. OUTPUT REQUIREMENTS**
- Begin with `[MODE: BDD]`
- Create feature files in Gherkin syntax
- Cover all business rules
- Use scenario outlines for data-driven tests
- Provide step definitions skeleton in Python

---

## 📗 ESPECIFICAÇÃO: `gilded-rose-prompts/test-quality-guide.md`

### Conteúdo Obrigatório:

**ESTE ARQUIVO CONSOLIDA OS 4 MATERIAIS TEÓRICOS**

**PART 1: TEST SMELLS CATALOG** (extrair de `test smell.md`)
- 8 categorias de test smells
- Cada smell com: Symptom, Why it's bad, Example (Python BAD vs GOOD)

**PART 2: MUTATION TESTING THEORY** (extrair de `mutacao.md`)
- Historical context (Lipton 1971, DeMillo 1978)
- Mutation score formula
- Mutation operators catalog (8+ operators Python-specific)
- How to read mutation testing reports
- Tools comparison (mutmut, mutatest, cosmic-ray)

**PART 3: TEST PATTERNS** (extrair de `testpattern.md`)
- Object Mother Pattern (complete Python implementation)
- Data Builder Pattern (complete Python implementation)
- Test Double patterns (brief overview)
- When to use each pattern

**PART 4: REFACTORING CATALOG** (extrair de `refatoracao.md`)
- Code smells vs Test smells
- Refactoring techniques catalog
- Safe refactoring practices
- Pythonic refactorings

**PART 5: QUALITY METRICS TABLE**
| Metric | Target | Tool | Command |
|--------|--------|------|---------|
| Line Coverage | 100% | pytest-cov | `pytest --cov` |
| Branch Coverage | 100% | pytest-cov | `pytest --cov --cov-branch` |
| Mutation Score | >80% | mutmut | `mutmut run` |
| Test Smells | 0 | Manual | Review checklist |
| Execution Time | <5s | pytest | `pytest --durations=10` |

**PART 6: BIBLIOGRAPHY**
- Complete academic references from all 4 materials
- APA format

---

## 📙 ESPECIFICAÇÃO: `gilded-rose-templates/`

### 6 Templates Requeridos:

**1. analysis-report.md**
- Seções: Project Info, Code Structure, Business Rules, Complexity Analysis, Code Smells, Edge Cases, Current Tests, Technical Debt, Recommendations

**2. coverage-report.md**
- Seções: Project Information, Coverage Summary, Test Suite Overview, Test Scenario Coverage (por tipo de item), Mutation Testing Results, Test Smells Analysis, Commands Used, Next Steps

**3. refactoring-report.md**
- Seções: Refactoring Summary, Code Smells Removed, SOLID Principles Applied, Before/After Comparison, Complexity Metrics, Test Results, Commits Log

**4. bdd-scenarios.md**
- Seções: Feature files completas em Gherkin (5 features minimum)

**5. FRAMEWORK-SUMMARY.md**
- Sumário executivo para apresentações
- Seções: Framework Overview, Quality Targets, Workflow, Outcomes, Metrics Table, Theoretical Foundation, Technologies Used

**6. README.md**
- Quick Start Guide
- Seções: Purpose, Framework Structure, Quick Start (5 steps), Available Commands, Quality Targets, Tools Installation (Python-specific), Validation Steps, For Academic Projects, Theoretical Foundation, Troubleshooting

---

## 🎯 ESTRATÉGIAS DE PROMPTING A APLICAR

**Você DEVE usar estas técnicas de prompt engineering:**

1. **Chain of Thought (CoT)**: 
   - Nos prompts, criar passos numerados sequenciais
   - Exemplo: "1. Understand business logic → 2. Identify edge cases → 3. Design test structure → 4. Write assertions"

2. **Few-Shot Learning**:
   - Incluir 2-3 exemplos completos de código para cada conceito
   - Formato: ❌ BAD (antipattern) vs ✅ GOOD (best practice)

3. **Role Prompting**:
   - Início de cada prompt: "You are a [specific role]..."
   - Exemplo: "You are a Python test engineer specializing in mutation testing..."

4. **Constraint-Based Prompting**:
   - Seções explícitas "Permitted" e "Forbidden" em cada modo
   - Listar ações proibidas com ❌

5. **Structured Output Prompting**:
   - Templates markdown com seções predefinidas
   - Tabelas, checklists, code blocks

6. **Knowledge Grounding**:
   - Citar autores e anos dos materiais teóricos
   - Exemplo: "(Meszaros 2007)", "(Fowler 1999)"

7. **Goal-Oriented Prompting**:
   - Targets quantificáveis no início
   - Exemplo: "Achieve 100% line coverage AND >80% mutation score"

---

## ✅ CHECKLIST DE VALIDAÇÃO FINAL

Antes de entregar, verifique se TODOS os itens foram criados:

### Arquivos de Instruções (2 arquivos)
- [ ] `gilded-rose-instructions/core.md` (4 modos detalhados, ~300-400 linhas)
- [ ] `gilded-rose-instructions/state.md` (variáveis de estado + checklists, ~100-150 linhas)

### Arquivos de Prompts (5 arquivos)
- [ ] `gilded-rose-prompts/analyze.prompt.md` (~200-250 linhas)
- [ ] `gilded-rose-prompts/unit-tests.prompt.md` (~700-800 linhas - ARQUIVO MAIS LONGO)
- [ ] `gilded-rose-prompts/refactor.prompt.md` (~300-400 linhas)
- [ ] `gilded-rose-prompts/bdd-scenarios.prompt.md` (~200-250 linhas)
- [ ] `gilded-rose-prompts/test-quality-guide.md` (~500-600 linhas - referência completa)

### Arquivos de Templates (6 arquivos)
- [ ] `gilded-rose-templates/analysis-report.md` (~150-200 linhas)
- [ ] `gilded-rose-templates/coverage-report.md` (~300-400 linhas)
- [ ] `gilded-rose-templates/refactoring-report.md` (~200-250 linhas)
- [ ] `gilded-rose-templates/bdd-scenarios.md` (~150-200 linhas)
- [ ] `gilded-rose-templates/FRAMEWORK-SUMMARY.md` (~100-150 linhas)
- [ ] `gilded-rose-templates/README.md` (~300-350 linhas)

### Conteúdo Teórico
- [ ] Teoria de Mutation Testing extraída de `mutacao.md` e integrada
- [ ] Test Smells extraídos de `test smell.md` com exemplos Python
- [ ] Test Patterns extraídos de `testpattern.md` com implementações Python
- [ ] Refactoring techniques extraídas de `refatoracao.md`
- [ ] Todas as citações acadêmicas incluídas (Lipton, DeMillo, Meszaros, Fowler, Martin, North)

### Adaptação Python
- [ ] Todos os exemplos de código em Python 3 idiomático
- [ ] Ferramentas Python especificadas (pytest, pytest-cov, mutmut, behave)
- [ ] Comandos de instalação corretos (`pip install ...`)
- [ ] Python best practices aplicadas (f-strings, no `(object)`, docstrings, etc.)
- [ ] Mutation operators Python-specific incluídos (`//`, `and/or`, `is/==`, etc.)

### Técnicas de Prompting
- [ ] Chain of Thought aplicado (passos numerados)
- [ ] Few-Shot Learning (exemplos BAD vs GOOD)
- [ ] Role Prompting (definição de papel)
- [ ] Constraint-Based (Permitted/Forbidden)
- [ ] Structured Output (templates)
- [ ] Knowledge Grounding (citações)
- [ ] Goal-Oriented (targets quantificáveis)

### Validação de Usabilidade
- [ ] Comandos slash funcionais (`/analyze`, `/test`, `/refactor`, `/bdd`)
- [ ] Mode declaration obrigatória (`[MODE: XXX]`)
- [ ] Transitions entre modos claramente definidas
- [ ] Prerequisites validados antes de cada modo
- [ ] Output requirements especificados para cada modo

---

## 🚀 COMO USAR ESTE PROMPT

1. **Anexe os 4 materiais teóricos**:
   - `mutacao.md`
   - `test smell.md`
   - `testpattern.md`
   - `refatoracao.md`

2. **Cole este prompt completo** na conversa com Claude/GPT

3. **Aguarde a geração** de todos os 13 arquivos

4. **Valide usando o checklist acima**

5. **Teste o framework** em um projeto Gilded Rose real

---

## 📊 RESULTADO ESPERADO

Ao final, você terá um framework completo e pronto para uso que:

✅ Guia a IA através de 4 fases sequenciais (ANALYZE → TEST → REFACTOR → BDD)
✅ Gera testes com 100% coverage E >80% mutation score
✅ Previne test smells através de exemplos e checklists
✅ Aplica test patterns (Object Mother, Data Builder)
✅ Refatora seguindo Clean Code e SOLID
✅ Cria cenários BDD em Gherkin
✅ É fundamentado em teoria acadêmica (Lipton, Meszaros, Fowler, Martin, North)
✅ Usa Python 3 idiomático com best practices
✅ Está pronto para uso imediato sem edições manuais

---

