import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("datasets/diabetes.csv")

# Select important columns
important_cols = [
'age','bmi','glucose_fasting','hba1c','insulin_level',
'systolic_bp','cholesterol_total',
'physical_activity_minutes_per_week',
'family_history_diabetes','smoking_status',
'diagnosed_diabetes'
]

df = df[important_cols]

# Convert categorical column
df['smoking_status'] = df['smoking_status'].map({
    'Never': 0,
    'Former': 1,
    'Current': 2
})

# Fill missing values
df.fillna(df.median(), inplace=True)

# Split data
X = df.drop('diagnosed_diabetes', axis=1)
y = df['diagnosed_diabetes']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "models/random_forest_model.pkl")

print("✅ Model trained & saved successfully!")