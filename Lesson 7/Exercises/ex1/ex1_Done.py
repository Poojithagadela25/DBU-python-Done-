# Importing libraries
import pandas as pd

# Creating a DataFrame
data = {'Product': ['A', 'B', 'C'], 'Sales': [100, 200, 300], 'Profit': [30, 50, 40]}
df = pd.DataFrame(data)

# Printing the DataFrame
print("Original DataFrame:")
print(df)

# Sorting it by Profit
df_sorted_by_profit = df.sort_values('Profit', ascending=False)
print("\nDataFrame Sorted by Profit:")
print(df_sorted_by_profit)
