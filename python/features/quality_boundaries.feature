@boundaries @quality_limits
Feature: Quality Boundary Enforcement
  As an inventory manager
  I want quality to never be negative or exceed 50 (except Sulfuras)
  So that quality values remain within valid business ranges

  Background:
    Given the Gilded Rose inventory system

  @quality_floor @normal
  Scenario: Normal item quality cannot go below 0
    Given a normal item with sellIn 5 and quality 0
    When the system updates quality
    Then the quality should be 0

  @quality_floor @aged_brie
  Scenario: Aged Brie can start at quality 0
    Given an Aged Brie with sellIn 5 and quality 0
    When the system updates quality
    Then the quality should be 1

  @quality_ceiling @aged_brie
  Scenario: Aged Brie quality cannot exceed 50
    Given an Aged Brie with sellIn 5 and quality 50
    When the system updates quality
    Then the quality should be 50

  @quality_ceiling @backstage
  Scenario: Backstage pass quality cannot exceed 50
    Given a Backstage pass with sellIn 5 and quality 50
    When the system updates quality
    Then the quality should be 50

  @quality_exception @legendary
  Scenario: Sulfuras quality is always 80 (exception to 50 limit)
    Given a Sulfuras with sellIn 0 and quality 80
    When the system updates quality
    Then the quality should be 80

  @quality_floor @backstage @expired
  Scenario: Backstage pass after concert drops to 0
    Given a Backstage pass with sellIn -1 and quality 45
    When the system updates quality
    Then the quality should be 0

  @scenario_outline @quality_limits
  Scenario Outline: Quality boundaries are enforced for all item types
    Given <item_type> with sellIn <sellIn> and quality <initial_quality>
    When the system updates quality
    Then the quality should be <final_quality>

    Examples: Quality floor (minimum 0)
      | item_type        | sellIn | initial_quality | final_quality |
      | a normal item    | 5      | 0               | 0             |
      | a normal item    | -1     | 1               | 0             |
      | a normal item    | -1     | 2               | 0             |
      | an Aged Brie     | 5      | 0               | 1             |
      | a Backstage pass | 5      | 0               | 3             |

    Examples: Quality ceiling (maximum 50, except Sulfuras)
      | item_type        | sellIn | initial_quality | final_quality |
      | an Aged Brie     | 5      | 50              | 50            |
      | an Aged Brie     | 5      | 49              | 50            |
      | an Aged Brie     | -1     | 48              | 50            |
      | a Backstage pass | 5      | 50              | 50            |
      | a Backstage pass | 5      | 49              | 50            |
      | a Backstage pass | 5      | 48              | 50            |
      | a Backstage pass | 10     | 49              | 50            |

    Examples: Sulfuras exception (always 80)
      | item_type   | sellIn | initial_quality | final_quality |
      | a Sulfuras  | 10     | 80              | 80            |
      | a Sulfuras  | 0      | 80              | 80            |
      | a Sulfuras  | -10    | 80              | 80            |
