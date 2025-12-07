# -*- coding: utf-8 -*-
"""Gilded Rose Inventory Management System.

This module implements the quality update logic for various item types
in the Gilded Rose inventory system using the Strategy Pattern.
"""

# Item name constants
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"

# Quality boundaries
MIN_QUALITY = 0
MAX_QUALITY = 50
SULFURAS_QUALITY = 80


class GildedRose:
    """Manages quality updates for inventory items.

    Uses the Strategy Pattern to apply item-specific update rules.
    """

    def __init__(self, items):
        """Initialize the Gilded Rose system with a list of items.

        Args:
            items: List of Item objects to manage.
        """
        self.items = items
        self.update_strategies = self._build_update_strategies()

    def _build_update_strategies(self):
        """Build strategy dictionary mapping item names to update methods.

        Returns:
            Dictionary mapping item names to their update methods.
        """
        return {
            AGED_BRIE: self._update_aged_brie,
            BACKSTAGE_PASSES: self._update_backstage_pass,
            SULFURAS: self._update_sulfuras,
        }

    def update_quality(self):
        """Update quality and sell_in for all items according to business rules."""
        for item in self.items:
            strategy = self.update_strategies.get(item.name, self._update_normal_item)
            strategy(item)

    def _update_normal_item(self, item):
        """Update quality for normal items.

        Normal items degrade by 1 before sell date, by 2 after.

        Args:
            item: Item to update.
        """
        self._decrease_quality(item)
        self._decrease_sell_in(item)

        if self._is_expired(item):
            self._decrease_quality(item)

    def _update_aged_brie(self, item):
        """Update quality for Aged Brie.

        Aged Brie improves by 1 before sell date, by 2 after.

        Args:
            item: Item to update.
        """
        self._increase_quality(item)
        self._decrease_sell_in(item)

        if self._is_expired(item):
            self._increase_quality(item)

    def _update_backstage_pass(self, item):
        """Update quality for Backstage passes.

        Quality increases by:
        - 1 when more than 10 days remain
        - 2 when 10 days or less remain
        - 3 when 5 days or less remain
        - Drops to 0 after concert (sell_in < 0)

        Args:
            item: Item to update.
        """
        self._increase_quality(item)

        if item.sell_in < 11:
            self._increase_quality(item)

        if item.sell_in < 6:
            self._increase_quality(item)

        self._decrease_sell_in(item)

        if self._is_expired(item):
            item.quality = MIN_QUALITY

    def _update_sulfuras(self, item):
        """Update quality for Sulfuras (legendary item).

        Sulfuras never changes quality or sell_in.

        Args:
            item: Item to update (no changes made).
        """
        pass  # Legendary items never change

    def _increase_quality(self, item):
        """Increase item quality by 1, respecting maximum bound.

        Args:
            item: Item whose quality to increase.
        """
        if item.quality < MAX_QUALITY:
            item.quality += 1

    def _decrease_quality(self, item):
        """Decrease item quality by 1, respecting minimum bound.

        Args:
            item: Item whose quality to decrease.
        """
        if item.quality > MIN_QUALITY:
            item.quality -= 1

    def _decrease_sell_in(self, item):
        """Decrease item sell_in by 1.

        Args:
            item: Item whose sell_in to decrease.
        """
        item.sell_in -= 1

    def _is_expired(self, item):
        """Check if item has passed its sell date.

        Args:
            item: Item to check.

        Returns:
            True if item.sell_in < 0, False otherwise.
        """
        return item.sell_in < 0


class Item:
    """Represents an inventory item with name, sell_in, and quality."""

    def __init__(self, name, sell_in, quality):
        """Initialize an inventory item.

        Args:
            name: Name of the item.
            sell_in: Days until sell date (negative means expired).
            quality: Quality value of the item.
        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        """Return string representation of item.

        Returns:
            String in format "name, sell_in, quality".
        """
        return f"{self.name}, {self.sell_in}, {self.quality}"
