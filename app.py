from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.linear_model import LinearRegression



app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "AI Business Growth Prediction API Running"})

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    expenses = float(data["expenses"])
    customers = float(data["customers"])

    predicted_sales = expenses + (customers * 350)

    health_score = 100

    if expenses > predicted_sales * 0.8:
        health_score -= 30

    if customers < 100:
        health_score -= 20

    if health_score >= 80:
        recommendation = "Business performance is excellent. Consider expansion."
    elif health_score >= 60:
        recommendation = "Business is stable. Focus on growth."
    else:
        recommendation = "Reduce expenses and increase customer acquisition."

    return jsonify({
        "predicted_sales": round(predicted_sales, 2),
        "health_score": health_score,
        "recommendation": recommendation
    })

if __name__ == "__main__":
    app.run(debug=True)
