# BDD Mode - Behavior-Driven Development Scenarios Prompt

## MODE DECLARATION
[MODE: BDD]

## OBJECTIVE
Create comprehensive Behavior-Driven Development (BDD) scenarios in Gherkin syntax that describe all business rules and behaviors of the Gilded Rose system in a format understandable by non-technical stakeholders.

---

## PREREQUISITES
✅ ANALYZE mode completed (business rules documented)
✅ Optional: REFACTOR mode completed (cleaner code to reference)

---

## BDD PRINCIPLES

### What is BDD?
BDD scenarios serve as:
- **Living Documentation**: Always up-to-date specification
- **Communication Tool**: Bridge between business and technical teams
- **Acceptance Criteria**: Definition of "done"
- **Test Specification**: Can drive automated tests

### Gherkin Format
- **Declarative, not imperative**: Describe WHAT, not HOW
- **Business language**: Avoid technical jargon
- **User perspective**: Focus on observable behavior
- **Examples**: Concrete scenarios, not abstract rules

---

## GHERKIN SYNTAX GUIDE

### Basic Structure
```gherkin
Feature: [Feature Name]
  [Optional: Feature description explaining business value]
  
  Scenario: [Scenario description]
    Given [precondition/context]
    When [action/event]
    Then [expected outcome]
    And [additional outcome]
```

### Scenario Outline (Data-Driven)
```gherkin
Scenario Outline: [Template description]
  Given [precondition with <parameter>]
  When [action with <parameter>]
  Then [outcome with <parameter>]
  
  Examples:
    | parameter1 | parameter2 | expected |
    | value1     | value2     | result1  |
    | value3     | value4     | result2  |
```

### Background (Shared Setup)
```gherkin
Feature: Item Quality Management

  Background:
    Given the Gilded Rose inventory system
    And the current date is [reference date]
```

---

## CRITICAL EDGE CASES CHECKLIST

### 🔴 Priority 1 - Must Have

#### Transition Days (sell_in = 0)
- ✅ Normal item on transition day → quality -2, sellIn becomes -1
- ✅ Aged Brie on transition day → quality +2, sellIn becomes -1
- ✅ Backstage pass on concert day → quality drops to 0, sellIn becomes -1
- ✅ Conjured on transition day → quality -4, sellIn becomes -1
- ✅ Sulfuras on any day → no changes

#### Backstage Pass Threshold Transitions
- ✅ Backstage crosses 11→10 threshold (should still get +1, not +2)
- ✅ Backstage crosses 6→5 threshold (should still get +2, not +3)

**Why critical?** Validates whether logic uses `sell_in` BEFORE or AFTER decrement.

#### Quality Cap with Multi-Increments
- ✅ Backstage quality 48 with +3 increment → caps at 50
- ✅ Backstage quality 49 with +2 increment → caps at 50
- ✅ Backstage quality 47 with +3 increment → caps at 50
- ✅ Aged Brie quality 49 with +2 increment → caps at 50

**Why critical?** Quality cap must work even when increment would exceed it.

### 🟡 Priority 2 - Should Have

#### Items Starting at Boundaries
- ✅ Aged Brie starting at quality 0 → increases to 1
- ✅ Backstage starting at quality 0 → increases by 1/2/3
- ✅ Normal item starting at quality 0 → stays at 0
- ✅ Items starting at quality 50 → don't exceed

#### Very Negative sell_in
- ✅ Normal item with sell_in -10 → still degrades by 2
- ✅ Aged Brie with sell_in -10 → still improves by 2
- ✅ Backstage with sell_in -10 → quality is 0

#### Conjured Edge Cases
- ✅ Conjured with quality 1 before sell → goes to 0, not negative
- ✅ Conjured with quality 2 after sell → goes to 0 (would be -2 without cap)

### Coverage Target
- ✅ **Minimum**: All Priority 1 scenarios (11 scenarios)
- ✅ **Recommended**: Priority 1 + Priority 2 (18+ scenarios)
- ✅ **Complete**: All edge cases + happy paths (~35-45 scenarios)

---

## 🚨 CRITICAL: BDD SCENARIO REQUIREMENTS (MANDATORY)

### ❌ PROHIBITED PATTERNS IN SCENARIOS

