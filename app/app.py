from flask import Flask, render_template, request, session, redirect, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from model import predict_diabetes, get_recommendation
from db import save_prediction, get_user_predictions, register_user, login_user

# PDF imports
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.secret_key = "secret123"


# --HOME--
@app.route("/")
def home():
    return render_template("home.html")


# --REGISTER--
@app.route("/register", methods=["GET","POST"])
def register():

    error = None

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        status = register_user(name, email, password)

        if status:
            return redirect("/login")
        else:
            error = "Email already exists"

    return render_template("register.html", error=error)


# --LOGIN--
@app.route("/login", methods=["GET","POST"])
def login():

    error = None

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = login_user(email)

        if user and check_password_hash(user[3], password):

            session["user_id"] = user[0]
            session["name"] = user[1]

            return redirect("/")

        else:
            error = "Invalid email or password"

    return render_template("login.html", error=error)


# --LOGOUT--
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# --PREDICT--
@app.route("/predict")
def predict():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("predict.html")

# --RESULT--
@app.route("/result", methods=["POST"])
def result():

    if "user_id" not in session:
        return redirect("/login")

    age = float(request.form["age"])
    bmi = float(request.form["bmi"])
    glucose = float(request.form["glucose"])
    hba1c = float(request.form["hba1c"])
    insulin = float(request.form["insulin"])
    bp = float(request.form["bp"])
    cholesterol = float(request.form["cholesterol"])
    activity = float(request.form["activity"])
    family_history = int(request.form["family_history"])

    smoking = request.form["smoking"]

    smoking_map = {
        "Never": 0,
        "Former": 1,
        "Current": 2
    }

    smoking_value = smoking_map[smoking]

    values = [
        age, bmi, glucose, hba1c, insulin,
        bp, cholesterol, activity, family_history, smoking_value
    ]

    session["latest_values"] = {
        "age": age,
        "bmi": bmi,
        "glucose": glucose,
        "hba1c": hba1c,
        "insulin": insulin,
        "bp": bp,
        "cholesterol": cholesterol,
        "activity": activity,
        "family_history": family_history,
        "smoking": smoking
    }

    prediction, probability = predict_diabetes(values)

    if probability >= 70:
        risk_level = "High Risk"
    elif probability >= 40:
        risk_level = "Moderate Risk"
    else:
        risk_level = "Low Risk"

    recommendation = get_recommendation(risk_level)

    save_prediction(session["user_id"], values, risk_level, probability)

    return render_template(
        "result.html",
        prediction=risk_level,
        probability=probability,
        recommendation=recommendation
    )


# .2--HISTORY--
@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect("/login")

    predictions = get_user_predictions(session["user_id"])

    return render_template("history.html", predictions=predictions)


# ---------------- DOWNLOAD (ONLY ONE CLEAN VERSION) ----------------
@app.route("/download")
def download():

    if "user_id" not in session:
        return redirect("/login")

    # get latest prediction
    predictions = get_user_predictions(session["user_id"])
    last = predictions[0]

    risk = last[4]
    probability = last[5]
    date = last[6]

    # ✅ GET ALL VALUES FROM SESSION
    data = session.get("latest_values")

    age = data["age"]
    bmi = data["bmi"]
    glucose = data["glucose"]
    hba1c = data["hba1c"]
    insulin = data["insulin"]
    bp = data["bp"]
    cholesterol = data["cholesterol"]
    activity = data["activity"]
    family_history = "Yes" if data["family_history"] == 1 else "No"
    smoking = data["smoking"]

    recommendation = get_recommendation(risk)

    file_path = os.path.join(os.getcwd(), "Diabetes_Report.pdf")

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()

    content = []

    # ================= TITLE =================
    content.append(Paragraph("<b><font size=18>🩺 Diabetes AI Health Report</font></b>", styles['Title']))
    content.append(Spacer(1, 10))

    # ================= USER INFO =================
    content.append(Paragraph(f"Patient Name: {session['name']}", styles['Normal']))
    content.append(Paragraph("Report ID: DIA-2026-001", styles['Normal']))
    content.append(Paragraph(f"Date: {date}", styles['Normal']))
    content.append(Spacer(1, 15))

    # ================= TABLE =================
    table_data = [
        ["Parameter", "Your Value", "Normal Range"],

        ["Age", age, "20 - 80"],
        ["BMI", bmi, "18 - 25"],
        ["Glucose", glucose, "70 - 140 mg/dL"],
        ["HbA1c", hba1c, "4 - 6 %"],
        ["Insulin", insulin, "2 - 25 µU/mL"],
        ["Blood Pressure", bp, "90 - 140 mmHg"],
        ["Cholesterol", cholesterol, "< 200 mg/dL"],
        ["Physical Activity", activity, "150+ min/week"],
        ["Family History", family_history, "Yes/No"],
        ["Smoking", smoking, "Never/Former/Current"],
    ]

    table = Table(table_data, colWidths=[150, 120, 150])

    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("GRID",(0,0),(-1,-1),1,colors.grey),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),
    ]))

    content.append(table)
    content.append(Spacer(1, 15))

    # ================= RISK COLOR =================
    if risk == "High Risk":
        color = "red"
    elif risk == "Moderate Risk":
        color = "orange"
    else:
        color = "green"

    content.append(Paragraph(f"<font color='{color}'><b>Risk Level: {risk}</b></font>", styles['Heading3']))
    content.append(Paragraph(f"Probability: {probability}%", styles['Normal']))

    content.append(Spacer(1, 15))

    # ================= INTERPRETATION =================
    content.append(Paragraph("<b>Interpretation</b>", styles['Heading3']))

    if risk == "High Risk":
        msg = "Your values are significantly above normal ranges, indicating a high likelihood of diabetes."
    elif risk == "Moderate Risk":
        msg = "Some values are slightly abnormal. Lifestyle changes are recommended."
    else:
        msg = "Your values are within normal limits. Maintain a healthy lifestyle."

    content.append(Paragraph(msg, styles['Normal']))

    content.append(Spacer(1, 15))

    # ================= RECOMMENDATION =================
    content.append(Paragraph("<b>Medical Recommendation</b>", styles['Heading3']))
    content.append(Paragraph(recommendation, styles['Normal']))

    content.append(Spacer(1, 20))

    # ================= FOOTER =================
    content.append(Paragraph(
        "This Report is Generated by Diabetes AI System | Chandigarh University,UP",
        styles['Italic']
    ))

    content.append(Spacer(1, 25))

    # BUILD PDF
    doc.build(content)

    return send_file(
        file_path,
        as_attachment=True,
        download_name="Diabetes_Report.pdf"
    )

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)