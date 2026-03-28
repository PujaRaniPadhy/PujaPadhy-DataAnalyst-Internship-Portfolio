import pandas as pd

# -------------------------------
# Step 1: Load Original Dataset
# -------------------------------

df = pd.read_csv("Dataset.csv")

print("Original dataset loaded successfully")

# -------------------------------
# Step 2: Create Sample Dataset
# -------------------------------

sample_df = df.head(1000)
sample_df.to_csv("sample_dataset.csv", index=False)

print("Sample dataset saved as sample_dataset.csv")

# -------------------------------
# Step 3: Data Access & Familiarization
# -------------------------------

# Load sample dataset
df = pd.read_csv("sample_dataset.csv")

print("\nDataset loaded successfully")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nColumns:")
print(df.columns)

# -------------------------------
# Step 4: Data Quality Assessment
# -------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

# -------------------------------
# Step 5: Data Cleaning
# -------------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with all missing values
df = df.dropna(how="all")

# Fill missing Age values
if "Age" in df.columns:
    df["Age"].fillna(df["Age"].mean(), inplace=True)

# Convert Date column format
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# -------------------------------
# Step 6: Feature Engineering
# -------------------------------

if "Age" in df.columns:
    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=[0, 18, 35, 60, 100],
        labels=["Teen", "Young Adult", "Adult", "Senior"]
    )

# -------------------------------
# Step 7: Save Clean Dataset
# -------------------------------

df.to_csv("cleaned_sample_dataset.csv", index=False)

print("\nData Wrangling Completed Successfully!")
print("Cleaned dataset saved as cleaned_sample_dataset.csv")