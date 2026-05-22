# Sales Correlation Analysis

**Analysis of the relationship between Revenue, Profit, and Profit Margins** in a retail sales dataset. This project investigates whether high-revenue products also deliver high profits and strong margins, or if there are important trade-offs.

## Project Overview
This analysis explores correlations between key financial metrics to understand product performance and potential risks.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- openpyxl

## Key Insights
- Revenue and Profit have a very strong positive correlation (0.971).
- Revenue and Profit Margin % show almost no correlation (-0.028).
- High revenue does **not** guarantee high profit margins.

## Visualizations
![Revenue vs Profit](plots/revenue_vs_profit.png)
![Revenue vs Profit Margin](plots/revenue_vs_profit_margin.png)

## Actionable Recommendations
1. Evaluate profit margins alongside revenue growth.
2. Closely monitor high-revenue, low-margin products.
3. Consider promoting products with both strong revenue and healthy margins.

## Limitations & Future Work
- Synthetic dataset.
- Correlation does not imply causation.
- **Next**: Add category/region breakdowns and interactive dashboard.

## How to Run
```bash
pip install -r requirements.txt
python correlation_analysis.py
