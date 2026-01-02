Feature: Verify Payment API

  @integration @verify
  Scenario: Verify card details without charging
    Given a verify payment request
    When I submit the verify payment
    Then the verify status code should be 200
