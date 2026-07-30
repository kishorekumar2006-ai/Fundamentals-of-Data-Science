import numpy as np

# Create NumPy array (Bedrooms, Sqft, Sale_Price)
house_data = np.array([
    [3, 1400, 7500000],
    [5, 2200, 12500000],
    [4, 1800, 9800000],
    [6, 3000, 18500000],
    [2, 1100, 5200000]
])

# Extract columns
bedrooms = house_data[:, 0]
sale_price = house_data[:, 2]

# Filter houses with more than 4 bedrooms
filtered_prices = sale_price[bedrooms > 4]

# Calculate average
average_price = np.mean(filtered_prices)

print("Average Sale Price (Bedrooms > 4):", average_price)
