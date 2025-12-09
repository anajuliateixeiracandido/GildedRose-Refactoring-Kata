# Gilded Rose Analysis Report Template

## PROJECT INFORMATION
- **Repository**: [URL or path]
- **Language**: [Programming language]
- **Date**: [Analysis date]
- **Analyst**: [Name or AI]

---

## 📁 CODE STRUCTURE

### Source Files
```
[List all source files with brief descriptions]
Example:
├── gilded_rose.py (Main update logic - 85 lines)
├── item.py (Item class definition - 15 lines)
└── test_gilded_rose.py (Existing tests - if any)
```

### Class Overview
| Class | Purpose | Methods | Lines of Code |
|-------|---------|---------|---------------|
| GildedRose | Main update orchestration | update_quality() | XX |
| Item | Data holder | __init__() | XX |

### Dependencies
- [List external dependencies]
- [List internal dependencies]

---

## 📋 BUSINESS RULES DOCUMENTATION

### Complete Rule Set
| Item Type | Behavior | Code Location | Complexity |
|-----------|----------|---------------|------------|
| **Normal Items** |
| | Quality decreases by 1 per day before sell date | Line XX | Simple |
| | Quality decreases by 2 per day after sell date | Line XX | Simple |
| | Quality never goes below 0 | Line XX | Simple |
| | SellIn decreases by 1 per day | Line XX | Simple |
| **Aged Brie** |
| | Quality increases by 1 per day before sell date | Line XX | Simple |
| | Quality increases by 2 per day after sell date | Line XX | Simple |
| | Quality never exceeds 50 | Line XX | Simple |
| **Sulfuras (Legendary)** |
| | Quality never changes (always 80) | Line XX | Simple |
| | SellIn never changes | Line XX | Simple |
| **Backstage Passes** |
| | Quality increases by 1 when sellIn > 10 | Line XX | Medium |
| | Quality increases by 2 when 6 ≤ sellIn ≤ 10 | Line XX | Medium |
| | Quality increases by 3 when 1 ≤ sellIn ≤ 5 | Line XX | Medium |
| | Quality drops to 0 when sellIn < 0 | Line XX | Medium |
| | Quality never exceeds 50 | Line XX | Simple |
| **Conjured Items** |
| | Quality decreases by 2 per day before sell date | Line XX | Simple |
| | Quality decreases by 4 per day after sell date | Line XX | Simple |
| | Quality never goes below 0 | Line XX | Simple |

### Business Rule Validation
- ✅ All rules identified: [Yes/No]
- ✅ Rules documented completely: [Yes/No]
- ✅ Edge cases understood: [Yes/No]

---

## 🔢 CODE COMPLEXITY METRICS

### Overall Complexity
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Lines of Code | XXX | - | 📊 |
| Average Cyclomatic Complexity | XX | < 10 | ⚠️/✅ |
| Maximum Cyclomatic Complexity | XX | < 15 | ⚠️/✅ |
| Maximum Nesting Depth | X | < 4 | ⚠️/✅ |
| Longest Method | XX lines | < 20 | ⚠️/✅ |
| Code Duplication | XX% | < 5% | ⚠️/✅ |

### Method-Level Complexity
| Method | Lines | Cyclomatic Complexity | Nesting | Assessment |
|--------|-------|----------------------|---------|------------|
| update_quality() | XX | XX | X | High/Medium/Low |
| [other methods] | XX | XX | X | High/Medium/Low |

### Complexity Hotspots
1. **[Method/Section Name]** - Lines XX-XX
   - Complexity: XX
   - Issue: [Nested conditionals, long method, etc.]
   - Impact: High

2. **[Method/Section Name]** - Lines XX-XX
   - Complexity: XX
   - Issue: [Description]
   - Impact: Medium

---

## ⚠️ CODE SMELLS IDENTIFIED

### Critical Issues (Fix Required)
1. **Long Method** - `update_quality()` (XX lines)
   - Location: Line XX
   - Impact: High
   - Description: Method handles all item types in one function
   - Refactoring: Extract item-specific methods/classes

2. **Switch Statement / Complex Conditionals** - Item type handling
   - Location: Lines XX-XX
   - Impact: High
   - Description: Nested if-else for item types
   - Refactoring: Replace with Strategy pattern

3. **Magic Numbers** - Throughout code
   - Location: Lines XX, XX, XX
   - Impact: Medium
   - Description: Hardcoded values (50, 80, 10, 5, etc.)
   - Refactoring: Extract named constants

### Medium Priority Issues
4. **Primitive Obsession**
   - Location: Item class
   - Impact: Medium
   - Description: Using primitive types instead of objects
   - Refactoring: Create ItemType or ItemBehavior classes

