from behave import given, when, then

from utils.payload_builder import (
    minimal_purchase_payload,
    invalid_card_payload
)

from utils.api_client import (
    create_payment,
    refund_payment,
    authorize_payment,
    capture_payment,
    cancel_payment,
    verify_payment
)

@given("valid API credentials")
def step_valid_credentials(context):
    context.headers = {
        "public-api-key": "DUMMY",
        "private-secret-key": "DUMMY"
    }


@given("a minimal purchase payload")
def step_minimal_payload(context):
    context.payload = minimal_purchase_payload()


@given("a purchase payload with invalid card number")
def step_invalid_card(context):
    context.payload = invalid_card_payload()


@when("I create a DIRECT purchase payment")
def step_create_payment(context):
    context.response = create_payment(context.payload)


@then("the response status code should be 201")
def step_success_status(context):
    assert context.response["status_code"] == 201


@then("the response status code should be 400")
def step_failure_status(context):
    assert context.response["status_code"] == 400


@given("a successful purchase exists")
def step_successful_purchase(context):
    context.payment = create_payment(minimal_purchase_payload())


@when("I request a refund for the payment")
def step_request_refund(context):
    context.refund_response = refund_payment(context.payment["payment_id"])


@then("the refund status code should be 200")
def step_refund_success(context):
    assert context.refund_response["status_code"] == 200


@given("a valid authorization exists")
def step_authorization(context):
    context.authorization = authorize_payment()


@when("I capture the authorized payment")
def step_capture(context):
    context.capture_response = capture_payment(context.authorization["auth_id"])


@then("the capture status code should be 200")
def step_capture_success(context):
    assert context.capture_response["status_code"] == 200

@when("I cancel the authorized payment")
def step_cancel(context):
    context.cancel_response = cancel_payment(context.authorization["auth_id"])


@then("the cancel status code should be 200")
def step_cancel_success(context):
    assert context.cancel_response["status_code"] == 200

@given("a verify payment request")
def step_verify_request(context):
    context.verify_request = True


@when("I submit the verify payment")
def step_verify(context):
    context.verify_response = verify_payment()


@then("the verify status code should be 200")
def step_verify_success(context):
    assert context.verify_response["status_code"] == 200

@given("a valid authorization request")
def step_valid_authorization_request(context):
    context.authorization = authorize_payment()
