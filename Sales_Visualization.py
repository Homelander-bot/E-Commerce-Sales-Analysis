import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/storage/emulated/0/Download/E-commerce sales.csv")

# Monthly Sales Visualization
monthly_sales = df.groupby("Month")["Total Price"].sum()
plt.figure(figsize=(10, 5))

ax = plt.gca()
ax.set_facecolor("black")
plt.gcf().set_facecolor("black")

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    color="blue",
    marker="o",
    linewidth=2
)
plt.title(
    "Monthly Sales Analysis",
    color="white",
    fontsize=16,
    fontweight="bold"
)
plt.xlabel("Month", color="white")
plt.ylabel("Sales (₹)", color="white")

plt.xticks(range(1, 13), color="white")
plt.yticks(color="white")

plt.grid(True, linestyle="--", alpha=0.3)

plt.tight_layout()
plt.show()


sales_by_category = df.groupby("Category")["Total Price"].sum()
plt.figure(figsize=(9, 5))
ax = plt.gca()
ax.set_facecolor("black")
plt.gcf().set_facecolor("black")
plt.bar(
    sales_by_category.index,
    sales_by_category.values,
    color="blue"
)
plt.title(
    "Sales by Category",
    color="white",
    fontsize=16,
    fontweight="bold"
)
plt.xlabel("Category", color="white")
plt.ylabel("Sales (₹)", color="white")
plt.xticks(color="white")
plt.yticks(color="white")
for i, value in enumerate(sales_by_category.values):
    plt.text(
        i,
        value,
        f"₹{value:,}",
        ha="center",
        va="bottom",
        color="white",
        fontweight="bold"
    )
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)
plt.tight_layout()
plt.show()

# Calculate sales by product
sales_by_product = df.groupby("Product Name")["Total Price"].sum()

# Sort from highest to lowest
sales_by_product = sales_by_product.sort_values(ascending=False)

plt.figure(figsize=(10, 6))

ax = plt.gca()
ax.set_facecolor("black")
plt.gcf().set_facecolor("black")

# Bar chart
plt.bar(
    sales_by_product.index,
    sales_by_product.values,
    color="blue"
)

