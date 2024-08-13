import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customers = pd.read_csv('customers_large.csv')
products = pd.read_csv('products_large.csv')
orders = pd.read_csv('orders_large.csv')
reviews = pd.read_csv('reviews_large.csv')

print(customers.head())
print(products.head())
print(orders.head())
print(reviews.head())

customers.dropna(inplace=True)
products.dropna(inplace=True)
orders.dropna(inplace=True)
reviews.dropna(inplace=True)

customers.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)
reviews.drop_duplicates(inplace=True)

orders['order_date'] = pd.to_datetime(orders['order_date'])

orders_customers = pd.merge(orders, customers, on='customer_id', how='left')
orders_customers_products = pd.merge(orders_customers, products, on='product_id', how='left')
full_data = pd.merge(orders_customers_products, reviews, on=['customer_id', 'product_id'], how='left')

print(full_data.head())

print("Columns in full_data:", full_data.columns)

plt.figure(figsize=(8, 4))
sns.countplot(data=customers, x='gender')
plt.title('Gender Distribution of Customers')
plt.show()


plt.figure(figsize=(8, 4))
sns.histplot(data=customers, x='age', bins=20, kde=True)
plt.title('Age Distribution of Customers')
plt.show()

if 'price' in full_data.columns:
    sales_trends = full_data.groupby('order_date')['price'].sum().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=sales_trends, x='order_date', y='price')
    plt.title('Sales Trend Over Time')
    plt.show()
else:
    print("Error: 'price' column not found in full_data")

top_products = full_data.groupby('product_name')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False)
plt.figure(figsize=(10, 5))
sns.barplot(data=top_products.head(10), x='quantity', y='product_name')
plt.title('Top 10 Products by Sales Quantity')
plt.show()

print("Columns in full_data for rating analysis:", full_data.columns)
print(full_data.dtypes)

print(full_data[['category', 'rating']].head())
print(full_data[['category', 'rating']].describe())

full_data.dropna(subset=['category', 'rating'], inplace=True)

avg_rating_by_category = full_data.groupby('category')['rating'].mean().reset_index()

plt.figure(figsize=(8, 4))
sns.barplot(data=avg_rating_by_category, x='rating', y='category')
plt.title('Average Product Rating by Category')
plt.show()
