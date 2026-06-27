from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

data = pd.read_csv("business_data.csv")

X = data[["expenses", "customers"]]
y = data["sales"]

model = LinearRegression()
model.fit(X, y)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    expenses = float(data['expenses'])
    customers = float(data['customers'])

    prediction = model.predict([[expenses, customers]])

    return jsonify({
        "predicted_sales": round(prediction[0], 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