5. **Feature Envy**
   - Location: [Specific method]
   - Impact: Medium
   - Description: [Method manipulates another class's data more than its own]
   - Refactoring: Move method to appropriate class

### Low Priority Issues
6. **Comments as Deodorant**
   - Location: [If any explanatory comments exist]
   - Impact: Low
   - Description: Comments explaining complex logic
   - Refactoring: Refactor code to be self-explanatory

### Code Smell Summary
| Smell Type | Count | Priority |
|------------|-------|----------|
| Long Method | X | Critical |
| Switch Statements | X | Critical |
| Magic Numbers | X | High |
| Primitive Obsession | X | Medium |
| Feature Envy | X | Medium |
| Duplicated Code | X | Medium |
| **Total Smells** | **X** | |

---

## 🎯 EDGE CASES & RISK AREAS

### Critical Edge Cases
| # | Edge Case | Current Handling | Test Required | Priority |
|---|-----------|------------------|---------------|----------|
| 1 | Quality = 0 with further degradation | [How handled] | ✅ | High |
| 2 | Quality = 50 with further improvement | [How handled] | ✅ | High |
| 3 | SellIn = 0 (transition day) | [How handled] | ✅ | High |
| 4 | Backstage pass at concert (sellIn = 0) | [How handled] | ✅ | High |
| 5 | Backstage pass quality approaching 50 with +3 | [How handled] | ✅ | High |
| 6 | Item with negative sellIn | [How handled] | ✅ | Medium |
| 7 | Item name case sensitivity | [How handled] | ✅ | Medium |
| 8 | Multiple items in same update | [How handled] | ✅ | Medium |
| 9 | Empty item list | [How handled] | ✅ | Low |
| 10 | Very large quality/sellIn values | [How handled] | ✅ | Low |

### Risk Assessment
- 🔴 **High Risk**: Edge cases that could cause incorrect calculations
- 🟡 **Medium Risk**: Edge cases that might cause unexpected behavior
- 🟢 **Low Risk**: Edge cases that are well-handled

**Total Edge Cases Identified**: XX
**High Priority Cases**: X
**Test Coverage Required**: XX scenarios

---

## 📊 CURRENT TEST COVERAGE ANALYSIS

### Existing Tests (if any)
- **Test Files**: [List existing test files]
- **Test Count**: [Number of tests]
- **Estimated Coverage**: [Percentage or "Unknown"]

### Current Test Inventory
| Test Name | Coverage | Item Type | Status |
|-----------|----------|-----------|--------|
| [test name] | [What it tests] | [Type] | ✅/⚠️ |

### Coverage Gaps Identified
- ❌ **Missing**: Normal item after sell date
- ❌ **Missing**: Aged Brie quality cap
- ❌ **Missing**: Sulfuras immutability
- ❌ **Missing**: Backstage pass threshold transitions
- ❌ **Missing**: Backstage pass drop to zero
- ❌ **Missing**: Conjured items (if implemented)
- ❌ **Missing**: Boundary conditions (quality 0, 50, 80)
- ❌ **Missing**: Negative sellIn handling

**Estimated Gap**: XX% of code paths untested

---

## 💰 TECHNICAL DEBT ASSESSMENT

### Maintainability Score: X/10
**Justification**: [How easy is it to modify the code?]
- Issues: [List specific maintainability issues]
- Impact: [How this affects maintenance work]

### Readability Score: X/10
**Justification**: [How clear is the code's intent?]
- Issues: [Unclear variable names, complex logic, etc.]
- Impact: [How this affects understanding]

### Testability Score: X/10
**Justification**: [How easy is it to test the code?]
- Issues: [Tightly coupled, hard to mock, etc.]
- Impact: [How this affects test creation]

### Extensibility Score: X/10
**Justification**: [How easy is it to add new features?]
- Issues: [Open/Closed principle violations, etc.]
- Impact: [How this affects adding new item types]

### Overall Technical Debt Score: X/10
**Interpretation**:
- 1-3: Severe debt, major refactoring needed
- 4-6: Moderate debt, targeted improvements needed
- 7-8: Acceptable debt, minor improvements beneficial
- 9-10: Low debt, well-maintained code

**Debt Category**: [High/Medium/Low]

**Estimated Refactoring Effort**: [Hours/Days]

---

## 🎯 PRIORITIZED RECOMMENDATIONS

### Phase 1: Foundation (TEST Mode)
1. **Generate comprehensive unit tests**
   - Target: 100% line and branch coverage
   - Priority: Critical
   - Estimated effort: [Hours]

### Phase 2: Refactoring (REFACTOR Mode)
2. **Extract named constants**
   - Replace magic numbers
   - Priority: High
   - Estimated effort: [Hours]

3. **Apply Strategy Pattern**
   - Create item-specific updaters
   - Priority: High
   - Estimated effort: [Hours]

4. **Extract helper methods**
   - Quality adjustment methods
   - Priority: Medium
   - Estimated effort: [Hours]

5. **Simplify conditionals**
   - Replace with polymorphism
   - Priority: High
   - Estimated effort: [Hours]

### Phase 3: Documentation (BDD Mode)
6. **Create BDD scenarios**
   - Gherkin feature files
   - Priority: Medium
   - Estimated effort: [Hours]

---

## 📈 SUCCESS METRICS

### Target Metrics (Post-Refactoring)
| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Test Coverage | X% | 100% | +XX% |
| Cyclomatic Complexity | XX | < 5 | -XX |
| Method Length | XX lines | < 20 lines | -XX |
| Code Duplication | XX% | < 5% | -XX% |
| Code Smells | X | 0 | -X |

---

## 🚀 NEXT STEPS

1. ✅ **Complete Analysis** - DONE
2. ⏭️ **Generate Unit Tests** - Ready to start with `/test`
3. ⏭️ **Refactor Codebase** - After tests complete
4. ⏭️ **Create BDD Scenarios** - After refactoring

**Status**: Analysis phase complete, ready for TEST mode

---

## 📝 NOTES

[Any additional observations, concerns, or insights]

---

## APPENDIX: Code Snippets

### Current Implementation (Simplified)
```[language]
[Include relevant code snippets showing current implementation]
```

### Identified Patterns
```[language]
[Show repeated patterns or duplicated code]
```

---

_Generated by Gilded Rose Quality Framework - ANALYZE Mode_
_Date: [Timestamp]_
