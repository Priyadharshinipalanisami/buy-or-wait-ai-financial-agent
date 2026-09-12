from decision_engine import make_decision


# Input values

purchase_amount = 80000
safe_amount = 30000
monthly_surplus = 30000


# Call the function

result = make_decision(
    purchase_amount,
    safe_amount,
    monthly_surplus
)


# Display Output

print("\n===== AI FINANCIAL DECISION =====\n")

print("Purchase Amount: ₹", purchase_amount)

print("Safe Amount: ₹", safe_amount)

print("Monthly Surplus: ₹", monthly_surplus)

print("\nStatus:", result["status"])

print("Decision:", result["decision"])

print(
    "Payment Method:",
    result["payment_method"]
)

print("\n=================================\n")