@aged_brie @unit
Feature: Aged Brie Quality Improvement
  As an inventory manager
  I want Aged Brie to increase in quality over time
  So that I can recognize its aging value

  Background:
    Given the Gilded Rose inventory system

  @smoke
  Scenario: Aged Brie quality increases by 1 before sell date
    Given an Aged Brie with sellIn 10 and quality 20
    When the system updates quality
    Then the quality should be 21
    And the sellIn should be 9

  @transition
  Scenario: Aged Brie quality increases by 2 on sell date (transition day)
    Given an Aged Brie with sellIn 0 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be -1

  Scenario: Aged Brie quality increases by 2 after sell date
    Given an Aged Brie with sellIn -1 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be -2

  @edge_case @quality_cap
  Scenario: Aged Brie quality caps at 50
    Given an Aged Brie with sellIn 5 and quality 50
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  @edge_case @quality_cap
  Scenario: Aged Brie at quality 49 increases to 50 before sell date
    Given an Aged Brie with sellIn 5 and quality 49
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  @edge_case @quality_cap @transition
  Scenario: Aged Brie at quality 49 caps at 50 on transition day
    Given an Aged Brie with sellIn 0 and quality 49
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be -1

  @edge_case @quality_cap
  Scenario: Aged Brie at quality 48 after sell date caps at 50
    Given an Aged Brie with sellIn -1 and quality 48
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be -2

  @edge_case
  Scenario: Aged Brie starting at quality 0 increases normally
    Given an Aged Brie with sellIn 5 and quality 0
    When the system updates quality
    Then the quality should be 1
    And the sellIn should be 4

  @edge_case
  Scenario: Aged Brie with very negative sell_in still improves by 2
    Given an Aged Brie with sellIn -10 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be -11
