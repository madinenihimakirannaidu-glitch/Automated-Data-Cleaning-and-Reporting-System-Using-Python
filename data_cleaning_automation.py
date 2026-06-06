import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Online Sales Data.csv")

# Original info
print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

print("Cleaned Shape:", df.shape)

# Save cleaned data
df.to_csv("Cleaned_Online_Sales_Data.csv", index=False)

# Summary Report
report = df.describe(include='all')

with open("report.txt", "w") as f:
    f.write(str(report))

# Revenue by Region
region_sales = df.groupby("Region")["Total Revenue"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("region_report.png")

print("Automation Completed Successfully!")