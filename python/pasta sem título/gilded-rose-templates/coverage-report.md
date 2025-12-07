# Test Coverage Report Template

## PROJECT INFORMATION
- **Repository**: [URL or path]
- **Language**: [Programming language]
- **Test Framework**: [JUnit, pytest, NUnit, etc.]
- **Coverage Tool**: [JaCoCo, Coverage.py, etc.]
- **Date**: [Report date]

---

## 📊 COVERAGE SUMMARY

### Overall Coverage Metrics
```
================================
FINAL COVERAGE REPORT
================================
Total Lines: XXX
Covered Lines: XXX
Line Coverage: 100% ✅

Total Branches: XXX
Covered Branches: XXX
Branch Coverage: 100% ✅

Total Methods: XXX
Covered Methods: XXX
Method Coverage: 100% ✅

Uncovered Lines: 0
Uncovered Branches: 0
================================
STATUS: ✅ 100% COVERAGE ACHIEVED
================================
```

### Coverage by File
| File | Line Coverage | Branch Coverage | Method Coverage | Status |
|------|---------------|-----------------|-----------------|--------|
| gilded_rose.[ext] | 100% (XX/XX) | 100% (XX/XX) | 100% (X/X) | ✅ |
| item.[ext] | 100% (XX/XX) | N/A | 100% (X/X) | ✅ |
| [updaters].[ext] | 100% (XX/XX) | 100% (XX/XX) | 100% (X/X) | ✅ |

---

## 🧪 TEST SUITE OVERVIEW

### Test Statistics
| Metric | Count |
|--------|-------|
| Total Test Files | X |
| Total Test Suites/Classes | X |
| Total Test Cases | XX |
| Passing Tests | XX ✅ |
| Failing Tests | 0 ✅ |
| Skipped Tests | 0 ✅ |
| Total Assertions | XXX |
| Execution Time | X.XXs |

### Test Organization
```
test_gilded_rose.[ext]
├── TestNormalItems (X tests)
├── TestAgedBrie (X tests)
├── TestSulfuras (X tests)
├── TestBackstagePasses (X tests)
├── TestConjuredItems (X tests)
└── TestEdgeCases (X tests)
```

---

## ✅ TEST SCENARIO COVERAGE

### Normal Items (X tests)
- ✅ Quality decreases by 1 before sell date
- ✅ Quality decreases by 2 after sell date
- ✅ Quality never goes negative
- ✅ SellIn decreases by 1 per day
- ✅ Quality at 0 remains at 0
- ✅ Multiple days progression
- ✅ [Additional scenarios]

**Coverage**: 100% of normal item logic

### Aged Brie (X tests)
- ✅ Quality increases by 1 before sell date
- ✅ Quality increases by 2 after sell date
- ✅ Quality caps at 50
- ✅ Quality at 50 remains at 50
- ✅ Quality at 49 before sell date (caps at 50)
- ✅ Quality at 49 after sell date (caps at 50)
- ✅ [Additional scenarios]

**Coverage**: 100% of Aged Brie logic

### Sulfuras - Legendary (X tests)
- ✅ Quality never changes
- ✅ Quality always equals 80
- ✅ SellIn never changes
- ✅ Behavior over multiple days
- ✅ [Additional scenarios]

**Coverage**: 100% of Sulfuras logic

### Backstage Passes (X tests)
- ✅ Quality +1 when sellIn > 10
- ✅ Quality +2 when sellIn = 10
- ✅ Quality +2 when 6 ≤ sellIn ≤ 10
- ✅ Quality +3 when sellIn = 5
- ✅ Quality +3 when 1 ≤ sellIn ≤ 5
- ✅ Quality drops to 0 when sellIn < 0
- ✅ Quality caps at 50
- ✅ Quality at 48 with sellIn = 5 (caps at 50)
- ✅ Quality at 49 with sellIn = 10 (caps at 50)
- ✅ [Additional scenarios]

**Coverage**: 100% of Backstage pass logic

