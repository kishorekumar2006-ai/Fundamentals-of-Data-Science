import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Titanic-Dataset.csv")

# 1. Dataset Information
print("===== Dataset Information =====")
print(df.info())

# 2. Missing Values
print("\n===== Missing Values =====")
print(df.isnull().sum())

# 3. Descriptive Statistics
print("\n===== Descriptive Statistics =====")
print(df.describe())

# Select Numeric Columns
numeric = df.select_dtypes(include='number')

# 4. Histograms
numeric.hist(figsize=(12,8))
plt.suptitle("Histograms of Numeric Features")
plt.show()

# 5. Box Plots
plt.figure(figsize=(12,6))
numeric.boxplot()
plt.title("Box Plots of Numeric Features")
plt.xticks(rotation=45)
plt.show()

# 6. Detect Outliers using IQR
Q1 = numeric.quantile(0.25)
Q3 = numeric.quantile(0.75)
IQR = Q3 - Q1

outliers = ((numeric < (Q1 - 1.5 * IQR)) |
            (numeric > (Q3 + 1.5 * IQR)))

print("\n===== Number of Outliers =====")
print(outliers.sum())

# 7. Remove Outliers
clean_df = df[~outliers.any(axis=1)]

print("\nOriginal Dataset Shape:", df.shape)
print("Cleaned Dataset Shape:", clean_df.shape)

# Histogram After Removing Outliers
clean_numeric = clean_df.select_dtypes(include='number')

clean_numeric.hist(figsize=(12,8))
plt.suptitle("Histograms After Removing Outliers")
plt.show()

# Box Plot After Removing Outliers
plt.figure(figsize=(12,6))
clean_numeric.boxplot()
plt.title("Box Plots After Removing Outliers")
plt.xticks(rotation=45)
plt.show()

# 8. Save Cleaned Dataset
clean_df.to_csv("Titanic_Cleaned.csv", index=False)

print("\nCleaned dataset saved as Titanic_Cleaned.csv")