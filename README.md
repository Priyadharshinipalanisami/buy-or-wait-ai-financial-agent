# 💰 Buy or Wait?
## AI-Powered Personal Financial Decision Agent

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> **An AI-powered financial decision agent that helps users determine whether they can safely afford a purchase based on their complete financial situation.**

---

# 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Input Parameters](#-input-parameters)
- [Decision Logic](#-decision-logic)
- [Output](#-output)
- [Installation](#-installation)
- [Running the Application](#-running-the-application)
- [Testing](#-testing)
- [Dataset](#-dataset)
- [Future Enhancements](#-future-enhancements)
- [Use Cases](#-use-cases)
- [License](#-license)
- [Author](#-author)

---

# 🔍 Overview

**Buy or Wait?** is an AI-powered personal financial decision agent designed to help users make safer and smarter purchase decisions.

A user may ask:

> **"Can I afford this laptop?"**

Instead of checking only the user's current bank balance, the system analyzes multiple financial factors, including:

- 💰 Current Balance
- 💵 Monthly Income
- 🏠 Essential Expenses
- 🔄 Recurring Expenses
- ⏳ Pending Payments
- 🛡️ Preferred Minimum Balance
- 📈 Monthly Surplus
- 💳 Purchase Amount

Based on this information, the system provides a personalized recommendation.

The AI agent determines whether the user should:

- ✅ Buy Now
- 💳 Buy with a Payment Plan
- ⏳ Wait Until Financially Safe
- ❌ Do Not Proceed

---

# ❗ Problem Statement

Many people make purchase decisions based only on their current account balance.

For example:

> "I have ₹1,00,000 in my account. Can I buy a ₹80,000 laptop?"

However, the current balance alone does not represent the user's actual financial capacity.

The user may still have:

- Rent to pay
- Loan EMIs
- Credit card payments
- Monthly bills
- Pending expenses
- Family responsibilities
- Essential living expenses

Therefore, a purchase that appears affordable based on the current balance may actually be financially risky.

The challenge is to build a system that analyzes the user's complete financial situation and provides a safe, personalized, and explainable purchase recommendation.

---

# 💡 Solution

**Buy or Wait?** provides an intelligent financial decision system that evaluates a user's financial condition before recommending a purchase.

The system calculates:

```text
Current Financial Position
        +
Monthly Income
        -
Essential Expenses
        -
Recurring Expenses
        -
Pending Payments
        -
Minimum Balance
        ↓
Safe Amount to Pay
        +
Monthly Surplus
        ↓
AI Financial Decision
```

The final recommendation includes:

- Amount Safe to Pay Today
- Affordability Status
- Recommended Payment Method
- Payment Plan
- Financial Forecast
- Spending Changes Needed
- Decision Explanation
- Final Recommendation

---

# ✨ Features

## 💰 Financial Analysis

The system analyzes:

- Current available balance
- Monthly income
- Essential monthly expenses
- Recurring expenses
- Pending payments
- Preferred minimum balance

---

## 🛡️ Safe Spending Calculation

The system calculates the maximum amount a user can safely spend today.

```text
Safe Amount

=

Current Balance

-

Essential Expenses

-

Recurring Expenses

-

Pending Payments

-

Minimum Balance
```

The system ensures that users maintain their preferred financial safety balance.

---

## 📈 Monthly Surplus Calculation

The system calculates the user's available monthly surplus.

```text
Monthly Surplus

=

Monthly Income

-

Essential Expenses

-

Recurring Expenses
```

This value helps determine whether the user can safely complete installment payments.

---

## 🤖 AI Decision Engine

The decision engine provides personalized financial recommendations.

Possible outcomes:

| Decision | Description |
|---|---|
| ✅ BUY NOW | The user can safely pay the full amount |
| 💳 BUY WITH A PLAN | Partial payment and installments are recommended |
| ⏳ WAIT | The user should save more before purchasing |
| ❌ DO NOT PROCEED | The purchase is currently financially unsafe |

---

## 💳 Smart Payment Planning

If the user cannot safely pay the full amount today, the system creates a payment plan.

Example:

```text
Laptop Price: ₹80,000

Safe Amount Today: ₹30,000
Monthly Surplus: ₹30,000
```

Recommended payment schedule:

| Payment | Amount |
|---|---:|
| Today | ₹30,000 |
| Month 1 | ₹30,000 |
| Month 2 | ₹20,000 |

---

## 📈 Financial Forecast

The system provides a **6-month financial forecast**.

The forecast helps users understand how their financial position may change over time.

Example:

```text
Month 1 → ₹1,20,000

Month 2 → ₹1,50,000

Month 3 → ₹1,80,000

Month 4 → ₹2,10,000

Month 5 → ₹2,40,000

Month 6 → ₹2,70,000
```

---

## ✂️ Smart Spending Suggestions

The system provides recommendations to improve affordability.

Examples:

- 🛍️ Reduce unnecessary shopping
- 🍔 Reduce food delivery spending
- 📺 Pause unused subscriptions
- 🎬 Reduce entertainment expenses
- 💰 Increase monthly savings
- 💳 Clear pending payments

---

## 🧠 Explainable AI Decision

The system provides a clear explanation for every recommendation.

Example:

> You should not pay the full amount today because it may reduce your financial safety balance. However, you can make a partial payment and use your monthly surplus to complete the remaining amount safely.

---

# 🏗️ System Architecture

```text
                    USER
                      │
                      ▼
          Enter Financial Details
                      │
                      ▼
              Purchase Request
                      │
                      ▼
             DATA PROCESSING
                      │
                      ▼
             FINANCIAL ENGINE
                      │
            ┌─────────┴─────────┐
            ▼                   ▼
       Safe Amount       Monthly Surplus
            │                   │
            └─────────┬─────────┘
                      ▼
             DECISION ENGINE
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       BUY NOW    PAYMENT PLAN    WAIT
          │           │           │
          └───────────┼───────────┘
                      ▼
              FINANCIAL FORECAST
                      │
                      ▼
            SPENDING SUGGESTIONS
                      │
                      ▼
              STREAMLIT DASHBOARD
```

---

# 📁 Project Structure

```text
buy-or-wait-ai-financial-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── data/
│   └── sample_requests.csv
│
└── src/
    ├── data_processing.py
    ├── financial_engine.py
    ├── decision_engine.py
    ├── payment_planner.py
    ├── forecast.py
    │
    ├── test_financial.py
    ├── test_decision.py
    └── test_payment.py
```

---

# 📄 File Description

## `app.py`

Main Streamlit application.

Responsible for:

- User interface
- Financial inputs
- Purchase inputs
- Financial analysis
- AI recommendations
- Payment plan visualization
- Financial forecast
- Spending suggestions

---

## `financial_engine.py`

Responsible for financial calculations.

Functions include:

```python
calculate_safe_amount()

calculate_monthly_surplus()

calculate_health_score()
```

---

## `decision_engine.py`

Responsible for generating financial decisions.

Possible decisions:

```text
BUY NOW

BUY WITH A PLAN

WAIT

DO NOT PROCEED
```

---

## `payment_planner.py`

Creates a recommended payment schedule.

Example:

```text
Purchase Amount
      ↓
Safe Payment Today
      ↓
Remaining Amount
      ↓
Monthly Installments
```

---

## `forecast.py`

Generates the future financial forecast.

```text
Current Balance
       +
Monthly Income
       -
Monthly Expenses
       ↓
Future Financial Balance
```

---

## `data_processing.py`

Responsible for:

- Reading financial datasets
- Cleaning data
- Handling missing values
- Preparing financial information

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| Streamlit | Web Application Framework |
| Pandas | Data Processing |
| Plotly | Data Visualization |
| AI Decision Logic | Financial Recommendations |

---

# 📊 Input Parameters

The system accepts the following financial information:

| Parameter | Description |
|---|---|
| 💰 Current Balance | Money currently available |
| 💵 Monthly Income | Confirmed monthly income |
| 🏠 Essential Expenses | Rent, food, utilities, etc. |
| 🔄 Recurring Expenses | EMI, subscriptions, insurance, etc. |
| ⏳ Pending Payments | Upcoming financial commitments |
| 🛡️ Minimum Balance | Financial safety amount to maintain |
| 🛒 Item Name | Requested purchase |
| 💳 Purchase Amount | Cost of the requested item |

---

# 🤖 Decision Logic

## 1️⃣ BUY NOW

The user can safely pay the full amount.

```text
Safe Amount ≥ Purchase Amount
```

Recommendation:

```text
Status:
Affordable Now

Decision:
BUY NOW

Payment Method:
Pay in Full
```

---

## 2️⃣ BUY WITH A PLAN

The user cannot safely pay the full amount today but can complete the purchase through installments.

```text
Safe Amount > 0

AND

Monthly Surplus > 0
```

Recommendation:

```text
Status:
Affordable With Plan

Decision:
BUY WITH A PLAN

Payment Method:
Partial Payment + Installments
```

---

## 3️⃣ WAIT

The user has a positive monthly surplus but should improve their financial position before purchasing.

```text
Monthly Surplus > 0
```

Recommendation:

```text
Status:
Affordable Later

Decision:
WAIT

Payment Method:
Wait Until Financially Safe
```

---

## 4️⃣ DO NOT PROCEED

The purchase is currently financially unsafe.

```text
Safe Amount ≤ 0

AND

Monthly Surplus ≤ 0
```

Recommendation:

```text
Status:
Not Affordable

Decision:
DO NOT PROCEED

Payment Method:
Not Recommended
```

---

# 📤 System Output

For every purchase request, the system provides:

```text
1. Amount Safe to Pay Today

2. Affordability Status

3. Recommended Payment Method

4. Payment Plan

5. Monthly Surplus

6. Financial Health Score

7. Financial Forecast

8. Spending Changes Needed

9. Decision Explanation

10. Final Recommendation
```

---

# 📊 Example Output

```text
💰 BUY OR WAIT?

AI-Powered Personal Financial Decision Agent

──────────────────────────────

📊 FINANCIAL ANALYSIS

💰 Current Balance

₹90,000


🛡️ Safe to Pay Today

₹30,000


📈 Monthly Surplus

₹30,000


❤️ Financial Health Score

64%


──────────────────────────────

🤖 AI RECOMMENDATION

⚠️ BUY WITH A PLAN


──────────────────────────────

📌 RECOMMENDATION DETAILS

Item:

Laptop


Purchase Amount:

₹80,000


Payment Method:

Partial Payment + Installments


──────────────────────────────

💳 PAYMENT PLAN

Today      ₹30,000

Month 1    ₹30,000

Month 2    ₹20,000


──────────────────────────────

📈 FINANCIAL FORECAST

6 Month Financial Prediction


──────────────────────────────

✂️ SPENDING SUGGESTIONS

• Reduce unnecessary shopping

• Reduce food delivery spending

• Pause unused subscriptions


──────────────────────────────

🧠 DECISION EXPLANATION

You should not pay the full amount today.
A partial payment combined with your monthly
surplus is recommended.


──────────────────────────────

🎯 FINAL DECISION

⚠️ BUY WITH A PAYMENT PLAN
```

---

# 📂 Dataset

The project includes a sample financial dataset.

Location:

```text
data/sample_requests.csv
```

Example:

```csv
user_id,current_balance,monthly_income,essential_expenses,recurring_expenses,pending_payments,purchase_amount
1,90000,60000,25000,5000,10000,80000
2,50000,40000,20000,8000,5000,60000
3,120000,80000,30000,10000,5000,40000
```

---

# ⚙️ Installation

## Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/buy-or-wait-ai-financial-agent.git
```

---

## Step 2: Navigate to the Project Folder

```bash
cd buy-or-wait-ai-financial-agent
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Your `requirements.txt` should contain:

```text
streamlit
pandas
plotly
```

---

# ▶️ Running the Application

Run the Streamlit application:

```bash
python -m streamlit run app.py
```

After running successfully, Streamlit will display:

```text
You can now view your Streamlit app.

Local URL:

http://localhost:8501
```

Open the local URL in your browser.

---

# 🧪 Testing

## Test Financial Engine

```bash
python src/test_financial.py
```

Tests:

- Safe amount calculation
- Monthly surplus calculation
- Financial health score

---

## Test Decision Engine

```bash
python src/test_decision.py
```

Tests:

- Buy Now
- Buy With Plan
- Wait
- Do Not Proceed

---

## Test Payment Planner

```bash
python src/test_payment.py
```

Tests:

- Partial payment calculation
- Installment planning
- Payment schedule generation

---

# 🚀 Deployment

The application can be deployed using:

- Streamlit Community Cloud
- GitHub
- Render
- Railway

## Recommended Deployment

```text
Local Project
      ↓
GitHub Repository
      ↓
Streamlit Community Cloud
      ↓
Live Application
```

Main file:

```text
app.py
```

---

# 🎯 Use Cases

This project can be used for:

### 👤 Personal Finance

Helping individuals make safe purchase decisions.

### 💳 Smart Installment Planning

Helping users decide between:

- Full payment
- Partial payment
- Installments

### 📊 Budget Management

Analyzing expenses and identifying areas where users can reduce spending.

### 🏦 Financial Wellness

Providing financial insights and recommendations.

### 🤖 AI Financial Assistants

Can be integrated into future AI-powered personal finance applications.

---

# 🔮 Future Enhancements

The following features can be added in future versions:

### 🏦 Bank Integration

Connect directly with bank accounts and transaction history.

---

### 📩 Message Analysis

Analyze financial information from:

- SMS messages
- Emails
- Payment notifications

---

### 🖼️ Receipt Analysis

Use OCR to analyze:

- Bills
- Receipts
- Payment screenshots

---

### 🤖 Machine Learning Model

Train a machine learning model to predict:

- Financial risk
- Purchase affordability
- Spending behavior
- Future financial position

---

### 📱 Mobile Application

Develop an Android and iOS version.

---

### 🔔 Smart Notifications

Provide alerts for:

- Overspending
- Upcoming payments
- Low balance
- High-risk purchases

---

### 🧠 AI Personal Financial Assistant

Develop a conversational AI agent where users can ask:

> Can I afford this laptop?

> Should I buy this phone now?

> Can I take this EMI?

> How much can I safely spend this month?

---

# 🏆 Hackathon Project

**Buy or Wait?** is designed as a hackathon project that demonstrates how AI-powered decision systems can provide:

- Personalized recommendations
- Safe spending analysis
- Explainable decisions
- Smart payment planning
- Financial forecasting

The project focuses on **financial safety rather than simply checking account balance**.

---

# 🔐 Financial Safety Principle

A recommendation is considered safe only when the user can:

```text
✓ Cover Essential Expenses

✓ Handle Pending Payments

✓ Maintain Minimum Balance

✓ Complete the Full Payment Plan

✓ Maintain Financial Stability
```

---

# 🎯 Project Objective

> **To develop an AI-powered financial decision agent that helps users make safe and personalized purchase decisions by analyzing their complete financial situation instead of relying only on their current account balance.**

---

# 👩‍💻 Author

**Priyadharshini**

---

# 📄 License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026 Priyadharshini

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

See the [LICENSE](LICENSE) file for more details.

---

# ⭐ Support

If you find this project useful:

⭐ Star the repository

🍴 Fork the project

🤝 Contribute to improve the system

---

<div align="center">

## 💰 Make Smarter Financial Decisions

### 🤖 Buy or Wait?

**AI-Powered Personal Financial Decision Agent**

</div>
