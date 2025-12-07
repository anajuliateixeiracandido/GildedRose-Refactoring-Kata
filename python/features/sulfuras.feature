@sulfuras @unit
Feature: Sulfuras Legendary Item Properties
  As an inventory manager
  I want Sulfuras to maintain constant quality and sell_in
  So that I can recognize its legendary status

  Background:
    Given the Gilded Rose inventory system

  @smoke
  Scenario: Sulfuras quality never changes
    Given a Sulfuras with sellIn 10 and quality 80
    When the system updates quality
    Then the quality should be 80
    And the sellIn should be 10

  @smoke
  Scenario: Sulfuras sell_in never decreases
    Given a Sulfuras with sellIn 5 and quality 80
    When 10 days pass
    Then the quality should be 80
    And the sellIn should be 5

  @edge_case
  Scenario: Sulfuras with negative sell_in maintains all properties
    Given a Sulfuras with sellIn -1 and quality 80
    When the system updates quality
    Then the quality should be 80
    And the sellIn should be -1

  @transition
  Scenario: Sulfuras on sell date maintains all properties
    Given a Sulfuras with sellIn 0 and quality 80
    When the system updates quality
    Then the quality should be 80
    And the sellIn should be 0
