import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset for demo purposes
data = np.random.rand(100, 4)  # 100 samples, 4 features (e.g., HR, speed, movement)
labels = np.random.randint(2, size=100)  # binary labels (0: low risk, 1: high risk)

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

def predict_injury_risk(features):
    prediction = model.predict([features])
    return "High Risk" if prediction[0] else "Low Risk"

# Example prediction
sample_features = np.random.rand(4)
risk = predict_injury_risk(sample_features)
print(f"Predicted Injury Risk: {risk}")
