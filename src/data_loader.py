import os
import yfinance as yf
import pandas as pd

def load_stock_data(ticker, start_date, end_date, data_dir='data'):
    """
    Download stock data and clean up MultiIndex formatting issues.
    """
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    file_path = os.path.join(data_dir, f"{ticker}_{start_date}_{end_date}.csv")
    
    if os.path.exists(file_path):
        print(f"Reading data from file: {file_path}")

        # Important: header=[0, 1] tells pandas that the first two rows are headers
        try:
            df = pd.read_csv(file_path, index_col=0, parse_dates=True, header=[0, 1])
        except:
            df = pd.read_csv(file_path, index_col=0, parse_dates=True)
    else:
        print(f"Downloading new data from Yahoo Finance for {ticker}...")
        df = yf.download(ticker, start=start_date, end=end_date)
        df.to_csv(file_path)
        print(f"Saved file at {file_path}")

    # Clean MultiIndex if exists
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    
    target_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    
    available_cols = [c for c in df.columns if c in target_cols]
    df = df[available_cols]

    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df.dropna(inplace=True)
    
    if df.empty:
        print("Warning: Data is empty after cleaning!")
    
    return df