plt.title(
    "Sales by Product",
    color="white",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Product", color="white")
plt.ylabel("Sales (₹)", color="white")

plt.xticks(rotation=30, color="white")
plt.yticks(color="white")

# Values above bars
for i, value in enumerate(sales_by_product.values):
    plt.text(
        i,
        value,
        f"₹{value:,}",
        ha="center",
        va="bottom",
        color="white",
        fontsize=9
    )

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig(
    "/storage/emulated/0/Documents/monthly_sales.png",
    dpi=300,
    facecolor="black",
    bbox_inches="tight"
)
plt.show()

# Calculate sales by region
sales_by_region = df.groupby("Region")["Total Price"].sum()

# Sort highest to lowest
sales_by_region = sales_by_region.sort_values(ascending=False)

plt.figure(figsize=(9, 5))

ax = plt.gca()
ax.set_facecolor("black")
plt.gcf().set_facecolor("black")

# Bar chart
plt.bar(
    sales_by_region.index,
    sales_by_region.values,
    color="blue"
)

plt.title(
    "Sales by Region",
    color="white",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Region", color="white")
plt.ylabel("Sales (₹)", color="white")

plt.xticks(color="white")
plt.yticks(color="white")

# Values above bars
for i, value in enumerate(sales_by_region.values):
    plt.text(
        i,
        value,
        f"₹{value:,}",
        ha="center",
        va="bottom",
        color="white",
        fontweight="bold"
    )

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig(
    "/storage/emulated/0/Documents/monthly_sales.png",
    dpi=300,
    facecolor="black",
    bbox_inches="tight"
)
plt.show()

import matplotlib.pyplot as plt

# Calculate sales by gender
sales_by_gender = df.groupby("Gender")["Total Price"].sum()

plt.figure(figsize=(8, 5))

ax = plt.gca()
ax.set_facecolor("black")
plt.gcf().set_facecolor("black")

# Bar chart
plt.bar(
    sales_by_gender.index,
    sales_by_gender.values,
    color="blue"
)

plt.title(
    "Sales by Gender",
    color="white",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Gender", color="white")
plt.ylabel("Sales (₹)", color="white")

plt.xticks(color="white")
plt.yticks(color="white")

# Values above bars
for i, value in enumerate(sales_by_gender.values):
    plt.text(
        i,
        value,
        f"₹{value:,}",
        ha="center",
        va="bottom",
        color="white",
        fontweight="bold"
    )

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig(
    "/storage/emulated/0/Documents/monthly_sales.png",
    dpi=300,
    facecolor="black",
    bbox_inches="tight"
)
plt.show()

import matplotlib.pyplot as plt

# Calculate sales by age group
sales_by_age = df.groupby(
    "Age Group",
    observed=True
)["Total Price"].sum()

# Keep age groups in their natural order
age_order = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56-65",
    "66-75"
]

sales_by_age = sales_by_age.reindex(age_order)

plt.figure(figsize=(10, 5))

ax = plt.gca()
ax.set_facecolor("black")
plt.gcf().set_facecolor("black")

# Bar chart
plt.bar(
    sales_by_age.index,
    sales_by_age.values,
    color="blue"
)

plt.title(
    "Sales by Age Group",
    color="white",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Age Group", color="white")
plt.ylabel("Sales (₹)", color="white")

plt.xticks(color="white")
plt.yticks(color="white")

# Add values above bars
for i, value in enumerate(sales_by_age.values):
    plt.text(
        i,
        value,
        f"₹{value:,}",
        ha="center",
        va="bottom",
        color="white",
        fontweight="bold"
    )

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig(
    "/storage/emulated/0/Documents/monthly_sales.png",
    dpi=300,
    facecolor="black",
    bbox_inches="tight"
)
plt.show()

import matplotlib.pyplot as plt

# Count orders by shipping status
orders_by_shipping = df["Shipping Status"].value_counts()

plt.figure(figsize=(9, 5))

ax = plt.gca()
ax.set_facecolor("black")
plt.gcf().set_facecolor("black")

# Bar chart
plt.bar(
    orders_by_shipping.index,
    orders_by_shipping.values,
    color="blue"
)

plt.title(
    "Orders by Shipping Status",
    color="white",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Shipping Status", color="white")
plt.ylabel("Number of Orders", color="white")

plt.xticks(color="white")
plt.yticks(color="white")

# Add values above bars
for i, value in enumerate(orders_by_shipping.values):
    plt.text(
        i,
        value,
        str(value),
        ha="center",
        va="bottom",
        color="white",
        fontweight="bold"
    )

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig(
    "/storage/emulated/0/Documents/monthly_sales.png",
    dpi=300,
    facecolor="black",
    bbox_inches="tight"
)
plt.show()

import matplotlib.pyplot as plt

# Total orders for each product
total_orders = df["Product Name"].value_counts()

# Returned orders for each product
returned_orders = (
    df[df["Shipping Status"] == "Returned"]["Product Name"]
    .value_counts()
)

# Calculate return rate
return_rate = (
    returned_orders
    .div(total_orders)
    .fillna(0)
    * 100
).round(2)

# Sort highest to lowest
return_rate = return_rate.sort_values(ascending=False)

plt.figure(figsize=(10, 6))

ax = plt.gca()
ax.set_facecolor("black")
plt.gcf().set_facecolor("black")

# Blue bars
plt.bar(
    return_rate.index,
    return_rate.values,
    color="blue"
)

plt.title(
    "Return Rate by Product",
    color="white",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Product", color="white")
plt.ylabel("Return Rate (%)", color="white")

plt.xticks(rotation=30, color="white")
plt.yticks(color="white")

# Add percentage above bars
for i, value in enumerate(return_rate.values):
    plt.text(
        i,
        value,
        f"{value:.2f}%",
        ha="center",
        va="bottom",
        color="white",
        fontweight="bold"
    )

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig(
    "/storage/emulated/0/Documents/monthly_sales.png",
    dpi=300,
    facecolor="black",
    bbox_inches="tight"
)
plt.show()