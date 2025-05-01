# Cohort Analysis for Customer Retention

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

## Cohort Analysis

Cohort Analysis groups customers based on their first purchase month, while the Cohort Index represents the number of months since that initial purchase, allowing businesses to track customer behavior over time.

```sql
DROP TABLE IF EXISTS #Cohort_Index;
SELECT 
	Y.[Customer ID],
	Y.[Sales],
	Y.OrderMonth,
	C.CohortMonth,
	DATEDIFF(MONTH, CAST(C.CohortMonth AS DATE), CAST(Y.[OrderMonth] AS DATE)) + 1 AS CohortIndex
INTO #Cohort_Index
FROM #Year_2016 Y
JOIN #Customer_Cohort C ON Y.[Customer ID] = C.[Customer ID];
```

**Customer Cohort Table** using SQL and Power BI

![Ảnh chụp màn hình 2025-05-01 180113](https://github.com/user-attachments/assets/b31b1de7-f8dc-4d10-be98-006fe2b58811)

**Sales Cohort Table** using SQL and Power BI

![Ảnh chụp màn hình 2025-05-01 180145](https://github.com/user-attachments/assets/ac83d6f6-5803-4af5-bdd2-c16cd006f083)

```python
def month_diff(column):
    return df_store[column].dt.month

OrderMonth = month_diff('OrderMonth')
CohortMonth = month_diff('CohortMonth')
month_diff = OrderMonth - CohortMonth

df_store['CohortIndex'] = month_diff + 1
```

**Customer Cohort Table** using Python

![Figure_1](https://github.com/user-attachments/assets/4c912b07-470b-4bfc-9a62-aa29072b96d6)

**Sales Cohort Table** using Python

![Figure_2](https://github.com/user-attachments/assets/952b2153-4e39-45dc-9a43-0b9daf555550)

## Application

- Track retention: Measure how many customers return after their first month.
- Sales drop-off: Observe when cohorts begin losing value.
- Lifecycle targeting: Apply lifecycle-based campaigns for re-engagement.

## Recommendations

- There is a steep drop in customer count after the first month across all cohorts, suggesting poor early retention.

→ Improve onboarding and early engagement. Launch a welcome campaign that includes helpful content, time-limited discounts, and personalized product suggestions in the first 30 days. This will help convert one-time buyers into repeat customers.

- Cohorts acquired between April and July maintain better retention and contribute higher revenue over time compared to others.

→ Analyze what drove better performance in these months-campaign type, product focus, or seasonal behavior—and replicate those strategies during other periods.

- Even when customer numbers shrink, some cohorts (e.g., 2016-04) sustain high revenue-indicating a small, loyal, high-value customer base.

→ Develop a loyalty or VIP program. Identify high spenders and reward them with exclusive access, early product launches, or loyalty perks to maximize their lifetime value and advocacy.

## Limitations

- Based on historical data (e.g., 2016), future behavior may differ.
- External impacts (e.g., seasonality, trends) are not modeled.
- The cohort index assumes fixed month intervals and may miss intra-month dynamics.

---

If you find this project useful, feel free to ⭐. Your support will be my super motivation ❤️.

---

## References

- [Cohort Analysis Base on Customer Retention/Revenue using SQL & Power BI | RINEZ](https://www.youtube.com/watch?v=y2g8J_A8VIM&t=789s)
- [Cohort Analysis Base on Customer Retention/Revenue using Python | RINEZ](https://www.youtube.com/watch?v=-MYoiJEVlUY&t=23s)

  ---

📌 **Author:** Nguyễn Hoàng Gia Phúc  

📧 **Contact:** nguyenhoanggiaphucwork@gmail.com

🔗 **LinkedIn:** [Nguyen Hoang Gia Phuc](https://www.linkedin.com/in/nguyenhoanggiaphuc)
