Feature: Authorization Payment API

  @integration @authorization
  Scenario: Successful authorization and capture
    Given a valid authorization request
    When I capture the authorized payment
    Then the capture status code should be 200
