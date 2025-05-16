import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load your CSV
df = pd.read_csv("lidar_activity_dataset.csv")

# Features and labels
X = df[["avg_height", "spread_x", "spread_y"]]
y = df["label"]

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

# Show results
print("✅ Classification Report:\n")
print(classification_report(y_test, y_pred))
print("\n📊 Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))
