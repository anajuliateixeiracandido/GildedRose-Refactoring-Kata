@integration
Feature: Multiple Item Management
  As an inventory manager
  I want to update multiple items simultaneously
  So that I can efficiently manage my entire inventory

  Background:
    Given the Gilded Rose inventory system

  @smoke @integration
  Scenario: Multiple items update independently in a single call
    Given multiple items of different types
    When the system updates quality
    Then each item should update according to its specific rules

  @integration
  Scenario: Empty inventory doesn't cause errors
    Given the Gilded Rose inventory system
    When the system updates quality
    Then no errors should occur

  @integration @regression
  Scenario: Mixed items over multiple days
    Given multiple items of different types
    When 3 days pass
    Then each item should have updated according to its rules for 3 days
