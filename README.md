# Interactive Dashboard & KPI Visualizations

## Project Overview

This project is an interactive business dashboard developed using Python, Streamlit, Pandas, and Plotly. The dashboard analyzes the Global Superstore dataset and presents important sales, profit, quantity, order, and performance insights through interactive visualizations and KPI cards.

## Objectives

- Analyze sales and profit performance
- Create interactive KPI visualizations
- Provide filters for Year, Region, Category, and Segment
- Visualize monthly sales trends
- Analyze sales and profit by category
- Analyze sales by country
- Identify top-performing products
- Analyze profit by sub-category
- Provide interactive drill-down analysis
- Display filtered dataset records
- Allow users to download filtered data

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Excel
- VS Code

## Dataset

The project uses the Global Superstore dataset stored in:

`Global Superstore.xls`

The dataset contains sales, profit, quantity, customer, product, category, region, country, and order information.

## Dashboard Features

### KPI Cards

The dashboard displays:

- Total Sales
- Total Quantity
- Total Orders
- Average Order Value
- Profit Margin

### Filters

Users can interactively filter the dashboard using:

- Year
- Region
- Category
- Segment

### Visualizations

The dashboard contains:

- Monthly Sales Trend
- Sales and Profit by Category
- Sales by Country
- Top 10 Products by Sales
- Profit by Sub-Category

### Interactive Drill-Down

Users can analyze data at different time levels:

- Year
- Quarter
- Month

Users can also select a category and analyze its sub-category sales.

### Filtered Dataset

Users can:

- View the filtered dataset
- Download the filtered data as a CSV file

## Project Structure

```text
Interactive_Dashboard_KPI/
│
├── app.py
├── Global Superstore.xls
├── requirements.txt
├── README.md
├── Dashboard_Report.pdf
└── Interactive_Dashboard_KPI.pbix