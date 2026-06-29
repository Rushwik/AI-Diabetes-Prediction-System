import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Models
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# 1. Load dataset
df = pd.read_csv("datasets/diabetes.csv")

# 🔥 Clean column names
df.columns = df.columns.str.strip().str.lower()

# 🔍 Check columns (optional)
print("Columns:", df.columns)

# 🔥 REMOVE DATA LEAKAGE COLUMNS (VERY IMPORTANT)
df = df.drop(["diabetes_risk_score", "diabetes_stage"], axis=1)

# 🔥 Target column
target_column = "diagnosed_diabetes"

# 2. Features & target
X = df.drop(target_column, axis=1)

# 🔥 Convert categorical to numeric
X = pd.get_dummies(X)

y = df[target_column]

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Define models
models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42)
}

# 5. Train + evaluate
results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    results.append({
        "Model": name,
        "Accuracy": round(acc, 3),
        "Precision": round(prec, 3),
        "Recall": round(rec, 3),
        "F1 Score": round(f1, 3)
    })

# 6. Convert to DataFrame
results_df = pd.DataFrame(results)

# 7. Sort by Accuracy
results_df = results_df.sort_values(by="Accuracy", ascending=False)

# 8. Print results
print("\nModel Comparison Results:\n")
print(results_df)

# 9. Save to CSV (for paper)
results_df.to_csv("model_comparison_results.csv", index=False)

print("\n✅ Results saved to model_comparison_results.csv")