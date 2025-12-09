# TEST Mode - Unit Tests with 100% Coverage Prompt

## MODE DECLARATION
[MODE: TEST]

## OBJECTIVE
Generate a comprehensive unit test suite achieving:
- **100% code coverage** (line and branch)
- **Maximum mutation kill rate** (minimize surviving mutants)
- **Zero test smells** (clean, maintainable tests)
- **Test patterns applied** (Object Mother, Data Builder, Test Doubles)

The goal is NOT just coverage, but **effective tests that kill mutants and detect real bugs**.

---

## PREREQUISITES
✅ ANALYZE mode completed
✅ Business rules documented
✅ Edge cases identified
✅ Test framework available

## THEORETICAL FOUNDATION

### Mutation Testing Mindset
**Coverage ≠ Quality**. A test with 100% coverage can still miss bugs.

**Mutation Testing Principle**: Insert small bugs (mutants) in the code. If tests don't fail, they're weak.

**Goal**: Write assertions that would fail if the code logic changes (kill mutants).

**Example**:
```
// CODE
if (quality > 0) { quality--; }

// MUTANT (changes > to >=)
if (quality >= 0) { quality--; }

// WEAK TEST (doesn't kill mutant)
assert item.quality >= 0  // Still passes!

// STRONG TEST (kills mutant)
assert item.quality == 9  // Fails if logic changes!
```

**Key Insight**: Use **specific assertions**, not generic "greater than" checks.

---

## ANTI-PATTERNS: TEST SMELLS TO AVOID

### 🚫 Critical Test Smells (NEVER DO THIS)

#### 1. Mystery Guest
**Problem**: Test depends on external data (files, DB) whose content is invisible.
```
❌ BAD
const data = readJson('fixture.json'); // What's in this file?
assert result.total == 100;  // Magic number!

✅ GOOD
const invoice = { items: [{ price: 50 }, { price: 50 }] };
const result = process(invoice);
assert result.total == 100; // Clear where 100 comes from
```

#### 2. Fragile Test
**Problem**: Test coupled to implementation details, breaks on harmless refactoring.
```
❌ BAD
assert html == '<div><h1>Report</h1></div>'; // Breaks if tags change

✅ GOOD
assert html.contains('Report'); // Tests behavior, not structure
```

#### 3. Conditional Logic in Test
**Problem**: Tests with if/for/while are unpredictable and may test nothing.
```
❌ BAD
for (item in items) {
  if (item.type == 'URGENT') {
    assert item.processed == true; // What if no URGENT items?
  }
}

✅ GOOD
const urgentItem = { type: 'URGENT', processed: false };
process(urgentItem);
assert urgentItem.processed == true; // One scenario, one test
```

#### 4. Obscure Setup
**Problem**: Test setup is longer and more complex than the test itself.
```
❌ BAD
const addr = new Address("St", 123, "NY");
const client = new Client("John", "123", addr);
const item1 = new Item("A", 2, 50);
// ... 20 more lines of setup ...

✅ GOOD (using patterns below)
const item = ItemBuilder.aDefaultItem().build();
```

#### 5. Assertion Roulette
**Problem**: Multiple assertions without clear messages, can't tell which failed.
```
❌ BAD
assert item.quality == 10;
assert item.sellIn == 5;
assert item.name == "Aged Brie";

✅ GOOD
assert item.quality == 10, "Quality should be 10";
assert item.sellIn == 5, "SellIn should be 5";
assert item.name == "Aged Brie", "Name should be Aged Brie";
```

#### 6. The Giant / The Sleeper
**Problem**: Test is too long (hundreds of lines) or uses sleep/setTimeout.
```
❌ BAD
test('integration test') {
  // ... 200 lines ...
  sleep(5000); // Wait for async operation
}

✅ GOOD
test('specific behavior') {
  // ... 10 lines max ...
  await waitForCondition(() => item.processed); // Explicit wait
}
```

### Test Smell Checklist
Before committing tests, verify:
- [ ] No external file dependencies (Mystery Guest)
- [ ] No implementation details tested (Fragile Test)
- [ ] No if/for/while in tests (Conditional Logic)
- [ ] Setup is simple and clear (No Obscure Setup)
- [ ] Each assertion has descriptive message (No Assertion Roulette)
- [ ] Tests are short (< 20 lines) (No Giant)
- [ ] No sleep/setTimeout (No Sleeper)

