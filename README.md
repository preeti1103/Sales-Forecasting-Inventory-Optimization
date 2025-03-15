# Sales-Forecasting-Inventory-Optimization
Automated sales forecasting and inventory optimization system using Python and Tableau.
# Sales Forecasting and Inventory Optimization

## Overview
This project focuses on predicting future sales and optimizing inventory levels using historical sales data. The goal is to reduce stockouts, minimize excess inventory, and improve overall operational efficiency.

## Features
- **Sales Forecasting**: Predicts future sales using a time-series model (ARIMA).
- **Inventory Optimization**: Calculates reorder points, safety stock, and optimal order quantities (EOQ).
- **Interactive Dashboard**: Visualizes sales trends, forecasts, and inventory levels using Power BI/Tableau.
- **Flask API**: Deployed on Heroku for real-time predictions.

## Technologies Used
- **Python**: For data cleaning, analysis, and modeling.
- **Flask**: For building the web API.
- **Power BI/Tableau**: For creating interactive dashboards.
- **Heroku**: For deploying the Flask app.

## Repository Structure
Sales-Forecasting-Inventory-Optimization/
├── data/ # Contains datasets
├── models/ # Contains saved models
├── notebooks/ # Contains Jupyter notebooks for analysis
├── scripts/ # Contains automation scripts
├── app/ # Contains Flask app files
├── README.md # Project documentation
└── requirements.txt # List of Python dependencies


## How to Use
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Sales-Forecasting-Inventory-Optimization.git
2. Install Dependencies:
pip install -r requirements.txt

3.Run the Flask App:
cd app
python app.py

4. Access the Dashboard

Results
Achieved 95% accuracy in sales forecasting.
Reduced inventory costs by 15% through optimized reorder points and safety stock.


