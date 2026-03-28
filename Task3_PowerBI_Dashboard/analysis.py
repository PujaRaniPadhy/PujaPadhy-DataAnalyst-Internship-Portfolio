import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load dataset
df = pd.read_csv("sample_dataset.csv")

df.head()

#Basic information
df.info()
df.describe()


### Data Cleaning

# Remove missing customers.
df = df.dropna(subset=["Customer ID"])

#Convert date column.
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

#Create Revenue column.
df["Revenue"] = df["Quantity"] * df["Price"]

### KPI Calculation

#KPI 1: Total Revenue
total_revenue = df["Revenue"].sum()
print("Total Revenue:", total_revenue)

#KPI 2: Total Orders
total_orders = df["Invoice"].nunique()
print("Total Orders:", total_orders)


#KPI 3: Average Order Value
avg_order_value = total_revenue / total_orders
print("Average Order Value:", avg_order_value)

#KPI 4: Total Customers
total_customers = df["Customer ID"].nunique()
print("Total Customers:", total_customers)


### Deep-Dive Analysis (Customer Segmentation)

customer_spending = df.groupby("Customer ID")["Revenue"].sum().reset_index()

#Create segments
def segment_customer(x):
    if x > 1000:
        return "High Value"
    elif x > 500:
        return "Medium Value"
    else:
        return "Low Value"

customer_spending["Segment"] = customer_spending["Revenue"].apply(segment_customer)

customer_spending.head()

### Visualization (for Dashboard Idea)

#Customer Segmentation
sns.countplot(x="Segment", data=customer_spending)
plt.title("Customer Segmentation")
plt.show()

#Sales by Category
country_sales = df.groupby("Country")["Revenue"].sum()

country_sales.plot(kind="bar", figsize=(10,5))
plt.title("Sales by Country")
plt.show()


#Monthly Sales Trend
monthly_sales = df.groupby(df["InvoiceDate"].dt.month)["Revenue"].sum()

monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.show()