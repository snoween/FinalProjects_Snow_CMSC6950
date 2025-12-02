import pandas as pd

def calculate_bollinger_bands(series, window=20, num_std_dev=2):
    """
    Task 2: Calculate Bollinger Bands (Middle, Upper, Lower).
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a Pandas Series")

    middle_band = series.rolling(window=window).mean()
    std_dev = series.rolling(window=window).std()
    
    upper_band = middle_band + (std_dev * num_std_dev)
    lower_band = middle_band - (std_dev * num_std_dev)
    
    return pd.DataFrame({
        'Middle': middle_band,
        'Upper': upper_band,
        'Lower': lower_band
    })

def detect_extreme_values(df, price_col='Close', upper_col='Upper', lower_col='Lower'):
    """
    Task 3: Identify meaningful extreme values (outside the Bollinger Bands).
    """

    extremes = df[
        (df[price_col] > df[upper_col]) | 
        (df[price_col] < df[lower_col])
    ]
    return extremes

def calculate_sma(series, window):
    """Calculate Simple Moving Average (SMA)."""
    return series.rolling(window=window).mean()