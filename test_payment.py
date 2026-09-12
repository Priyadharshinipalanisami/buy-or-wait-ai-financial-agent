from payment_planner import create_payment_plan


purchase_amount = 80000
safe_amount = 30000
monthly_surplus = 30000


# Create Payment Plan

payment_plan = create_payment_plan(
    purchase_amount,
    safe_amount,
    monthly_surplus
)


# Display Output

print("\n===== PAYMENT PLAN =====\n")

print(payment_plan)

print("\n========================\n")