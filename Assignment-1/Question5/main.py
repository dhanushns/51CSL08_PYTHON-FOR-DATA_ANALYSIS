import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
online_sales = pd.read_csv('online_sales.csv')
store_sales = pd.read_csv('store_sales.csv')
inventory = pd.read_csv('inventory.csv')
customer_feedback = pd.read_csv('customer_feedback.csv')

# Clean the datasets
online_sales.fillna(0, inplace=True)
store_sales.fillna(0, inplace=True)
inventory.fillna(0, inplace=True)
customer_feedback.fillna('', inplace=True)

# Merge datasets
merged_sales = pd.concat([online_sales, store_sales], axis=0)
merged_sales_inventory = pd.merge(merged_sales, inventory, on='product_id', how='left')
full_data = pd.merge(merged_sales_inventory, customer_feedback, on='order_id', how='left')

# Derived features
full_data['total_sales'] = full_data['quantity_sold'] * full_data['price']
full_data['low_inventory'] = full_data['stock_level'] < full_data['reorder_level']

# Save the cleaned and merged data
full_data.to_csv('cleaned_merged_sales_data.csv', index=False)

# Visualization
# 1. Bar Plot of Total Sales by Product
plt.figure(figsize=(10, 6))
sns.barplot(data=full_data, x='product_name', y='total_sales', estimator=sum, ci=None)
plt.title('Total Sales by Product')
plt.xlabel('Product Name')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.show()

# 2. Count Plot of Low Inventory Products
plt.figure(figsize=(8, 6))
sns.countplot(data=full_data, x='product_name', hue='low_inventory')
plt.title('Low Inventory Status by Product')
plt.xlabel('Product Name')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Low Inventory')
plt.show()

# 3. Box Plot of Customer Ratings by Product
plt.figure(figsize=(10, 6))
sns.boxplot(data=full_data, x='product_name', y='rating')
plt.title('Customer Ratings by Product')
plt.xlabel('Product Name')
plt.ylabel('Rating')
plt.xticks(rotation=45)
plt.show()

print("Data wrangling and visualization complete.")
