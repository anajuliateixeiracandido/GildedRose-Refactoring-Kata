@integration @multiple_items
Feature: Multiple Items Update Independently
  As an inventory manager
  I want to update multiple items in one operation
  So that the daily inventory update is efficient

  Background:
    Given the Gilded Rose inventory system

  @smoke @integration
  Scenario: Multiple items of different types update independently
    Given multiple items of different types
    When the system updates quality
    Then each item should update according to its own rules

  @integration @all_types
  Scenario: All item types in one inventory update correctly
    Given the following items in inventory:
      | name                                       | sellIn | quality |
      | Normal Item                                | 5      | 10      |
      | Aged Brie                                  | 5      | 10      |
      | Sulfuras, Hand of Ragnaros                 | 5      | 80      |
      | Backstage passes to a TAFKAL80ETC concert  | 5      | 10      |
    When the system updates quality
    Then the items should have the following properties:
      | name                                       | sellIn | quality |
      | Normal Item                                | 4      | 9       |
      | Aged Brie                                  | 4      | 11      |
      | Sulfuras, Hand of Ragnaros                 | 5      | 80      |
      | Backstage passes to a TAFKAL80ETC concert  | 4      | 13      |

  @edge_case @empty_inventory
  Scenario: Empty inventory doesn't crash the system
    Given an empty inventory
    When the system updates quality
    Then no errors should occur

  @integration @large_inventory
  Scenario: Large inventory updates efficiently
    Given 100 items of various types in inventory
    When the system updates quality
    Then all items should be updated
    And the operation should complete quickly

  @integration @mixed_states
  Scenario: Items at different lifecycle stages update correctly
    Given the following items in inventory:
      | name                                       | sellIn | quality | description          |
      | Normal Item                                | 10     | 20      | Well before sell     |
      | Normal Item                                | 0      | 15      | On sell date         |
      | Normal Item                                | -5     | 10      | Well past sell       |
      | Aged Brie                                  | 10     | 30      | Before sell          |
      | Aged Brie                                  | -5     | 40      | Past sell            |
      | Backstage passes to a TAFKAL80ETC concert  | 15     | 20      | Far from concert     |
      | Backstage passes to a TAFKAL80ETC concert  | 10     | 25      | 10 days to concert   |
      | Backstage passes to a TAFKAL80ETC concert  | 5      | 30      | 5 days to concert    |
      | Backstage passes to a TAFKAL80ETC concert  | 0      | 35      | Concert day          |
      | Backstage passes to a TAFKAL80ETC concert  | -1     | 40      | After concert        |
      | Sulfuras, Hand of Ragnaros                 | 0      | 80      | Legendary            |
    When the system updates quality
    Then each item should update according to its state and type

  @regression @order_independence
  Scenario: Item update order doesn't affect results
    Given the following items in inventory:
      | name        | sellIn | quality |
      | Item A      | 5      | 10      |
      | Item B      | 3      | 8       |
      | Item C      | 7      | 15      |
    When the system updates quality
    Then the update order should not affect the final quality values
