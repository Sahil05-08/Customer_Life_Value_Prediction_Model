# 🚀 Customer Lifetime Value Prediction System

## 📌 Overview

This project is an end-to-end Machine Learning web application designed to predict Customer Lifetime Value (CLV) and determine whether a customer is profitable for a business. The system analyzes demographic, behavioral, transactional, and engagement-related data to estimate long-term revenue potential.

The goal of this project is to help businesses identify high-value customers and support data-driven marketing and retention strategies.

---

## 🎯 Key Features

- Predicts customer profitability using a trained ML model  
- Classifies customers as:
  - 💎 Premium Customer  
  - ✅ Profitable Customer  
  - ❌ Non-Profitable Customer  
- Real-time prediction through a Flask web interface  
- Backend validation (age limits, no negative values)  
- Clean and structured project architecture  

---

## 🛠️ Technologies Used

- **Python**
- **Flask** (Web Framework)
- **Pandas & NumPy** (Data Processing)
- **Matplotlib & Seaborn** (Data Visualization)
- **Scikit-learn** (Machine Learning)
- **Linear Regression Model**
- **Joblib** (Model Serialization)
- **HTML & CSS** (Frontend)

---

## 🤖 Machine Learning Approach

- Performed data cleaning and preprocessing  
- Conducted exploratory data analysis using visualization tools  
- Selected relevant customer behavior and transaction features  
- Trained a Linear Regression model to predict lifetime value  
- Saved the trained model as a `.pkl` file for deployment  
- Integrated the model into a Flask application for real-time predictions  

---

## 🔄 Application Workflow

1. User enters customer details via web form  
2. Backend validates inputs (age range and non-negative constraints)  
3. Data is structured into a Pandas DataFrame  
4. The trained ML model generates a prediction  
5. Business logic categorizes the customer based on predicted value  
6. Final result is displayed on a dedicated result page  

---

## 📊 Business Impact

- Identifies high-value customers  
- Supports targeted marketing decisions  
- Helps improve customer retention strategies  
- Enables revenue forecasting and profitability analysis  

---

## 📂 Project Structure

```
Customer_Life_Value_Prediction_Model/
│
├── app.py
├── Life_Time_Value.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   ├── home.html
│   ├── predict.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── High_value_customer.ipynb

```
