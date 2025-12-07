# Gilded Rose BDD Test Suite

## Overview

This directory contains Behavior-Driven Development (BDD) scenarios for the Gilded Rose inventory system. The scenarios are written in Gherkin format and can be executed using the `behave` framework.

## Directory Structure

```
features/
├── __init__.py                    # Package marker
├── normal_items.feature           # Normal item scenarios (10 scenarios)
├── aged_brie.feature             # Aged Brie scenarios (9 scenarios)
├── sulfuras.feature              # Sulfuras legendary item scenarios (4 scenarios)
├── backstage_passes.feature      # Backstage pass scenarios (14 scenarios)
├── quality_boundaries.feature    # Quality boundary scenarios (4 scenarios)
├── multiple_items.feature        # Integration scenarios (3 scenarios)
└── steps/
    ├── __init__.py               # Package marker
    └── gilded_rose_steps.py      # Step definitions (all functions with unique names)
```

## Total Coverage

- **44 BDD scenarios** covering all business rules
- **6 feature files** organized by item type
- **17 step definitions** with unique function names
- **100% business rule coverage**

## Setup

### Prerequisites

```bash
pip install behave
```

### Installation

The features are already set up. The step definitions automatically import the `gilded_rose` module from the parent directory.

## Running Tests

### Run All Scenarios

```bash
# From the python/ directory
behave

# Or specify the features directory
behave features/
```

### Run Specific Feature

```bash
behave features/normal_items.feature
behave features/aged_brie.feature
behave features/sulfuras.feature
behave features/backstage_passes.feature
behave features/quality_boundaries.feature
behave features/multiple_items.feature
```

### Run by Tags

```bash
# Run only smoke tests (fastest feedback)
behave --tags=@smoke

# Run only edge cases
behave --tags=@edge_case

# Run specific item type
behave --tags=@aged_brie
behave --tags=@backstage
behave --tags=@sulfuras
behave --tags=@normal

# Run quality boundary tests
behave --tags=@quality_cap
behave --tags=@quality_floor

# Run transition day tests (sell_in = 0)
behave --tags=@transition

# Run integration tests
behave --tags=@integration

# Combine tags (OR)
behave --tags=@smoke --tags=@edge_case

# Combine tags (AND)
behave --tags=@edge_case,@aged_brie

# Exclude tags
behave --tags=-@wip
```

### Different Output Formats

```bash
# Pretty format (default, colorized)
behave --format=pretty

# Progress format (compact dots)
behave --format=progress

# JSON format (for parsing)
behave --format=json --outfile=bdd-results.json

# JUnit XML format (for CI/CD)
behave --format=junit --outfile=bdd-results.xml
```

### Verbose Output

```bash
# Show all step details
behave -v

# Very verbose (show step definitions)
behave -vv

# Show stdout/stderr during execution
behave --no-capture
```

### Debugging

```bash
# Stop on first failure
behave --stop

# Show snippets for undefined steps
behave --snippets

# Dry run (don't execute steps)
behave --dry-run
```

## Tag Categories

### By Priority

- `@smoke` - Critical tests for basic functionality (11 scenarios)
- `@regression` - Full regression suite (4 scenarios)
- `@critical` - Must-pass scenarios (2 scenarios)

### By Test Type

- `@edge_case` - Boundary conditions and edge cases (17 scenarios)
- `@integration` - Multi-item interaction tests (3 scenarios)
- `@unit` - Single item behavior tests (all item-specific scenarios)

### By Quality Concern

- `@quality_cap` - Tests verifying quality doesn't exceed 50 (8 scenarios)
- `@quality_floor` - Tests verifying quality doesn't go below 0 (5 scenarios)
- `@transition` - Tests for sell_in = 0 behavior (5 scenarios)

### By Item Type

- `@normal` - Normal item tests (10 scenarios)
- `@aged_brie` - Aged Brie tests (9 scenarios)
- `@sulfuras` - Sulfuras legendary item tests (4 scenarios)
- `@backstage` - Backstage pass tests (14 scenarios)

## Scenario Breakdown

### Normal Items (10 scenarios)
- Quality degradation before/on/after sell date
- Quality floor enforcement (never negative)
- Edge cases with low quality values
- Multi-day progression

### Aged Brie (9 scenarios)
- Quality improvement before/on/after sell date
- Quality cap enforcement (never exceeds 50)
- Edge cases at quality boundaries (0, 48, 49, 50)
- Very negative sell_in behavior

