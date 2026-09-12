import pandas as pd


def create_payment_plan(
    purchase_amount,
    safe_amount,
    monthly_surplus
):

    payment_plan = []

    remaining_amount = purchase_amount


    # Pay Today

    if safe_amount > 0:

        payment_today = min(
            safe_amount,
            purchase_amount
        )

        payment_plan.append({

            "Payment":
            "Today",

            "Amount":
            payment_today

        })

        remaining_amount = (

            remaining_amount
            - payment_today

        )


    # Monthly Payments

    month = 1

    while (
        remaining_amount > 0
        and monthly_surplus > 0
    ):

        payment = min(

            monthly_surplus,

            remaining_amount

        )

        payment_plan.append({

            "Payment":
            f"Month {month}",

            "Amount":
            payment

        })

        remaining_amount = (

            remaining_amount
            - payment

        )

        month += 1


    return pd.DataFrame(
        payment_plan
    )