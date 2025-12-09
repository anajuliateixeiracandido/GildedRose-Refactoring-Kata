# REFACTOR Mode - Clean Code Refactoring Prompt

## MODE DECLARATION
[MODE: REFACTOR]

## OBJECTIVE
Refactor the Gilded Rose codebase following Clean Code principles and design patterns, improving maintainability, readability, and extensibility while maintaining 100% behavioral compatibility verified by the existing test suite.

---

## PREREQUISITES
✅ TEST mode completed
✅ 100% test coverage achieved
✅ All tests passing
✅ Business rules understood

---

## CRITICAL SAFETY RULE
🚨 **ALL TESTS MUST PASS AFTER EVERY REFACTORING STEP**

If tests fail at any point:
1. STOP immediately
2. Rollback the change
3. Analyze what broke
4. Adjust approach
5. Try again with smaller steps

---

## REFACTORING STRATEGY

### Phase 1: Preparation
- [ ] Ensure all tests are green
- [ ] Create baseline complexity metrics
- [ ] Identify primary refactoring targets
- [ ] Plan refactoring sequence (safest to riskiest)

### Phase 2: Extract Item Types
- [ ] Create Item type hierarchy or strategy pattern
- [ ] Extract specialized classes for each item type
- [ ] Move behavior from conditional logic to polymorphism
- [ ] Run tests after each extraction

### Phase 3: Simplify Main Logic
- [ ] Replace complex conditionals with polymorphic calls
- [ ] Extract methods for clarity
- [ ] Remove duplicated code
- [ ] Improve naming

### Phase 4: Polish
- [ ] Remove dead code
- [ ] Add clarifying comments (sparingly)
- [ ] Ensure consistent formatting
- [ ] Final test run

---

## CLEAN CODE PRINCIPLES TO APPLY

### 1. Single Responsibility Principle (SRP)
**Current Problem**: Main update method handles all item types
**Solution**: Each item type handles its own update logic

```
Bad:
if (item.name == "Aged Brie") {
    // Aged Brie logic
} else if (item.name == "Sulfuras") {
    // Sulfuras logic
}

Good:
item.updateQuality() // Polymorphic call
```

### 2. Open/Closed Principle (OCP)
**Goal**: Open for extension, closed for modification
**Solution**: New item types added without changing existing code

```
Strategy Pattern or Inheritance:
- ItemUpdater (interface/base)
  - NormalItemUpdater
  - AgedBrieUpdater
  - SulfurasUpdater
  - BackstagePassUpdater
  - ConjuredItemUpdater
```

### 3. Meaningful Names
**Replace**:
- Generic variables: `item`, `i`, `x`
- Magic numbers: `50`, `10`, `5`, `80`
- Unclear names: `update()`, `process()`

**With**:
- Intention-revealing: `qualityItem`, `backstagePass`
- Named constants: `MAX_QUALITY = 50`, `LEGENDARY_QUALITY = 80`
- Clear methods: `updateQuality()`, `degradeQuality()`

### 4. Python 3 Modern Practices
**CRITICAL - Always Apply**:

✅ **No Object Inheritance**
```python
# ❌ BAD (Python 2 style)
class GildedRose(object):
    pass

# ✅ GOOD (Python 3)
class GildedRose:
    pass
```

✅ **Use F-Strings**
```python
# ❌ BAD (old style)
def __repr__(self):
    return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

# ✅ GOOD (modern Python)
def __repr__(self):
    return f"{self.name}, {self.sell_in}, {self.quality}"
```

✅ **Simplify Control Flow (No Else After Return)**
```python
# ❌ BAD
if condition:
    return value1
else:
    return value2

# ✅ GOOD
if condition:
    return value1
return value2
```

✅ **Always Add Docstrings**
```python
# ❌ BAD
def update_quality(self):
    for item in self.items:
        # ...

# ✅ GOOD
def update_quality(self):
    """Update quality and sell_in values for all items."""
    for item in self.items:
        # ...
```

