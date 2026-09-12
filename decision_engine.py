def make_decision(
    purchase_amount,
    safe_amount,
    monthly_surplus
):

    # BUY NOW
    if safe_amount >= purchase_amount:

        return {
            "status": "Affordable Now",
            "decision": "BUY NOW",
            "payment_method": "Pay in Full"
        }

    # BUY WITH PAYMENT PLAN
    elif safe_amount > 0 and monthly_surplus > 0:

        return {
            "status": "Affordable With Plan",
            "decision": "BUY WITH A PLAN",
            "payment_method": "Partial Payment + Installments"
        }

    # WAIT
    elif monthly_surplus > 0:

        return {
            "status": "Affordable Later",
            "decision": "WAIT",
            "payment_method": "Wait Until Financially Safe"
        }

    # DO NOT PROCEED
    else:

        return {
            "status": "Not Affordable",
            "decision": "DO NOT PROCEED",
            "payment_method": "Not Recommended"
        }