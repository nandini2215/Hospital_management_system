from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='frontend/templates')


# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'medinsight_user'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'medinsight_db'

mysql = MySQL(app)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    if request.method == 'POST':
        name = request.form['name']
        specialization = request.form['specialization']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO doctors(name, specialization) VALUES(%s, %s)", (name, specialization))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

@app.route('/get_doctors', methods=['GET'])
def get_doctors():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM doctors")
    doctors = cur.fetchall()
    cur.close()
    return jsonify(doctors)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        disease = request.form['disease']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO patients(name, age, disease) VALUES(%s, %s, %s)", (name, age, disease))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

@app.route('/get_patients', methods=['GET'])
def get_patients():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patients")
    patients = cur.fetchall()
    cur.close()
    return jsonify(patients)

@app.route('/assign_doctor', methods=['POST'])
def assign_doctor():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE patients SET doctor_id=%s WHERE id=%s", (doctor_id, patient_id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

@app.route('/get_patient_history/<int:patient_id>', methods=['GET'])
def get_patient_history(patient_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM consultations WHERE patient_id=%s", [patient_id])
    history = cur.fetchall()
    cur.close()
    return jsonify(history)

@app.route('/add_consultation', methods=['POST'])
def add_consultation():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        comments = request.form['comments']
        precautions = request.form['precautions']
        medications = request.form['medications']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO consultations(patient_id, doctor_id, comments, precautions, medications) VALUES(%s, %s, %s, %s, %s)",
                    (patient_id, doctor_id, comments, precautions, medications))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
