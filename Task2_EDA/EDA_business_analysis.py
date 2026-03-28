# Exploratory Data Analysis (EDA) & Business Intelligence

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sample_dataset.csv")

print("First 5 rows of dataset:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())


# -----------------------------
# Univariate Analysis
# -----------------------------

# Histogram for Quantity
plt.hist(df["Quantity"], bins=20)
plt.title("Distribution of Quantity")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

# Histogram for Price
plt.hist(df["Price"], bins=20)
plt.title("Distribution of Price")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Bar chart for Country
df["Country"].value_counts().head(10).plot(kind="bar")

plt.title("Top Countries by Orders")
plt.xlabel("Country")
plt.ylabel("Count")

plt.show()

# -----------------------------
# Multivariate Analysis
# -----------------------------

# Scatter plot Quantity vs Price
plt.scatter(df["Quantity"], df["Price"])

plt.xlabel("Quantity")
plt.ylabel("Price")

plt.title("Quantity vs Price")

plt.show()

# -----------------------------
# Correlation Heatmap
# -----------------------------

numeric_df = df[["Quantity", "Price", "Customer ID"]]

sns.heatmap(numeric_df.corr(), annot=True)

plt.title("Correlation Heatmap")

plt.show()

# -----------------------------
# Pair Plot (Multivariate Analysis)
# -----------------------------

numeric_df = df[["Quantity", "Price", "Customer ID"]]

sns.pairplot(numeric_df)

plt.show()

print("\nEDA Analysis Completed Successfully.")


print("Total Sales:", (df["Quantity"]*df["Price"]).sum())
print("Total Quantity:", df["Quantity"].sum())
print("Total Customers:", df["Customer ID"].nunique())
print("Average Price:", df["Price"].mean())
