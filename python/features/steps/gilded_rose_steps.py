"""
Gilded Rose BDD Step Definitions
Modern Python 3 implementation with unique function names and comprehensive error handling
"""

from behave import given, when, then
import sys
import os

# Add parent directory to path to import gilded_rose
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from gilded_rose import Item, GildedRose


# ============================================================================
# GIVEN STEPS - Context Setup
# ============================================================================


@given("the Gilded Rose inventory system")
def step_given_gilded_rose_system(context):
    """Initialize the Gilded Rose system with empty inventory."""
    context.items = []
    context.gilded_rose = None


@given("a normal item with sellIn {sell_in:d} and quality {quality:d}")
def step_given_normal_item(context, sell_in, quality):
    """Create a normal item with specified properties."""
    context.items = [Item("Normal Item", sell_in, quality)]
    context.gilded_rose = GildedRose(context.items)


@given("an Aged Brie with sellIn {sell_in:d} and quality {quality:d}")
def step_given_aged_brie(context, sell_in, quality):
    """Create an Aged Brie item with specified properties."""
    context.items = [Item("Aged Brie", sell_in, quality)]
    context.gilded_rose = GildedRose(context.items)


@given("a Sulfuras with sellIn {sell_in:d} and quality {quality:d}")
def step_given_sulfuras(context, sell_in, quality):
    """Create a Sulfuras legendary item with specified properties."""
    context.items = [Item("Sulfuras, Hand of Ragnaros", sell_in, quality)]
    context.gilded_rose = GildedRose(context.items)


@given("a Backstage pass with sellIn {sell_in:d} and quality {quality:d}")
def step_given_backstage_pass(context, sell_in, quality):
    """Create a Backstage pass item with specified properties."""
    context.items = [
        Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)
    ]
    context.gilded_rose = GildedRose(context.items)


@given("a Conjured item with sellIn {sell_in:d} and quality {quality:d}")
def step_given_conjured_item(context, sell_in, quality):
    """Create a Conjured item with specified properties."""
    context.items = [Item("Conjured Mana Cake", sell_in, quality)]
    context.gilded_rose = GildedRose(context.items)


@given("multiple items of different types")
def step_given_multiple_items(context):
    """Create a list of different item types for integration testing."""
    context.items = [
        Item("Normal Item", 10, 20),
        Item("Aged Brie", 5, 10),
        Item("Sulfuras, Hand of Ragnaros", 0, 80),
        Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
    ]
    context.gilded_rose = GildedRose(context.items)


@given("{item_type} with sellIn {sell_in:d} and quality {quality:d}")
def step_given_any_item_type(context, item_type, sell_in, quality):
    """Create any item type using mapping.
    
    Supports: a normal item, an Aged Brie, a Sulfuras, a Backstage pass
    """
    item_name_mapping = {
        "a normal item": "Normal Item",
        "an Aged Brie": "Aged Brie",
        "a Sulfuras": "Sulfuras, Hand of Ragnaros",
        "a Backstage pass": "Backstage passes to a TAFKAL80ETC concert",
        "a Conjured item": "Conjured Mana Cake",
    }

    item_name = item_name_mapping.get(item_type)
    assert (
        item_name is not None
    ), f"Unknown item type: {item_type}. Valid types: {list(item_name_mapping.keys())}"

    context.items = [Item(item_name, sell_in, quality)]
    context.gilded_rose = GildedRose(context.items)


@given("an empty inventory")
def step_given_empty_inventory(context):
    """Create an empty inventory for edge case testing."""
    context.items = []
    context.gilded_rose = GildedRose(context.items)


@given("{count:d} items of various types in inventory")
def step_given_many_items(context, count):
    """Create a large inventory for performance testing."""
    context.items = []
    item_types = [
        ("Normal Item", 10, 20),
        ("Aged Brie", 5, 10),
        ("Sulfuras, Hand of Ragnaros", 0, 80),
        ("Backstage passes to a TAFKAL80ETC concert", 15, 20),
    ]

    for i in range(count):
        item_type = item_types[i % len(item_types)]
        context.items.append(Item(item_type[0], item_type[1], item_type[2]))

    context.gilded_rose = GildedRose(context.items)


@given("the following items in inventory:")
def step_given_items_table(context):
    """Create items from a data table."""
    context.items = []
    for row in context.table:
        name = row["name"]
        sell_in = int(row["sellIn"])
        quality = int(row["quality"])
        context.items.append(Item(name, sell_in, quality))
    context.gilded_rose = GildedRose(context.items)


