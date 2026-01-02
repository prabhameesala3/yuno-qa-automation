def create_payment(payload):
    """
    Simulates payment creation
    """
    if payload["payment_method"]["card"]["number"] == "0000000000000000":
        return {"status_code": 400}
    return {"status_code": 201, "payment_id": "PAY123"}


def refund_payment(payment_id):
    """
    Simulates refund
    """
    if payment_id:
        return {"status_code": 200}
    return {"status_code": 404}


def authorize_payment():
    """
    Simulates authorization
    """
    return {"status_code": 201, "auth_id": "AUTH123"}


def capture_payment(auth_id):
    """
    Simulates capture
    """
    if auth_id:
        return {"status_code": 200}
    return {"status_code": 400}


def cancel_payment(auth_id):
    """
    Simulates cancel
    """
    if auth_id:
        return {"status_code": 200}
    return {"status_code": 400}


def verify_payment():
    """
    Simulates verify payment
    """
    return {"status_code": 200}
