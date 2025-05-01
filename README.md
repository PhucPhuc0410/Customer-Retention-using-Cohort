# Customer-Retention-using-Cohort

---

## Overview

This project applies Cohort Analysis to track customer retention and sales behavior over time. By grouping customers based on their first purchase month (cohort), businesses can better understand retention rates, optimize marketing strategies, and improve lifetime value.
## Dataset

**Source:** `Supply Chain & Sales Datasets` from [The Analyst Challenge](https://www.linkedin.com/showcase/the-analyst-challenge/posts/?feedView=all)

## Tools Used

- **SQL Server Management Studio (SSMS)** for querying and data processing.
- **Python** for data extraction, processing, and visualization.
- **Matplotlib** & **Seaborn** for data visualization.

## Data Cleaning and Preparation

- Filter transactions in the target year (e.g., 2016).
- Identify first purchase month per customer to assign cohort groups.
- Calculate `CohortIndex` (difference in months between order and first purchase).

## ABC Analysis
ABC Analysis segments products based on their contribution to total revenue:

- **A**: Top 40% revenue contributors.
- **B**: Next 40% revenue contributors.
- **C**: Bottom 20% revenue contributors.

```sql
DROP TABLE IF EXISTS #Product_Sales;
SELECT 
    PRO.ProductKey,
    PRO.EnglishProductName,
    SUM(FACT.SalesAmount) AS Total_Sales_Amount,
    SUM(FACT.SalesAmount) / @Total_sales * 100 AS Percent_Revenue 
INTO #Product_Sales
FROM FactResellerSales FACT
JOIN DimProduct PRO 
ON FACT.ProductKey = PRO.ProductKey
GROUP BY PRO.ProductKey, PRO.EnglishProductName;
```

XYZ Analysis categorizes products based on sales consistency:

- **X**: Coefficient of Variation ≤ 10%.
- **Y**: 10% < Coefficient of Variation ≤ 25%.
- **Z**: Coefficient of Variation > 25%.

```sql
DROP TABLE IF EXISTS #XYZ_Analysis;
SELECT 
    PRO.ProductKey,
    PRO.EnglishProductName,
    AVG(PSPM.MonthlySales) AS Avg_Sales,
    STDEV(PSPM.MonthlySales) AS STDV_Sales,  
    CASE 
        WHEN AVG(PSPM.MonthlySales) = 0 THEN NULL 
        ELSE STDEV(PSPM.MonthlySales) * 100 / NULLIF(AVG(PSPM.MonthlySales), 0) 
    END AS Coefficient_Variation 
INTO #XYZ_Analysis
FROM #Product_Sales_Per_Month PSPM
JOIN DimProduct PRO 
ON PSPM.ProductKey = PRO.ProductKey
GROUP BY PRO.ProductKey, PRO.EnglishProductName;
```

## Application

![HHIG VOULUMN](https://github.com/user-attachments/assets/76424e2a-a17f-42bf-800f-b744253a76f1)

- Ensure availability of **high-volume, stable** (**AX**) products while adjusting stock for **highly fluctuating** (**BZ**, **CZ**) items.
- Promote and bundle **underperforming** products (**CZ**) with **high-revenue** items (**AX**, **AY**).
- Target price-sensitive customers with **stable** (**BX**, **CX**) products and implement dynamic pricing for **highly fluctuating** (**BZ**, **CZ**) items.

## Recommendations
- Focus on high-revenue (A) and low-variability (X) products.
- Adjust stock for (Z) category products.
- Ensure consistent availability of (AX, BX) products while dynamically managing (CZ) items.

## Limitations
- Analysis is based on historical data and may not predict future trends.
- External factors such as seasonality and market fluctuations are not considered.
- Regular updates are needed to maintain accuracy.

If you find this project useful, feel free to ⭐. Your support will be my super motivation ❤️.

---

## References

- [ABC XYZ Analysis in Inventory Management](https://abcsupplychain.com/abc-xyz-analysis/)
- [ABC XYZ Analysis for Inventory Management: Example in Excel (Full Tutorial)](https://www.youtube.com/watch?v=-GoYI746kEY)

  ---

📌 **Author:** Nguyễn Hoàng Gia Phúc  

📧 **Contact:** nguyenhoanggiaphucwork@gmail.com

🔗 **LinkedIn:** [Nguyen Hoang Gia Phuc](https://www.linkedin.com/in/nguyenhoanggiaphuc)
