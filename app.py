from flask import Flask, request, jsonify
import joblib
import logging
logging.basicConfig(level=logging.INFO)

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
# Rule-based API (DevOps requirement)
@app.route("/predict-risk", methods=["POST"])
def predict_risk():
    data = request.json
    logging.info(f"BCS205 Request: {data}")

    if data["tickets_30d"] > 5:
        risk = "High Risk"
    elif data["tickets_30d"] >= 3:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    return jsonify({
        "student": "BCS205",
        "risk": risk,
        "type": "rule-based"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)