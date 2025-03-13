# 🔹 Import necessary libraries
from joblib import load
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import train_test_split

# 🔹 Load the training data
training_data = pd.read_csv('data/Training.csv')

# 🔹 Split data into features and target
X = training_data.drop('prognosis', axis=1)
y = training_data['prognosis']

# 🔹 Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 Load the optimized model
optimized_model = load('symptom_analysis/utils/optimized_random_forest_model.pkl')

# 🔹 Make predictions using the optimized model
y_pred_optimized = optimized_model.predict(X_test)

# 🔹 Calculate and print the optimized model’s accuracy
print(f"✅ Optimized model accuracy: {accuracy_score(y_test, y_pred_optimized) * 100:.2f}%")
