import pandas as pd
df = pd.read_csv("/storage/emulated/0/Download/E-commerce sales.csv")

# getting some info
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())

# Handle missing values
df["Region"] = df["Region"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Shipping Status"] = df["Shipping Status"].fillna("Unknown")

# Check missing values
print("Missing values after cleaning:")
print(df.isnull().sum())

# Checking duplicate rows
print("Duplicate rows:")
print(df.duplicated().sum())

df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed")
print(df.dtypes)

print("Minimum Age:", df["Age"].min())
print("Maximum Age:", df["Age"].max())
print(df["Age"].describe())

print("Minimum values:")

print("Unit Price:", df["Unit Price"].min())
print("Quantity:", df["Quantity"].min())
print("Total Price:", df["Total Price"].min())
print("Shipping Fee:", df["Shipping Fee"].min())
df["Calculated Total"] = df["Unit Price"] * df["Quantity"]
df["Price Difference"] = (
    df["Calculated Total"] - df["Total Price"]
)
print("Price differences:")
print(df["Price Difference"].value_counts())

mismatches = df[df["Price Difference"].abs() > 0.01]

print("Mismatched records:")
print(mismatches[
    ["Customer ID", "Unit Price", "Quantity",
     "Total Price", "Calculated Total", "Price Difference"]
])

df["Price Check"] = df["Price Difference"].abs() <= 0.01

print("Price validation:")
print(df["Price Check"].value_counts())

print("Number of price mismatches:",
      (~df["Price Check"]).sum())
      
df = df.drop(columns=[
    "Calculated Total",
    "Price Difference",
    "Price Check"
])

print(df.columns)

df["Revenue"] = df["Total Price"]
print(df[["Total Price", "Revenue"]].head())

df["Year"] = df["Order Date"].dt.year
print(df[["Order Date", "Year"]].head())

df["Month"] = df["Order Date"].dt.month
print(df[["Order Date", "Month"]].head())

df["Month Name"] = df["Order Date"].dt.month_name()
print(df[["Order Date", "Month", "Month Name"]].head())

df["Total Amount"] = df["Total Price"] + df["Shipping Fee"]
print(df[[
    "Total Price",
    "Shipping Fee",
    "Total Amount"
]].head())

bins = [17, 25, 35, 45, 55, 65, 75]

labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56-65",
    "66-75"
]

df["Age Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

print(df[["Age", "Age Group"]].head(10))

print("Updated dataset:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)