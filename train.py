import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
df = pd.read_csv("data.csv")

df["contract"] = df["contract"].map({
    "month-to-month": 0,
    "one-year": 1,
    "two-year": 2
})

X = df[["tickets_30d", "monthly_charge", "contract"]]
y = df["churn"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model_bcs205.pkl")

print("BCS205 Model trained successfully!")