#### 1. Incomplete Assertions (NEVER DO THIS)
```gherkin
# ❌ WRONG - Only validates quality, ignores sell_in
Scenario: Normal item degrades
  Given a normal item with quality 10 and sellIn 5
  When we update quality
  Then the quality should be 9
  # MISSING: And the sellIn should be 4

# ✅ CORRECT - Validates ALL affected properties
Scenario: Normal item degrades before sell date
  Given a normal item with quality 10 and sellIn 5
  When we update quality
  Then the quality should be 9
  And the sellIn should be 4
  And the name should not change
```

**WHY CRITICAL**: Incomplete assertions let mutants survive. Tests must verify ALL state changes.

#### 2. Hardcoded Values Without Context
```gherkin
# ❌ WRONG - Magic numbers without meaning
Then the quality should be 50
Then the quality should be 80

# ✅ CORRECT - Use descriptive language
Then the quality should be at maximum (50)
Then the quality should remain at Sulfuras quality (80)
```

#### 3. Vague Scenario Descriptions
```gherkin
# ❌ WRONG - Unclear behavior
Scenario: Item updates correctly

# ✅ CORRECT - Specific behavior
Scenario: Normal item loses 1 quality per day before sell date
```

### ✅ MANDATORY PATTERNS FOR ALL SCENARIOS

#### Complete State Validation Template
```gherkin
Scenario: [Specific behavior being tested]
  Given [item type] with quality [value] and sellIn [value]
  When we update quality
  Then the quality should be [expected_value]
  And the sellIn should be [expected_value]
  And the name should not change
```

#### Multi-Day Scenarios Must Show Progression
```gherkin
Scenario: Aged Brie increases quality over multiple days
  Given an Aged Brie with quality 20 and sellIn 5
  When we update quality for 3 days
  Then the quality should be 23
  And the sellIn should be 2
  # Explanation: +1 quality per day = 20 + 3 = 23
```

---

## BDD SCENARIO CHECKLIST

### Core Item Types
- [ ] Normal items quality degradation scenarios
- [ ] Aged Brie quality improvement scenarios
- [ ] Sulfuras legendary item scenarios
- [ ] Backstage passes concert scenarios
- [ ] Conjured items scenarios (if implemented)

### Quality Boundaries
- [ ] Quality never exceeds 50 (except Sulfuras)
- [ ] Quality never goes below 0
- [ ] Sulfuras always at quality 80

### Time Progression
- [ ] Before sell date behaviors
- [ ] On sell date (day 0) behaviors
- [ ] After sell date behaviors
- [ ] Multiple day progression

### Edge Cases
- [ ] Items starting at quality 0
- [ ] Items starting at quality 50
- [ ] Items with negative sellIn
- [ ] Multiple items updating together

---

## FEATURE FILE STRUCTURE

### Feature 1: Normal Items
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

### Feature 2: Aged Brie
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

  Scenario: Aged Brie approaching maximum quality after sell date
    Given an Aged Brie with sellIn -1 and quality 49
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be -2
```

### Feature 3: Sulfuras (Legendary Item)
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

### Feature 4: Backstage Passes
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

  Scenario: Backstage pass becomes worthless after concert
    Given a Backstage pass with sellIn 0 and quality 20
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be -1

  Scenario: Backstage pass quality caps at 50
    Given a Backstage pass with sellIn 5 and quality 48
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

### Feature 5: Conjured Items (if applicable)
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
```

### Feature 6: Quality Boundaries
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

## WRITING EFFECTIVE SCENARIOS

### ✅ Good Practices

**Declarative Style**:
```gherkin
✅ When 5 days pass
❌ When I call updateQuality() 5 times
```

**Business Language**:
```gherkin
✅ Given a Backstage pass for a concert in 10 days
❌ Given an item with name="Backstage passes" and sellIn=10
```

**Concrete Examples**:
```gherkin
✅ Given an Aged Brie with quality 20
❌ Given an Aged Brie with some quality
```

**Single Concept**:
```gherkin
✅ Scenario: Quality increases by 1 before sell date
❌ Scenario: Quality changes and sellIn decreases and other things happen
```

### ❌ Anti-Patterns to Avoid

**Too Technical**:
```gherkin
❌ When I instantiate GildedRose with Item array
✅ When the system updates quality
```

**Implementation Details**:
```gherkin
❌ Then item.quality should equal 9
✅ Then the quality should be 9
```