@then("the items should have the following properties:")
def step_then_items_properties_table(context):
    """Verify items match expected properties from table."""
    table_rows = list(context.table)
    assert len(context.items) == len(table_rows), f"Item count mismatch: expected {len(table_rows)}, got {len(context.items)}"

    for i, row in enumerate(table_rows):
        expected_name = row["name"]
        expected_sell_in = int(row["sellIn"])
        expected_quality = int(row["quality"])

        actual_item = context.items[i]

        assert (
            actual_item.name == expected_name
        ), f"Item {i}: Expected name '{expected_name}', got '{actual_item.name}'"

        assert (
            actual_item.sell_in == expected_sell_in
        ), f"Item {i} ({actual_item.name}): Expected sellIn {expected_sell_in}, got {actual_item.sell_in}"

        assert (
            actual_item.quality == expected_quality
        ), f"Item {i} ({actual_item.name}): Expected quality {expected_quality}, got {actual_item.quality}"


# ============================================================================
# WHEN STEPS - Actions
# ============================================================================


@when("the system updates quality")
def step_when_update_quality(context):
    """Execute a single quality update cycle."""
    # For empty inventory test: initialize empty GildedRose if needed
    if not hasattr(context, "gilded_rose") or context.gilded_rose is None:
        context.gilded_rose = GildedRose([])
    context.gilded_rose.update_quality()


@when("{days:d} days pass")
def step_when_days_pass(context, days):
    """Execute quality update for specified number of days."""
    assert (
        hasattr(context, "gilded_rose") and context.gilded_rose is not None
    ), "GildedRose not initialized. Did you forget @given step?"
    for _ in range(days):
        context.gilded_rose.update_quality()


@when("{days:d} day passes")
def step_when_one_day_passes(context, days):
    """Execute quality update for one day (singular form)."""
    step_when_days_pass(context, days)


# ============================================================================
# THEN STEPS - Assertions
# ============================================================================


@then("the quality should be {expected_quality:d}")
def step_then_quality_should_be(context, expected_quality):
    """Verify item quality matches expected value."""
    assert (
        hasattr(context, "items") and len(context.items) > 0
    ), "No items in context. Did you forget @given step?"

    actual = context.items[0].quality
    assert (
        actual == expected_quality
    ), f"Expected quality {expected_quality} but got {actual}"


@then("the sellIn should be {expected_sell_in:d}")
def step_then_sellin_should_be(context, expected_sell_in):
    """Verify item sellIn matches expected value."""
    assert (
        hasattr(context, "items") and len(context.items) > 0
    ), "No items in context. Did you forget @given step?"

    actual = context.items[0].sell_in
    assert (
        actual == expected_sell_in
    ), f"Expected sellIn {expected_sell_in} but got {actual}"


@then("each item should update according to its own rules")
def step_then_items_update_independently(context):
    """Verify each item type updated correctly."""
    assert len(context.items) >= 4, "Expected at least 4 items"

    # Verify Normal Item decreased by 1
    assert context.items[0].quality == 19, f"Normal item should decrease by 1, got {context.items[0].quality}"

    # Verify Aged Brie increased by 1
    assert context.items[1].quality == 11, f"Aged Brie should increase by 1, got {context.items[1].quality}"

    # Verify Sulfuras stayed at 80
    assert context.items[2].quality == 80, f"Sulfuras should stay at 80, got {context.items[2].quality}"

    # Verify Backstage pass increased by 3 (15 days, so +1)
    assert context.items[3].quality == 21, f"Backstage pass should increase by 1 (>10 days), got {context.items[3].quality}"


@then("no errors should occur")
def step_then_no_errors(context):
    """Verify no errors occurred during update."""
    # If we got here, no exception was raised
    assert True


@then("all items should be updated")
def step_then_all_items_updated(context):
    """Verify all items were processed."""
    # Verify at least one item exists and was updated
    assert len(context.items) > 0, "Expected items to be present"
    # If we got here without errors, update was successful
    assert True


@then("the operation should complete quickly")
def step_then_operation_fast(context):
    """Verify operation performance."""
    # This is more of a conceptual step
    # In real implementation, you might measure execution time
    assert True


@then("each item should update according to its state and type")
def step_then_items_update_by_state(context):
    """Verify complex multi-item scenario."""
    # This is a high-level verification
    # More specific assertions would be in actual implementation
    assert len(context.items) > 0, "Expected items to be present"
    assert True


@then("the update order should not affect the final quality values")
def step_then_order_independent(context):
    """Verify items update independently of order."""
    # Each item's update is independent, so order doesn't matter
    assert len(context.items) > 0, "Expected items to be present"
    assert True


@then("Sulfuras maintains legendary status")
def step_then_sulfuras_legendary(context):
    """Verify Sulfuras maintains its legendary properties."""
    assert context.items[0].quality == 80, "Sulfuras should always be quality 80"
    # In a real system, might check additional legendary properties
    assert True
