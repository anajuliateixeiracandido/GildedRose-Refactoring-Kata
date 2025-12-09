@sulfuras @legendary @special_item
Feature: Sulfuras Legendary Item Properties
  As an inventory manager
  I want Sulfuras to never degrade or change
  So that legendary items maintain their eternal value

  Background:
    Given the Gilded Rose inventory system

  @smoke @immutable
  Scenario: Sulfuras quality never changes
    Given a Sulfuras with sellIn 10 and quality 80
    When the system updates quality
    Then the quality should be 80
    And the sellIn should be 10

  @immutable
  Scenario: Sulfuras sellIn never decreases
    Given a Sulfuras with sellIn 5 and quality 80
    When the system updates quality
    Then the quality should be 80
    And the sellIn should be 5

  @edge_case @immutable
  Scenario: Sulfuras maintains properties with negative sellIn
    Given a Sulfuras with sellIn -1 and quality 80
    When the system updates quality
    Then the quality should be 80
    And the sellIn should be -1

  @edge_case @transition
  Scenario: Sulfuras on sell date maintains all properties
    Given a Sulfuras with sellIn 0 and quality 80
    When the system updates quality
    Then the quality should be 80
    And the sellIn should be 0

  @time_progression @immutable
  Scenario Outline: Sulfuras never changes over time
    Given a Sulfuras with sellIn <initial_sellIn> and quality 80
    When <days> days pass
    Then the quality should be 80
    And the sellIn should be <initial_sellIn>

    Examples:
      | initial_sellIn | days |
      | 10             | 1    |
      | 5              | 5    |
      | 0              | 10   |
      | -1             | 100  |
      | -100           | 1000 |

  @business_rule
  Scenario: Sulfuras is always quality 80
    Given a Sulfuras with sellIn 0 and quality 80
    When the system updates quality
    Then the quality should be 80
    And the sellIn should be 0
    And Sulfuras maintains legendary status
