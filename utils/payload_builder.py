def minimal_purchase_payload():
    return {
        "workflow": "DIRECT",
        "amount": 100,
        "currency": "USD",
        "payment_method": {
            "type": "CARD",
            "card": {
                "number": "4111111111111111",
                "cvv": "123",
                "expiry_month": "12",
                "expiry_year": "2026"
            }
        }
    }


def invalid_card_payload():
    payload = minimal_purchase_payload()
    payload["payment_method"]["card"]["number"] = "0000000000000000"
    return payload
