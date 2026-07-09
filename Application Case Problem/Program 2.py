import pandas as pd
from sklearn.linear_model import LogisticRegression

# Dataset
data = {
    "Num_Links": [1, 6, 0, 4, 2],
    "Num_Caps_Words": [3, 15, 1, 10, 5],
    "Email_Length": [120, 300, 80, 250, 160],
    "Spam": [0, 1, 0, 1, 0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[["Num_Links", "Num_Caps_Words", "Email_Length"]]
y = df["Spam"]

# Train Logistic Regression Model
model = LogisticRegression()
model.fit(X, y)

# User Input
links = int(input("Enter Number of Links: "))
caps = int(input("Enter Number of Capitalized Words: "))
length = int(input("Enter Email Length: "))

# Create DataFrame for new email
new_email = pd.DataFrame({
    "Num_Links": [links],
    "Num_Caps_Words": [caps],
    "Email_Length": [length]
})

# Prediction
prediction = model.predict(new_email)

if prediction[0] == 1:
    print("Prediction: Spam Email")
else:
    print("Prediction: Not Spam")