---

## PYTHON 3 MODERN PRACTICES

When writing Python tests, enforce these modern standards:

### 1. NO Object Inheritance in Python 3
```python
# ❌ BAD - Unnecessary in Python 3
class TestGildedRose(object):
    pass

# ✅ GOOD - Clean Python 3 syntax
class TestGildedRose:
    pass
```

### 2. F-Strings for All String Formatting
```python
# ❌ BAD - Old-style formatting
def test_item_quality():
    assert item.quality == 10, "Expected %s, got %s" % (10, item.quality)

# ✅ GOOD - Modern f-strings
def test_item_quality():
    assert item.quality == 10, f"Expected 10, got {item.quality}"
```

### 3. Docstrings for Test Methods
```python
# ❌ BAD - No documentation
def test_aged_brie():
    item = Item("Aged Brie", 5, 10)
    # test code...

# ✅ GOOD - Clear docstring
def test_aged_brie():
    """Test that Aged Brie increases in quality before sell date."""
    item = Item("Aged Brie", 5, 10)
    # test code...
```

### 4. No Trailing Whitespace
Always configure your editor to remove trailing whitespace automatically.

### 5. Simplified Control Flow
```python
# ❌ BAD - Unnecessary else after return
def get_test_item(item_type):
    if item_type == "normal":
        return Item("Normal", 5, 10)
    else:
        return Item("Special", 5, 10)

# ✅ GOOD - No else needed
def get_test_item(item_type):
    if item_type == "normal":
        return Item("Normal", 5, 10)
    return Item("Special", 5, 10)
```

### Python Test Quality Checklist
- [ ] No `(object)` inheritance - all classes use clean Python 3 syntax
- [ ] All string formatting uses f-strings
- [ ] Every test method has a docstring
- [ ] No trailing whitespace in any file
- [ ] No else-after-return patterns
- [ ] Pylint score ≥ 9.0/10
- [ ] Flake8 reports zero warnings

### 🚫 Test Smell Prevention Checklist (CRITICAL)
- [ ] **ZERO code duplication** - ItemBuilder used in ALL tests
- [ ] **ZERO magic numbers** - All values from constants.py
- [ ] **ZERO hardcoded strings** - All item names from constants.py
- [ ] **ZERO obscure tests** - Multi-day tests have clear calculations
- [ ] **ZERO incomplete assertions** - All tests verify quality AND sell_in
- [ ] **100% builder usage** - No direct Item() instantiation in tests
- [ ] **All assertions have messages** - Explain expected vs actual

---

## 🚨 CRITICAL: TEST SMELL PREVENTION (MANDATORY)

### ❌ PROHIBITED PATTERNS - DO NOT GENERATE THESE

#### 1. Code Duplication - Setup Repetition
```python
# ❌ NEVER DO THIS - Repeated in every test
def test_normal_item():
    items = [Item("Normal Item", 5, 10)]  # Duplicated
    gilded_rose = GildedRose(items)       # Duplicated
    gilded_rose.update_quality()          # Duplicated
    assert items[0].quality == 9

def test_aged_brie():
    items = [Item("Aged Brie", 5, 10)]   # Duplicated again!
    gilded_rose = GildedRose(items)       # Duplicated again!
    gilded_rose.update_quality()          # Duplicated again!
    assert items[0].quality == 11
```

**WHY THIS IS CRITICAL**: 35 tests with duplicated setup = 140+ duplicated lines. Any constructor change requires editing 35+ files.

#### 2. Magic Numbers Without Context
```python
# ❌ NEVER DO THIS
assert item.quality == 50  # What is 50?
assert item.quality == 80  # What is 80?
assert item.sell_in == 0   # What is 0?

# ✅ ALWAYS DO THIS
MAX_QUALITY = 50
SULFURAS_QUALITY = 80
TRANSITION_DAY = 0

assert item.quality == MAX_QUALITY, f"Quality should not exceed {MAX_QUALITY}"
assert item.quality == SULFURAS_QUALITY, f"Sulfuras always at {SULFURAS_QUALITY}"
assert item.sell_in == TRANSITION_DAY, "Today is the sell date"
```

