import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/random_forest_model.pkl")

def predict_diabetes(input_data):

    columns = [
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
    ]

    data = pd.DataFrame([input_data], columns=columns)

    prediction = model.predict(data)[0]
    probability = float(model.predict_proba(data)[0][1]) * 100

    return prediction, round(probability, 2)


# Health Recommendation Function
def get_recommendation(risk_level):

    if risk_level == "High Risk":
        return "High risk of diabetes detected. Please consult a doctor immediately. Maintain a strict diet, monitor blood sugar regularly, and increase physical activity."

    elif risk_level == "Moderate Risk":
        return "Moderate risk detected. Reduce sugar intake, exercise regularly, and monitor blood glucose levels frequently."

    else:
        return "Low risk detected. Maintain a healthy lifestyle with balanced diet and regular exercise."