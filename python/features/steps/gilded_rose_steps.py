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


@then("the quality should not exceed {max_quality:d}")
def step_then_quality_not_exceed(context, max_quality):
    """Verify quality does not exceed maximum value."""
    assert (
        hasattr(context, "items") and len(context.items) > 0
    ), "No items in context. Did you forget @given step?"

    actual = context.items[0].quality
    assert actual <= max_quality, f"Quality {actual} exceeds maximum {max_quality}"


@then("no errors should occur")
def step_then_no_errors(context):
    """Verify no exceptions were raised during execution."""
    # For empty inventory test: initialize empty GildedRose if needed
    if not hasattr(context, "gilded_rose"):
        context.gilded_rose = GildedRose([])
    # If we reached this step, no errors occurred
    pass


@then("each item should update according to its specific rules")
def step_then_each_item_updates(context):
    """Validate each item type updates correctly in multi-item scenario."""
    assert (
        hasattr(context, "items") and len(context.items) >= 4
    ), "Expected at least 4 items in context for multi-item test"

    # Expected behavior after 1 update:
    # Normal item: quality decreased by 1
    assert (
        context.items[0].quality == 19
    ), f"Normal item quality should be 19 but got {context.items[0].quality}"
    assert (
        context.items[0].sell_in == 9
    ), f"Normal item sellIn should be 9 but got {context.items[0].sell_in}"

    # Aged Brie: quality increased by 1
    assert (
        context.items[1].quality == 11
    ), f"Aged Brie quality should be 11 but got {context.items[1].quality}"
    assert (
        context.items[1].sell_in == 4
    ), f"Aged Brie sellIn should be 4 but got {context.items[1].sell_in}"

    # Sulfuras: unchanged
    assert (
        context.items[2].quality == 80
    ), f"Sulfuras quality should be 80 but got {context.items[2].quality}"
    assert (
        context.items[2].sell_in == 0
    ), f"Sulfuras sellIn should be 0 but got {context.items[2].sell_in}"

    # Backstage: quality increased by 1 (>10 days away)
    assert (
        context.items[3].quality == 21
    ), f"Backstage pass quality should be 21 but got {context.items[3].quality}"
    assert (
        context.items[3].sell_in == 14
    ), f"Backstage pass sellIn should be 14 but got {context.items[3].sell_in}"


@then("each item should have updated according to its rules for {days:d} days")
def step_then_items_updated_for_days(context, days):
    """Validate items updated correctly over multiple days."""
    assert (
        hasattr(context, "items") and len(context.items) >= 4
    ), "Expected at least 4 items in context"

    # After 3 days:
    # Normal item (sellIn 10, quality 20): quality -3 = 17, sellIn = 7
    assert (
        context.items[0].quality == 17
    ), f"Normal item quality should be 17 but got {context.items[0].quality}"
    assert (
        context.items[0].sell_in == 7
    ), f"Normal item sellIn should be 7 but got {context.items[0].sell_in}"

    # Aged Brie (sellIn 5, quality 10): quality +3 = 13, sellIn = 2
    assert (
        context.items[1].quality == 13
    ), f"Aged Brie quality should be 13 but got {context.items[1].quality}"
    assert (
        context.items[1].sell_in == 2
    ), f"Aged Brie sellIn should be 2 but got {context.items[1].sell_in}"

    # Sulfuras: unchanged
    assert (
        context.items[2].quality == 80
    ), f"Sulfuras quality should be 80 but got {context.items[2].quality}"
    assert (
        context.items[2].sell_in == 0
    ), f"Sulfuras sellIn should be 0 but got {context.items[2].sell_in}"

    # Backstage (sellIn 15, quality 20): quality +3 = 23, sellIn = 12
    assert (
        context.items[3].quality == 23
    ), f"Backstage pass quality should be 23 but got {context.items[3].quality}"
    assert (
        context.items[3].sell_in == 12
    ), f"Backstage pass sellIn should be 12 but got {context.items[3].sell_in}"


@then("item {index:d} should have quality {expected_quality:d}")
def step_then_item_quality_by_index(context, index, expected_quality):
    """Verify specific item in list has expected quality."""
    assert (
        hasattr(context, "items") and len(context.items) > index
    ), f"Not enough items in context. Need at least {index + 1} items."

    actual = context.items[index].quality
    assert (
        actual == expected_quality
    ), f"Item {index}: expected quality {expected_quality} but got {actual}"
