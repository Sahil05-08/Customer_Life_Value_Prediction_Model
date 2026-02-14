from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("Life_Time_Value.pkl")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    # 🔹 If GET → show form page
    if request.method == "GET":
        return render_template("predict.html")

    try:
        # 🔴 AGE VALIDATION
        age = float(request.form.get("age"))

        if age < 7:
            return redirect(url_for("result", message="⚠️ Age is too small. Invalid data."))

        if age > 80:
            return redirect(url_for("result", message="⚠️ Age cannot be greater than 80."))

        # 🔴 NUMERIC VALIDATION (No negatives allowed)
        numeric_fields = [
            "membership_years", "login_frequency", "session_duration_avg",
            "pages_per_session", "cart_abandonment_rate", "wishlist_items",
            "total_purchases", "average_order_value", "days_since_last_purchase",
            "discount_usage_rate", "returns_rate", "email_open_rate",
            "customer_service_calls", "product_reviews_written",
            "social_media_engagement_score", "mobile_app_usage",
            "payment_method_diversity", "credit_balance"
        ]

        for field in numeric_fields:
            value = float(request.form.get(field))
            if value < 0:
                return redirect(
                    url_for("result",
                            message=f"⚠️ {field.replace('_',' ').title()} cannot be negative.")
                )

        # ✅ Create input dictionary
        data = {
            "Age": age,
            "Gender": request.form.get("gender"),
            "Country": request.form.get("country"),
            "City": request.form.get("city"),
            "Membership_Years": float(request.form.get("membership_years")),
            "Login_Frequency": float(request.form.get("login_frequency")),
            "Session_Duration_Avg": float(request.form.get("session_duration_avg")),
            "Pages_Per_Session": float(request.form.get("pages_per_session")),
            "Cart_Abandonment_Rate": float(request.form.get("cart_abandonment_rate")),
            "Wishlist_Items": float(request.form.get("wishlist_items")),
            "Total_Purchases": float(request.form.get("total_purchases")),
            "Average_Order_Value": float(request.form.get("average_order_value")),
            "Days_Since_Last_Purchase": float(request.form.get("days_since_last_purchase")),
            "Discount_Usage_Rate": float(request.form.get("discount_usage_rate")),
            "Returns_Rate": float(request.form.get("returns_rate")),
            "Email_Open_Rate": float(request.form.get("email_open_rate")),
            "Customer_Service_Calls": float(request.form.get("customer_service_calls")),
            "Product_Reviews_Written": float(request.form.get("product_reviews_written")),
            "Social_Media_Engagement_Score": float(request.form.get("social_media_engagement_score")),
            "Mobile_App_Usage": float(request.form.get("mobile_app_usage")),
            "Payment_Method_Diversity": float(request.form.get("payment_method_diversity")),
            "Credit_Balance": float(request.form.get("credit_balance")),
            "Signup_Quarter": request.form.get("signup_quarter")
        }

        input_df = pd.DataFrame([data])
        prediction_value = model.predict(input_df)[0]

        # 💰 Business Decision Logic
        if prediction_value > 1000:
            result_message = f"💎 Premium Customer! Expected Profit: ${prediction_value:,.2f}"
        elif prediction_value > 0:
            result_message = f"✅ Profitable Customer. Expected Profit: ${prediction_value:,.2f}"
        else:
            result_message = "❌ This customer is not expected to generate profit."

        return redirect(url_for("result", message=result_message))

    except Exception as e:
        return redirect(url_for("result", message="Error: " + str(e)))


@app.route("/result")
def result():
    message = request.args.get("message")

    if not message:
        message = "No result available."

    return render_template("result.html", prediction=message)


if __name__ == "__main__":
    app.run(debug=True)