### Conjured Items (X tests) - If Implemented
- ✅ Quality decreases by 2 before sell date
- ✅ Quality decreases by 4 after sell date
- ✅ Quality never goes negative
- ✅ Quality at 1 before sell date (becomes 0)
- ✅ [Additional scenarios]

**Coverage**: 100% of Conjured item logic

### Edge Cases & Boundaries (X tests)
- ✅ Item at quality 0 with degradation
- ✅ Item at quality 50 with improvement
- ✅ Item at quality 1 after sell date
- ✅ Item at quality 49 increasing by 2
- ✅ Backstage pass at sellIn = 0
- ✅ Multiple items in same update
- ✅ Empty item list
- ✅ Very large sellIn values
- ✅ Very negative sellIn values
- ✅ [Additional edge cases]

**Coverage**: 100% of edge cases identified in analysis

---

## 📋 TEST SCENARIO MATRIX

| Item Type | Scenario Category | Test Count | Branch Coverage | Status |
|-----------|-------------------|------------|-----------------|--------|
| Normal | Before sell date | X | 100% | ✅ |
| Normal | After sell date | X | 100% | ✅ |
| Normal | Boundaries (0, 50) | X | 100% | ✅ |
| Aged Brie | Before sell date | X | 100% | ✅ |
| Aged Brie | After sell date | X | 100% | ✅ |
| Aged Brie | Quality cap (50) | X | 100% | ✅ |
| Sulfuras | Immutability | X | 100% | ✅ |
| Backstage | >10 days | X | 100% | ✅ |
| Backstage | 6-10 days | X | 100% | ✅ |
| Backstage | 1-5 days | X | 100% | ✅ |
| Backstage | After concert | X | 100% | ✅ |
| Backstage | Quality cap (50) | X | 100% | ✅ |
| Conjured | Before/after sell | X | 100% | ✅ |
| Edge Cases | Boundaries | X | 100% | ✅ |
| **TOTAL** | **All Categories** | **XX** | **100%** | **✅** |

---

## 🎯 BRANCH COVERAGE DETAILS

### Conditional Branches Tested
| Condition | True Branch | False Branch | Status |
|-----------|-------------|--------------|--------|
| sellIn < 0 | ✅ Tested | ✅ Tested | ✅ |
| quality > 0 | ✅ Tested | ✅ Tested | ✅ |
| quality < 50 | ✅ Tested | ✅ Tested | ✅ |
| item type == "Aged Brie" | ✅ Tested | ✅ Tested | ✅ |
| item type == "Sulfuras" | ✅ Tested | ✅ Tested | ✅ |
| item type == "Backstage passes" | ✅ Tested | ✅ Tested | ✅ |
| sellIn <= 10 (Backstage) | ✅ Tested | ✅ Tested | ✅ |
| sellIn <= 5 (Backstage) | ✅ Tested | ✅ Tested | ✅ |
| [Additional conditions] | ✅ Tested | ✅ Tested | ✅ |

**Total Branches**: XX
**Branches Covered**: XX
**Branch Coverage**: 100% ✅

---

## 🔍 COVERAGE VALIDATION

### Uncovered Code
```
No uncovered lines or branches detected ✅
```

### Coverage Tool Output
```
[Paste actual coverage tool output here]

Example for Python:
---------- coverage: platform darwin, python 3.x -----------
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
gilded_rose.py           XX      0   100%
item.py                  XX      0   100%
---------------------------------------------------
TOTAL                    XX      0   100%
```

### Coverage Report Screenshots
*[Attach or link to coverage report HTML/screenshots]*
- Line coverage report: [Link or screenshot]
- Branch coverage report: [Link or screenshot]

---

## ✅ TEST QUALITY ASSESSMENT

### Test Quality Metrics
| Quality Attribute | Assessment | Notes |
|-------------------|------------|-------|
| **Descriptive Names** | ✅ Pass | All tests have clear, intention-revealing names |
| **Single Responsibility** | ✅ Pass | Each test focuses on one concept |
| **Independence** | ✅ Pass | Tests can run in any order |
| **Fast Execution** | ✅ Pass | Total suite runs in < Xs |
| **No Test Smells** | ✅ Pass | No magic numbers, fragile tests, or unclear assertions |
| **AAA Pattern** | ✅ Pass | Arrange-Act-Assert structure followed |
| **Comprehensive** | ✅ Pass | All edge cases and boundaries covered |

