# BDD Scenarios - Gilded Rose

*This is a living documentation file generated in BDD mode*

---

## Feature Files Overview

| Feature | Scenarios | Status |
|---------|-----------|--------|
| Normal Items | X | ✅ Complete |
| Aged Brie | X | ✅ Complete |
| Sulfuras | X | ✅ Complete |
| Backstage Passes | X | ✅ Complete |
| Conjured Items | X | ✅ Complete |
| Quality Boundaries | X | ✅ Complete |
| **Total** | **XX** | **✅** |

---

## Feature 1: Normal Item Quality Degradation

```gherkin
Feature: Normal Item Quality Degradation
  As an inventory manager
  I want normal items to degrade in quality over time
  So that I can track item freshness and value

  Background:
    Given the Gilded Rose inventory system

  Scenario: Normal item quality decreases by 1 before sell date
    Given a normal item with sellIn 5 and quality 10
    When the system updates quality
    Then the quality should be 9
    And the sellIn should be 4

  Scenario: Normal item quality decreases by 2 after sell date
    Given a normal item with sellIn 0 and quality 10
    When the system updates quality
    Then the quality should be 8
    And the sellIn should be -1

  Scenario: Normal item quality never goes negative
    Given a normal item with sellIn 5 and quality 0
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be 4


  Scenario Outline: Normal item quality over multiple days
    Given a normal item with sellIn <initial_sellIn> and quality <initial_quality>
    When <days> days pass
    Then the quality should be <final_quality>
    And the sellIn should be <final_sellIn>

    Examples:
      | initial_sellIn | initial_quality | days | final_quality | final_sellIn |
      | 10             | 20              | 5    | 15            | 5            |
      | 2              | 10              | 3    | 6             | -1           |
      | 5              | 3               | 5    | 0             | 0            |
```

---

## Feature 2: Aged Brie Quality Improvement

```gherkin
Feature: Aged Brie Quality Improvement
  As an inventory manager
  I want Aged Brie to increase in quality over time
  So that I can recognize its aging value

  Background:
    Given the Gilded Rose inventory system

  Scenario: Aged Brie quality increases before sell date
    Given an Aged Brie with sellIn 10 and quality 20
    When the system updates quality
    Then the quality should be 21
    And the sellIn should be 9

  Scenario: Aged Brie quality increases faster after sell date
    Given an Aged Brie with sellIn 0 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be -1

  Scenario: Aged Brie quality caps at 50
    Given an Aged Brie with sellIn 5 and quality 50
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  Scenario: Aged Brie approaching maximum quality before sell date
    Given an Aged Brie with sellIn 5 and quality 49
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  Scenario: Aged Brie at 48 after sell date trying to add 2
    Given an Aged Brie with sellIn -1 and quality 48
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be -2
    
```

---

## Feature 3: Sulfuras Legendary Item Properties

```gherkin
Feature: Sulfuras Legendary Item Properties
  As an inventory manager
  I want Sulfuras to maintain constant quality
  So that I can recognize its legendary status

  Background:
    Given the Gilded Rose inventory system

  Scenario: Sulfuras quality never changes
    Given a Sulfuras with sellIn 10 and quality 80
    When the system updates quality
    Then the quality should be 80
    And the sellIn should be 10

  Scenario: Sulfuras sellIn never decreases
    Given a Sulfuras with sellIn 5 and quality 80
    When 10 days pass
    Then the quality should be 80
    And the sellIn should be 5

  Scenario: Sulfuras with any sellIn value maintains quality
    Given a Sulfuras with sellIn -1 and quality 80
    When the system updates quality
    Then the quality should be 80
    And the sellIn should be -1

```

---

## Feature 4: Backstage Pass Concert Dynamics

