# 1 import all labraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2 load all csv files
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
sales = pd.read_csv("sales.csv")

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
sales = pd.read_csv("sales.csv")

# 3 check the data using method
customers.info()
customers.describe()
customers.isnull().sum()

products.info()
products.describe()
products.isnull().sum()

sales.info()
sales.describe()
sales.isnull().sum()


# 4 handle the missing values
# fill missing age with median 
# convert age to numeric 
customers["age"] = pd.to_numeric(customers["age"], errors="coerce")

# fill the median
customers["age"] = customers["age"].fillna(customers["age"].median())
print(customers)

# fill missing price with mean
# convert price into numeric
products["price"] = pd.to_numeric(products["price"], errors="coerce")

# fill with mean
products["price"] = products["price"].fillna(products["price"].mean())
print(products)

# handle missing join_date
# convert to datetime
customers["join_date"] = pd.to_datetime(customers["join_date"], errors="coerce")

# fill missing with mode
customers["join_date"] = customers["join_date"].fillna(customers["join_date"].mode()[0])
print(sales)

# 5 Reove duplicate records
sales.duplicated().sum()
sales = sales.drop_duplicates()

# convert order_date to datetime
sales["order_date"] = pd.to_datetime(sales["order_date"])
print(sales)

# Data merging 
# merge sales and customers
df = pd.merge(sales, customers, on="customer_id", how="inner")
print(df)

# merge with product
retail_df = pd.merge(df, products, on="product_id", how="inner")
print(retail_df)

# create total_sales column
total_sale = retail_df["total_sales"] = retail_df["price"] * retail_df["quantity"]
print(total_sale)

# Data analysis
# top 5 customers
print(retail_df.head())

# sales by city 
city_sales = retail_df.groupby("city")["total_sales"].sum()
print(city_sales)

# sales by categary
sales_catagory = retail_df.groupby("category")["total_sales"].sum()
print(sales_catagory)

# monthly sales trend
retail_df["month"] = retail_df["order_date"].dt.month
retail_df.groupby("month")["total_sales"].sum()
print(retail_df) 

# most sold product
most_sold_product = retail_df.groupby("product_name")["quantity"].sum().sort_values(ascending=False)
print(most_sold_product)

# Average age per city
avg_age_city = retail_df.groupby("city")["age"].mean()
print(avg_age_city)

# Visualization
# bar plot sales by city
retail_df.groupby("city")["total_sales"].sum().plot(kind="bar")
plt.title("Sales by City")
plt.show()

# line plot monthly sales
retail_df.groupby("month")["total_sales"].sum().plot(kind="line")
plt.title("monthly sales trend")
plt.show()

# pie chart category contribution
retail_df.groupby("category")["total_sales"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("monthly contribution")
plt.show()

# heatmap contribution
sns.heatmap(retail_df.corr(numeric_only=True), annot=True)
plt.title("heatmap")
plt.show()

# numpy task
# convert price to numpy array
price_array = retail_df["price"].to_numpy()
print("Mean : ", np.mean(price_array))
print("Std : ", np.std(price_array))
print("Max : ", np.max(price_array))

# create 10% discount simulation
discount_price = price_array * 0.9
discount_price[:5] 
print(discount_price)