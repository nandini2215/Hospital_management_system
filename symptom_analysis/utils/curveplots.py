import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.metrics import accuracy_score, roc_curve, auc
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier

# Step 1: Load and preprocess datasets
# Step 1: Load and preprocess datasets
files = {
    "precautions": "data/precautions_df.csv",
    "symptom_severity": "data/Symptom-severity.csv",
    "symptoms": "data/symptoms_df.csv",  # fixed typo
    "training": "data/Training.csv",
    "workout": "data/workout_df.csv",
    "description": "data/description.csv",
    "diets": "data/diets.csv",
    "medications": "data/medications.csv"
}


datasets = {name: pd.read_csv(path) for name, path in files.items()}

# Drop unnecessary columns (Unnamed columns)
for name, df in datasets.items():
    df.drop(columns=[col for col in df.columns if 'Unnamed' in col], inplace=True, errors='ignore')

# Check for missing values and fill them appropriately
for name, df in datasets.items():
    df.fillna("Not Available", inplace=True)

# Convert categorical disease names to numerical labels
le = LabelEncoder()
datasets['training']['prognosis'] = le.fit_transform(datasets['training']['prognosis'])

# Function to map symptom severity
def map_severity(symptom):
    row = datasets['symptom_severity'][datasets['symptom_severity']['Symptom'] == symptom]
    return row['weight'].values[0] if not row.empty else 0

# Convert symptoms into weighted values in training dataset
for col in datasets['training'].columns[:-1]:  # Exclude target column
    if col in datasets['symptom_severity']['Symptom'].values:
        datasets['training'][col] *= map_severity(col)

# Step 2: Splitting Data for ML
X = datasets['training'].drop(columns=['prognosis'])
y = datasets['training']['prognosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Defining models to evaluate
models = {
    'Random Forest': RandomForestClassifier(),
    'SVC': SVC(probability=True),
    'KNN': KNeighborsClassifier(),
    'Logistic Regression': LogisticRegression(),
    'Gradient Boosting': GradientBoostingClassifier()
}

# Step 4: Training models and evaluating performance
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = {
        'accuracy': accuracy,
        'model': model
    }

# Step 5: Accuracy Comparison Plot
model_names = list(results.keys())
accuracy_scores = [results[name]['accuracy'] for name in model_names]

plt.figure(figsize=(10, 6))
sns.barplot(x=model_names, y=accuracy_scores, palette='viridis')
plt.title("Accuracy Comparison of Models")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.show()

# Step 6: Learning Curve Plot for Each Model
for model_name, model in models.items():
    plt.figure(figsize=(10, 6))
    train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5, n_jobs=-1, train_sizes=[0.1, 0.2, 0.4, 0.6, 0.8, 1.0])
    
    train_mean = train_scores.mean(axis=1)
    test_mean = test_scores.mean(axis=1)
    
    plt.plot(train_sizes, train_mean, label=f"Training - {model_name}")
    plt.plot(train_sizes, test_mean, label=f"Cross-validation - {model_name}", linestyle='--')

    plt.title(f"Learning Curve - {model_name}")
    plt.xlabel("Training Size")
    plt.ylabel("Score")
    plt.legend(loc="best")
    plt.show()

# Step 7: ROC Curve Plot for All Models (Multiclass Support)
plt.figure(figsize=(12, 8))

# Binarize the output labels for multiclass ROC
y_test_bin = label_binarize(y_test, classes=[0, 1, 2, 3, 4])  # Adjust based on number of classes in your data
# Binarize the output labels for multiclass ROC based on unique classes
n_classes = len(le.classes_)
y_test_bin = label_binarize(y_test, classes=range(n_classes))

# Fit the model using binarized labels for ROC curves
for model_name, model in models.items():
    model = OneVsRestClassifier(model)
    model.fit(X_train, label_binarize(y_train, classes=range(n_classes)))  # fix here

    y_pred_prob = model.predict_proba(X_test)

    # Compute ROC curve and ROC AUC for each class
    for i in range(n_classes):
        fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_pred_prob[:, i])
        roc_auc = auc(fpr, tpr)
        
        plt.plot(fpr, tpr, label=f'{model_name} - Class {i} (AUC = {roc_auc:.2f})')

plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label="Random Classifier")
plt.title('Receiver Operating Characteristic (ROC) Curve (Multiclass)')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc='best')
plt.show()
