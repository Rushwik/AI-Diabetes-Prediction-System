import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Ammanana2525",
    database="diabetes_db"
)

cursor = connection.cursor()


# ---------------- REGISTER USER ----------------

def register_user(name, email, password):

    query = "SELECT * FROM users WHERE email=%s"
    cursor.execute(query,(email,))

    user = cursor.fetchone()

    if user:
        return False

    query = """
    INSERT INTO users (name,email,password)
    VALUES (%s,%s,%s)
    """

    cursor.execute(query,(name,email,password))
    connection.commit()

    return True


# ---------------- LOGIN USER ----------------

def login_user(email):

    query = "SELECT * FROM users WHERE email=%s"

    cursor.execute(query,(email,))

    return cursor.fetchone()


# ---------------- SAVE PREDICTION ----------------

def save_prediction(user_id, values, risk_level, probability):

    query = """
    INSERT INTO predictions
    (user_id,age,bmi,glucose,hba1c,insulin,bp,cholesterol,activity,family_history,smoking_status,result,probability)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(
        user_id,
        values[0],
        values[1],
        values[2],
        values[3],
        values[4],
        values[5],
        values[6],
        values[7],
        values[8],
        values[9],
        risk_level,
        probability
    ))

    connection.commit()


# ---------------- USER HISTORY ----------------

def get_user_predictions(user_id):

    query = """
    SELECT age,bmi,glucose,hba1c,result,probability,created_at
    FROM predictions
    WHERE user_id=%s
    ORDER BY created_at DESC
    """

    cursor.execute(query,(user_id,))

    return cursor.fetchall()