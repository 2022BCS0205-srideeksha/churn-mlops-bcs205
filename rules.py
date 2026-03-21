def predict_risk_bcs205(customer):
    if customer["tickets_30d"] > 5:
        return "High Risk"
    elif customer["tickets_30d"] >= 3:
        return "Medium Risk"
    else:
        return "Low Risk"
    # Example test (for assignment proof)
customer = {"tickets_30d": 6}
print("BCS205 Rule Output:", predict_risk_bcs205(customer))