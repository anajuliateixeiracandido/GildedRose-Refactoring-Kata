# Test Quality Guide - Complete Reference

## Part 1: Test Smells Catalog

### Code Smells (In Test Code)

#### 1. Mystery Guest 🎭
**Symptom**: Test depends on external resources (files, DB, network) not visible in test code.

**Why it's bad**: 
- Can't understand test without checking external files
- Brittle (file changes break tests)
- Hard to debug failures

**Example**:
```python
# ❌ BAD
def test_process_invoice():
    data = load_json('fixtures/invoice_complex.json')  # What's in this file?
    result = process_invoice(data)
    assert result.total == 99.50  # Where does 99.50 come from?

# ✅ GOOD
def test_process_invoice_with_two_items():
    invoice = {
        'items': [
            {'name': 'Item A', 'price': 50.00},
            {'name': 'Item B', 'price': 49.50}
        ]
    }
    result = process_invoice(invoice)
    assert result.total == 99.50  # Clear: 50 + 49.50
```

---

#### 2. Fragile Test 🍃
**Symptom**: Test breaks when implementation changes, even if behavior is unchanged.

**Why it's bad**:
- Prevents safe refactoring
- Creates false positives
- Developers lose trust in tests

**Example**:
```java
// ❌ BAD - Coupled to HTML structure
@Test
void testGenerateReport() {
    String html = generateReport(data);
    assertEquals("<div><h1>Report</h1><p>Sales: OK</p></div>", html);
    // Breaks if we change <div> to <section>!
}

// ✅ GOOD - Tests behavior
@Test
void testGenerateReport_containsRequiredElements() {
    String html = generateReport(data);
    assertThat(html).contains("Report");
    assertThat(html).contains("Sales: OK");
    // Won't break with structural changes
}
```

---

#### 3. Conditional Logic in Test 🔀
**Symptom**: Test contains if, switch, for, or while statements.

**Why it's bad**:
- Test may not test anything (if condition never true)
- Unpredictable behavior
- Hard to understand what's being tested

**Example**:
```javascript
// ❌ BAD
test('process items', () => {
    for (let item of allItems) {
        if (item.type === 'URGENT') {
            expect(item.processed).toBe(true);
        }
    }
    // What if allItems has no URGENT items? Test passes but tests nothing!
});

// ✅ GOOD - One scenario per test
test('urgent items are processed', () => {
    const urgentItem = { type: 'URGENT', processed: false };
    processItems([urgentItem]);
    expect(urgentItem.processed).toBe(true);
});

test('non-urgent items are not processed', () => {
    const normalItem = { type: 'NORMAL', processed: false };
    processItems([normalItem]);
    expect(normalItem.processed).toBe(false);
});
```

---

#### 4. Obscure Setup 🌫️
**Symptom**: Test setup is longer and more complex than the test itself.

**Why it's bad**:
- Hard to understand what's being tested
- Violates DRY principle
- Maintenance nightmare

**Example**:
```csharp
// ❌ BAD
[Test]
public void TestCalculateTax() {
    // 30 lines of setup...
    var address = new Address("Street", 123, "NY", "10001");
    var client = new Client("John", "123-45-6789", address);
    var item1 = new Item("Product A", 2, 50.00m);
    var item2 = new Item("Product B", 1, 30.00m);
    var items = new List<Item> { item1, item2 };
    var invoice = new Invoice(998, client, items, "ACTIVE");
    invoice.SetDate(DateTime.Now);
    // ...finally the test
    var tax = calculator.CalculateTax(invoice);
    Assert.AreEqual(13.00m, tax);
}

// ✅ GOOD - Using Builder Pattern
[Test]
public void TestCalculateTax() {
    var invoice = InvoiceBuilder.AnInvoice()
                                .WithItems(50.00m, 30.00m)
                                .Build();
    
    var tax = calculator.CalculateTax(invoice);
    
    Assert.AreEqual(13.00m, tax);
}
```

---

#### 5. Assertion Roulette 🎰
**Symptom**: Multiple assertions without descriptive messages.

**Why it's bad**:
- When test fails, can't tell which assertion failed
- Hard to debug
- Poor failure feedback

**Example**:
```python
# ❌ BAD
def test_item_update():
    item = Item("Normal", 5, 10)
    update_quality(item)
    assert item.quality == 9
    assert item.sellIn == 4
    assert item.name == "Normal"
    # Which one failed? Who knows!

# ✅ GOOD
def test_item_update():
    item = Item("Normal", 5, 10)
    update_quality(item)
    assert item.quality == 9, "Quality should decrease by 1"
    assert item.sellIn == 4, "SellIn should decrease by 1"
    assert item.name == "Normal", "Name should remain unchanged"
```

---

#### 6. The Giant 🦕
**Symptom**: Test method is excessively long (>50 lines).

