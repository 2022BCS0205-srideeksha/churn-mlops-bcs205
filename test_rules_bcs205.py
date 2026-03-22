from rules import predict_risk_bcs205

def test_high_risk():
    customer = {"tickets_30d": 6}
    assert predict_risk_bcs205(customer) == "High Risk"

def test_medium_risk():
    customer = {"tickets_30d": 3}
    assert predict_risk_bcs205(customer) == "Medium Risk"

def test_low_risk():
    customer = {"tickets_30d": 1}
    assert predict_risk_bcs205(customer) == "Low Risk"