import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Dataset
data = {
    "Income": [45000, 30000, 60000, 28000, 52000],
    "Credit_Score": [720, 650, 780, 620, 710],
    "Existing_Loans": [0, 1, 0, 2, 1],
    "Approved": [1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["Income", "Credit_Score", "Existing_Loans"]]
y = df["Approved"]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

income = int(input("Enter Monthly Income: "))
credit = int(input("Enter Credit Score (0-900): "))
if credit < 0 or credit > 900:
    print("Invalid Credit Score! Please enter between 0 and 900.")
    exit(1)
loans = int(input("Enter Existing Loans: "))
if credit < 680:
    print("Loan Status: Rejected")
    print("Reason: Credit Score is below 680.")

else:
    new_applicant = pd.DataFrame({
        "Income": [income],
        "Credit_Score": [credit],
        "Existing_Loans": [loans]
    })

    prediction = model.predict(new_applicant)

    if prediction[0] == 1:
        print("Loan Status: Approved")
    else:
        print("Loan Status: Rejected")