#### 3. Hardcoded Item Names
```python
# ❌ NEVER DO THIS
item = Item("Aged Brie", 5, 10)  # Typo risk, no reuse
item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)  # Unmaintainable

# ✅ ALWAYS DO THIS - Define constants module
# constants.py
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
NORMAL_ITEM = "Normal Item"

MAX_QUALITY = 50
SULFURAS_QUALITY = 80
MIN_QUALITY = 0

# In tests
from constants import AGED_BRIE, MAX_QUALITY
item = Item(AGED_BRIE, 5, 10)
```

#### 4. Obscure Multi-Day Tests
```python
# ❌ NEVER DO THIS
for _ in range(5):
    gilded_rose.update_quality()
assert item.quality == 25  # How did we get 25?

# ✅ ALWAYS DO THIS
INITIAL_QUALITY = 20
DAYS = 5
QUALITY_INCREASE_PER_DAY = 1

for day in range(1, DAYS + 1):
    gilded_rose.update_quality()
    expected = INITIAL_QUALITY + (day * QUALITY_INCREASE_PER_DAY)
    # Optional: intermediate assertions for clarity

expected_final = INITIAL_QUALITY + (DAYS * QUALITY_INCREASE_PER_DAY)
assert item.quality == expected_final, \
    f"After {DAYS} days at +{QUALITY_INCREASE_PER_DAY}/day: expected {expected_final}, got {item.quality}"
```

#### 5. Incomplete Assertions
```python
# ❌ NEVER DO THIS - Only validates quality
assert item.quality == 9

# ✅ ALWAYS DO THIS - Validate all affected properties
assert item.quality == 9, f"Quality should decrease by 1, got {item.quality}"
assert item.sell_in == 4, f"SellIn should decrease by 1, got {item.sell_in}"
assert item.name == NORMAL_ITEM, "Item name should not change"
```

### ✅ MANDATORY PATTERNS - YOU MUST USE THESE

#### REQUIRED #1: Test Data Builder (NON-NEGOTIABLE)

**YOU MUST implement ItemBuilder before writing any tests.**

```python
# test_builders.py (CREATE THIS FIRST)
from constants import NORMAL_ITEM, AGED_BRIE, BACKSTAGE_PASSES, SULFURAS

class ItemBuilder:
    """Builder for creating test Item instances with fluent API."""
    
    def __init__(self):
        self._name = NORMAL_ITEM
        self._sell_in = 5
        self._quality = 10
    
    @staticmethod
    def an_item():
        """Start building a new item."""
        return ItemBuilder()
    
    def with_name(self, name: str):
        """Set item name."""
        self._name = name
        return self
    
    def with_sell_in(self, sell_in: int):
        """Set sell_in days."""
        self._sell_in = sell_in
        return self
    
    def with_quality(self, quality: int):
        """Set quality value."""
        self._quality = quality
        return self
    
    # Convenience methods
    def as_aged_brie(self):
        """Configure as Aged Brie."""
        self._name = AGED_BRIE
        return self
    
    def as_backstage_pass(self):
        """Configure as Backstage Pass."""
        self._name = BACKSTAGE_PASSES
        return self
    
    def as_sulfuras(self):
        """Configure as Sulfuras."""
        self._name = SULFURAS
        self._quality = 80  # Sulfuras always 80
        return self
    
    def expired(self):
        """Set as expired (negative sell_in)."""
        self._sell_in = -1
        return self
    
    def at_max_quality(self):
        """Set quality to maximum."""
        self._quality = 50
        return self
    
    def at_min_quality(self):
        """Set quality to minimum."""
        self._quality = 0
        return self
    
    def build(self):
        """Build the Item instance."""
        return Item(self._name, self._sell_in, self._quality)

# Usage in tests - CLEAN AND READABLE
def test_normal_item_quality_decreases():
    """Normal items decrease quality by 1 before sell date."""
    item = ItemBuilder.an_item().build()  # Uses defaults
    gilded_rose = GildedRose([item])
    
    gilded_rose.update_quality()
    
    assert item.quality == 9

def test_aged_brie_increases():
    """Aged Brie increases in quality."""
    item = ItemBuilder.an_item().as_aged_brie().with_quality(20).build()
    gilded_rose = GildedRose([item])
    
    gilded_rose.update_quality()
    
    assert item.quality == 21

def test_expired_item_double_decay():
    """Expired items degrade twice as fast."""
    item = ItemBuilder.an_item().expired().build()
    gilded_rose = GildedRose([item])
    
    gilded_rose.update_quality()
    
    assert item.quality == 8  # Decreased by 2
```

