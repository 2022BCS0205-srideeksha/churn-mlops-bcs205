import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.pipeline import Pipeline
import joblib

# Load data
df = pd.read_csv("data.csv")

# Feature Engineering
df["ticket_freq_7d"] = df["tickets_30d"] / 4
df["ticket_freq_90d"] = df["tickets_30d"] * 3
df["charge_change"] = df["monthly_charge"].diff().fillna(0)

# Encode categorical
df["contract"] = df["contract"].map({
    "month-to-month": 0,
    "one-year": 1,
    "two-year": 2
})

# Features & target
X = df[[
    "tickets_30d",
    "monthly_charge",
    "contract",
    "ticket_freq_7d",
    "ticket_freq_90d",
    "charge_change"
]]
y = df["churn"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y
)

# Pipeline model
pipeline = Pipeline([
    ("model", RandomForestClassifier())
])

# Train
pipeline.fit(X_train, y_train)

# Predict
y_pred = pipeline.predict(X_test)

# Evaluation
print("BCS205 Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_pred))

# Save model
joblib.dump(pipeline, "model_bcs205.pkl")