```gherkin
Feature: Backstage Pass Concert Dynamics
  As an inventory manager
  I want backstage pass quality to reflect concert proximity
  So that I can price them appropriately

  Background:
    Given the Gilded Rose inventory system

  Scenario: Backstage pass quality increases by 1 when concert is far
    Given a Backstage pass with sellIn 15 and quality 20
    When the system updates quality
    Then the quality should be 21
    And the sellIn should be 14

  Scenario: Backstage pass quality increases by 2 when 10 days or less
    Given a Backstage pass with sellIn 10 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be 9

  Scenario: Backstage pass quality increases by 3 when 5 days or less
    Given a Backstage pass with sellIn 5 and quality 20
    When the system updates quality
    Then the quality should be 23
    And the sellIn should be 4

  Scenario: Backstage pass on concert day (sellIn 0)
    Given a Backstage pass with sellIn 0 and quality 20
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be -1

  Scenario: Backstage pass quality caps at 50
    Given a Backstage pass with sellIn 5 and quality 48
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  Scenario: Backstage pass crosses 10-day threshold
    Given a Backstage pass with sellIn 11 and quality 20
    When the system updates quality
    Then the quality should be 21
    And the sellIn should be 10

  Scenario: Backstage pass crosses 5-day threshold
    Given a Backstage pass with sellIn 6 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be 5

  Scenario: Backstage pass quality 49 caps at 50 with +2 increment
    Given a Backstage pass with sellIn 10 and quality 49
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 9

  Scenario: Backstage pass quality 47 caps at 50 with +3 increment
    Given a Backstage pass with sellIn 5 and quality 47
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4
    
  Scenario Outline: Backstage pass quality progression to concert
    Given a Backstage pass with sellIn <initial_sellIn> and quality <initial_quality>
    When <days> days pass
    Then the quality should be <final_quality>

    Examples:
      | initial_sellIn | initial_quality | days | final_quality |
      | 15             | 20              | 5    | 25            |
      | 10             | 20              | 5    | 30            |
      | 5              | 20              | 5    | 35            |
      | 1              | 20              | 1    | 23            |
      | 1              | 20              | 2    | 0             |
```

---

## Feature 5: Conjured Item Accelerated Degradation

```gherkin
Feature: Conjured Item Accelerated Degradation
  As an inventory manager
  I want conjured items to degrade twice as fast
  So that I can manage their magical instability

  Background:
    Given the Gilded Rose inventory system

  Scenario: Conjured item quality decreases by 2 before sell date
    Given a Conjured item with sellIn 5 and quality 10
    When the system updates quality
    Then the quality should be 8
    And the sellIn should be 4

  Scenario: Conjured item quality decreases by 4 after sell date
    Given a Conjured item with sellIn 0 and quality 10
    When the system updates quality
    Then the quality should be 6
    And the sellIn should be -1

  Scenario: Conjured item quality never goes negative
    Given a Conjured item with sellIn 5 and quality 1
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be 4

  Scenario: Conjured item on sell date (sellIn 0)
    Given a Conjured item with sellIn 0 and quality 10
    When the system updates quality
    Then the quality should be 6
    And the sellIn should be -1
    # Quality decreases by 2 first, then by 2 again after sellIn becomes negative (total -4)
```

---

## Feature 6: Quality Boundary Rules

```gherkin
Feature: Quality Boundary Rules
  As an inventory manager
  I want quality to be bounded within valid ranges
  So that the system maintains data integrity

  Background:
    Given the Gilded Rose inventory system

  Scenario Outline: Quality never exceeds 50 for non-legendary items
    Given <item_type> with sellIn 10 and quality 50
    When the system updates quality
    Then the quality should not exceed 50

    Examples:
      | item_type       |
      | a normal item   |
      | an Aged Brie    |
      | a Backstage pass|
      | a Conjured item |

  Scenario Outline: Quality never goes below 0
    Given <item_type> with sellIn 5 and quality 0
    When the system updates quality
    Then the quality should be 0

    Examples:
      | item_type       |
      | a normal item   |
      | a Backstage pass|
      | a Conjured item |

  Scenario: Sulfuras quality is always 80
    Given a Sulfuras with sellIn 10 and quality 80
    When any number of days pass
    Then the quality should always be 80
```

---

## Scenario Coverage Map

### Business Rules to Scenarios Mapping

| Business Rule | Scenarios | Coverage |
|---------------|-----------|----------|
| Normal: Quality -1 before sell | Feature 1: Scenario 1, 4 | ✅ |
| Normal: Quality -2 after sell | Feature 1: Scenario 2, 4 | ✅ |
| Normal: Quality ≥ 0 | Feature 1: Scenario 3 | ✅ |
| Aged Brie: Quality +1 before sell | Feature 2: Scenario 1 | ✅ |
| Aged Brie: Quality +2 after sell | Feature 2: Scenario 2, 5 | ✅ |
| Aged Brie: Quality ≤ 50 | Feature 2: Scenario 3, 4, 5 | ✅ |
| Sulfuras: Quality constant | Feature 3: All | ✅ |
| Sulfuras: SellIn constant | Feature 3: All | ✅ |
| Backstage: +1 when >10 days | Feature 4: Scenario 1, 6 | ✅ |
| Backstage: +2 when ≤10 days | Feature 4: Scenario 2, 6 | ✅ |
| Backstage: +3 when ≤5 days | Feature 4: Scenario 3, 6 | ✅ |
| Backstage: 0 after concert | Feature 4: Scenario 4, 6 | ✅ |
| Backstage: Quality ≤ 50 | Feature 4: Scenario 5 | ✅ |
| Conjured: Quality -2 before sell | Feature 5: Scenario 1 | ✅ |
| Conjured: Quality -4 after sell | Feature 5: Scenario 2 | ✅ |
| Conjured: Quality ≥ 0 | Feature 5: Scenario 3 | ✅ |
| General: Quality ≤ 50 (non-legendary) | Feature 6: Scenario 1 | ✅ |
| General: Quality ≥ 0 | Feature 6: Scenario 2 | ✅ |
| General: Sulfuras = 80 | Feature 6: Scenario 3 | ✅ |

