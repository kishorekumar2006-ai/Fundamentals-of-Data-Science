import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Brand": ["Maruti", "Hyundai", "Honda", "Toyota", "Tata"],
    "Age": [2, 5, 3, 7, 1],
    "Kms_Driven": [25000, 60000, 40000, 90000, 15000],
    "Engine_CC": [1200, 1500, 1300, 1800, 1000],
    "Resale_Price": [650000, 420000, 520000, 300000, 720000]
}

df = pd.DataFrame(data)

# Convert Brand into numeric values
df["Brand_Code"] = df["Brand"].astype("category").cat.codes

# Features and Target
X = df[["Brand_Code", "Age", "Kms_Driven", "Engine_CC"]]
y = df["Resale_Price"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Brand Mapping
brands = {
    0: "Honda",
    1: "Hyundai",
    2: "Maruti",
    3: "Tata",
    4: "Toyota"
}

print("Available Brands:")
for code, brand in brands.items():
    print(code, "-", brand)

brand = int(input("Enter Brand Code: "))
age = int(input("Enter Car Age (Years): "))
kms = int(input("Enter Kilometers Driven: "))
engine = int(input("Enter Engine CC: "))

new_car = pd.DataFrame({
    "Brand_Code": [brand],
    "Age": [age],
    "Kms_Driven": [kms],
    "Engine_CC": [engine]
})

price = model.predict(new_car)

print("Estimated Resale Price: ₹", round(price[0], 2))