#### REQUIRED #2: Constants Module

**YOU MUST create constants.py with all magic values.**

```python
# constants.py (CREATE THIS FIRST)
"""Constants for Gilded Rose business rules."""

# Item names
NORMAL_ITEM = "Normal Item"
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured"

# Quality constraints
MAX_QUALITY = 50
MIN_QUALITY = 0
SULFURAS_QUALITY = 80

# Time thresholds
TRANSITION_DAY = 0
BACKSTAGE_THRESHOLD_1 = 10  # +2 quality
BACKSTAGE_THRESHOLD_2 = 5   # +3 quality

# Quality changes
NORMAL_DEGRADATION = 1
EXPIRED_MULTIPLIER = 2
AGED_BRIE_INCREASE = 1
BACKSTAGE_BASE_INCREASE = 1
BACKSTAGE_MEDIUM_INCREASE = 2
BACKSTAGE_HIGH_INCREASE = 3
```

#### REQUIRED #3: Base Test Class with setUp

```python
import unittest
from gilded_rose import GildedRose
from test_builders import ItemBuilder
from constants import *

class GildedRoseTestBase(unittest.TestCase):
    """Base class for Gilded Rose tests with common setup."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.builder = ItemBuilder()
    
    def update_quality(self, item, days=1):
        """Helper to update quality for specified days."""
        gilded_rose = GildedRose([item])
        for _ in range(days):
            gilded_rose.update_quality()
        return item
    
    def assert_item_state(self, item, expected_quality, expected_sell_in, message=""):
        """Assert both quality and sell_in values."""
        self.assertEqual(expected_quality, item.quality, 
                        f"{message} - Quality mismatch")
        self.assertEqual(expected_sell_in, item.sell_in,
                        f"{message} - SellIn mismatch")

# Usage
class TestNormalItems(GildedRoseTestBase):
    def test_quality_decreases_before_sell_date(self):
        """Normal items lose 1 quality per day before sell date."""
        item = self.builder.an_item().with_quality(10).with_sell_in(5).build()
        
        self.update_quality(item)
        
        self.assert_item_state(item, 9, 4, "After 1 day")
```

---

## TEST PATTERNS TO APPLY

### Pattern 1: Object Mother (Use with Builder)
**Purpose**: Centralize creation of complex test objects in reusable factories.

**When to use**: When multiple tests need the same complex object setup.

**Implementation**:
```language
class ItemMother {
    static createNormalItem() {
        return new Item("Normal Item", sellIn=5, quality=10);
    }
    
    static createAgedBrie() {
        return new Item("Aged Brie", sellIn=10, quality=20);
    }
    
    static createExpiredItem() {
        return new Item("Normal Item", sellIn=-1, quality=10);
    }
}

// Usage in tests
test_normalItem_decreases() {
    item = ItemMother.createNormalItem(); // Clean!
    updateQuality(item);
    assert item.quality == 9;
}
```

### Pattern 2: Data Builder (Preferred for flexibility)
**Purpose**: Create test objects with fluent API, customizing only what matters.

**When to use**: When you need variations of the same object type.

