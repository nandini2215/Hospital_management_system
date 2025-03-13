from joblib import dump
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Load the training data
training_data = pd.read_csv('data/Training.csv')

# Split data into features and target
X = training_data.drop('prognosis', axis=1)
y = training_data['prognosis']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Optimized Random Forest model
optimized_rf = RandomForestClassifier(n_estimators=200, max_depth=20, random_state=42)
optimized_rf.fit(X_train, y_train)

# Evaluate the model
y_pred = optimized_rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Optimized Accuracy: {accuracy * 100:.2f}%")

# Save the optimized model
dump(optimized_rf, 'symptom_analysis/utils/optimized_random_forest_model.pkl')
dump(scaler, "symptom_analysis/utils/random_scaler.pkl")
print("Optimized model saved successfully!")
