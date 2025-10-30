# Student Performance Prediction
# Day 19–20 Project

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load data
df = pd.read_csv('student_performance.csv')
print("Dataset preview:")
print(df.head(), "\n")

# Step 2: Define features (X) and target (y)
X = df[['StudyHours', 'Attendance', 'InternalMarks']]
y = df['Pass']

# Step 3: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 5: Predict on test data
y_pred = model.predict(X_test)

# Step 6: Evaluate model performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 7: Make a new prediction
new_student = [[6, 82, 76]]  # [StudyHours, Attendance, InternalMarks]
prediction = model.predict(new_student)
result = "Pass " if prediction[0] == 1 else "Fail "
print("\nPredicted result for new student:", result)