**Why it's bad**:
- Hard to understand
- Likely testing multiple concepts
- Difficult to maintain

**Solution**: Split into multiple focused tests.

---

#### 7. The Sleeper 😴
**Symptom**: Test uses sleep() or setTimeout() to wait for async operations.

**Why it's bad**:
- Slow test suite
- Flaky (race conditions)
- Arbitrary wait times

**Example**:
```javascript
// ❌ BAD
test('async operation', async () => {
    startAsyncOperation();
    await sleep(5000);  // Hope it's done by then...
    expect(result).toBe(true);
});

// ✅ GOOD
test('async operation', async () => {
    startAsyncOperation();
    await waitFor(() => operationCompleted, { timeout: 5000 });
    expect(result).toBe(true);
});
```

---

### Project Smells (Test Suite Management)

#### 8. Slow Tests 🐌
**Symptom**: Test suite takes minutes to run.

**Solutions**:
- Mock external dependencies
- Use in-memory databases
- Parallelize tests
- Separate unit from integration tests

---

#### 9. Test Code Duplication 📋
**Symptom**: Same setup code repeated across many tests.

**Solutions**:
- Object Mother pattern
- Data Builder pattern
- setUp/beforeEach methods
- Test utilities

---

## Part 2: Mutation Testing Deep Dive

### What is Mutation Testing?

**Concept**: Insert small bugs (mutants) into code. If tests don't fail, they're weak.

**Formula**: 
```
Mutation Score = (Killed Mutants / Total Mutants) × 100%
```

**Target**: >80% mutation score

---

### Common Mutation Operators

#### 1. Arithmetic Operator Replacement
```
Original: x + y
Mutants:  x - y, x * y, x / y, x % y
```

**How to kill**: Use specific expected values
```python
# Weak: doesn't kill + → - mutant
assert result > 0

# Strong: kills + → - mutant
assert result == 15  # If inputs are 10 and 5
```

---

#### 2. Relational Operator Replacement
```
Original: x > y
Mutants:  x >= y, x < y, x <= y, x == y, x != y
```

**How to kill**: Test boundary values
```python
# Weak
assert quality > 0

# Strong
assert quality == 9  # Exact value
```

---

#### 3. Conditional Boundary Mutation
```
Original: if (x < 10)
Mutants:  if (x <= 10), if (x < 11)
```

**How to kill**: Test exact boundary
```python
# Tests x = 10 case
item.sellIn = 10
update_quality(item)
assert item.quality == 22  # +2, not +1 or +3
```

---

#### 4. Negate Conditionals
```
Original: if (condition)
Mutant:   if (!condition)
```

**How to kill**: Test both branches explicitly
```python
# Test positive case
item.quality = 10
update_quality(item)
assert item.quality == 9

# Test boundary case (condition false)
item.quality = 0
update_quality(item)
assert item.quality == 0  # Doesn't go negative
```

---

#### 5. Return Value Mutation
```
Original: return true;
Mutant:   return false;
```

**How to kill**: Assert on return value
```python
# Weak - doesn't check return
process_item(item)

# Strong - checks return
result = process_item(item)
assert result == True
```

---

#### 6. Void Method Call Removal
```
Original: item.quality--;
Mutant:   // deleted
```

**How to kill**: Assert state changes
```python
# Strong - verifies side effect
initial_quality = item.quality
update_quality(item)
assert item.quality == initial_quality - 1
```

---

#### 7. Increment/Decrement Mutation
```
Original: quality--
Mutants:  quality++, --quality, ++quality
```

**How to kill**: Specific value assertions
```python
item.quality = 10
update_quality(item)
assert item.quality == 9  # Not 10, not 11, exactly 9
```

---

### Mutation Testing Strategy

#### Step 1: Achieve 100% Code Coverage
Without full coverage, many mutants won't even be executed.

#### Step 2: Run Mutation Testing Tool
```bash
# Java
mvn org.pitest:pitest-maven:mutationCoverage

# Python
mutmut run

# JavaScript
npx stryker run

# C#
dotnet stryker
```

#### Step 3: Analyze Survivors
Check report for mutants that survived. Common reasons:
- Generic assertions (>= instead of ==)
- Missing boundary tests
- Untested error paths

#### Step 4: Add Targeted Tests
For each survivor, add a test with specific assertion that would fail if that mutation occurred.

#### Step 5: Re-run Until >80%
Iterate until mutation score is high.

---

## Part 3: Test Patterns Application Guide

### When to Use Each Pattern

| Pattern | Use When | Gilded Rose Application |
|---------|----------|-------------------------|
| **Object Mother** | Need same complex objects repeatedly | ItemMother.createNormalItem() |
| **Data Builder** | Need variations of same object | ItemBuilder.anItem().withQuality(50).build() |
| **Test Doubles** | Dependencies on external systems | N/A for Gilded Rose (no dependencies) |