### Sulfuras (4 scenarios)
- Immutability of quality (always 80)
- Immutability of sell_in
- Behavior with negative sell_in
- Transition day immunity

### Backstage Passes (14 scenarios)
- All increment levels (+1, +2, +3)
- Threshold crossings (11→10, 6→5)
- Concert day behavior (drops to 0)
- After concert (quality stays 0)
- Quality cap with multi-increments
- Full progression to concert

### Quality Boundaries (4 scenarios)
- Max quality enforcement for all item types
- Min quality enforcement for all item types
- Sulfuras special case (always 80)
- Multi-item boundary respect

### Multiple Items (3 scenarios)
- Independent updates
- Empty inventory handling
- Multi-day mixed updates

## Step Definitions

All step definitions have **unique, descriptive function names** following the pattern:
- `step_given_{description}` for @given steps
- `step_when_{description}` for @when steps
- `step_then_{description}` for @then steps

This ensures:
- Debuggable stack traces
- IDE autocomplete works properly
- Code is self-documenting
- Easy to locate specific implementations

### Available Steps

**Context Setup (@given):**
- `Given the Gilded Rose inventory system`
- `Given a normal item with sellIn {n} and quality {n}`
- `Given an Aged Brie with sellIn {n} and quality {n}`
- `Given a Sulfuras with sellIn {n} and quality {n}`
- `Given a Backstage pass with sellIn {n} and quality {n}`
- `Given a Conjured item with sellIn {n} and quality {n}`
- `Given multiple items of different types`
- `Given {item_type} with sellIn {n} and quality {n}`

**Actions (@when):**
- `When the system updates quality`
- `When {n} days pass`
- `When {n} day passes`

**Assertions (@then):**
- `Then the quality should be {n}`
- `Then the sellIn should be {n}`
- `Then the quality should not exceed {n}`
- `Then no errors should occur`
- `Then each item should update according to its specific rules`
- `Then each item should have updated according to its rules for {n} days`
- `Then item {index} should have quality {n}`

## Business Rules Coverage

All 15 business rules are covered:

1. ✅ Normal items degrade by 1 before sell
2. ✅ Normal items degrade by 2 after sell
3. ✅ Quality never negative
4. ✅ Quality never exceeds 50 (non-legendary)
5. ✅ Aged Brie improves by 1 before sell
6. ✅ Aged Brie improves by 2 after sell
7. ✅ Sulfuras never changes quality
8. ✅ Sulfuras never changes sell_in
9. ✅ Sulfuras quality is 80
10. ✅ Backstage +1 when >10 days
11. ✅ Backstage +2 when ≤10 days
12. ✅ Backstage +3 when ≤5 days
13. ✅ Backstage drops to 0 after concert
14. ✅ SellIn decreases by 1 (except Sulfuras)
15. ✅ Multiple items update independently

## Expected Output

Successful run:
```
Feature: Normal Item Quality Degradation # features/normal_items.feature:1

  Scenario: Normal item quality decreases by 1 before sell date
    Given the Gilded Rose inventory system
    Given a normal item with sellIn 5 and quality 10
    When the system updates quality
    Then the quality should be 9
    And the sellIn should be 4

  ... (43 more scenarios)

6 features passed, 0 failed, 0 skipped
44 scenarios passed, 0 failed, 0 skipped
XXX steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.XXXs
```

## CI/CD Integration

Example GitHub Actions workflow:

```yaml
name: BDD Tests

on: [push, pull_request]

jobs:
  bdd:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install behave
      - name: Run smoke tests
        run: behave --tags=@smoke
      - name: Run full BDD suite
        run: behave
      - name: Generate report
        if: always()
        run: behave --format=json --outfile=bdd-results.json
```

## Extending the Suite

To add new scenarios:

1. Add scenario to appropriate feature file
2. Use existing steps or create new ones in `gilded_rose_steps.py`
3. Ensure new step functions have unique names
4. Add appropriate tags (@smoke, @edge_case, etc.)
5. Run tests to verify

## Troubleshooting

**Import errors:**
- Ensure you're running from the `python/` directory
- Check that `gilded_rose.py` is in the parent directory

**Undefined steps:**
- Run `behave --snippets` to see missing step definitions
- Check step definition function names are unique

**All tests failing:**
- Verify `gilded_rose.py` is working with unit tests first
- Check Python version compatibility (Python 3.7+)

## References

- [Behave Documentation](https://behave.readthedocs.io/)
- [Gherkin Syntax](https://cucumber.io/docs/gherkin/reference/)
- [BDD Best Practices](https://cucumber.io/docs/bdd/)