### Test Smell Check
- ❌ No magic numbers in tests (using named constants) ✅
- ❌ No test interdependencies ✅
- ❌ No obscure test intent ✅
- ❌ No fragile assertions ✅
- ❌ No excessive setup ✅
- ❌ No slow tests (all < 50ms) ✅

**Test Quality Score**: 10/10 ✅

---

## 📈 COVERAGE PROGRESSION

### Coverage History
| Date | Line Coverage | Branch Coverage | Test Count |
|------|---------------|-----------------|------------|
| [Initial] | 0% | 0% | 0 |
| [After core tests] | XX% | XX% | XX |
| [After edge cases] | XX% | XX% | XX |
| [Final] | 100% ✅ | 100% ✅ | XX ✅ |

---

## 🚀 MUTATION TESTING (Optional)

*If mutation testing was performed:*

### Mutation Score
```
Mutants Generated: XXX
Mutants Killed: XXX
Mutants Survived: X
Mutation Score: XX%
```

### Survived Mutants
| Mutant | Location | Test Gap | Action Required |
|--------|----------|----------|-----------------|
| [Description] | Line XX | [What's missing] | [Add test for...] |

**Mutation Testing Status**: [✅ Passed / ⚠️ Needs improvement]

---

## 📝 TEST EXAMPLES

### Sample Test: Normal Item Quality Degradation
```[language]
test_normalItem_qualityDecreasesByOne_beforeSellDate():
    # ARRANGE
    item = Item("Normal Item", sellIn=5, quality=10)
    gilded_rose = GildedRose([item])
    
    # ACT
    gilded_rose.update_quality()
    
    # ASSERT
    assert item.quality == 9
    assert item.sellIn == 4
```

### Sample Test: Backstage Pass Quality Spike
```[language]
test_backstagePass_qualityIncreasesBy3_whenFiveDaysOrLess():
    # ARRANGE
    item = Item("Backstage passes to a TAFKAL80ETC concert", sellIn=5, quality=20)
    gilded_rose = GildedRose([item])
    
    # ACT
    gilded_rose.update_quality()
    
    # ASSERT
    assert item.quality == 23
    assert item.sellIn == 4
```

### Sample Test: Boundary Condition
```[language]
test_agedBrie_qualityCapsAt50_whenIncreasing():
    # ARRANGE
    item = Item("Aged Brie", sellIn=5, quality=49)
    gilded_rose = GildedRose([item])
    
    # ACT
    gilded_rose.update_quality()
    
    # ASSERT
    assert item.quality == 50  # Caps at 50, not 51
    assert item.sellIn == 4
```

---

## ✅ COMPLETION CHECKLIST

- ✅ All business rules have corresponding tests
- ✅ 100% line coverage achieved
- ✅ 100% branch coverage achieved
- ✅ All edge cases tested
- ✅ All boundary values tested
- ✅ Tests follow AAA pattern
- ✅ Test names are descriptive
- ✅ No test smells present
- ✅ All tests passing
- ✅ Fast execution time (< Xs)
- ✅ Coverage report generated and documented
- ✅ Ready for refactoring phase

---

## 🎯 NEXT STEPS

**Current Status**: TEST mode complete ✅

**Ready for**: REFACTOR mode
- All behavior now protected by comprehensive tests
- Safe to refactor knowing tests will catch regressions
- Use `/refactor` command to proceed

---

## 📎 APPENDIX

### Test Execution Logs
```
[Include test runner output]
```

### Coverage Command
```bash
# Command used to generate coverage
[e.g., pytest --cov=gilded_rose --cov-report=html]
```

### Environment
- OS: [Operating system]
- Language Version: [Version]
- Test Framework Version: [Version]
- Coverage Tool Version: [Version]

---

_Generated by Gilded Rose Quality Framework - TEST Mode_
_Date: [Timestamp]_