**Implementation**:
```language
class ItemBuilder {
    private name = "Normal Item";
    private sellIn = 5;
    private quality = 10;
    
    static anItem() {
        return new ItemBuilder();
    }
    
    withName(newName) {
        this.name = newName;
        return this;
    }
    
    withSellIn(newSellIn) {
        this.sellIn = newSellIn;
        return this;
    }
    
    withQuality(newQuality) {
        this.quality = newQuality;
        return this;
    }
    
    build() {
        return new Item(this.name, this.sellIn, this.quality);
    }
}

// Usage: Customize only what matters for each test
test_agedBrie_increases() {
    item = ItemBuilder.anItem()
                      .withName("Aged Brie")
                      .withQuality(20)
                      .build();
    
    updateQuality(item);
    assert item.quality == 21;
}

test_expiredItem_doubleDecay() {
    item = ItemBuilder.anItem()
                      .withSellIn(-1) // Only customize sellIn
                      .build();
    
    updateQuality(item);
    assert item.quality == 8; // Decreased by 2
}
```

### Pattern 3: Test Doubles (for dependencies)
**Purpose**: Isolate unit under test from external dependencies.

**Types**:
- **Dummy**: Passed but never used
- **Stub**: Returns canned responses
- **Spy**: Records how it was called
- **Mock**: Pre-programmed with expectations
- **Fake**: Working implementation (simplified)

**For Gilded Rose**: Typically not needed (no external dependencies), but know the pattern.

---

## TEST GENERATION CHECKLIST

### 1. MANDATORY INFRASTRUCTURE (DO THIS FIRST)
- [ ] **CREATE constants.py** with all item names and magic values
- [ ] **CREATE test_builders.py** with ItemBuilder class
- [ ] **CREATE base test class** with setUp() and helper methods
- [ ] Verify no hardcoded strings or magic numbers in infrastructure

### 2. TEST FRAMEWORK SETUP
- [ ] Identify appropriate test framework for language (JUnit, pytest, NUnit, etc.)
- [ ] Set up test file structure following conventions
- [ ] Import necessary testing utilities (including builders and constants)
- [ ] Configure test runner if needed

### 3. TEST ORGANIZATION STRATEGY
- [ ] Group tests by item type or feature
- [ ] Use descriptive test class/suite names
- [ ] Follow naming convention: `test_<scenario>_<expected_behavior>`
- [ ] All test classes inherit from base test class
- [ ] **USE ItemBuilder in EVERY test** (no direct Item() instantiation)

### 3. COVERAGE REQUIREMENTS

#### 100% Line Coverage
Every single line of source code must be executed at least once

#### 100% Branch Coverage  
Every conditional branch (if/else, switch cases) must be tested in both directions

#### Boundary Value Coverage
- [ ] Quality = 0 (minimum)
- [ ] Quality = 50 (maximum for most items)
- [ ] Quality = 80 (Sulfuras constant)
- [ ] SellIn = 0 (transition point)
- [ ] SellIn = 5 (backstage pass threshold)
- [ ] SellIn = 10 (backstage pass threshold)
- [ ] SellIn = negative values
- [ ] SellIn = large positive values

---

## TEST SCENARIOS BY ITEM TYPE

### NORMAL ITEMS
```
✅ Test: Normal item quality decreases by 1 before sell date
✅ Test: Normal item quality decreases by 2 after sell date
✅ Test: Normal item quality never goes negative
✅ Test: Normal item sellIn decreases by 1
✅ Test: Normal item with quality 0 stays at 0
✅ Test: Normal item quality after multiple days
```

### AGED BRIE
```
✅ Test: Aged Brie quality increases by 1 before sell date
✅ Test: Aged Brie quality increases by 2 after sell date
✅ Test: Aged Brie quality caps at 50
✅ Test: Aged Brie at quality 50 stays at 50
✅ Test: Aged Brie at quality 49 before sell date
✅ Test: Aged Brie at quality 49 after sell date (should cap at 50)
```

### SULFURAS (LEGENDARY)
```
✅ Test: Sulfuras quality never changes
✅ Test: Sulfuras quality is always 80
✅ Test: Sulfuras sellIn never changes
✅ Test: Sulfuras behavior over multiple days
```

