# Telco-Customer-Churn---EDA

This project provides a detailed exploratory data analysis (EDA) of a Telco customer churn dataset. The main goal is to understand which customer attributes and service-related factors are associated with churn, and to extract actionable insights that can help improve customer retention strategies.

## Dataset Overview

The dataset includes 7,032 customer records and features related to:

- Demographics (gender, age, senior citizen status, dependents)
- Services (phone, internet, streaming, online security, tech support)
- Account and billing (contract type, paperless billing, payment method)
- Usage and financial data (tenure, monthly charges, total charges)
- Churn status (whether the customer left within the last month)

## Key Questions Addressed

- What customer characteristics are linked to higher churn?
- How do contract types, billing methods, and service usage impact churn rates?
- What trends exist among long-term vs. short-term customers?
- Which combinations of features can help predict or reduce churn?

## Analysis Summary

The analysis is organized into the following sections:

1. **Demographic Distribution**  
   - Compared churn rates by gender, dependents, senior citizen status, and partner presence.

2. **Service Type and Churn**  
   - Examined how internet services, streaming options, and value-added features (e.g., online security, tech support) relate to churn.

3. **Contract & Billing Behavior**  
   - Assessed the impact of contract duration, paperless billing, and payment method on customer retention.

4. **Numeric Feature Trends**  
   - Used pairplots to analyze relationships between tenure, charges, and churn likelihood.

## Key Insights

- Churn is highest among customers on month-to-month contracts.
- Customers using electronic check as a payment method are more likely to churn.
- Those who subscribe to security or tech support services tend to stay longer.
- Churn is most common in the first 12 months of tenure.

## Tools & Libraries

- Python 3
- Pandas
- Matplotlib
- Seaborn

## License

This project is for educational and analytical purposes only.
