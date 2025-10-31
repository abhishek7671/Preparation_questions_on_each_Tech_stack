# # ===============================
# # 🎓 STUDENT EXAM PERFORMANCE PREDICTION
# # ===============================

# # 1️⃣ Import necessary libraries
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# # 2️⃣ Create dataset
# data = {
#     'StudyHours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     'Attendance': [50, 60, 65, 70, 72, 80, 85, 90, 95, 98],
#     'PreviousScore': [40, 45, 50, 55, 60, 70, 75, 80, 85, 90],
#     'Result': ['Fail', 'Fail', 'Fail', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass']
# }

# df = pd.DataFrame(data)
# print("🎯 Original DataFrame:")
# print(df)
# print("\n")


# # 3️⃣ Encode categorical target variable (Pass=1, Fail=0)
# df['Result'] = df['Result'].map({'Fail': 0, 'Pass': 1})
# print("✅ Encoded DataFrame:")
# print(df)
# print("\n")


# # 4️⃣ Separate features (X) and target (y)
# X = df[['StudyHours', 'Attendance', 'PreviousScore']]
# y = df['Result']


# # 5️⃣ Split data into training and testing sets (80/20)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# print("📊 Training and Testing data prepared.")
# print("Training samples:", X_train.shape[0])
# print("Testing samples:", X_test.shape[0])
# print("\n")


# # 6️⃣ Feature Scaling (Standardization)
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)
# print("📏 Features scaled successfully.\n")


# # 7️⃣ Train Logistic Regression Model
# model = LogisticRegression()
# model.fit(X_train_scaled, y_train)
# print("🤖 Model training completed.\n")


# # 8️⃣ Make predictions on test data
# y_pred = model.predict(X_test_scaled)
# print("🔮 Predictions on Test Data:")
# print("Predicted:", y_pred)
# print("Actual   :", list(y_test))
# print("\n")


# # 9️⃣ Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# conf_matrix = confusion_matrix(y_test, y_pred)
# class_report = classification_report(y_test, y_pred)

# print("📈 Model Evaluation Results:")
# print("Accuracy Score:", accuracy)
# print("\nConfusion Matrix:\n", conf_matrix)
# print("\nClassification Report:\n", class_report)


# # 🔟 Visualize Relationship between StudyHours and Result
# plt.figure(figsize=(8, 5))
# plt.scatter(df['StudyHours'], df['Result'], color='blue', label="Students")
# plt.title("📊 Study Hours vs Exam Result (0=Fail, 1=Pass)")
# plt.xlabel("Study Hours")
# plt.ylabel("Result")
# plt.grid(True)
# plt.legend()
# plt.show()


# # 1️⃣1️⃣ Predict new student's performance
# print("\n🧮 Predicting New Student Result:")

# # Example: A student with 6 study hours, 85% attendance, and 75 previous score
# new_student = np.array([[6, 85, 75]])
# new_student_scaled = scaler.transform(new_student)
# prediction = model.predict(new_student_scaled)

# if prediction == 1:
#     print("✅ The student is likely to PASS the exam.")
# else:
#     print("❌ The student is likely to FAIL the exam.")





# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Create dataset
data = {
    'Size_sqft': [1000, 1500, 2000, 2500, 3000],
    'Price': [200000, 250000, 300000, 350000, 400000]
}
df = pd.DataFrame(data)

# Step 2: Separate features (X) and target (y)
X = df[['Size_sqft']]   # input feature
y = df['Price']         # target variable

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create the model
model = LinearRegression()

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Display results
print("Predicted prices:", y_pred)
print("Actual prices:", list(y_test))

# Step 8: Visualize
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('House Size (sqft)')
plt.ylabel('House Price ($)')
plt.title('Linear Regression Example')
plt.legend()
plt.show()
