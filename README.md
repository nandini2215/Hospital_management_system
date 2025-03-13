AI-Powered Disease Prediction and Patient Management System

Overview
This project is an AI-driven disease prediction and patient management system designed to provide real-time disease predictions based on user-reported symptoms and facilitate efficient doctor-patient consultations. Leveraging a trained Random Forest Machine Learning model, the system offers an interactive and user-friendly experience for both patients and medical professionals.

Built with a Flask-based backend and a React.js (or similar) frontend, the project integrates MySQL for robust database management and ensures seamless interaction between users and the system.

Key Features
🏥 User Roles
Patients:
- Register and log in securely.
- Input symptoms and receive AI-based disease predictions.
- Request doctor consultations.
- View medical history and previous consultations.
- Log out securely.

Doctors:
- View patient details and symptom history.
- Review AI-generated disease predictions.
- Provide medical advice through consultation records.
- Access patient medical history.

Admin:
- Manage doctor and patient accounts.
- View and assign doctors to patient consultation requests.

🤖 AI-Based Disease Prediction
- Utilizes a trained Random Forest Model for disease prediction based on input symptoms.
- Preprocesses user input using a scaler ('random_scaler.pkl') before feeding it into the model.
- Uses 'Training.csv' dataset containing symptoms and corresponding diseases for accurate predictions.

🔗 Backend (Flask API & MySQL Database)
The Flask backend offers RESTful API endpoints for:
- User authentication and session management.
- Storing and retrieving medical records.
- Processing and storing AI-based disease predictions.

MySQL 8.0 Database stores:
- Patient details and medical history.
- Doctor profiles and assigned consultations.
- Disease prediction results with timestamps.

🎨 Frontend (User Interface - React.js or Equivalent)
- User-friendly web interface for symptom input, doctor consultations, and medical history tracking.
- Intuitive dashboards for patients and doctors.
- Real-time display of disease prediction results.

Tech Stack
Component            Technology Used
Backend              Flask (Python)
Database             MySQL 8.0
Machine Learning     Random Forest, Scikit-learn
Frontend             React.js (or another JavaScript framework)
Deployment           AWS / Heroku / DigitalOcean

Installation & Setup
1. Backend Setup (Flask API)
- Install dependencies:
  ```bash
  cd backend
  pip install -r requirements.txt
  ```
- Run the Flask app:
  ```bash
  python app.py
  ```

2. Frontend Setup (React.js or equivalent framework)
- Install dependencies:
  ```bash
  cd frontend
  npm install
  ```
- Start the frontend app:
  ```bash
  npm start
  ```

Future Enhancements
🚀 Potential Improvements:
- Integrate real-time chat between doctors and patients.
- Expand the AI model using deep learning techniques for improved accuracy.
- Add support for mobile applications (Android/iOS).

Project Structure
Backend (Flask)
- `authapp.py`: Main Flask application.
- `config.py`: Configuration settings.
- `models.py`: Database model definitions.
- `model.ipynb`: Jupyter Notebook used for training and testing ML models.
- `random_forest_model.pkl`: Trained Random Forest model for disease prediction.
- `random_scaler.pkl`: Scaler for preprocessing input data.
- `Training.csv`: Dataset used for model training.
- `requirements.txt`: List of dependencies.

Frontend (React or similar framework)
- Located in the `medinsight-frontend` directory, handling user interface and client-side functionality.

Contributing
Contributions are welcome! If you discover bugs or have feature enhancement ideas, feel free to submit a pull request.

