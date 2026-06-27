from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)

# Load Dataset
data = pd.read_csv("business_data.csv")

# Train Model
X = data[["expenses", "customers"]]
y = data["sales"]

model = LinearRegression()
model.fit(X, y)

@app.route('/')
def home():
    return jsonify({
        "message": "AI Business Growth Prediction API Running Successfully"
    })

@app.route('/predict', methods=['POST'])
def predict():

    try:
        req_data = request.get_json()

        expenses = float(req_data['expenses'])
        customers = float(req_data['customers'])

        predicted_sales = model.predict([[expenses, customers]])[0]

        # Business Health Score
        score = 100

        if expenses > predicted_sales * 0.8:
            score -= 30

        if customers < 100:
            score -= 20

        score = max(0, min(score, 100))

        # AI Recommendation
        recommendations = []

        if expenses > predicted_sales * 0.8:
            recommendations.append(
                "Reduce operational expenses to improve profitability."
            )

        if customers < 100:
            recommendations.append(
                "Focus on customer acquisition and retention."
            )

        if predicted_sales > 80000:
            recommendations.append(
                "Business growth is strong. Consider expanding operations."
            )

        if len(recommendations) == 0:
            recommendations.append(
                "Business performance is healthy. Maintain current strategy."
            )

        return jsonify({
            "predicted_sales": round(float(predicted_sales), 2),
            "health_score": score,
            "recommendations": recommendations
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
