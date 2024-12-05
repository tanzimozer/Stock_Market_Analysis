import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data using Yahoo Finance API.

    Parameters:
        ticker (str): Stock ticker symbol (e.g., 'AAPL').
        start_date (str): Start date in the format 'YYYY-MM-DD'.
        end_date (str): End date in the format 'YYYY-MM-DD'.

    Returns:
        DataFrame: Historical stock data.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Example usage:
if __name__ == "__main__":
    ticker = "AAPL"  # Replace with any stock ticker
    start_date = "2020-01-01"
    end_date = "2023-01-01"
    data = fetch_stock_data(ticker, start_date, end_date)
    print(data.head())  # Print first few rows of the data
