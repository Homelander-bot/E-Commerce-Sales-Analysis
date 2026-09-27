import pandas as pd
df = pd.read_csv("/storage/emulated/0/Download/E-commerce sales.csv")

print("===== PRODUCT ANALYSIS =====")

sales_by_product = df.groupby("Product Name")["Total Price"].sum()
quantity_by_product = df.groupby("Product Name")["Quantity"].sum()
orders_by_product = df["Product Name"].value_counts()

print("\nSales by Product:")
print(sales_by_product)
print("\nQuantity by Product:")
print(quantity_by_product)
print("\nOrders by Product:")
print(orders_by_product)


print("===== REGIONAL ANALYSIS =====")

sales_by_region = df.groupby("Region")["Total Price"].sum()
quantity_by_region = df.groupby("Region")["Quantity"].sum()
orders_by_region = df["Region"].value_counts()

print("\nSales by Region:")
print(sales_by_region)
print("\nQuantity by Region:")
print(quantity_by_region)
print("\nOrders by Region:")
print(orders_by_region)
print()

print("===== GENDER ANALYSIS =====")

orders_by_gender = df["Gender"].value_counts()
sales_by_gender = df.groupby("Gender")["Total Price"].sum()
quantity_by_gender = df.groupby("Gender")["Quantity"].sum()
aov_by_gender = df.groupby("Gender")["Total Price"].mean()

print("\nOrders by Gender:")
print(orders_by_gender)
print("\nSales by Gender:")
print(sales_by_gender)
print("\nQuantity by Gender:")
print(quantity_by_gender)
print("\nAverage Order Value by Gender:")
print(aov_by_gender)

print("===== AGE GROUP ANALYSIS =====")

orders_by_age = df["Age Group"].value_counts().sort_index()
sales_by_age = df.groupby("Age Group", observed=True)["Total Price"].sum()
quantity_by_age = df.groupby("Age Group", observed=True)["Quantity"].sum()

print("\nOrders by Age Group:")
print(orders_by_age)
print("\nSales by Age Group:")
print(sales_by_age)
print("\nQuantity by Age Group:")
print(quantity_by_age)

print("===== SHIPPING ANALYSIS =====")

orders_by_shipping = df["Shipping Status"].value_counts()
sales_by_shipping = df.groupby("Shipping Status")["Total Price"].sum()
quantity_by_shipping = df.groupby("Shipping Status")["Quantity"].sum()

print("\nOrders by Shipping Status:")
print(orders_by_shipping)
print("\nSales by Shipping Status:")
print(sales_by_shipping)
print("\nQuantity by Shipping Status:")
print(quantity_by_shipping)

print("===== RETURN ANALYSIS BY PRODUCT =====")

returned_df = df[df["Shipping Status"] == "Returned"]
returned_orders_by_product = (
    returned_df["Product Name"].value_counts()
)
returned_sales_by_product = (
    returned_df.groupby("Product Name")["Total Price"].sum()
)

print("\nReturned Orders by Product:")
print(returned_orders_by_product)
print("\nReturned Sales by Product:")
print(returned_sales_by_product)

print("===== RETURN RATE BY PRODUCT =====")

total_orders_by_product = df["Product Name"].value_counts()
returned_orders_by_product = (
    df[df["Shipping Status"] == "Returned"]["Product Name"]
    .value_counts()
)
return_rate = (
    returned_orders_by_product
    .div(total_orders_by_product)
    .fillna(0)
    * 100
).round(2)

print("\nReturn Rate by Product (%):")
print(return_rate.sort_values(ascending=False))