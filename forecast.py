import pandas as pd


def create_forecast(

    current_balance,

    monthly_income,

    essential_expenses,

    recurring_expenses,

    months=6
):

    forecast = []

    balance = current_balance


    for month in range(
        1,
        months + 1
    ):

        balance = (

            balance

            + monthly_income

            - essential_expenses

            - recurring_expenses

        )


        forecast.append({

            "Month":
            f"Month {month}",

            "Predicted Balance":
            balance

        })


    return pd.DataFrame(
        forecast
    )
        # ==================================
    # STEP 22 - FINANCIAL FORECAST
    # ==================================

    st.header("📈 6-Month Financial Forecast")

    forecast_df = create_forecast(

        current_balance,

        monthly_income,

        essential_expenses,

        recurring_expenses

    )


    st.dataframe(
        forecast_df,
        use_container_width=True
    )


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
    
        # ==================================
    # STEP 23 - SPENDING SUGGESTIONS
    # ==================================

    st.header("✂️ Smart Spending Suggestions")


    if result["status"] == "Affordable Now":

        st.success(
            "🎉 No major spending changes are required!"
        )


    elif result["status"] == "Affordable With Plan":

        st.warning(
            "⚠️ Reduce some flexible expenses to safely complete your payment plan."
        )

        st.write("🛍️ Reduce unnecessary shopping")

        st.write("🍔 Reduce food delivery expenses")

        st.write("📺 Pause unused subscriptions")


    elif result["status"] == "Affordable Later":

        st.info(
            "⏳ Save money and reduce flexible expenses before purchasing."
        )

        st.write("💰 Increase monthly savings")

        st.write("🍔 Reduce food delivery expenses")

        st.write("🛍️ Avoid unnecessary purchases")


    else:

        st.error(
            "❌ This purchase is currently not financially safe."
        )

        st.write("💰 Focus on increasing savings")

        st.write("📉 Reduce recurring expenses")

        st.write("⏳ Wait before making this purchase")