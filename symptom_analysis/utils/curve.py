import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
import matplotlib.pyplot as plt

# Load the training dataset
training_data = pd.read_csv('data/Training.csv')

# Split features and target
X = training_data.drop(columns=['prognosis'])
y = training_data['prognosis']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the models
models = {
    'Random Forest': RandomForestClassifier(),
    'SVC': SVC(probability=True),
    'KNN': KNeighborsClassifier(),
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Gradient Boosting': GradientBoostingClassifier()
}

# Binarize the output labels for ROC curve calculation
y_test_bin = label_binarize(y_test, classes=list(set(y_train)))  
n_classes = y_test_bin.shape[1]

plt.figure(figsize=(10, 6))
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
print(set(y_train))

# Plot ROC curves for each model
for model_name, model in models.items():
    model = OneVsRestClassifier(model)
    model.fit(X_train, y_train)
    
    # Get predicted probabilities
    y_pred_prob = model.predict_proba(X_test)
    
    # Compute the macro-average ROC curve
    fpr, tpr, _ = roc_curve(y_test_bin.ravel(), y_pred_prob.ravel())
    roc_auc = auc(fpr, tpr)
    
    # Plot ROC curve for the model
    plt.plot(fpr, tpr, label=f'{model_name} (AUC = {roc_auc:.2f})')

# Plot diagonal line for random guessing
plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label="Random Classifier")

# Labels and title
plt.title('ROC Curve Comparison of Models')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc='lower right')
plt.show()
