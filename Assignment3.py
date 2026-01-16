import pandas as pd

# --- Part 1: Reading and inspecting data ---
# Read the data from the csv file
df = pd.read_csv('global_sales.csv')

print("--- First 5 rows ---")
print(df.head()) # Default is 5

print("\n--- Data Types ---")
print(df.dtypes)

# --- Part 2: Data Cleaning and Indexing ---

# 1. Handling Missing Values and Casting
# Fill missing values in Units_Sold with the mean of the column
mean_units = df['Units_Sold'].mean()
df['Units_Sold'] = df['Units_Sold'].fillna(mean_units)

# Convert Sales to numeric (coercing errors to NaN), then fill NaNs with 0
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Sales'] = df['Sales'].fillna(0.0)

# Convert Date column to datetime objects
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 2. Indexing and Setting
# Set OrderID as the initial index
df = df.set_index('OrderID')

# Reset index and then set Date as the new index (important for time series analysis)
df = df.reset_index()
df = df.set_index('Date')

print("\n--- Index set to Date ---")
print(df.index.name)

# --- Part 3: Filtering, Modifying, and Sorting ---

# 1. Filtering Data
# Create a new DataFrame with Sales > 500 and Region equals 'Europe'
high_value_sales = df[(df['Sales'] > 500) & (df['Region'] == 'Europe')]
print("\n--- High Value Sales in Europe (Head) ---")
print(high_value_sales.head())

# 2. Updating and Adding Columns
# Update the 5th row (index 4) of the original DataFrame, setting Units_Sold to 99
# We use iloc for position-based indexing
df.iloc[4, df.columns.get_loc('Units_Sold')] = 99

# Add a new column 'Profit' calculated as Sales * 0.20
df['Profit'] = df['Sales'] * 0.20

print("\n--- Modified DataFrame with Profit (Head) ---")
print(df[['Sales', 'Profit']].head())

# 3. Sorting Data
# Sort by Region (ascending) and then by Sales (descending)
sorted_df = df.sort_values(by=['Region', 'Sales'], ascending=[True, False])

print("\n--- Sorted DataFrame (Head) ---")
print(sorted_df.head())

# --- Part 4: Grouping and Aggregation (Analysis) ---

# 1. Regional Performance
# Group by Region: Sum of Sales and Mean of Units_Sold
print("\n--- Regional Performance ---")
regional_performance = df.groupby('Region').agg({
    'Sales': 'sum',
    'Units_Sold': 'mean'
})
print(regional_performance)

# 2. Product Deep Dive
# Find the maximum Profit achieved for each product
print("\n--- Max Profit per Product ---")
product_profit = df.groupby('Product')['Profit'].max()
print(product_profit)

# 3. Time Series Analysis
# Calculate monthly total sales using resample (ME = Month End)
print("\n--- Monthly Total Sales ---")
monthly_sales = df['Sales'].resample('ME').sum()
print(monthly_sales)