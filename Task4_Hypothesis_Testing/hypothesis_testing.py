import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


# Load dataset
df = pd.read_csv("sample_dataset.csv")

# Display first rows
df.head()

#Dataset Information
df.info()
df.describe()

#Data Cleaning
df = df.dropna()

df.isnull().sum()


#Create Sales Column
df["Sales"] = df["Quantity"] * df["Price"]

df.head()

#Basic Statistics
df.describe()

#Top 10 Products by Sales
top_products = df.groupby("Description")["Sales"].sum().sort_values(ascending=False).head(10)

print(top_products)


#Sales by Country
country_sales = df.groupby("Country")["Sales"].sum().sort_values(ascending=False)

print(country_sales.head(10))


#Visualization (Sales vs Quantity)
plt.figure()

plt.scatter(df["Quantity"], df["Sales"])

plt.title("Relationship Between Quantity and Sales")
plt.xlabel("Quantity Purchased")
plt.ylabel("Sales Revenue")

plt.show()


#### Hypothesis
# H0: Quantity purchased does not affect total sales revenue

# H1: Higher quantity purchased increases total sales revenue


#Hypothesis Testing (T-Test)
high_quantity = df[df["Quantity"] > 5]["Sales"]

low_quantity = df[df["Quantity"] <= 5]["Sales"]

t_stat, p_value = ttest_ind(high_quantity, low_quantity)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

#Interpretation
if p_value < 0.05:
    print("Reject Null Hypothesis")
    print("Higher purchase quantity significantly increases sales revenue.")
else:
    print("Fail to Reject Null Hypothesis")

#Correlation Analysis
correlation = df["Quantity"].corr(df["Sales"])

print("Correlation between Quantity and Sales:", correlation)


