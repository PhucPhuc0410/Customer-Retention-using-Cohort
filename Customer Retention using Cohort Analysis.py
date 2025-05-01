import pandas as pd
import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns

# Import data
file_path = 'D:/The Analyst Challenge/Supply Chain & Sales Datasets.xls'
df_store = pd.read_excel(file_path)

df_store.info()

# Change order date to datetime (if needed)
df_store['Order Date'] = pd.to_datetime(df_store['Order Date'])
df_store['Year'] = df_store['Order Date'].dt.year

# Choose the year
print("Available years:", df_store['Year'].unique())
year_select = int(input("Enter the year for analyzing: "))
df_store = df_store.loc[df_store['Year'] == year_select]

# Check null
df_store[['Customer ID', 'Order Date', 'Sales']].isnull().sum()

# Choose columns
df_customer = df_store[['Customer ID', 'Order Date', 'Sales']]
df_customer.info()

# Check number of customer
df_customer['Customer ID'].nunique()
df_customer['Customer ID'].value_counts().head()

# Order Month Calculation
df_store['OrderMonth'] = df_store['Order Date'].dt.to_period('M').dt.to_timestamp()

#Cohort Month Calculation
cohort = df_store.groupby('Customer ID')['OrderMonth'].min()
df_store['CohortMonth'] = df_store['Customer ID'].map(cohort)

# Cohort Index Calculation
def month_diff(column):
    return df_store[column].dt.month

OrderMonth = month_diff('OrderMonth')
CohortMonth = month_diff('CohortMonth')
month_diff = OrderMonth - CohortMonth

df_store['CohortIndex'] = month_diff + 1

# Unique customers per cohort
cohort_customer = df_store.groupby(
    ['CohortMonth', 'OrderMonth', 'CohortIndex']
)['Customer ID'].nunique().reset_index(name='CustomerCount')

print("Customer Cohort Table:")
print(cohort_customer.head())

# Total sales per cohort
cohort_sales = df_store.groupby(
    ['CohortMonth', 'OrderMonth', 'CohortIndex']
)['Sales'].sum().reset_index(name='TotalSales')

print("Sales Cohort Table:")
print(cohort_sales.head())

# Visualizing
cohort_pivot = cohort_customer.pivot(index='CohortMonth', columns='CohortIndex', values='CustomerCount')
sales_pivot = cohort_sales.pivot(index='CohortMonth', columns='CohortIndex', values='TotalSales')

cohort_pivot.index = cohort_pivot.index.strftime('%Y-%m')
sales_pivot.index = sales_pivot.index.strftime('%Y-%m')

plt.figure(figsize=(12, 6))
sns.heatmap(cohort_pivot, annot=True, fmt='g', cmap='YlGnBu')
plt.title(f'Customer Cohort Table ({year_select})')
plt.xlabel('Cohort Index')
plt.ylabel('Cohort Month')
plt.show()

plt.figure(figsize=(12, 6))
sns.heatmap(sales_pivot, annot=True, fmt='.0f', cmap='Oranges')
plt.title(f'Sales Cohort Table ({year_select})')
plt.xlabel('Cohort Index')
plt.ylabel('Cohort Month')
plt.show()