import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# Data Loading & Cleaning
# -------------------------

df = pd.read_excel("data/sales_data.xlsx")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Standardize returned column
df["returned"] = df["returned"].str.strip().str.lower()

# Convert Excel serial date
df["order_date"] = pd.to_datetime(df["order_date"], origin="1899-12-30", unit="D")

# -------------------------
# Correlation Analysis
# -------------------------

numeric_cols = ["revenue", "profit", "profit_margin_pct"]

correlation_matrix = df[numeric_cols].corr()

print("Correlation Matrix:")
print(correlation_matrix.round(3))

# -------------------------
# Visualizations
# -------------------------

# Revenue vs Profit
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='revenue', y='profit')
plt.title('Revenue vs Profit')
plt.xlabel('Revenue')
plt.ylabel('Profit')
plt.grid(True, alpha=0.3)
plt.savefig('plots/revenue_vs_profit.png')
plt.close()

# Revenue vs Profit Margin
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='revenue', y='profit_margin_pct')
plt.title('Revenue vs Profit Margin %')
plt.xlabel('Revenue')
plt.ylabel('Profit Margin (%)')
plt.grid(True, alpha=0.3)
plt.savefig('plots/revenue_vs_profit_margin.png')
plt.close()

# -------------------------
# Summary
# -------------------------

print("\n=== Correlation Analysis Summary ===")
print(f"Revenue vs Profit correlation: {correlation_matrix.loc['revenue', 'profit']:.3f}")
print(f"Revenue vs Profit Margin correlation: {correlation_matrix.loc['revenue', 'profit_margin_pct']:.3f}")

print("\nKey Business Insight:")
print("- High revenue strongly predicts higher absolute profit.")
print("- However, high revenue does NOT guarantee high profit margins.")
