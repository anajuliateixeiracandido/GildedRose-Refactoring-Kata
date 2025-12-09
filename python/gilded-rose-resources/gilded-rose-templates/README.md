# Gilded Rose Quality Framework - Quick Start Guide

## 🎯 Purpose

This lightweight framework helps you use Claude Sonnet 4.5 to generate **EFFECTIVE**, not just comprehensive, tests and refactorings:

1. ✅ **Unit tests with 100% coverage AND high mutation kill rate** (>80%)
2. ✅ **Zero test smells** - clean, maintainable tests
3. ✅ **Test patterns applied** - Object Mother, Data Builder
4. ✅ **Refactor following Clean Code principles**
5. ✅ **BDD scenarios in Gherkin format**

**Key Insight**: Coverage alone is NOT enough. Tests must **kill mutants** and **detect real bugs**.

Perfect for the **Gilded Rose Kata** challenge and academic projects requiring quality metrics.

---

## 📁 Framework Structure

```
.github/
├── gilded-rose-instructions/
│   ├── core.md              # Main framework instructions
│   └── state.md             # Current state tracking
├── gilded-rose-prompts/
│   ├── analyze.prompt.md        # Analysis phase guidance
│   ├── unit-tests.prompt.md     # Test generation with mutation testing
│   ├── refactor.prompt.md       # Refactoring guidance
│   ├── bdd-scenarios.prompt.md  # BDD scenarios guidance
│   └── test-quality-guide.md    # Complete Test Smells & Patterns reference
└── gilded-rose-templates/
    ├── analysis-report.md    # Analysis deliverable template
    ├── coverage-report.md    # Coverage report template
    ├── refactoring-report.md # Refactoring report template
    └── bdd-scenarios.md      # BDD deliverable template
```

---

## 🚀 Quick Start

### Step 1: Initialize
Open your Gilded Rose repository and start a conversation with Claude:

```
Hi Claude! I'm working on the Gilded Rose Kata. Please load the 
Gilded Rose Quality Framework from .github/gilded-rose-instructions/core.md
```

### Step 2: Analyze
```
/analyze
```
Claude will perform deep code analysis and generate an analysis report.

### Step 3: Generate Tests
```
/test
```
Claude will create comprehensive unit tests achieving:
- 100% line and branch coverage
- High mutation score (>80%)
- Zero test smells
- Test patterns applied (Builder/Mother)

### Step 4: Refactor
```
/refactor
```
Claude will refactor the code following Clean Code principles.

### Step 5: Create BDD Scenarios
```
/bdd
```
Claude will generate BDD scenarios in Gherkin format.

---

## 📝 Available Commands

| Command | Mode | Purpose |
|---------|------|---------|
| `/analyze` | ANALYZE | Deep code analysis |
| `/test` | TEST | Generate unit tests with 100% coverage |
| `/refactor` | REFACTOR | Refactor following Clean Code |
| `/bdd` | BDD | Create BDD scenarios |
| `/status` | - | Show current progress |
| `/reset` | - | Start over from analysis |

---

## 🎓 For Academic Projects

### Recommended Workflow for Assignments

1. **Document Your Prompts**: Save each prompt you use
2. **Capture Evidence**: Screenshot coverage reports, mutation testing
3. **Track Metrics**: Before/after complexity, coverage percentages
4. **Critical Analysis**: Evaluate AI output quality

### Integration with Assignment Requirements

This framework directly supports:
- ✅ **Prompt Engineering**: Structured prompts in each mode
- ✅ **100% Coverage**: TEST mode ensures comprehensive tests
- ✅ **Mutation Testing**: Built-in guidance for killing mutants
- ✅ **Zero Test Smells**: Automatic smell detection and prevention
- ✅ **Test Patterns**: Object Mother, Data Builder patterns
- ✅ **Clean Code**: REFACTOR mode applies SOLID principles
- ✅ **BDD Scenarios**: BDD mode generates Gherkin files
- ✅ **Documentation**: Templates for all deliverables
- ✅ **Quality Metrics**: Coverage, mutation score, complexity

---

## 📊 Expected Deliverables

### After ANALYZE Mode
- `analysis-report.md` with code structure, complexity, code smells

### After TEST Mode
- Complete test suite with:
  - ✅ 100% line coverage
  - ✅ 100% branch coverage
  - ✅ Mutation score >80%
  - ✅ Zero test smells
  - ✅ Test patterns applied
- `coverage-report.md` with proof
- Coverage tool output (HTML reports, screenshots)
- Mutation testing report

### After REFACTOR Mode
- Refactored codebase
- `refactoring-report.md` with before/after metrics
- All tests still passing

