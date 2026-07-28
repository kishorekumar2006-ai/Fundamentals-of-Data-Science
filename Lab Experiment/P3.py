import numpy as np

house_data = np.genfromtxt(
    "House_data.csv",
    delimiter=",",
    skip_header=1,
    usecols=(1, 3),
    dtype=float
)

houses_more_than_4 = house_data[house_data[:, 0] > 4]

average_price = np.mean(houses_more_than_4[:, 1])

print(
    "Average price of houses with more than 4 bedrooms:",
    round(average_price, 2)
)