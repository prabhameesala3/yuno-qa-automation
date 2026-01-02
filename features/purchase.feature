Feature: Purchase Payment API

  @sanity @purchase
  Scenario: Successful purchase with minimal required fields
    Given valid API credentials
    And a minimal purchase payload
    When I create a DIRECT purchase payment
    Then the response status code should be 201

  @regression @negative
  Scenario: Purchase fails with invalid card number
    Given valid API credentials
    And a purchase payload with invalid card number
    When I create a DIRECT purchase payment
    Then the response status code should be 400