**Vague Assertions**:
```gherkin
❌ Then the quality changes appropriately
✅ Then the quality should be 8
```

**Overly Complex**:
```gherkin
❌ Given 5 items of different types with various qualities...
✅ [Break into multiple focused scenarios]
```

---

## SCENARIO COVERAGE MATRIX

Track coverage to ensure completeness:

| Item Type | Scenarios | Coverage |
|-----------|-----------|----------|
| Normal Items | Quality -1 before sell, -2 after, never negative, multiple days | ✅ |
| Aged Brie | Quality +1 before sell, +2 after, caps at 50, approaching cap | ✅ |
| Sulfuras | Quality constant, sellIn constant, legendary status | ✅ |
| Backstage | +1/>10 days, +2/≤10 days, +3/≤5 days, drops to 0 after, caps at 50 | ✅ |
| Conjured | Quality -2 before sell, -4 after, never negative | ✅ |
| Boundaries | Max 50 (except Sulfuras), Min 0, Sulfuras always 80 | ✅ |

**Total Scenarios**: ~25-35 scenarios covering all rules

---

## OUTPUT FORMAT

### Directory Structure
```
features/
├── gilded_rose.feature (or split into multiple)
├── normal_items.feature
├── aged_brie.feature
├── sulfuras.feature
├── backstage_passes.feature
├── conjured_items.feature
└── quality_boundaries.feature
```

### Feature File Template
```gherkin
Feature: [Feature Name]
  [Business value description]
  
  Background:
    [Common setup]
  
  Scenario: [First scenario]
    Given [context]
    When [action]
    Then [outcome]
  
  Scenario: [Second scenario]
    ...
  
  Scenario Outline: [Data-driven template]
    Given [parameterized context]
    When [parameterized action]
    Then [parameterized outcome]
    
    Examples:
      | param1 | param2 | expected |
      | ...    | ...    | ...      |
```

---

## DELIVERABLE

Complete BDD specification including:
✅ Feature files in Gherkin syntax
✅ All business rules covered as scenarios
✅ Scenario outlines for data-driven tests
✅ Clear Given-When-Then structure
✅ Business-friendly language
✅ Concrete examples throughout
✅ Scenarios mapped to code coverage
✅ ~25-35 total scenarios

---

## VALIDATION CHECKLIST

Before considering BDD mode complete:

### Scenario Coverage
- [ ] All item types have dedicated scenarios
- [ ] All business rules translated to scenarios
- [ ] All boundary conditions covered
- [ ] Scenario outlines used for data-driven tests

### 🚫 Assertion Completeness (CRITICAL)
- [ ] **EVERY scenario validates BOTH quality AND sellIn** (not just quality)
- [ ] **EVERY scenario confirms item name doesn't change**
- [ ] **Multi-day scenarios show progression** with clear calculations
- [ ] **NO scenarios with only quality assertion** - must include sellIn
- [ ] **Edge cases validate all constraints** (max/min quality, Sulfuras constant)

### Edge Case Coverage
- [ ] All transition days (sell_in = 0) covered for each item type
- [ ] Backstage threshold crossings (11→10, 6→5) covered
- [ ] All quality cap scenarios with multi-increments covered
- [ ] No duplicate scenarios (sell_in=0 used correctly)
- [ ] Items starting at boundary values (0, 50) covered
- [ ] Very negative sell_in values tested

### Gherkin Quality
- [ ] Language is declarative, not imperative
- [ ] No technical implementation details leaked
- [ ] Examples are concrete and specific
- [ ] Gherkin syntax is valid
- [ ] Scenarios can serve as living documentation

### Python Code Quality (Step Definitions)
- [ ] No `(object)` inheritance in step definition files
- [ ] All string formatting uses f-strings
- [ ] All step definitions have docstrings
- [ ] No trailing whitespace
- [ ] No else-after-return patterns
- [ ] Pylint score ≥ 9.0/10
- [ ] Flake8 reports zero warnings

---

## PYTHON 3 STEP DEFINITIONS BEST PRACTICES

### MANDATORY: Use Constants Module

**Step definitions MUST use constants.py for all item names and magic values.**

