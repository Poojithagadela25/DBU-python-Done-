# Import libraries
import pandas as pd

# Create a DataFrame with missing values
data = {'Country': ['USA', 'UK', 'Canada', None],
        'GDP': [21.43, 2.83, 1.74, 0.3]}
df = pd.DataFrame(data)


# Exercise 2: clean the missing values and sort by GDP

# Filling the missing country name with 'Unknown'
df['Country'].fillna('Unknown', inplace=True)  

 # Sorting by GDP in descending order
df_sorted = df.sort_values(by='GDP', ascending=False)


# Exercise 3: calculate the total GDP

total_gdp = df['GDP'].sum()

# Display results
print(df_sorted)
print(f"Total GDP: {total_gdp}")
