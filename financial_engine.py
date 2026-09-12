def calculate_safe_amount(
    current_balance,
    essential_expenses,
    recurring_expenses,
    pending_payments,
    minimum_balance
):

    safe_amount = (

        current_balance

        - essential_expenses

        - recurring_expenses

        - pending_payments

        - minimum_balance

    )

    return max(
        0,
        safe_amount
    )


def calculate_monthly_surplus(
    monthly_income,
    essential_expenses,
    recurring_expenses
):

    monthly_surplus = (

        monthly_income

        - essential_expenses

        - recurring_expenses

    )

    return monthly_surplus


def calculate_health_score(
    current_balance,
    monthly_income,
    total_expenses,
    minimum_balance
):

    available_money = (

        current_balance

        + monthly_income

    )

    remaining_money = (

        available_money

        - total_expenses

        - minimum_balance

    )

    if available_money == 0:

        return 0

    score = (

        remaining_money
        / available_money

    ) * 100

    score = max(
        0,
        min(100, score)
    )

    return round(
        score,
        2
    )