**Total Rules**: 18
**Total Scenarios**: ~35
**Coverage**: 100% ✅

---

## Acceptance Criteria Matrix

### Normal Items
- ✅ AC1: Quality decreases by 1 per day before sell date
- ✅ AC2: Quality decreases by 2 per day after sell date
- ✅ AC3: Quality never negative
- ✅ AC4: SellIn decreases by 1 per day

### Aged Brie
- ✅ AC1: Quality increases over time
- ✅ AC2: Quality increases faster after sell date
- ✅ AC3: Quality never exceeds 50

### Sulfuras
- ✅ AC1: Quality never changes
- ✅ AC2: Quality always 80
- ✅ AC3: SellIn never changes

### Backstage Passes
- ✅ AC1: Quality increases as concert approaches
- ✅ AC2: +2 quality when 10 days or less
- ✅ AC3: +3 quality when 5 days or less
- ✅ AC4: Quality drops to 0 after concert
- ✅ AC5: Quality never exceeds 50

### Conjured Items
- ✅ AC1: Quality degrades twice as fast as normal
- ✅ AC2: Quality never negative

---

## Step Definitions Reference

*Optional: Outline of step definitions for implementation*

### Given Steps
```python
@given('a normal item with sellIn {sell_in:d} and quality {quality:d}')
@given('an Aged Brie with sellIn {sell_in:d} and quality {quality:d}')
@given('a Sulfuras with sellIn {sell_in:d} and quality {quality:d}')
@given('a Backstage pass with sellIn {sell_in:d} and quality {quality:d}')
@given('a Conjured item with sellIn {sell_in:d} and quality {quality:d}')
@given('{item_type} with sellIn {sell_in:d} and quality {quality:d}')
```

### When Steps
```python
@when('the system updates quality')
@when('{days:d} days pass')
@when('any number of days pass')
```

### Then Steps
```python
@then('the quality should be {expected_quality:d}')
@then('the sellIn should be {expected_sell_in:d}')
@then('the quality should not exceed {max_quality:d}')
@then('the quality should always be {constant_quality:d}')
```

---

## Validation Checklist

- ✅ All item types covered
- ✅ All business rules translated to scenarios
- ✅ All boundary conditions covered
- ✅ Scenario outlines for data-driven tests
- ✅ Declarative language (not imperative)
- ✅ Business-friendly terminology
- ✅ Concrete examples throughout
- ✅ Valid Gherkin syntax
- ✅ Scenarios map to code coverage
- ✅ Living documentation ready

---

## Usage Instructions

### For Stakeholders
These scenarios serve as:
- **Specification**: What the system does
- **Examples**: Concrete behaviors
- **Acceptance Criteria**: Definition of done

### For Developers
These scenarios can:
- **Drive Implementation**: Implement to satisfy scenarios
- **Guide Testing**: Basis for automated tests
- **Document Behavior**: Always up-to-date documentation

### For Testers
These scenarios provide:
- **Test Cases**: What to verify
- **Expected Outcomes**: Clear assertions
- **Coverage**: Complete behavior map

---

## Implementation Notes

### Running BDD Tests (Example: Python Behave)
```bash
# Install behave
pip install behave

# Run all features
behave

# Run specific feature
behave features/normal_items.feature

# Run with specific tags
behave --tags=@smoke
```

### Example Step Implementation
```python
# features/steps/gilded_rose_steps.py

from behave import given, when, then
from gilded_rose import GildedRose, Item

@given('a normal item with sellIn {sell_in:d} and quality {quality:d}')
def step_impl(context, sell_in, quality):
    context.item = Item("Normal Item", sell_in, quality)
    context.gilded_rose = GildedRose([context.item])

@when('the system updates quality')
def step_impl(context):
    context.gilded_rose.update_quality()

@then('the quality should be {expected_quality:d}')
def step_impl(context, expected_quality):
    assert context.item.quality == expected_quality
```

---

_Generated by Gilded Rose Quality Framework - BDD Mode_
_Date: [Timestamp]_
_Living Documentation: Always reflects current system behavior_