### After BDD Mode
- Feature files in Gherkin format
- `bdd-scenarios.md` with all scenarios
- Scenario-to-code mapping

---

## 💡 Tips for Best Results

### 1. Be Specific with Context
Provide Claude with:
- Programming language
- Test framework
- Coverage tool
- Any constraints (e.g., can't modify Item class)

### 2. Iterative Approach
Don't rush through modes. Take time to:
- Review analysis before generating tests
- Verify coverage before refactoring
- Run tests after each refactoring step

### 3. Save Your Prompts
For academic work, document:
- What you asked Claude to do
- How you phrased your requests
- Any adjustments you made

### 4. Validate AI Output
Always:
- Run the tests yourself
- Check coverage with tools (JaCoCo, Coverage.py, etc.)
- **Run mutation testing** (PIT, Stryker, mutmut)
- Review refactored code
- Test behavioral compatibility
- Verify no test smells present

---

## 🔧 Language-Specific Setup

### Python
```bash
# Test framework: pytest
pip install pytest pytest-cov

# Run tests with coverage
pytest --cov=gilded_rose --cov-report=html

# Mutation testing
pip install mutmut
mutmut run
mutmut show  # See surviving mutants
mutmut results  # Summary
```

### Java
```xml
<!-- Test framework: JUnit 5 -->
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.9.0</version>
</dependency>

<!-- Coverage: JaCoCo -->
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
</plugin>

<!-- Mutation: PIT -->
<plugin>
    <groupId>org.pitest</groupId>
    <artifactId>pitest-maven</artifactId>
</plugin>
```

```bash
# Run tests with coverage and mutation
mvn clean test
mvn jacoco:report  # Coverage report in target/site/jacoco/
mvn org.pitest:pitest-maven:mutationCoverage  # Mutation report
```

### C#
```bash
# Test framework: NUnit
dotnet add package NUnit
dotnet add package NUnit3TestAdapter

# Coverage: coverlet
dotnet add package coverlet.collector
dotnet test /p:CollectCoverage=true /p:CoverletOutputFormat=html

# Mutation: Stryker
dotnet tool install -g dotnet-stryker
dotnet stryker
```

### JavaScript/TypeScript
```bash
# Test framework: Jest
npm install --save-dev jest @types/jest

# Run with coverage
npm test -- --coverage

# Mutation: Stryker
npm install --save-dev @stryker-mutator/core @stryker-mutator/jest-runner
npx stryker run
```

---

## 📚 Additional Resources

### Gilded Rose Kata
- **Repository**: https://github.com/emilybache/GildedRose-Refactoring-Kata
- **Requirements**: Original kata specification
- **Languages**: Available in 30+ languages

### Clean Code Principles
- Robert C. Martin's "Clean Code"
- SOLID principles
- Refactoring patterns

### BDD & Gherkin
- Cucumber documentation
- Behavior-Driven Development principles
- Gherkin syntax reference

---

## 🆘 Troubleshooting

### "Claude doesn't recognize my commands"
- Ensure you've loaded the framework: mention `.github/gilded-rose-instructions/core.md`
- Use exact command format: `/analyze`, `/test`, etc.

### "Tests don't achieve 100% coverage"
- Review coverage report for gaps
- Ask Claude: "What lines/branches are uncovered?"
- Request specific tests for missing coverage

### "Refactoring broke tests"
- This should never happen with the framework
- If it does, Claude will rollback automatically
- Review what changed and adjust approach

### "BDD scenarios don't match my code"
- Ensure ANALYZE mode was completed
- Scenarios should match business rules from analysis
- Ask Claude to map scenarios to specific code lines

---

## 📧 Framework Info

- **Version**: 1.0.0
- **Optimized for**: Claude Sonnet 4.5
- **License**: Free for educational use
- **Use Case**: Gilded Rose Kata and similar refactoring challenges

---

## ✅ Success Checklist

Use this to verify you've completed everything:

- [ ] Framework loaded and initialized
- [ ] `/analyze` completed with full analysis report
- [ ] `/test` completed with 100% coverage
- [ ] **Coverage verified with coverage tool (100% line & branch)**
- [ ] **Mutation testing run (score >80%)**
- [ ] **Zero test smells verified**
- [ ] **Test patterns applied (Builder/Mother)**
- [ ] `/refactor` completed with all tests passing
- [ ] Code quality improved measurably
- [ ] `/bdd` completed with Gherkin scenarios
- [ ] All deliverables documented
- [ ] Prompts saved for presentation
- [ ] Evidence captured (screenshots, reports, mutation results)

---

**Ready to start? Just say: `/analyze`** 🚀
