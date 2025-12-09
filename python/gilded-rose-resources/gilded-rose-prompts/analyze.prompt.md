# ANALYZE Mode - Deep Code Analysis Prompt

## MODE DECLARATION
[MODE: ANALYZE]

## OBJECTIVE
Perform a comprehensive, systematic analysis of the Gilded Rose codebase to understand its structure, business logic, complexity, and quality issues before any modifications.

---

## ANALYSIS CHECKLIST

### 1. CODE STRUCTURE ANALYSIS
- [ ] Identify all source files and their purposes
- [ ] Map class relationships and dependencies
- [ ] Document public interfaces and methods
- [ ] Identify entry points and main logic flow
- [ ] Note any existing abstractions or patterns

### 2. BUSINESS RULES EXTRACTION
Extract and document ALL business rules from the code:

- [ ] **Normal Items**:
  - Quality decreases by 1 per day
  - After sell date, quality degrades twice as fast
  - Quality never negative
  - Quality never exceeds 50

- [ ] **Aged Brie**:
  - Quality increases as it ages
  - After sell date, quality increases twice as fast
  - Quality capped at 50

- [ ] **Sulfuras** (Legendary):
  - Never decreases in quality
  - Never needs to be sold
  - Quality is always 80

- [ ] **Backstage Passes**:
  - Quality increases as sell date approaches
  - +1 when more than 10 days
  - +2 when 10 days or less
  - +3 when 5 days or less
  - Quality drops to 0 after concert (sellIn < 0)

- [ ] **Conjured Items** (if applicable):
  - Quality decreases twice as fast as normal items

### 3. CODE COMPLEXITY ANALYSIS
- [ ] Calculate cyclomatic complexity per method
- [ ] Count nested conditional levels
- [ ] Identify longest methods (LOC)
- [ ] Measure code duplication
- [ ] Find magic numbers and strings

### 4. CODE SMELLS IDENTIFICATION
Look for these specific smells:

- [ ] **Long Method**: Methods > 20 lines
- [ ] **Long Parameter List**: > 3 parameters
- [ ] **Large Class**: Classes with too many responsibilities
- [ ] **Primitive Obsession**: Overuse of primitives vs objects
- [ ] **Feature Envy**: Methods more interested in other classes
- [ ] **Data Clumps**: Same group of data appearing together
- [ ] **Switch Statements**: Type-based conditionals (refactoring candidates)
- [ ] **Duplicated Code**: Repeated logic blocks
- [ ] **Dead Code**: Unreachable or unused code
- [ ] **Comments as Deodorant**: Excessive explanatory comments

### 5. EDGE CASES & RISK AREAS
Identify potential problematic scenarios:

- [ ] Boundary conditions (sellIn = 0, quality = 0, quality = 50)
- [ ] Negative values handling
- [ ] Maximum value handling
- [ ] Item name variations (case sensitivity, spacing)
- [ ] Multiple special items interaction
- [ ] Integer overflow possibilities
- [ ] Null/undefined handling

### 6. CURRENT TEST COVERAGE (if any)
- [ ] List existing test files
- [ ] Document what is currently tested
- [ ] Identify coverage gaps
- [ ] Note test quality issues
- [ ] Measure current coverage percentage

### 7. TECHNICAL DEBT ASSESSMENT
Rate from 1-10 (10 = severe debt):

- [ ] **Maintainability**: How easy to modify?
- [ ] **Readability**: How clear is the intent?
- [ ] **Testability**: How easy to test?
- [ ] **Extensibility**: How easy to add features?
- [ ] **Overall Quality Score**:

---

## ANALYSIS OUTPUT FORMAT

Provide analysis in this structured format:

### 📁 CODE STRUCTURE
```
├── [File/Class Name]
│   ├── Method: [name] (lines: X, complexity: Y)
│   ├── Method: [name] (lines: X, complexity: Y)
│   └── Dependencies: [list]
```

### 📋 BUSINESS RULES SUMMARY
Table format:
| Item Type | Business Rule | Code Location |
|-----------|---------------|---------------|
| Normal    | Quality -1/day | Line XX |
| ...       | ...            | ...          |

### 🔢 COMPLEXITY METRICS
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Avg Cyclomatic Complexity | X | < 10 | ⚠️ |
| Max Nesting Level | X | < 4 | ✅ |
| Longest Method | X lines | < 20 | ⚠️ |
| Code Duplication | X% | < 5% | ⚠️ |

### ⚠️ CODE SMELLS FOUND
1. **[Smell Name]** - Location: [file:line]
   - Impact: High/Medium/Low
   - Description: [what's wrong]
   - Refactoring suggestion: [how to fix]

### 🎯 EDGE CASES & RISKS
Priority list:
1. **[Risk description]** - Priority: Critical/High/Medium/Low
   - Current handling: [how code handles it]
   - Test requirement: [what needs testing]

### 📊 TEST COVERAGE ANALYSIS
Current state:
- Existing tests: [count]
- Estimated coverage: [percentage]
- Missing scenarios: [list]

### 💰 TECHNICAL DEBT SCORE
| Dimension | Score (1-10) | Justification |
|-----------|--------------|---------------|
| Maintainability | X | [reason] |
| Readability | X | [reason] |
| Testability | X | [reason] |
| Extensibility | X | [reason] |
| **Overall** | **X** | [summary] |

---

## EXECUTION STEPS

1. **Read all source files** in the repository
   - Use `grep_search` or `semantic_search` to find Gilded Rose files
   - Use `read_file` to examine each file thoroughly

2. **Map the code structure**
   - Create visual representation of classes/methods
   - Document public APIs

3. **Extract business rules**
   - Go through code line-by-line
   - Map each conditional to a business rule
   - Cross-reference with kata requirements

4. **Calculate complexity**
   - Count branches per method
   - Measure nesting depth
   - Identify long methods

5. **Identify code smells**
   - Apply systematic code review
   - Categorize by severity

6. **Document edge cases**
   - Think adversarially
   - List boundary conditions
   - Identify undefined behaviors

7. **Assess test coverage**
   - Find existing tests
   - Map coverage to code
   - Identify gaps

8. **Generate final report**
   - Compile all findings
   - Prioritize issues
   - Set baseline for next phases

---

## DELIVERABLE

A comprehensive analysis document containing:
✅ Complete code structure map
✅ All business rules documented
✅ Complexity metrics calculated
✅ Code smells identified and prioritized
✅ Edge cases and risks listed
✅ Current test coverage assessment
✅ Technical debt score

This document will serve as the foundation for TEST, REFACTOR, and BDD modes.

---

## PYTHON 3 CODE QUALITY AWARENESS

When analyzing Python code, note these quality indicators:

### Modern Python 3 Practices
- ✅ Classes without `(object)` inheritance (Python 3 default)
- ✅ F-strings for string formatting (not % or .format())
- ✅ Docstrings present for all public methods
- ✅ No trailing whitespace
- ✅ Simplified control flow (no else-after-return)

### Quality Issues to Flag
- ❌ Old-style `class ClassName(object):` syntax
- ❌ Old string formatting: `"%s" % value` or `"{}".format(value)`
- ❌ Missing docstrings on public methods
- ❌ Trailing whitespace in files
- ❌ Unnecessary else blocks after return statements

**Note**: These will be enforced in subsequent TEST and REFACTOR modes.

---

## TRANSITION CRITERIA

Ready to move to TEST mode when:
- ✅ All 7 analysis sections complete
- ✅ Business rules 100% documented
- ✅ Edge cases identified
- ✅ Analysis deliverable created
- ✅ Python quality baseline noted

**Next Command**: `/test` to enter TEST mode

