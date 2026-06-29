# 🩺 Diabetes Prediction System Using Machine Learning

## 📌 Project Overview

The **Diabetes Prediction System** is an intelligent web-based healthcare application developed using **Machine Learning** and **Flask**. The system predicts the likelihood of diabetes based on a user's medical and lifestyle information. It provides real-time predictions, risk probability, health recommendations, prediction history, and downloadable PDF reports.

The main objective of this project is to support **early diabetes detection** and assist healthcare professionals and patients in making informed decisions.

---

# 🎯 Objectives

- Predict diabetes risk using Machine Learning.
- Support early disease detection.
- Provide a user-friendly web interface.
- Generate detailed PDF health reports.
- Maintain prediction history for users.
- Compare multiple Machine Learning algorithms to select the best model.

---

# 🚀 Features

- 🔐 User Registration & Login
- 📝 Diabetes Prediction Form
- 🤖 Machine Learning Prediction
- 📊 Risk Probability Display
- 📈 Animated Speedometer Gauge
- 📋 Health Recommendations
- 📄 Downloadable PDF Health Report
- 🗂 Prediction History
- 💾 Database Integration
- 🎨 Responsive User Interface

---

# 🏥 Input Parameters

The prediction model uses the following health parameters:

- Age
- BMI (Body Mass Index)
- Glucose Level
- HbA1c
- Insulin Level
- Blood Pressure
- Cholesterol Level
- Physical Activity
- Family History
- Smoking Status

---

# 🧠 Machine Learning Models

Three Machine Learning algorithms were implemented and compared.

### 1. Random Forest
- Ensemble Learning Algorithm
- Highest Accuracy (92%)
- Handles complex medical data
- Reduces overfitting
- Selected as the final prediction model

### 2. Decision Tree
- Simple tree-based classifier
- Easy to understand
- Moderate performance
- Can overfit training data

### 3. Logistic Regression
- Linear classification algorithm
- Fast and efficient
- Suitable for binary classification
- Lower performance on complex datasets

---

# 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|---------|----------|-----------|--------|----------|
| Random Forest | 92.0% | 0.999 | 0.866 | 0.928 |
| Decision Tree | 86.4% | 0.879 | 0.894 | 0.886 |
| Logistic Regression | 84.9% | 0.860 | 0.891 | 0.875 |

Random Forest was selected as the final model because it achieved the best overall performance.

---

# ⚙️ Data Preprocessing

The dataset was preprocessed before model training by:

- Removing unnecessary features
- Handling missing values
- Encoding categorical variables
- Removing data leakage features
- Feature selection
- Train-Test Split (80:20)

---

# 🌐 System Workflow

1. User Registration/Login
2. User enters health details
3. Data preprocessing
4. Machine Learning prediction
5. Display diabetes risk and probability
6. Generate recommendations
7. Save prediction history
8. Generate downloadable PDF report

---

# 🖥 Technology Stack

### Frontend
- HTML5
- CSS3
- Bootstrap
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Database
- My SQL

### PDF Generation
- ReportLab

---

# 📂 Project Structure

```
diabetes_prediction_project/
│
├── app.py
├── model.py
├── model_comparison.py
├── requirements.txt
├── README.md
│
├── datasets/
│   └── diabetes.csv
│
├── static/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── prediction.html
│   ├── result.html
│   └── history.html
│
├── models/
│
├── reports/
│
└── database/
```

---

# ▶️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd diabetes_prediction_project
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 📸 Application Modules

- Home Page
- Login & Registration
- Prediction Form
- Prediction Result
- History Page
- PDF Health Report

---

# 📄 PDF Report Includes

- Patient Name
- Health Parameters
- Normal Ranges
- Diabetes Risk Level
- Prediction Probability
- Interpretation
- Health Recommendations
- Date and Signature Section

---

# 🎓 Research Contribution

This project demonstrates the practical implementation of Machine Learning in healthcare by combining predictive analytics with a user-friendly web application. It improves diabetes prediction accuracy while providing additional features such as prediction history, PDF report generation, and an interactive interface.

---

# 👨‍💻 Developer

**Nelapati Rushwik Kumar**

M.Tech – Computer Science & Engineering (AI & ML)

Chandigarh University, Uttar Pradesh

---

# 🙏 Acknowledgement

I sincerely thank **Dr. Atul Kumar Verma** for his valuable guidance, support, and encouragement throughout the development of this project.

---

# 📜 License

This project is developed for educational and research purposes.