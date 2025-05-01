-- Choose the year
DROP TABLE IF EXISTS #Choose_Year;
SELECT *
INTO #Choose_Year
FROM ['Retail Order']
WHERE YEAR([Order Date]) = 2016

-- Orders from year 2016
DROP TABLE IF EXISTS #Year_2016;
SELECT
	[Customer ID],
	[Order Date],
	[Sales],
	FORMAT([Order Date], 'yyyy-MM-01' ) OrderMonth
INTO #Year_2016
FROM #Choose_Year

-- First purchase month (cohort)
DROP TABLE IF EXISTS #Customer_Cohort;
SELECT 
	[Customer ID],
	FORMAT(MIN([Order Date]), 'yyyy-MM-01' ) AS CohortMonth
INTO #Customer_Cohort
FROM #Year_2016
GROUP BY [Customer ID];

-- Calculate cohort index
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

-- Unique customers per cohort
DROP TABLE IF EXISTS #Cohort_Customer;
SELECT 
	CohortMonth,
	OrderMonth,
	CohortIndex,
	COUNT(DISTINCT [Customer ID]) AS CustomerCount
INTO #Cohort_Customer
FROM #Cohort_Index
GROUP BY CohortMonth, OrderMonth, CohortIndex;

SELECT * FROM #Cohort_Customer

-- Total sales per cohort
DROP TABLE IF EXISTS #Cohort_Sales;
SELECT 
	CohortMonth,
	OrderMonth,
	CohortIndex,
	SUM([Sales]) AS TotalSales
INTO #Cohort_Sales
FROM #Cohort_Index
GROUP BY CohortMonth, OrderMonth, CohortIndex;

SELECT * FROM #Cohort_Sales