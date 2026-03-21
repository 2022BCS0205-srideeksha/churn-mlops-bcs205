from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model_bcs205.pkl")
@app.route("/")
def home():
    return "BCS205 API is running"
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Convert contract to numeric
    contract_map = {
        "month-to-month": 0,
        "one-year": 1,
        "two-year": 2
    }

    input_data = [[
        data["tickets_30d"],
        data["monthly_charge"],
        contract_map[data["contract"]]
    ]]

    prediction = model.predict(input_data)[0]

    # Convert prediction to risk
    risk = "High" if prediction == 1 else "Low"

    return jsonify({
        "student": "BCS205",
        "prediction": int(prediction),
        "risk": risk
    })

if __name__ == "__main__":
    app.run(debug=True)