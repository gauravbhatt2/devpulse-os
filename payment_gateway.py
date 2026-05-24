# Payment Gateway — Hotfix for 500 error on /checkout
def process_payment(cart_id, amount):
    # SCRUM-6: added retry logic for 500 errors
    for attempt in range(3):
        result = call_payment_api(cart_id, amount)
        if result.status == "ok":
            return result
    raise PaymentFailureError("Payment API unreachable after 3 retries")
#SCRUM-6 hotfix: fix 500 error on checkout endpoint
