import streamlit as st
import plotly.express as px
import sys
import os


# ==========================================
# ADD SRC FOLDER TO PYTHON PATH
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

sys.path.append(SRC_DIR)


# ==========================================
# IMPORT PROJECT MODULES
# ==========================================

from financial_engine import (
    calculate_safe_amount,
    calculate_monthly_surplus,
    calculate_health_score
)

from decision_engine import make_decision

from payment_planner import create_payment_plan

from forecast import create_forecast


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Buy or Wait?",
    page_icon="💰",
    layout="wide"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 45px;
        font-weight: bold;
        text-align: center;
    }

    .sub-title {
        font-size: 20px;
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# APP HEADER
# ==========================================

st.markdown(
    '<div class="main-title">💰 Buy or Wait?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'AI-Powered Personal Financial Decision Agent'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    """
    Make smarter purchase decisions by analyzing your current balance,
    income, essential expenses, recurring commitments, pending payments,
    and preferred minimum balance.
    """
)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("💳 Financial Profile")

st.sidebar.markdown("---")


# ==========================================
# FINANCIAL INPUTS
# ==========================================

current_balance = st.sidebar.number_input(
    "💰 Current Balance (₹)",
    min_value=0.0,
    value=90000.0,
    step=1000.0
)


monthly_income = st.sidebar.number_input(
    "💵 Monthly Income (₹)",
    min_value=0.0,
    value=60000.0,
    step=1000.0
)


essential_expenses = st.sidebar.number_input(
    "🏠 Essential Expenses (₹)",
    min_value=0.0,
    value=25000.0,
    step=1000.0
)


recurring_expenses = st.sidebar.number_input(
    "🔄 Recurring Expenses / EMI (₹)",
    min_value=0.0,
    value=5000.0,
    step=1000.0
)


pending_payments = st.sidebar.number_input(
    "⏳ Pending Payments (₹)",
    min_value=0.0,
    value=10000.0,
    step=1000.0
)


minimum_balance = st.sidebar.number_input(
    "🛡️ Preferred Minimum Balance (₹)",
    min_value=0.0,
    value=20000.0,
    step=1000.0
)


# ==========================================
# PURCHASE REQUEST
# ==========================================

st.sidebar.markdown("---")

st.sidebar.title("🛒 Purchase Request")


item_name = st.sidebar.text_input(
    "Item Name",
    value="Laptop"
)


purchase_amount = st.sidebar.number_input(
    "Purchase Amount (₹)",
    min_value=0.0,
    value=80000.0,
    step=1000.0
)


# ==========================================
# ONLY ONE ANALYZE BUTTON
# ==========================================

analyze = st.sidebar.button(
    "🤖 Analyze Purchase",
    key="analyze_purchase_button",
    use_container_width=True
)


# ==========================================
# MAIN ANALYSIS
# ==========================================

if analyze:


    # ==========================================
    # STEP 1 - SAFE AMOUNT CALCULATION
    # ==========================================

    safe_amount = calculate_safe_amount(
        current_balance,
        essential_expenses,
        recurring_expenses,
        pending_payments,
        minimum_balance
    )


    # ==========================================
    # STEP 2 - MONTHLY SURPLUS
    # ==========================================

    monthly_surplus = calculate_monthly_surplus(
        monthly_income,
        essential_expenses,
        recurring_expenses
    )


    # ==========================================
    # STEP 3 - TOTAL EXPENSES
    # ==========================================

    total_expenses = (
        essential_expenses
        + recurring_expenses
        + pending_payments
    )


    # ==========================================
    # STEP 4 - FINANCIAL HEALTH SCORE
    # ==========================================

    health_score = calculate_health_score(
        current_balance,
        monthly_income,
        total_expenses,
        minimum_balance
    )


    # ==========================================
    # STEP 5 - AI DECISION
    # ==========================================

    result = make_decision(
        purchase_amount,
        safe_amount,
        monthly_surplus
    )


    # ==========================================
    # FINANCIAL ANALYSIS
    # ==========================================

    st.markdown("---")

    st.header("📊 Financial Analysis")


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "💰 Current Balance",
            f"₹{current_balance:,.0f}"
        )


    with col2:

        st.metric(
            "🛡️ Safe to Pay Today",
            f"₹{safe_amount:,.0f}"
        )


    with col3:

        st.metric(
            "📈 Monthly Surplus",
            f"₹{monthly_surplus:,.0f}"
        )


    with col4:

        st.metric(
            "❤️ Financial Health",
            f"{health_score}%"
        )


    # ==========================================
    # FINANCIAL SUMMARY
    # ==========================================

    st.subheader("📋 Financial Summary")


    summary_col1, summary_col2, summary_col3 = st.columns(3)


    with summary_col1:

        st.write(
            "🏠 Essential Expenses"
        )

        st.write(
            f"### ₹{essential_expenses:,.0f}"
        )


    with summary_col2:

        st.write(
            "🔄 Recurring Expenses"
        )

        st.write(
            f"### ₹{recurring_expenses:,.0f}"
        )


    with summary_col3:

        st.write(
            "⏳ Pending Payments"
        )

        st.write(
            f"### ₹{pending_payments:,.0f}"
        )


    # ==========================================
    # AI RECOMMENDATION
    # ==========================================

    st.markdown("---")

    st.header("🤖 AI Recommendation")


    if result["status"] == "Affordable Now":

        st.success(
            f"✅ Recommendation: {result['decision']}"
        )


    elif result["status"] == "Affordable With Plan":

        st.warning(
            f"⚠️ Recommendation: {result['decision']}"
        )


    elif result["status"] == "Affordable Later":

        st.info(
            f"⏳ Recommendation: {result['decision']}"
        )


    else:

        st.error(
            f"❌ Recommendation: {result['decision']}"
        )


    # ==========================================
    # RECOMMENDATION DETAILS
    # ==========================================

    st.subheader("📌 Recommendation Details")


    detail_col1, detail_col2 = st.columns(2)


    with detail_col1:

        st.write(
            f"### 🛒 Item: {item_name}"
        )

        st.write(
            f"### 💰 Price: ₹{purchase_amount:,.0f}"
        )

        st.write(
            f"### 📊 Status: {result['status']}"
        )


    with detail_col2:

        st.write(
            "### 💳 Recommended Payment Method"
        )

        st.write(
            result["payment_method"]
        )

        st.write(
            f"### 🛡️ Maximum Safe Payment Today"
        )

        st.write(
            f"₹{safe_amount:,.0f}"
        )


    # ==========================================
    # PAYMENT PLAN
    # ==========================================

    st.markdown("---")

    st.header("💳 Recommended Payment Plan")


    if purchase_amount == 0:

        st.info(
            "Please enter a purchase amount greater than ₹0."
        )


    elif safe_amount <= 0 and monthly_surplus <= 0:

        st.error(
            "No safe payment plan can currently be created."
        )


    else:

        payment_plan = create_payment_plan(
            purchase_amount,
            safe_amount,
            monthly_surplus
        )


        if not payment_plan.empty:

            st.dataframe(
                payment_plan,
                use_container_width=True
            )


            # ==========================================
            # PAYMENT PLAN CHART
            # ==========================================

            st.subheader(
                "📊 Payment Plan Visualization"
            )


            fig_payment = px.bar(
                payment_plan,
                x="Payment",
                y="Amount",
                text="Amount",
                title="Recommended Payment Schedule"
            )


            st.plotly_chart(
                fig_payment,
                use_container_width=True
            )


        else:

            st.warning(
                "A payment plan could not be generated."
            )


    # ==========================================
    # 6 MONTH FINANCIAL FORECAST
    # ==========================================

    st.markdown("---")

    st.header("📈 6-Month Financial Forecast")


    forecast_df = create_forecast(
        current_balance,
        monthly_income,
        essential_expenses,
        recurring_expenses,
        months=6
    )


    st.dataframe(
        forecast_df,
        use_container_width=True
    )


    # ==========================================
    # FORECAST CHART
    # ==========================================

    fig_forecast = px.line(
        forecast_df,
        x="Month",
        y="Predicted Balance",
        markers=True,
        title="Future Financial Position"
    )


    st.plotly_chart(
        fig_forecast,
        use_container_width=True
    )


    # ==========================================
    # SPENDING CHANGES
    # ==========================================

    st.markdown("---")

    st.header("✂️ Spending Changes Needed")


    if result["status"] == "Affordable Now":

        st.success(
            "🎉 No major spending changes are required. "
            "You can safely proceed while maintaining your minimum balance."
        )


    elif result["status"] == "Affordable With Plan":

        st.warning(
            "⚠️ Some flexible expenses should be reduced "
            "to safely complete the payment plan."
        )

        st.write("🛍️ Reduce unnecessary shopping")

        st.write("🍔 Reduce food delivery spending")

        st.write("📺 Pause unused subscriptions")

        st.write("🎬 Reduce entertainment expenses")


    elif result["status"] == "Affordable Later":

        st.info(
            "⏳ Wait and improve your financial position "
            "before making this purchase."
        )

        st.write("💰 Increase monthly savings")

        st.write("🍔 Reduce food delivery expenses")

        st.write("🛍️ Avoid unnecessary purchases")

        st.write("📉 Reduce recurring expenses")


    else:

        st.error(
            "❌ This purchase is currently not financially safe."
        )

        st.write("💰 Focus on increasing your savings")

        st.write("📉 Reduce recurring expenses")

        st.write("⏳ Wait before making this purchase")

        st.write("💳 Clear pending payments first")


    # ==========================================
    # DECISION EXPLANATION
    # ==========================================

    st.markdown("---")

    st.header("🧠 Decision Explanation")


    if result["status"] == "Affordable Now":

        st.write(
            f"""
            You can safely afford the **{item_name}** because your
            safe amount of **₹{safe_amount:,.0f}** is sufficient
            to cover the purchase amount of
            **₹{purchase_amount:,.0f}** while maintaining your
            preferred minimum balance.
            """
        )


    elif result["status"] == "Affordable With Plan":

        st.write(
            f"""
            You should not pay the full amount of
            **₹{purchase_amount:,.0f}** today.
            However, you can safely make a partial payment of up to
            **₹{safe_amount:,.0f}** and use your monthly surplus of
            **₹{monthly_surplus:,.0f}** to complete the remaining amount.
            """
        )


    elif result["status"] == "Affordable Later":

        st.write(
            f"""
            The purchase amount of **₹{purchase_amount:,.0f}**
            is currently higher than your safe payment amount.
            It is recommended to wait and save from your monthly
            surplus of **₹{monthly_surplus:,.0f}**.
            """
        )


    else:

        st.write(
            f"""
            This purchase is currently not recommended because
            your available safe amount and monthly financial position
            are insufficient to safely support this expense.
            """
        )


    # ==========================================
    # FINAL DECISION
    # ==========================================

    st.markdown("---")

    st.header("🎯 Final Decision")


    if result["status"] == "Affordable Now":

        st.success(
            f"""
            ✅ BUY NOW

            You can afford the {item_name}.
            Recommended method: {result['payment_method']}
            """
        )


    elif result["status"] == "Affordable With Plan":

        st.warning(
            f"""
            ⚠️ BUY WITH A PAYMENT PLAN

            Avoid paying the full amount immediately.
            Recommended method: {result['payment_method']}
            """
        )


    elif result["status"] == "Affordable Later":

        st.info(
            f"""
            ⏳ WAIT

            Save more money before purchasing the {item_name}.
            """
        )


    else:

        st.error(
            f"""
            ❌ DO NOT PROCEED

            The {item_name} is currently not financially safe.
            """
        )


# ==========================================
# DEFAULT SCREEN
# ==========================================

else:

    st.markdown("---")

    st.info(
        """
        👈 Enter your financial details in the sidebar.

        Then click **🤖 Analyze Purchase** to receive your
        personalized AI financial recommendation.
        """
    )


    st.subheader("🚀 What This AI Agent Analyzes")


    feature_col1, feature_col2, feature_col3 = st.columns(3)


    with feature_col1:

        st.write("💰 Current Balance")

        st.write("💵 Monthly Income")

        st.write("🏠 Essential Expenses")


    with feature_col2:

        st.write("🔄 Recurring Expenses")

        st.write("⏳ Pending Payments")

        st.write("🛡️ Minimum Balance")


    with feature_col3:

        st.write("🤖 AI Decision")

        st.write("💳 Payment Plan")

        st.write("📈 Financial Forecast")