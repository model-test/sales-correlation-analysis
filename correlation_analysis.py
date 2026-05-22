import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("data/sales_data.xlsx")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Convert returned columns to lowercase for consistency
df["returned"] = df["returned"].str.strip().str.lower()

# Convert order_date (Excel serial date)
df["order_date"] = pd.to_datetime(df["order_date"], origin="1899-12-30", unit="D")

#print(df.head())
#print(f"\nShape:\n{df.shape}")
#print(f"\nColumns:\n{df.columns.tolist()}")

# Columns being investigated for correlation
numeric_cols = ["revenue", "profit", "profit_margin_pct"]

# Calculate correlation matrix
correlation_matrix = df[numeric_cols].corr()

print(correlation_matrix)


# Scatter Plot: Revenue vs Profit
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='revenue', y='profit')
plt.title('Revenue vs Profit')
plt.xlabel('Revenue')
plt.ylabel('Profit')
plt.grid(True, alpha=0.3)
plt.savefig('plots/revenue_vs_profit.png')
plt.show()

# Scatter plot: Revenue vs Profit Margin
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='revenue', y='profit_margin_pct')
plt.title('Revenue vs Profit Margin %')
plt.xlabel('Revenue')
plt.ylabel('Profit Margin (%)')
plt.grid(True, alpha=0.3)
plt.savefig('plots/revenue_vs_profit_margin.png')
plt.show()

# Summary
print("\n=== Correlation Analysis Summary ===")
print("Revenue vs Profit correlation:", correlation_matrix.loc['revenue', 'profit'].round(3))
print("Revenue vs Profit Margin correlation:", correlation_matrix.loc['revenue', 'profit_margin_pct'].round(3))
print("\nKey Business Insight:")
print("- High revenue strongly predicts higher absolute profit.")
print("- However, high revenue does NOT guarantee high profit margins.")
