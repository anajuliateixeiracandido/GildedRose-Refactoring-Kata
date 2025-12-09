@aged_brie @special_item
Feature: Aged Brie Quality Improvement
  As an inventory manager
  I want Aged Brie to increase in quality as it ages
  So that I can price aged cheese appropriately

  Background:
    Given the Gilded Rose inventory system

  @smoke
  Scenario: Aged Brie quality increases by 1 before sell date
    Given an Aged Brie with sellIn 10 and quality 20
    When the system updates quality
    Then the quality should be 21
    And the sellIn should be 9

  @transition
  Scenario: Aged Brie quality increases by 2 on sell date
    Given an Aged Brie with sellIn 0 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be -1

  Scenario: Aged Brie quality increases by 2 after sell date
    Given an Aged Brie with sellIn -1 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be -2

  @edge_case @quality_ceiling
  Scenario: Aged Brie quality never exceeds 50
    Given an Aged Brie with sellIn 5 and quality 50
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  @edge_case @quality_ceiling
  Scenario: Aged Brie at quality 49 increases to 50 (not beyond)
    Given an Aged Brie with sellIn 5 and quality 49
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  @edge_case @quality_ceiling
  Scenario: Aged Brie at quality 49 after sell date caps at 50
    Given an Aged Brie with sellIn -1 and quality 49
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be -2

  @edge_case @quality_ceiling
  Scenario: Aged Brie at quality 48 after sell date caps at 50
    Given an Aged Brie with sellIn -1 and quality 48
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be -2

  @edge_case @quality_floor
  Scenario: Aged Brie starting at quality 0 increases normally
    Given an Aged Brie with sellIn 5 and quality 0
    When the system updates quality
    Then the quality should be 1
    And the sellIn should be 4

  @regression
  Scenario: Aged Brie with very negative sellIn improves by 2
    Given an Aged Brie with sellIn -10 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be -11

  @time_progression
  Scenario Outline: Aged Brie quality improvement over time
    Given an Aged Brie with sellIn <initial_sellIn> and quality <initial_quality>
    When <days> days pass
    Then the quality should be <final_quality>
    And the sellIn should be <final_sellIn>

    Examples:
      | initial_sellIn | initial_quality | days | final_quality | final_sellIn |
      | 10             | 0               | 1    | 1             | 9            |
      | 10             | 20              | 5    | 25            | 5            |
      | 5              | 40              | 5    | 45            | 0            |
      | 2              | 45              | 3    | 49            | -1           |
      | 0              | 48              | 1    | 50            | -1           |
      | -5             | 30              | 5    | 40            | -10          |
