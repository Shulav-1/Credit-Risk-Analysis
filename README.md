# Credit-Risk-Analysis
Overview

The Credit Risk Analysis Web App is a machine learning project that predicts whether a loan applicant is a good credit risk or bad credit risk based on their financial and personal details.

This project demonstrates an end-to-end data science workflow, including:

Data preprocessing
Exploratory Data Analysis (EDA)
Feature engineering
Machine learning model training
Model deployment using Streamlit
It is designed as a portfolio project for entry-level Data Analyst / Data Scientist roles.

  Problem Statement

Financial institutions face losses when loans are given to high-risk customers.
The goal of this project is to classify customers based on credit risk so that better lending decisions can be made.

 Solution Approach

Analyze customer credit data
Clean and preprocess the dataset
Perform EDA to understand risk patterns
Engineer meaningful features
Train a machine learning classification model
Deploy the trained model as an interactive web app

 Tech Stack

Language: Python
Data Analysis: Pandas, NumPy
Visualization: Matplotlib, Seaborn
Machine Learning: Scikit-learn, XGBoost
Web App: Streamlit
Version Control: Git & GitHub

 Project Structure
Credit-Risk-Analysis/
│
├── data/
│   └── german_credit_data.csv
│
├── credit_risk_analysis.ipynb
├── app.py
├── model.pkl
├── README.md
└── requirements.txt

Dataset

Name: German Credit Dataset
Description: Contains customer details such as:
Age
Credit amount
Loan duration
Job type
Housing
Purpose of loan
The target variable indicates whether the customer is creditworthy or risky.

 Machine Learning Model

Algorithm Used: XGBoost Classifier
Reason for Selection:
Handles imbalanced datasets effectively
High predictive performance
Commonly used in financial risk modeling

 Model Evaluation
The model performance was evaluated using:
Accuracy Score
Confusion Matrix
Classification Report
ROC-AUC Score

 Streamlit Web App

The web application allows users to:
Enter customer details through a simple form
Get instant credit risk prediction
View results in a clear and interactive way