### BACKSTAGE PASSES
```
✅ Test: Backstage pass quality +1 when sellIn > 10
✅ Test: Backstage pass quality +2 when sellIn = 10
✅ Test: Backstage pass quality +2 when 6 ≤ sellIn ≤ 10
✅ Test: Backstage pass quality +3 when sellIn = 5
✅ Test: Backstage pass quality +3 when 1 ≤ sellIn ≤ 5
✅ Test: Backstage pass quality drops to 0 when sellIn < 0
✅ Test: Backstage pass quality caps at 50
✅ Test: Backstage pass at quality 48 with sellIn = 5 (caps at 50, not 51)
✅ Test: Backstage pass at quality 49 with sellIn = 10 (caps at 50)
```

### CONJURED ITEMS (if implemented)
```
✅ Test: Conjured item quality decreases by 2 before sell date
✅ Test: Conjured item quality decreases by 4 after sell date
✅ Test: Conjured item quality never goes negative
✅ Test: Conjured item with quality 1 before sell date (becomes 0, not -1)
```

---

## TEST STRUCTURE TEMPLATE

### AAA Pattern (Arrange-Act-Assert)

```language
test_normalItem_qualityDecreasesByOne_beforeSellDate():
    # ARRANGE: Setup test data (use Builder or Mother)
    item = ItemBuilder.anItem()
                      .withSellIn(5)
                      .withQuality(10)
                      .build()
    
    # ACT: Execute the behavior under test
    update_quality(item)
    
    # ASSERT: Verify expected outcome with SPECIFIC values
    assert item.quality == 9, "Quality should decrease by 1"
    assert item.sellIn == 4, "SellIn should decrease by 1"
```

**Critical**: Separate Arrange, Act, Assert with blank lines for clarity.

### Mutation-Killing Assertions

**Weak Assertion** (mutants survive):
```
assert item.quality >= 0  // Too generic, mutants survive
```

**Strong Assertion** (kills mutants):
```
assert item.quality == 9  // Exact value, kills mutants
```

**Always prefer**:
- ✅ Exact equality (`==`)
- ✅ Specific values (not ranges)
- ✅ Multiple assertions covering all state changes

### Parameterized Tests (for data-driven scenarios)

```language
@parameterized([
    (sellIn=5, quality=10, expectedQuality=9),
    (sellIn=1, quality=10, expectedQuality=9),
    (sellIn=0, quality=10, expectedQuality=8),
    (sellIn=-1, quality=10, expectedQuality=8),
])
test_normalItem_qualityDegradation(sellIn, quality, expectedQuality):
    item = create_item("Normal", sellIn, quality)
    update_quality(item)
    assert item.quality == expectedQuality
```

---

## EDGE CASE TESTS

### Critical Boundaries
- [ ] Item at quality 0 with continued degradation
- [ ] Item at quality 50 with continued improvement
- [ ] Item at quality 1 after sell date (should become 0, not -1)
- [ ] Item at quality 49 that increases by 2 (should cap at 50)
- [ ] Backstage pass at sellIn = 0 (transitions to worthless)
- [ ] Multiple items in same update cycle
- [ ] Empty item list
- [ ] Item with very large sellIn value
- [ ] Item with very negative sellIn value

### Special Scenarios
- [ ] Item name variations (case, spacing): "aged brie" vs "Aged Brie"
- [ ] Multiple Sulfuras items
- [ ] Backstage pass exactly at concert date
- [ ] Zero quality items of each type
- [ ] Max quality items of each type

---

## TEST QUALITY STANDARDS

### ✅ Good Test Characteristics
- **Single Concept**: Tests ONE thing only
- **Descriptive Name**: Intent clear from name alone (`test_agedBrie_qualityIncreasesByOne_beforeSellDate`)
- **Independent**: No dependencies on other tests or execution order
- **Fast**: Executes in milliseconds (no I/O, no sleeps)
- **Repeatable**: Same result every time (deterministic)
- **Self-Validating**: Clear pass/fail (no manual interpretation)
- **AAA Structure**: Clear Arrange-Act-Assert separation
- **Specific Assertions**: Exact values, not ranges (`== 9`, not `>= 0`)
- **Descriptive Failures**: Messages explain what failed
- **No Test Smells**: Passes all smell checks above

