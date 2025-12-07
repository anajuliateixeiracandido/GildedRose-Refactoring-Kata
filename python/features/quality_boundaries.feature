@quality_cap @quality_floor
Feature: Quality Boundary Rules
  As an inventory manager
  I want quality to be bounded within valid ranges
  So that the system maintains data integrity

  Background:
    Given the Gilded Rose inventory system

  @smoke
  Scenario Outline: Quality never exceeds 50 for non-legendary items
    Given <item_type> with sellIn 10 and quality 50
    When the system updates quality
    Then the quality should not exceed 50

    Examples:
      | item_type           |
      | a normal item       |
      | an Aged Brie        |
      | a Backstage pass    |

  @smoke
  Scenario Outline: Quality never goes below 0
    Given <item_type> with sellIn 5 and quality 0
    When the system updates quality
    Then the quality should be <expected_quality>

    Examples:
      | item_type        | expected_quality |
      | a normal item    | 0                |
      | a Backstage pass | 3                |

  @smoke @sulfuras
  Scenario: Sulfuras quality is always 80
    Given a Sulfuras with sellIn 10 and quality 80
    When 100 days pass
    Then the quality should be 80

  @edge_case
  Scenario: Multiple items respect individual quality bounds
    Given multiple items of different types
    When the system updates quality
    Then each item should update according to its specific rules