```python
# constants.py (REQUIRED)
\"\"\"Constants for Gilded Rose business rules.\"\"\"

# Item names
NORMAL_ITEM = \"Normal Item\"
AGED_BRIE = \"Aged Brie\"
BACKSTAGE_PASSES = \"Backstage passes to a TAFKAL80ETC concert\"
SULFURAS = \"Sulfuras, Hand of Ragnaros\"
CONJURED = \"Conjured\"

# Quality constraints
MAX_QUALITY = 50
MIN_QUALITY = 0
SULFURAS_QUALITY = 80

# steps.py - CORRECT Usage
from constants import AGED_BRIE, MAX_QUALITY, SULFURAS, SULFURAS_QUALITY

@given('an Aged Brie with sellIn {sell_in:d} and quality {quality:d}')
def step_aged_brie(context, sell_in, quality):
    \"\"\"Create an Aged Brie item.\"\"\"
    context.items = [Item(AGED_BRIE, sell_in, quality)]  # ✅ Use constant
    context.gilded_rose = GildedRose(context.items)

@then('the quality should be at maximum')
def step_quality_at_max(context):
    \"\"\"Verify quality is at maximum allowed value.\"\"\"
    actual = context.items[0].quality
    assert actual == MAX_QUALITY, \
        f\"Quality should be capped at {MAX_QUALITY}, got {actual}\"  # ✅ Use constant

@given('a Sulfuras with sellIn {sell_in:d}')
def step_sulfuras(context, sell_in):
    \"\"\"Create a Sulfuras item (always quality 80).\"\"\"
    context.items = [Item(SULFURAS, sell_in, SULFURAS_QUALITY)]  # ✅ Use constants
    context.gilded_rose = GildedRose(context.items)
```

### MANDATORY: Complete Assertions

**Every step validation MUST check ALL affected properties:**

```python
# ❌ WRONG - Incomplete assertion
@then('the quality should be {expected:d}')
def step_check_quality(context, expected):
    assert context.items[0].quality == expected

# ✅ CORRECT - Validates quality + sellIn + name
@then('the quality should be {quality:d} and sellIn should be {sell_in:d}')
def step_check_complete_state(context, quality, sell_in):
    \"\"\"Verify both quality and sellIn values.\"\"\"
    item = context.items[0]
    assert item.quality == quality, \
        f\"Quality: expected {quality}, got {item.quality}\"
    assert item.sell_in == sell_in, \
        f\"SellIn: expected {sell_in}, got {item.sell_in}\"

@then('the item name should not change')
def step_name_unchanged(context):
    \"\"\"Verify item name remains constant.\"\"\"
    original_name = context.original_name
    current_name = context.items[0].name
    assert current_name == original_name, \
        f\"Name changed from '{original_name}' to '{current_name}'\"
```

### Modern Python 3 Style

When creating Python step definitions, follow these modern practices:

```python
# ❌ BAD - Old Python 2 style
class StepContext(object):  # Unnecessary (object)
    pass

@then('the quality should be {quality}')
def check_quality(context, quality):
    msg = "Expected %s but got %s" % (quality, context.item.quality)  # Old formatting
    assert context.item.quality == int(quality), msg

# ✅ GOOD - Modern Python 3 style
class StepContext:
    """Context holder for step definitions."""
    pass

@then('the quality should be {quality}')
def check_quality(context, quality):
    """Verify item quality matches expected value."""
    expected = int(quality)
    actual = context.item.quality
    msg = f"Expected {expected} but got {actual}"
    assert actual == expected, msg
```

---

## OPTIONAL: STEP DEFINITIONS OUTLINE

While not required, you can outline step definitions for reference:

```python
# Python behave example
@given('a normal item with sellIn {sell_in:d} and quality {quality:d}')
def step_impl(context, sell_in, quality):
    context.item = Item("Normal Item", sell_in, quality)

@when('the system updates quality')
def step_impl(context):
    gilded_rose = GildedRose([context.item])
    gilded_rose.update_quality()

@then('the quality should be {expected_quality:d}')
def step_impl(context, expected_quality):
    assert context.item.quality == expected_quality
```

---

## COMPLETION

BDD mode complete when:
- ✅ All feature files created
- ✅ All business rules covered
- ✅ Scenarios validated for clarity
- ✅ Documentation ready for stakeholder review

**Framework workflow complete! 🎉**

All three deliverables ready:
1. ✅ Unit tests with 100% coverage (TEST mode)
2. ✅ Refactored clean code (REFACTOR mode)
3. ✅ BDD scenarios (BDD mode)
