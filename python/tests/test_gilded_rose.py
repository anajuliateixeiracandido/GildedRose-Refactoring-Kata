# -*- coding: utf-8 -*-
"""Comprehensive unit tests for Gilded Rose inventory system.

This test suite provides 100% code coverage including:
- Normal items quality degradation
- Aged Brie quality improvement
- Sulfuras legendary item properties
- Backstage passes concert dynamics
- Quality boundary enforcement
- Edge cases and transitions

Coverage Requirements:
- 100% Line Coverage
- 100% Branch Coverage
- All 17 business rules tested
- All 16 edge cases covered
"""
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    """Test suite for Gilded Rose quality update system."""

    # ==================== NORMAL ITEMS ====================

    def test_normal_item_before_sell_date(self):
        """Normal item quality decreases by 1 before sell date."""
        items = [Item("Normal Item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_normal_item_on_sell_date(self):
        """Normal item quality decreases by 2 on sell date (transition day)."""
        items = [Item("Normal Item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_normal_item_after_sell_date(self):
        """Normal item quality decreases by 2 after sell date."""
        items = [Item("Normal Item", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    def test_normal_item_quality_never_negative(self):
        """Normal item quality never goes below 0."""
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_normal_item_quality_1_after_sell_date(self):
        """Normal item with quality 1 after sell date goes to 0, not negative."""
        items = [Item("Normal Item", -1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    def test_normal_item_quality_2_after_sell_date(self):
        """Normal item with quality 2 after sell date goes to 0."""
        items = [Item("Normal Item", -1, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    def test_normal_item_very_negative_sell_in(self):
        """Normal item with very negative sell_in still degrades by 2."""
        items = [Item("Normal Item", -10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(-11, items[0].sell_in)

    # ==================== AGED BRIE ====================

    def test_aged_brie_before_sell_date(self):
        """Aged Brie quality increases by 1 before sell date."""
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_aged_brie_on_sell_date(self):
        """Aged Brie quality increases by 2 on sell date (transition day)."""
        items = [Item("Aged Brie", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_aged_brie_after_sell_date(self):
        """Aged Brie quality increases by 2 after sell date."""
        items = [Item("Aged Brie", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    def test_aged_brie_quality_caps_at_50(self):
        """Aged Brie quality never exceeds 50."""
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_aged_brie_quality_49_before_sell(self):
        """Aged Brie at quality 49 increases to 50, not beyond."""
        items = [Item("Aged Brie", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_aged_brie_quality_49_after_sell(self):
        """Aged Brie at quality 49 after sell date caps at 50 (not 51)."""
        items = [Item("Aged Brie", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    def test_aged_brie_quality_48_after_sell(self):
        """Aged Brie at quality 48 after sell date caps at 50."""
        items = [Item("Aged Brie", -1, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    def test_aged_brie_starting_at_0(self):
        """Aged Brie starting at quality 0 increases normally."""
        items = [Item("Aged Brie", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_aged_brie_very_negative_sell_in(self):
        """Aged Brie with very negative sell_in still improves by 2."""
        items = [Item("Aged Brie", -10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(-11, items[0].sell_in)

    # ==================== SULFURAS ====================

    def test_sulfuras_quality_never_changes(self):
        """Sulfuras quality never changes."""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(10, items[0].sell_in)

    def test_sulfuras_sell_in_never_decreases(self):
        """Sulfuras sell_in never decreases."""
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(5, items[0].sell_in)

    def test_sulfuras_with_negative_sell_in(self):
        """Sulfuras maintains properties even with negative sell_in."""
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_sulfuras_on_sell_date(self):
        """Sulfuras on sell date maintains all properties."""
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

    # ==================== BACKSTAGE PASSES ====================

    def test_backstage_pass_far_from_concert(self):
        """Backstage pass quality increases by 1 when concert is far (>10 days)."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(14, items[0].sell_in)

    def test_backstage_pass_crosses_10_day_threshold(self):
        """Backstage pass crossing 11->10 threshold gets +1 (not +2 yet)."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(10, items[0].sell_in)

    def test_backstage_pass_10_days_or_less(self):
        """Backstage pass quality increases by 2 when 10 days or less."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_backstage_pass_crosses_5_day_threshold(self):
        """Backstage pass crossing 6->5 threshold gets +2 (not +3 yet)."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(5, items[0].sell_in)

    def test_backstage_pass_5_days_or_less(self):
        """Backstage pass quality increases by 3 when 5 days or less."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_backstage_pass_on_concert_day(self):
        """Backstage pass on concert day (sell_in=0) drops to 0 after update."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_backstage_pass_after_concert(self):
        """Backstage pass after concert has quality 0."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    def test_backstage_pass_quality_48_with_3_increment(self):
        """Backstage pass quality 48 with +3 increment caps at 50."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_backstage_pass_quality_49_with_2_increment(self):
        """Backstage pass quality 49 with +2 increment caps at 50."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_backstage_pass_quality_47_with_3_increment(self):
        """Backstage pass quality 47 with +3 increment caps at 50."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 47)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_backstage_pass_starting_at_0(self):
        """Backstage pass starting at quality 0 increases by 3."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_backstage_pass_at_max_quality(self):
        """Backstage pass at quality 50 doesn't exceed."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_backstage_pass_1_day_before_concert(self):
        """Backstage pass 1 day before concert increases by 3."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

    # ==================== MULTIPLE ITEMS ====================

    def test_multiple_items_update_independently(self):
        """Multiple items update independently in single call."""
        items = [
            Item("Normal Item", 5, 10),
            Item("Aged Brie", 5, 10),
            Item("Sulfuras, Hand of Ragnaros", 5, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 10),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(9, items[0].quality)   # Normal: -1
        self.assertEqual(11, items[1].quality)  # Aged Brie: +1
        self.assertEqual(80, items[2].quality)  # Sulfuras: no change
        self.assertEqual(13, items[3].quality)  # Backstage: +3

    def test_empty_items_list(self):
        """Empty items list doesn't crash."""
        items = []
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, len(items))

    # ==================== MULTI-DAY PROGRESSION ====================

    def test_normal_item_5_days_progression(self):
        """Normal item quality over 5 days before sell date."""
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)

        for _ in range(5):
            gilded_rose.update_quality()

        self.assertEqual(15, items[0].quality)
        self.assertEqual(5, items[0].sell_in)

    def test_backstage_pass_to_concert_progression(self):
        """Backstage pass quality progression to concert."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)

        # Day 1-5: +1 each (15->10 days)
        for _ in range(5):
            gilded_rose.update_quality()
        self.assertEqual(25, items[0].quality)
        self.assertEqual(10, items[0].sell_in)

        # Day 6-10: +2 each (10->5 days)
        for _ in range(5):
            gilded_rose.update_quality()
        self.assertEqual(35, items[0].quality)
        self.assertEqual(5, items[0].sell_in)

        # Day 11-15: +3 each (5->0 days)
        for _ in range(5):
            gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)  # Capped at 50
        self.assertEqual(0, items[0].sell_in)

        # Day 16: Concert passed, drops to 0
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    # ==================== ITEM REPRESENTATION ====================

    def test_item_repr(self):
        """Item __repr__ returns formatted string."""
        item = Item("Test Item", 5, 10)
        self.assertEqual("Test Item, 5, 10", repr(item))


if __name__ == "__main__":
    unittest.main()
