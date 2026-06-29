import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc

# Load dataset
data = pd.read_csv("datasets/diabetes.csv")

# Convert smoking_status to numeric
smoking_map = {
    "Never": 0,
    "Former": 1,
    "Current": 2
}
data["smoking_status"] = data["smoking_status"].map(smoking_map)

# Features
X = data[[
    'age',
    'bmi',
    'glucose_fasting',
    'hba1c',
    'insulin_level',
    'systolic_bp',
    'cholesterol_total',
    'physical_activity_minutes_per_week',
    'family_history_diabetes',
    'smoking_status'
]]

# Target
y = data["diagnosed_diabetes"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Load trained model
model = joblib.load("models/random_forest_model.pkl")

# Predictions
y_pred = model.predict(X_test)

# Print results
print("\nConfusion Matrix")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# ================= CONFUSION MATRIX =================
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.savefig("confusion_matrix.png")
plt.close()

# ================= FEATURE IMPORTANCE =================
importance = model.feature_importances_
features = X.columns

plt.figure(figsize=(8,5))
plt.barh(features, importance)

plt.title("Feature Importance")
plt.xlabel("Importance Score")

plt.savefig("feature_importance.png")
plt.close()

# ================= ROC CURVE =================
y_prob = model.predict_proba(X_test)[:,1]

fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6,5))
plt.plot(fpr, tpr, label="AUC = %0.2f" % roc_auc)
plt.plot([0,1],[0,1])

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()

plt.savefig("roc_curve.png")
plt.close()

print("\n All images saved successfully!")