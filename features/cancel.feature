Feature: Cancel Payment API

  @integration @cancel
  Scenario: Cancel an authorized payment successfully
    Given a valid authorization exists
    When I cancel the authorized payment
    Then the cancel status code should be 200
