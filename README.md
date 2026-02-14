📌 Customer Lifetime Value Prediction System
🚀 Project Highlights

Built an end-to-end Machine Learning web application using Flask.

Predicts whether a customer will be Premium, Profitable, or Non-Profitable.

Implemented input validation (age limits, no negative values).

Applied business logic for actionable decision-making.

Structured project using clean folder architecture.

Deployed model using joblib for real-time predictions.

🛠️ Technologies Used

🐍 Python

🌐 Flask (Web Framework)

📊 Pandas & NumPy (Data Processing)

📈 Matplotlib & Seaborn (Data Visualization)

🤖 Scikit-learn (Machine Learning)

📦 Joblib (Model Serialization)

💻 HTML & CSS (Frontend UI)

🤖 Machine Learning Approach

Performed data cleaning and preprocessing.

Selected relevant behavioral and transactional features.

Trained a Linear Regression model to predict Customer Lifetime Value.

Evaluated model performance using regression metrics.

Saved the trained model as a .pkl file for deployment.

🔄 Application Workflow (Pipeline)

User enters customer details through web form.

Backend validates inputs (age range, no negative values).

Data is converted into a Pandas DataFrame.

Pre-trained ML model predicts Customer Lifetime Value.

Business logic classifies customer into:

💎 Premium Customer

✅ Profitable Customer

❌ Non-Profitable Customer

Result is displayed on a dedicated result page.

📊 Business Impact

Helps businesses identify high-value customers.

Supports targeted marketing strategies.

Assists in revenue forecasting.

Improves customer retention decisions.

📂 Project Structure
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