✅ **No Trailing Whitespace**
- Clean all line endings
- No spaces on blank lines
- Use linter to verify

### 4. Small Functions
**Goal**: Each function does ONE thing well
**Target**: Functions < 20 lines, ideally < 10

Extract methods like:
- `increaseQuality(amount)`
- `decreaseQuality(amount)`
- `clampQualityToMax()`
- `hasExpired()`
- `daysUntilConcert()`

### 5. DRY (Don't Repeat Yourself)
**Identify duplicate patterns**:
- Quality increase logic (Aged Brie, Backstage passes)
- Quality decrease logic (Normal, Conjured)
- Quality boundary checks (0-50 range)

**Extract to shared methods**:
- `adjustQuality(delta)` with automatic clamping
- `isLegendary()` check
- `hasPassedSellDate()` check

### 6. Command Query Separation
**Commands** (modify state): `updateQuality()`
**Queries** (return info): `getQuality()`, `hasExpired()`

Don't mix: `updateAndGetQuality()` ❌

### 7. Replace Conditionals with Polymorphism
**Before**:
```
if (item.name == "X") { ... }
else if (item.name == "Y") { ... }
else if (item.name == "Z") { ... }
```

**After**:
```
itemUpdater.update() // Polymorphic dispatch
```

---

## RECOMMENDED REFACTORING PATTERNS

### Strategy Pattern (Preferred)
```
interface ItemUpdateStrategy {
    update(item)
}

class NormalItemStrategy implements ItemUpdateStrategy {
    update(item) {
        decreaseQuality(item, hasExpired(item) ? 2 : 1)
        decreaseSellIn(item)
    }
}

class GildedRose {
    strategies = {
        "Aged Brie": new AgedBrieStrategy(),
        "Sulfuras": new SulfurasStrategy(),
        "Backstage passes": new BackstagePassStrategy(),
        default: new NormalItemStrategy()
    }
    
    updateQuality() {
        for (item in items) {
            strategy = getStrategy(item.name)
            strategy.update(item)
        }
    }
}
```

### Inheritance Pattern (Alternative)
```
abstract class QualityItem {
    name, sellIn, quality
    
    abstract updateQuality()
    
    protected increaseQuality(amount) { ... }
    protected decreaseQuality(amount) { ... }
    protected clampQuality() { ... }
}

class NormalItem extends QualityItem {
    updateQuality() {
        decreaseQuality(hasExpired() ? 2 : 1)
        sellIn--
    }
}

class AgedBrie extends QualityItem {
    updateQuality() {
        increaseQuality(hasExpired() ? 2 : 1)
        sellIn--
    }
}
```

---

## REFACTORING CHECKLIST

### Extract Constants
- [ ] `MAX_QUALITY = 50`
- [ ] `MIN_QUALITY = 0`
- [ ] `LEGENDARY_QUALITY = 80`
- [ ] `BACKSTAGE_PASS_FIRST_THRESHOLD = 10`
- [ ] `BACKSTAGE_PASS_SECOND_THRESHOLD = 5`
- [ ] `NORMAL_DEGRADATION_RATE = 1`
- [ ] `EXPIRED_DEGRADATION_MULTIPLIER = 2`

### Extract Helper Methods
- [ ] `increaseQuality(item, amount)` - with bounds checking
- [ ] `decreaseQuality(item, amount)` - with bounds checking
- [ ] `clampQuality(item)` - ensure 0 ≤ quality ≤ 50
- [ ] `hasExpired(item)` - returns sellIn < 0
- [ ] `isLegendaryItem(name)` - checks if Sulfuras
- [ ] `decreaseSellIn(item)` - only if not legendary

### Extract Item Type Classes
- [ ] Create `ItemUpdateStrategy` interface or base class
- [ ] Implement `NormalItemStrategy/Updater`
- [ ] Implement `AgedBrieStrategy/Updater`
- [ ] Implement `SulfurasStrategy/Updater`
- [ ] Implement `BackstagePassStrategy/Updater`
- [ ] Implement `ConjuredItemStrategy/Updater` (if applicable)

