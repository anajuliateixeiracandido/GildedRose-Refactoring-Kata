@backstage @unit
Feature: Backstage Pass Concert Dynamics
  As an inventory manager
  I want backstage pass quality to reflect concert proximity
  So that I can price them appropriately

  Background:
    Given the Gilded Rose inventory system

  @smoke
  Scenario: Backstage pass quality increases by 1 when concert is far (>10 days)
    Given a Backstage pass with sellIn 15 and quality 20
    When the system updates quality
    Then the quality should be 21
    And the sellIn should be 14

  @edge_case
  Scenario: Backstage pass crossing 11 to 10 day threshold gets +1
    Given a Backstage pass with sellIn 11 and quality 20
    When the system updates quality
    Then the quality should be 21
    And the sellIn should be 10

  @smoke
  Scenario: Backstage pass quality increases by 2 when 10 days or less
    Given a Backstage pass with sellIn 10 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be 9

  @edge_case
  Scenario: Backstage pass crossing 6 to 5 day threshold gets +2
    Given a Backstage pass with sellIn 6 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be 5

  @smoke
  Scenario: Backstage pass quality increases by 3 when 5 days or less
    Given a Backstage pass with sellIn 5 and quality 20
    When the system updates quality
    Then the quality should be 23
    And the sellIn should be 4

  Scenario: Backstage pass 1 day before concert increases by 3
    Given a Backstage pass with sellIn 1 and quality 20
    When the system updates quality
    Then the quality should be 23
    And the sellIn should be 0

  @transition @critical
  Scenario: Backstage pass on concert day drops to 0 after increases
    Given a Backstage pass with sellIn 0 and quality 20
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be -1

  @critical
  Scenario: Backstage pass after concert has quality 0
    Given a Backstage pass with sellIn -1 and quality 20
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be -2

  @edge_case @quality_cap
  Scenario: Backstage pass quality 48 with +3 increment caps at 50
    Given a Backstage pass with sellIn 5 and quality 48
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  @edge_case @quality_cap
  Scenario: Backstage pass quality 49 with +2 increment caps at 50
    Given a Backstage pass with sellIn 10 and quality 49
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 9

  @edge_case @quality_cap
  Scenario: Backstage pass quality 47 with +3 increment caps at 50
    Given a Backstage pass with sellIn 5 and quality 47
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  @edge_case @quality_cap
  Scenario: Backstage pass at quality 50 doesn't exceed
    Given a Backstage pass with sellIn 5 and quality 50
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  @edge_case
  Scenario: Backstage pass starting at quality 0 increases by 3
    Given a Backstage pass with sellIn 5 and quality 0
    When the system updates quality
    Then the quality should be 3
    And the sellIn should be 4

  @regression
  Scenario: Backstage pass quality progression to concert
    Given a Backstage pass with sellIn 15 and quality 20
    When 5 days pass
    Then the quality should be 25
    And the sellIn should be 10
    When 5 days pass
    Then the quality should be 35
    And the sellIn should be 5
    When 5 days pass
    Then the quality should be 50
    And the sellIn should be 0
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be -1
