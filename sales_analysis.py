"""
Supermarket Sales Analysis - End-to-End EDA
Run:  python sales_analysis.py
Input:  data/supermarket.csv
Output: images/*.png  (all charts saved automatically)
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

DATA_PATH = "data/supermarket.csv"
IMG_DIR = "images"
os.makedirs(IMG_DIR, exist_ok=True)
sns.set_style("darkgrid")


def save(name):
    plt.tight_layout()
    plt.savefig(f"{IMG_DIR}/{name}.png", dpi=150)
    plt.close()


# ------------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------------
df = pd.read_csv(DATA_PATH)

# ------------------------------------------------------------------
# 2. DATA INSPECTION
# ------------------------------------------------------------------
print("First rows:\n", df.head(), "\n")
print("Last rows:\n", df.tail(3), "\n")
print("Info:")
df.info()
print("\nSize:", df.size)
print("Shape:", df.shape)
print("\nSummary statistics:\n", df.describe())
print("\nMissing values:\n", df.isnull().sum())

# ------------------------------------------------------------------
# 3. FEATURE ENGINEERING
# ------------------------------------------------------------------
df["Date"] = pd.to_datetime(df["Date"])
df["weekday"] = df["Date"].dt.day_name()
df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M").dt.hour

# ------------------------------------------------------------------
# 4. CUSTOMER DEMOGRAPHICS
# ------------------------------------------------------------------
print("\nGender counts:\n", df["Gender"].value_counts())
print("\nBranch counts:\n", df["Branch"].value_counts())

plt.figure(figsize=(6, 4))
sns.countplot(x="Gender", data=df)
plt.title("Total Number of Male and Female Customers")
save("01_gender_count")

plt.figure(figsize=(12, 5))
sns.countplot(x="Customer type", hue="Branch", data=df, palette="rocket_r")
plt.title("Customer Types in All Branches")
plt.xlabel("Customer type")
plt.ylabel("Customer Count")
save("02_customer_type_by_branch")

# ------------------------------------------------------------------
# 5. PAYMENT BEHAVIOR
# ------------------------------------------------------------------
plt.figure(figsize=(12, 5))
sns.countplot(x="Payment", hue="Branch", data=df, palette="tab20")
plt.title("Payment Distribution in All Branches")
plt.xlabel("Payment method")
plt.ylabel("People Count")
save("03_payment_by_branch")

# ------------------------------------------------------------------
# 6. CUSTOMER SATISFACTION (RATINGS)
# ------------------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.histplot(df["Rating"], kde=True)
plt.title("Rating Distribution")
plt.grid(True)
save("04_rating_distribution")

plt.figure(figsize=(8, 5))
sns.scatterplot(x="Rating", y="gross income", data=df)
plt.title("Gross Income vs Rating")
save("05_gross_income_vs_rating")

plt.figure(figsize=(8, 5))
sns.boxplot(x="Branch", y="Rating", data=df, hue="Branch", palette="RdYlBu", legend=False)
plt.title("Rating in All Branches")
plt.grid(True)
save("06_rating_by_branch")

# ------------------------------------------------------------------
# 7. REVENUE / GROSS INCOME ANALYSIS
# ------------------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x="Branch", y="gross income", data=df)
plt.title("Gross Income vs Branch")
save("07_gross_income_by_branch")

plt.figure(figsize=(8, 5))
sns.boxplot(x="Gender", y="gross income", data=df)
plt.title("Gross Income vs Gender")
save("08_gross_income_by_gender")

plt.figure(figsize=(12, 5))
sns.lineplot(x=df.index, y=df["gross income"])
plt.title("Gross Income Across Transactions")
save("09_gross_income_trend")

product_income = (
    df.groupby("Product line", as_index=False)["gross income"]
    .sum()
    .sort_values("gross income", ascending=False)
)
print("\nGross income by product line:\n", product_income)

plt.figure(figsize=(14, 6))
sns.barplot(x="Product line", y="gross income", data=product_income)
plt.title("Gross Income vs Product Line")
save("10_gross_income_by_product_line")

city_income = (
    df.groupby("City", as_index=False)["gross income"]
    .sum()
    .sort_values("gross income", ascending=False)
)
print("\nGross income by city:\n", city_income)

plt.figure(figsize=(10, 5))
sns.barplot(y="City", x="gross income", data=city_income, hue="City", palette="Set1", legend=False)
plt.title("Total Gross Income by City")
save("11_gross_income_by_city")

# ------------------------------------------------------------------
# 8. PRODUCT ANALYSIS
# ------------------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.histplot(df["Quantity"], bins=10, kde=True)
plt.title("Quantity Distribution")
save("12_quantity_distribution")

plt.figure(figsize=(14, 6))
sns.countplot(x="Product line", hue="Gender", data=df)
plt.title("Transactions by Product Line and Gender")
save("13_product_line_by_gender")

plt.figure(figsize=(10, 6))
sns.barplot(y="Product line", x="Rating", data=df)
plt.title("Average Rating by Product Line")
save("14_rating_by_product_line")

# ------------------------------------------------------------------
# 9. TIME-BASED ANALYSIS
# ------------------------------------------------------------------
order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
plt.figure(figsize=(8, 5))
sns.countplot(x="weekday", data=df, order=order)
plt.title("Daily Sales by Day of Week")
save("15_sales_by_weekday")

print("\nTransactions by hour:\n", df["Hour"].value_counts().sort_index())
plt.figure(figsize=(10, 5))
sns.countplot(x="Hour", data=df, hue="Hour", palette="viridis", legend=False)
plt.title("Transactions by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Transaction Count")
plt.grid(axis="y", linestyle="--", alpha=0.7)
save("16_transactions_by_hour")

plt.figure(figsize=(10, 5))
sns.lineplot(x="Hour", y="Quantity", data=df)
plt.title("Product Sales per Hour")
save("17_quantity_by_hour")

print(f"\nDone. {len(os.listdir(IMG_DIR))} charts saved in '{IMG_DIR}/'.")
