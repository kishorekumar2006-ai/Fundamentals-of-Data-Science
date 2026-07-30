import pandas as pd
from sklearn.linear_model import LogisticRegression

# Dataset
data = {
    "Num_Links": [1, 6, 0, 4, 2],
    "Num_Caps_Words": [3, 15, 1, 10, 5],
    "Email_Length": [120, 300, 80, 250, 160],
    "Spam": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Num_Links", "Num_Caps_Words", "Email_Length"]]
y = df["Spam"]

# Train Model
model = LogisticRegression()
model.fit(X, y)

# Test Email
test_email = pd.DataFrame({
    "Num_Links": [3],
    "Num_Caps_Words": [8],
    "Email_Length": [200]
})

# Prediction
prediction = model.predict(test_email)

if prediction[0] == 1:
    print("Prediction: Spam")
else:
    print("Prediction: Not Spam")