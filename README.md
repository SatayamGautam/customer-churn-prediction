# Customer Churn Prediction – End-to-End Data Science Project

## Project Overview
This project focuses on predicting customer churn for a telecom company using machine learning.
The goal is to identify customers likely to churn and understand the key drivers behind churn,
so that the business can take proactive retention actions.

## Business Problem
Can we predict which customers are likely to churn in the next billing cycle and identify
the most important factors influencing churn?

## Dataset
- Telco Customer Churn Dataset
- ~7,000 customer records
- Mix of demographic, service usage, and billing features
- Target variable: Churn (Yes / No)

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- FastAPI (for deployment concept)

## Project Workflow
1. Data understanding and cleaning
2. Exploratory Data Analysis (EDA)
3. Feature engineering and encoding
4. Model building (Logistic Regression, Random Forest)
5. Model evaluation using Recall, F1-score, ROC-AUC
6. Threshold tuning for business optimization
7. Model interpretation and insights
8. Deployment-ready API design using FastAPI

## Key Insights
- Customers with low tenure have higher churn probability
- Month-to-month contracts show significantly higher churn
- Higher monthly charges increase churn risk

## Model Deployment
The trained model is designed to be deployed using FastAPI.
The API accepts customer information and returns:
- Churn probability
- Churn prediction based on a tuned threshold

## Limitations
- Dataset represents a single telecom provider
- Analysis is snapshot-based and not fully time-series
- External customer behavior factors are not included

## Future Improvements
- Add time-based churn features
- Use advanced models like XGBoost
- Add explainability using SHAP
- Deploy using Docker with monitoring

## Author
Gautam