---

### Object Mother - Complete Example

```python
class ItemMother:
    """Centralized factory for common test items"""
    
    @staticmethod
    def createNormalItem():
        return Item("Normal Item", sellIn=5, quality=10)
    
    @staticmethod
    def createExpiredItem():
        return Item("Expired Item", sellIn=-1, quality=10)
    
    @staticmethod
    def createAgedBrie():
        return Item("Aged Brie", sellIn=10, quality=20)
    
    @staticmethod
    def createAgedBrieAtMaxQuality():
        return Item("Aged Brie", sellIn=5, quality=50)
    
    @staticmethod
    def createSulfuras():
        return Item("Sulfuras, Hand of Ragnaros", sellIn=0, quality=80)
    
    @staticmethod
    def createBackstagePass_MoreThan10Days():
        return Item("Backstage passes to a TAFKAL80ETC concert", sellIn=15, quality=20)
    
    @staticmethod
    def createBackstagePass_10DaysOrLess():
        return Item("Backstage passes to a TAFKAL80ETC concert", sellIn=10, quality=20)
    
    @staticmethod
    def createBackstagePass_5DaysOrLess():
        return Item("Backstage passes to a TAFKAL80ETC concert", sellIn=5, quality=20)
    
    @staticmethod
    def createBackstagePass_Expired():
        return Item("Backstage passes to a TAFKAL80ETC concert", sellIn=0, quality=20)
```

---

### Data Builder - Complete Example

```java
public class ItemBuilder {
    private String name = "Normal Item";
    private int sellIn = 5;
    private int quality = 10;
    
    public static ItemBuilder anItem() {
        return new ItemBuilder();
    }
    
    public ItemBuilder withName(String name) {
        this.name = name;
        return this;
    }
    
    public ItemBuilder agedBrie() {
        this.name = "Aged Brie";
        return this;
    }
    
    public ItemBuilder sulfuras() {
        this.name = "Sulfuras, Hand of Ragnaros";
        this.quality = 80;
        return this;
    }
    
    public ItemBuilder backstagePass() {
        this.name = "Backstage passes to a TAFKAL80ETC concert";
        return this;
    }
    
    public ItemBuilder withSellIn(int sellIn) {
        this.sellIn = sellIn;
        return this;
    }
    
    public ItemBuilder expired() {
        this.sellIn = -1;
        return this;
    }
    
    public ItemBuilder withQuality(int quality) {
        this.quality = quality;
        return this;
    }
    
    public ItemBuilder atMaxQuality() {
        this.quality = 50;
        return this;
    }
    
    public ItemBuilder atMinQuality() {
        this.quality = 0;
        return this;
    }
    
    public Item build() {
        return new Item(name, sellIn, quality);
    }
}

// Usage examples:
Item item1 = ItemBuilder.anItem().build(); // Default normal item

Item item2 = ItemBuilder.anItem()
                        .agedBrie()
                        .withSellIn(10)
                        .build(); // Aged Brie, sellIn=10, quality=10

Item item3 = ItemBuilder.anItem()
                        .backstagePass()
                        .withSellIn(5)
                        .atMaxQuality()
                        .build(); // Backstage pass, sellIn=5, quality=50
```

---

## Part 4: Quality Metrics Summary

### Test Suite Health Metrics

| Metric | Target | Critical Threshold |
|--------|--------|-------------------|
| Line Coverage | 100% | > 95% |
| Branch Coverage | 100% | > 90% |
| Mutation Score | > 80% | > 70% |
| Test Execution Time | < 5s | < 30s |
| Test Smells | 0 | < 3 |
| Avg Test Length | < 15 lines | < 25 lines |
| Test Independence | 100% | 100% |

---

## Part 5: Quick Reference Checklist

### Before Committing Tests

- [ ] ✅ 100% line coverage
- [ ] ✅ 100% branch coverage
- [ ] ✅ Mutation score > 80%
- [ ] ✅ No Mystery Guest
- [ ] ✅ No Fragile Tests
- [ ] ✅ No Conditional Logic in tests
- [ ] ✅ No Obscure Setup
- [ ] ✅ No Assertion Roulette
- [ ] ✅ No Giant tests (all < 20 lines)
- [ ] ✅ No Sleeper tests
- [ ] ✅ AAA pattern in all tests
- [ ] ✅ Specific assertions (not ranges)
- [ ] ✅ Descriptive test names
- [ ] ✅ Clear failure messages
- [ ] ✅ Builder or Mother pattern used
- [ ] ✅ Fast execution (< 5s total)
- [ ] ✅ All tests independent

---

_This guide provides the theoretical foundation for writing high-quality, effective tests that not only achieve coverage but actually catch bugs._
