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

  @edge_case
  Scenario: Normal item with very negative sell_in still degrades by 2
    Given a normal item with sellIn -10 and quality 10
    When the system updates quality
    Then the quality should be 8
    And the sellIn should be -11

  @regression
  Scenario: Normal item quality over 5 days before sell date
    Given a normal item with sellIn 10 and quality 20
    When 5 days pass
    Then the quality should be 15
    And the sellIn should be 5

  @regression
  Scenario: Normal item crossing sell date
    Given a normal item with sellIn 2 and quality 10
    When 3 days pass
    Then the quality should be 6
    And the sellIn should be -1

  @edge_case
  Scenario: Normal item starting at high quality
    Given a normal item with sellIn 5 and quality 50
    When the system updates quality
    Then the quality should be 49
    And the sellIn should be 4
