Stock Market Analysis and Predictive Modeling

This project analyzes historical stock data for 10 companies to uncover trends, visualize patterns, and build predictive models to forecast future stock prices. It also includes backtesting strategies to evaluate potential trading performance.

Features
Data Collection: Automated fetching of stock data using the Alpha Vantage API.
Exploratory Data Analysis (EDA): Visualizations of stock trends, volatility, and correlations.
Feature Engineering: Calculated indicators like moving averages, RSI, and Bollinger Bands.
Predictive Modeling: Implemented regression models and LSTM for stock price forecasting.
Backtesting: Evaluated trading strategies like Moving Average Crossover.
Interactive Dashboard: Visualized insights and predictions using Streamlit.

Technologies Used
Programming Language: Python
Libraries:
Data Analysis: pandas, numpy
Visualization: matplotlib, seaborn, plotly
Machine Learning: scikit-learn, keras
API Integration: alpha_vantage
Dashboard: streamlit

Project Workflow
Data Collection: Used the Alpha Vantage API to fetch daily historical data for 10 stocks.
Saved the data in .csv format for further analysis.
EDA: Visualized trends in stock prices and trading volumes.
Analyzed correlations between stocks to identify market relationships.
Feature Engineering:Created features like moving averages (10, 50, 200-day), RSI, Bollinger Bands, and daily returns.
Predictive Modeling:Implemented linear regression and LSTM models for price forecasting.
Evaluated model performance using RMSE and accuracy metrics.
Backtesting:Simulated trading strategies to evaluate their profitability compared to a "Buy and Hold" approach.
Dashboard:Developed an interactive dashboard using Streamlit to showcase trends, indicators, and predictions.

Installation
Follow these steps to run the project:

Clone the Repository:
git clone https://github.com/tanzimozer/stock_market_analysis.git
cd stock_market_analysis

Install Dependencies: Install the required Python libraries using:
pip install -r requirements.txt

Run the Scripts:
Data Collection: Fetch stock data using:
python scripts/data_fetch.py
Dashboard: Launch the Streamlit dashboard:
streamlit run dashboard/app.py

Visualizations
Example Insights:
Stock Price Trends:

Correlation Heatmap:

Model Predictions:

Results
Predictive Models:
LSTM achieved an RMSE of X% for price forecasting.
Regression models predicted price movements with Y% accuracy.
Backtesting Strategies:
Moving Average Crossover outperformed "Buy and Hold" with a Z% return.
Future Improvements
Real-time data integration for live predictions.
Expanding analysis to additional stocks or indices.
Incorporating sentiment analysis from news or social media.
Acknowledgements
Alpha Vantage API for providing historical stock data.
Libraries like pandas, scikit-learn, and keras for enabling robust analysis and modeling.

