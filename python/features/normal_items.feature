@normal @unit
Feature: Normal Item Quality Degradation
  As an inventory manager
  I want normal items to degrade in quality over time
  So that I can track item freshness and value

  Background:
    Given the Gilded Rose inventory system

  @smoke
  Scenario: Normal item quality decreases by 1 before sell date
    Given a normal item with sellIn 5 and quality 10
    When the system updates quality
    Then the quality should be 9
    And the sellIn should be 4

  @transition
  Scenario: Normal item quality decreases by 2 on sell date (transition day)
    Given a normal item with sellIn 0 and quality 10
    When the system updates quality
    Then the quality should be 8
    And the sellIn should be -1

  Scenario: Normal item quality decreases by 2 after sell date
    Given a normal item with sellIn -1 and quality 10
    When the system updates quality
    Then the quality should be 8
    And the sellIn should be -2

  @edge_case @quality_floor
  Scenario: Normal item quality never goes negative
    Given a normal item with sellIn 5 and quality 0
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be 4

  @edge_case @quality_floor
  Scenario: Normal item with quality 1 after sell date goes to 0
    Given a normal item with sellIn -1 and quality 1
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be -2

  @edge_case @quality_floor
  Scenario: Normal item with quality 2 after sell date goes to 0
    Given a normal item with sellIn -1 and quality 2
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be -2

  @regression
  Scenario: Normal item with very negative sellIn still degrades by 2
    Given a normal item with sellIn -10 and quality 10
    When the system updates quality
    Then the quality should be 8
    And the sellIn should be -11

  @time_progression
  Scenario Outline: Normal item quality degradation over time
    Given a normal item with sellIn <initial_sellIn> and quality <initial_quality>
    When <days> days pass
    Then the quality should be <final_quality>
    And the sellIn should be <final_sellIn>

    Examples:
      | initial_sellIn | initial_quality | days | final_quality | final_sellIn |
      | 10             | 20              | 1    | 19            | 9            |
      | 10             | 20              | 5    | 15            | 5            |
      | 5              | 10              | 5    | 5             | 0            |
      | 2              | 10              | 3    | 6             | -1           |
      | 0              | 10              | 1    | 8             | -1           |
      | -1             | 10              | 1    | 8             | -2           |