### Simplify Main Logic
- [ ] Replace nested if-else with strategy lookup
- [ ] Remove duplicated quality adjustment code
- [ ] Extract complex conditions to named methods
- [ ] Eliminate magic numbers

### Improve Naming
- [ ] Rename unclear variables
- [ ] Use verb-noun method names
- [ ] Add missing parameter names
- [ ] Follow language conventions

---

## STEP-BY-STEP EXECUTION

### Step 1: Extract Constants
Replace all magic numbers with named constants
```
50 → MAX_QUALITY
0 → MIN_QUALITY
80 → LEGENDARY_QUALITY
10, 5 → threshold constants
```
**Run tests** ✅

### Step 2: Extract Quality Adjustment Methods
Create reusable methods for quality changes
```
increaseQuality(item, amount):
    item.quality = min(item.quality + amount, MAX_QUALITY)

decreaseQuality(item, amount):
    item.quality = max(item.quality - amount, MIN_QUALITY)
```
**Replace inline logic with method calls**
**Run tests** ✅

### Step 3: Extract Condition Checks
```
hasExpired(item):
    return item.sellIn < 0

isLegendary(itemName):
    return itemName == "Sulfuras, Hand of Ragnaros"
```
**Replace inline conditions with method calls**
**Run tests** ✅

### Step 4: Create Item Type Strategy/Classes
For each item type, create a dedicated updater
```
class NormalItemUpdater:
    update(item):
        decreaseQuality(item, 1 if not hasExpired(item) else 2)
        item.sellIn -= 1
```
**Run tests after each class** ✅

### Step 5: Replace Main Logic with Polymorphism
```
updateQuality():
    for item in items:
        updater = getUpdaterForItem(item)
        updater.update(item)
```
**Run tests** ✅

### Step 6: Remove Duplicated Code
Identify and eliminate any remaining duplication
**Run tests** ✅

### Step 7: Final Polish
- Improve method names
- Add strategic comments (not obvious ones)
- Ensure consistent formatting
- Remove dead code
**Run tests** ✅

---

## COMPLEXITY REDUCTION TARGETS

### Before Refactoring
| Metric | Current | Target |
|--------|---------|--------|
| Cyclomatic Complexity | ~15-20 | < 5 per method |
| Max Method Length | ~50-80 lines | < 20 lines |
| Nesting Depth | 4-5 levels | ≤ 2 levels |
| Code Duplication | ~20-30% | < 5% |
| Class Count | 1-2 | 6-8 (with strategies) |

### After Refactoring
Should achieve:
- ✅ Cyclomatic complexity < 5 per method
- ✅ No method > 20 lines
- ✅ Max nesting depth = 2
- ✅ Minimal duplication
- ✅ Clear separation of concerns

---

## ANTI-PATTERNS TO AVOID

### ❌ Don't Change Behavior
- Don't "fix bugs" during refactoring
- Don't add new features
- Don't change business rules
- If behavior seems wrong, document it but don't change it

### ❌ Don't Break Tests
- Never skip running tests
- Never modify tests to make them pass
- If tests fail, the refactoring is wrong

### ❌ Don't Over-Engineer
- Don't add unnecessary abstraction layers
- Don't use complex patterns for simple problems
- Keep it as simple as possible

### ❌ Don't Refactor Everything At Once
- Small, incremental changes
- Test after each change
- Commit working states frequently

---

## OUTPUT FORMAT

### Refactored Code Structure
```
gilded_rose/
├── constants.{ext}
│   └── MAX_QUALITY, MIN_QUALITY, etc.
├── item_updaters/
│   ├── item_updater.{ext} (interface/base)
│   ├── normal_item_updater.{ext}
│   ├── aged_brie_updater.{ext}
│   ├── sulfuras_updater.{ext}
│   ├── backstage_pass_updater.{ext}
│   └── conjured_item_updater.{ext}
├── gilded_rose.{ext} (simplified main class)
└── item.{ext} (unchanged or minimal changes)
```

