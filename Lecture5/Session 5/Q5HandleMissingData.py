# import pandas as pd

# data = {
#     "Patient": ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
#     "Sugar_Level": [110, None, 95, 130, None, 105, 120, None],
# }

# df = pd.DataFrame(data)
# print("Original DataFrame:\n", df)

# print("\nMissing Values:\n", df.isnull())

# mean_value = df["Sugar_Level"].mean()
# print("\nMean Sugar Level:", mean_value)

# df["Sugar_Level"].fillna(mean_value, inplace=True)

# print("\nCleaned DataFrame:\n", df)






# 2nd way to handle missing data

import pandas as pd

# Create DataFrame
data = {
    "Patient": ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
    "Sugar_Level": [110, None, 95, 130, None, 105, 120, None],
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Print missing values
print("\nMissing Values:\n", df.isnull())

# Calculate mean
mean_value = df["Sugar_Level"].mean()
print("\nMean Sugar Level:", mean_value)

# Replace NaN with mean
df["Sugar_Level"].fillna(mean_value, inplace=True)

# Show cleaned DataFrame
print("\nCleaned DataFrame:\n", df)
