# 🛒 Retail Sales & Customer Analysis Project

## 📌 Project Overview

This project analyzes retail sales data using Python, Pandas, NumPy,
Matplotlib, and Seaborn.

The objective of this project is to: - Clean messy retail data - Handle
missing and duplicate values - Merge multiple datasets - Perform data
analysis - Create meaningful visualizations - Generate business insights

------------------------------------------------------------------------

## 📂 Dataset Files

### 1️⃣ customers.csv

Contains: - customer_id - name - gender - age - city - join_date

### 2️⃣ products.csv

Contains: - product_id - product_name - category - price

### 3️⃣ sales.csv

Contains: - order_id - customer_id - product_id - quantity - order_date

------------------------------------------------------------------------

## 🧹 Data Cleaning

-   Checked data using `.info()`, `.describe()`, `.isnull().sum()`
-   Filled missing **age** using median
-   Filled missing **price** using mean
-   Filled missing **join_date** using mode
-   Removed duplicate records
-   Converted date columns to datetime

------------------------------------------------------------------------

## 🔗 Data Merging

Merged datasets using `pd.merge()`: - sales + customers - merged
result + products

Created new column: total_sales = price \* quantity

------------------------------------------------------------------------

## 📊 Data Analysis

-   Top 5 customers by purchase
-   Sales by city
-   Sales by category
-   Monthly sales trend
-   Most sold product
-   Average age per city

------------------------------------------------------------------------

## 📊 Visualizations

-   Bar Plot -- Sales by City
-   Line Plot -- Monthly Sales Trend
-   Pie Chart -- Category Contribution
-   Heatmap -- Correlation Matrix

------------------------------------------------------------------------

## 🔢 NumPy Tasks

-   Calculated mean, std deviation, and max price
-   Simulated 10% discount using vectorization

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn
-   VS Code

------------------------------------------------------------------------

## 🚀 How to Run

1.  Install dependencies: pip install pandas numpy matplotlib seaborn

2.  Run: python main.py

------------------------------------------------------------------------

## 👤 Author

Vivek Jadhav
Data Analytics Enthusiast
