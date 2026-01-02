Feature: Refund Payment API

  @integration @refund
  Scenario: Successful refund for a completed payment
    Given a successful purchase exists
    When I request a refund for the payment
    Then the refund status code should be 200