### Refactoring Report

**Complexity Improvements**:
| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Cyclomatic Complexity | X | Y | ↓ Z% |
| Longest Method | X lines | Y lines | ↓ Z lines |
| Nesting Depth | X | Y | ↓ Z levels |
| Code Duplication | X% | Y% | ↓ Z% |
| Class Count | X | Y | ↑ Z classes |

**Refactorings Applied**:
1. ✅ Extracted constants for magic numbers
2. ✅ Applied Strategy pattern for item types
3. ✅ Extracted quality adjustment methods
4. ✅ Simplified conditional logic
5. ✅ Improved method and variable names
6. ✅ Reduced method lengths
7. ✅ Eliminated code duplication

**Test Status**:
✅ All X tests passing
✅ 100% coverage maintained
✅ No behavioral changes detected

**Python 3 Quality Checklist**:
✅ No `(object)` inheritance in class definitions
✅ All string formatting uses f-strings
✅ All public methods have docstrings
✅ No trailing whitespace
✅ No unnecessary `else` after `return`
✅ Code passes Pylint with score ≥ 9.0/10
✅ Code passes Flake8 with zero warnings

---

## DELIVERABLE

Refactored codebase featuring:
✅ Clean, readable code
✅ Single Responsibility Principle applied
✅ Open/Closed Principle applied
✅ Strategy/Inheritance pattern implemented
✅ Magic numbers replaced with constants
✅ Complex conditionals simplified
✅ Reduced cyclomatic complexity
✅ No code duplication
✅ All tests still passing
✅ 100% coverage maintained
✅ **Python 3 modern practices enforced**
✅ **Pylint score ≥ 9.0/10**
✅ **Zero Flake8 warnings**
✅ Refactoring report with metrics

---

## TRANSITION CRITERIA

Ready to move to BDD mode when:

### Functional Requirements ✅
- ✅ All tests passing (100% success rate)
- ✅ Test coverage maintained at 99-100%
- ✅ No behavioral changes introduced
- ✅ Performance not degraded

### Code Quality ✅
- ✅ Cyclomatic complexity reduced significantly
- ✅ No method longer than 20 lines
- ✅ No nesting deeper than 3 levels
- ✅ No code duplication
- ✅ Code quality improved measurably

### Python Best Practices ✅
- ✅ **No `(object)` inheritance** - Modern Python 3 syntax only
- ✅ **F-strings everywhere** - All string formatting modernized
- ✅ **All public methods documented** - Docstrings present
- ✅ **No trailing whitespace** - Clean formatting
- ✅ **No else after return** - Simplified control flow
- ✅ **Pylint score ≥ 9.0/10** - Verified with linter
- ✅ **Flake8 zero warnings** - PEP8 compliant
- ✅ **Radon all A grades** - Low complexity verified

### Design Patterns ✅
- ✅ Strategy or inheritance pattern applied
- ✅ Factory method implemented
- ✅ Single Responsibility Principle
- ✅ Open/Closed Principle

**Next Command**: `/bdd` to enter BDD mode

---

## LANGUAGE-SPECIFIC PATTERNS

### Python
```python
from abc import ABC, abstractmethod

class ItemUpdater(ABC):
    @abstractmethod
    def update(self, item):
        pass

class NormalItemUpdater(ItemUpdater):
    def update(self, item):
        self._decrease_quality(item, 2 if self._has_expired(item) else 1)
        item.sell_in -= 1
```

### Java
```java
public interface ItemUpdater {
    void update(Item item);
}

public class NormalItemUpdater implements ItemUpdater {
    @Override
    public void update(Item item) {
        decreaseQuality(item, hasExpired(item) ? 2 : 1);
        item.sellIn--;
    }
}
```

### C#
```csharp
public interface IItemUpdater {
    void Update(Item item);
}

public class NormalItemUpdater : IItemUpdater {
    public void Update(Item item) {
        DecreaseQuality(item, HasExpired(item) ? 2 : 1);
        item.SellIn--;
    }
}
```
