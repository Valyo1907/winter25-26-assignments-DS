#Assignment 2 - ## Part 1: NumPy Array Manipulation (The Core Data)

import numpy as np

#1. Product Data ---

product_ids = np.arange(1001, 1011)

stock = np.array([50, 120, 30, 80, 60, 20, 15, 90, 110, 45])

avg_sales = np.array([15.5, 3.2, 25.0, 10.0, 8.5, 5.0, 2.0, 7.5, 18.0, 12.3])

unit_cost = np.array([10.99, 50.50, 5.00, 12.49, 8.30, 2.99, 1.50, 7.20, 15.00, 4.75])

inventory_data = np.column_stack([stock, avg_sales, unit_cost])


#2. Checking basic things ---

print("Shape of the inventory array:", inventory_data.shape)
print("Data type:", inventory_data.dtype)

total_value = stock * unit_cost
print("Total stock value for each product:", total_value)


#3. Slicing and simple stats ---

print("\nProducts 3 to 7:")
print(inventory_data[3:8])

avg_sales_mean = np.mean(avg_sales)
print("\nAverage weekly sales (all products):", round(avg_sales_mean, 2))

print("\nUnit cost of the first product:", inventory_data[0, 2])



## Part 2: Advanced NumPy Analysis (Re-stocking Logic)

# 1) Boolean Masking (Low-Stock Check)
weeks_of_stock = stock / avg_sales
print("\nWeeks of stock for each product:", weeks_of_stock)

# low stock = less than 4 weeks
low_stock_mask = weeks_of_stock < 4
print("\nLow-stock mask (True means low stock):", low_stock_mask)

# show the rows of products that are low in stock
low_stock_products = inventory_data[low_stock_mask]
print("\nProducts that are low in stock (rows from inventory_data):")
print(low_stock_products)

# 2) Reshaping + Concatenation (Updating Data)
# reorder_quantity = (4 * avg_sales) - current stock
# meaning: order enough to reach a 4-week supply
reorder_quantity = (4 * avg_sales) - stock

reorder_quantity = np.maximum(reorder_quantity, 0)

print("\nReorder quantity for each product:", reorder_quantity)

reorder_quantity_2d = reorder_quantity.reshape(-1, 1)

updated_inventory_data = np.concatenate((inventory_data, reorder_quantity_2d), axis=1)

print("\nUpdated inventory data (Stock, Avg Sales, Unit Cost, Reorder Qty):")
print(updated_inventory_data)
print("New shape:", updated_inventory_data.shape)



## Part 3: Introduction to Pandas (Viewing the Results)

import pandas as pd

# 1) Creating DataFrame
df = pd.DataFrame(
    updated_inventory_data,
    columns=["Stock", "Sales", "Cost", "Reorder Qty"]
)

print("\n--- DataFrame (full) ---")
print(df)

# 2) Selecting Specific Columns
print("\n--- Only Stock and Reorder Qty ---")
print(df[["Stock", "Reorder Qty"]])

# 3) First 5 rows
print("\n--- First 5 rows ---")
print(df.head(5))
