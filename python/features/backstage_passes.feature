@backstage @special_item @concert
Feature: Backstage Pass Concert Ticket Dynamics
  As an inventory manager
  I want backstage pass quality to increase as the concert approaches
  So that ticket prices reflect proximity to the event

  Background:
    Given the Gilded Rose inventory system

  @smoke @far_from_concert
  Scenario: Backstage pass increases by 1 when concert is far (>10 days)
    Given a Backstage pass with sellIn 15 and quality 20
    When the system updates quality
    Then the quality should be 21
    And the sellIn should be 14

  @threshold @critical
  Scenario: Backstage pass crossing 11→10 threshold gets +1 (not +2 yet)
    Given a Backstage pass with sellIn 11 and quality 20
    When the system updates quality
    Then the quality should be 21
    And the sellIn should be 10

  @moderate_urgency
  Scenario: Backstage pass increases by 2 when 10 days or less
    Given a Backstage pass with sellIn 10 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be 9

  @threshold @critical
  Scenario: Backstage pass crossing 6→5 threshold gets +2 (not +3 yet)
    Given a Backstage pass with sellIn 6 and quality 20
    When the system updates quality
    Then the quality should be 22
    And the sellIn should be 5

  @high_urgency
  Scenario: Backstage pass increases by 3 when 5 days or less
    Given a Backstage pass with sellIn 5 and quality 20
    When the system updates quality
    Then the quality should be 23
    And the sellIn should be 4

  @critical @concert_day
  Scenario: Backstage pass on concert day (sellIn=0) drops to 0 after update
    Given a Backstage pass with sellIn 0 and quality 20
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be -1

  @expired @worthless
  Scenario: Backstage pass after concert has quality 0
    Given a Backstage pass with sellIn -1 and quality 20
    When the system updates quality
    Then the quality should be 0
    And the sellIn should be -2

  @edge_case @quality_ceiling
  Scenario: Backstage pass quality 48 with +3 increment caps at 50
    Given a Backstage pass with sellIn 5 and quality 48
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  @edge_case @quality_ceiling
  Scenario: Backstage pass quality 49 with +2 increment caps at 50
    Given a Backstage pass with sellIn 10 and quality 49
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 9

  @edge_case @quality_ceiling
  Scenario: Backstage pass quality 47 with +3 increment caps at 50
    Given a Backstage pass with sellIn 5 and quality 47
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  @edge_case @quality_floor
  Scenario: Backstage pass starting at quality 0 increases by 3
    Given a Backstage pass with sellIn 5 and quality 0
    When the system updates quality
    Then the quality should be 3
    And the sellIn should be 4

  @edge_case @quality_ceiling
  Scenario: Backstage pass at max quality doesn't exceed 50
    Given a Backstage pass with sellIn 5 and quality 50
    When the system updates quality
    Then the quality should be 50
    And the sellIn should be 4

  @edge_case @last_minute
  Scenario: Backstage pass 1 day before concert increases by 3
    Given a Backstage pass with sellIn 1 and quality 20
    When the system updates quality
    Then the quality should be 23
    And the sellIn should be 0

  @time_progression @full_journey
  Scenario: Backstage pass quality progression from 15 days to concert
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
    When 1 day passes
    Then the quality should be 0
    And the sellIn should be -1

  @scenario_outline @quality_progression
  Scenario Outline: Backstage pass quality at different time periods
    Given a Backstage pass with sellIn <sellIn> and quality <initial_quality>
    When the system updates quality
    Then the quality should be <final_quality>
    And the sellIn should be <final_sellIn>

    Examples: Far from concert (>10 days)
      | sellIn | initial_quality | final_quality | final_sellIn |
      | 15     | 20              | 21            | 14           |
      | 12     | 30              | 31            | 11           |
      | 11     | 40              | 41            | 10           |

    Examples: 10 days or less (6-10 days)
      | sellIn | initial_quality | final_quality | final_sellIn |
      | 10     | 20              | 22            | 9            |
      | 8      | 25              | 27            | 7            |
      | 6      | 35              | 37            | 5            |

    Examples: 5 days or less (1-5 days)
      | sellIn | initial_quality | final_quality | final_sellIn |
      | 5      | 20              | 23            | 4            |
      | 3      | 30              | 33            | 2            |
      | 1      | 40              | 43            | 0            |

    Examples: Concert day and after
      | sellIn | initial_quality | final_quality | final_sellIn |
      | 0      | 45              | 0             | -1           |
      | -1     | 40              | 0             | -2           |
      | -5     | 30              | 0             | -6           |