### ❌ Test Smells to Avoid (DETAILED)
- **Mystery Guest**: External file dependencies ❌
- **Fragile Test**: Coupled to implementation details ❌
- **Conditional Logic**: if/for/while in tests ❌
- **Obscure Setup**: Complex, lengthy setup ❌
- **Assertion Roulette**: Assertions without messages ❌
- **The Giant**: Tests > 20 lines ❌
- **The Sleeper**: sleep/setTimeout usage ❌
- **Magic Numbers**: Unexplained values ❌
- **Generic Assertions**: `assertTrue(condition)` without context ❌
- **Excessive Setup**: Too much boilerplate ❌

---

## COVERAGE VALIDATION

### Steps to Verify 100% Coverage

1. **Run Coverage Tool**
   - JaCoCo (Java)
   - Coverage.py (Python)
   - coverlet (C#)
   - nyc/istanbul (JavaScript)

2. **Analyze Report**
   - Check line coverage percentage
   - Check branch coverage percentage
   - Identify uncovered lines
   - Identify uncovered branches

3. **Add Missing Tests**
   - Write tests for uncovered lines
   - Write tests for uncovered branches
   - Re-run coverage

4. **Document Results**
   - Screenshot or export coverage report
   - List final coverage metrics
   - Confirm 100% achievement

---

## MUTATION TESTING VALIDATION

### After achieving 100% coverage, verify mutation score

**Goal**: Kill as many mutants as possible (target: >80% mutation score)

### Common Mutation Operators (What gets changed)
1. **Arithmetic Operator Replacement**: `+` → `-`, `*` → `/`
2. **Relational Operator Replacement**: `>` → `>=`, `<` → `<=`, `==` → `!=`
3. **Logical Operator Replacement**: `&&` → `||`, `!` → ` `
4. **Conditional Boundary**: `>` → `>=`, `<` → `<=`
5. **Negate Conditionals**: `if (x)` → `if (!x)`
6. **Return Value Mutation**: `return true` → `return false`
7. **Void Method Call Removal**: Delete method calls
8. **Increment/Decrement**: `++` → `--`

### How to Kill Mutants

**Mutant Example**:
```
// ORIGINAL
if (quality > 0) { quality--; }

// MUTANT (changes > to >=)
if (quality >= 0) { quality--; }
```

**Weak Test** (doesn't kill):
```
item.quality = 0;
updateQuality(item);
assert item.quality >= 0; // Still passes with mutant! 😱
```

**Strong Test** (kills mutant):
```
item.quality = 0;
updateQuality(item);
assert item.quality == 0; // Fails with mutant! Quality would be -1! ✅
```

### Mutation Testing Checklist
- [ ] Run mutation testing tool (PIT, Stryker, mutmut)
- [ ] Achieve >80% mutation score
- [ ] Analyze surviving mutants
- [ ] Add specific tests to kill survivors
- [ ] Document final mutation score

**Tools by Language**:
- Java: PIT (pitest)
- JavaScript/TypeScript: Stryker
- Python: mutmut, cosmic-ray
- C#: Stryker.NET

---

## OUTPUT FORMAT

### Test File Structure
```
test_gilded_rose.{ext}
├── Class: TestNormalItems
│   ├── test_quality_decreases_by_one_before_sell_date()
│   ├── test_quality_decreases_by_two_after_sell_date()
│   └── ...
├── Class: TestAgedBrie
│   ├── test_quality_increases_before_sell_date()
│   └── ...
├── Class: TestSulfuras
├── Class: TestBackstagePasses
└── Class: TestConjuredItems (if applicable)
```

### Coverage Report Summary
```
================================
COVERAGE REPORT
================================
Total Lines: XXX
Covered Lines: XXX
Line Coverage: 100%

Total Branches: XXX
Covered Branches: XXX
Branch Coverage: 100%

Uncovered Lines: None
Uncovered Branches: None
================================
```

### Test Scenario Matrix
| Item Type | Test Count | Scenarios Covered |
|-----------|------------|-------------------|
| Normal    | X          | ✅ All           |
| Aged Brie | X          | ✅ All           |
| Sulfuras  | X          | ✅ All           |
| Backstage | X          | ✅ All           |
| Conjured  | X          | ✅ All           |
| Edge Cases| X          | ✅ All           |
| **TOTAL** | **X**      | **✅ Complete**  |

---

## EXECUTION STEPS

1. **Setup test environment**
   - Import test framework
   - Create test file structure
   - Set up helper methods if needed

2. **Generate core tests**
   - Start with normal items
   - Add special items one by one
   - Follow checklist systematically

3. **Add boundary tests**
   - Test all identified edge cases
   - Cover all boundary values

4. **Run and verify coverage**
   - Execute test suite
   - Generate coverage report
   - Identify gaps

5. **Fill coverage gaps**
   - Add tests for uncovered lines/branches
   - Re-run coverage
   - Iterate until 100%

6. **Quality check**
   - Review test names for clarity
   - Check for test smells
   - Ensure independence
   - Verify fast execution

7. **Document results**
   - Create coverage report summary
   - List all test scenarios
   - Confirm completion

---

## DELIVERABLE

A complete test suite containing:
✅ Test files following conventions
✅ **100% line coverage**
✅ **100% branch coverage**
✅ **High mutation score (>80%)**
✅ **Zero test smells**
✅ **Test patterns applied** (Builder/Mother)
✅ All business rules tested
✅ All edge cases tested
✅ Coverage report generated
✅ Mutation testing report (if available)
✅ Test scenario documentation
✅ All tests passing
✅ Fast execution (< 5s total)

---

## QUALITY CHECKLIST

Before considering TEST mode complete, verify:

### Coverage ✅
- [ ] 100% line coverage achieved
- [ ] 100% branch coverage achieved
- [ ] Coverage report documented

### Mutation Testing ✅
- [ ] Mutation testing executed
- [ ] Mutation score >80%
- [ ] Surviving mutants analyzed
- [ ] Critical mutants killed

### Test Smells ✅
- [ ] No Mystery Guest (external files)
- [ ] No Fragile Tests (implementation coupling)
- [ ] No Conditional Logic (if/for/while)
- [ ] No Obscure Setup (complex setup)
- [ ] No Assertion Roulette (missing messages)
- [ ] No Giant Tests (> 20 lines)
- [ ] No Sleeper Tests (sleep/setTimeout)

### Test Patterns ✅
- [ ] Object Mother or Data Builder used
- [ ] Test Doubles used (if applicable)
- [ ] AAA pattern consistently applied

### Test Quality ✅
- [ ] Descriptive test names
- [ ] Single concept per test
- [ ] Independent tests
- [ ] Fast execution
- [ ] Specific assertions (no ranges)
- [ ] Clear failure messages

---

## TRANSITION CRITERIA

Ready to move to REFACTOR mode when:

### Test Coverage ✅
- ✅ 100% line coverage achieved
- ✅ 100% branch coverage achieved
- ✅ All tests passing
- ✅ Coverage report documented
- ✅ No test smells present

### Python Best Practices ✅
- ✅ **No `(object)` inheritance** - Modern Python 3 syntax only
- ✅ **F-strings everywhere** - All string formatting modernized
- ✅ **All test methods documented** - Docstrings present
- ✅ **No trailing whitespace** - Clean formatting
- ✅ **No else after return** - Simplified control flow
- ✅ **Pylint score ≥ 9.0/10** - Verified with linter
- ✅ **Flake8 zero warnings** - PEP8 compliant

**Next Command**: `/refactor` to enter REFACTOR mode

---

## LANGUAGE-SPECIFIC EXAMPLES

### Python (pytest)
```python
def test_normal_item_quality_decreases():
    items = [Item("Normal", sellIn=5, quality=10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 9
```

### Java (JUnit 5)
```java
@Test
void normalItem_qualityDecreases_beforeSellDate() {
    Item item = new Item("Normal", 5, 10);
    GildedRose app = new GildedRose(new Item[]{item});
    app.updateQuality();
    assertEquals(9, item.quality);
}
```

### C# (NUnit)
```csharp
[Test]
public void NormalItem_QualityDecreases_BeforeSellDate() {
    var item = new Item { Name = "Normal", SellIn = 5, Quality = 10 };
    var app = new GildedRose(new List<Item> { item });
    app.UpdateQuality();
    Assert.AreEqual(9, item.Quality);
}
```
