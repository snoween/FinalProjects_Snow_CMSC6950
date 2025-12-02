import sys
import os
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import load_stock_data
from src.analysis_function import calculate_bollinger_bands, detect_extreme_values, calculate_sma

# Configuration
TICKER = 'AAPL'
START = '2020-01-01'
END = '2025-01-01'
FIGURES_DIR = 'figures'

if not os.path.exists(FIGURES_DIR):
    os.makedirs(FIGURES_DIR)

def main():
    df = load_stock_data(TICKER, START, END)
    
    # Calculate Bollinger Bands (Default 2 SD)
    bands = calculate_bollinger_bands(df['Close'], window=20, num_std_dev=2)
    df = df.join(bands)
    
    # Calculate SMAs
    df['SMA_50'] = calculate_sma(df['Close'], 50)
    df['SMA_200'] = calculate_sma(df['Close'], 200)
    
    df['Returns'] = df['Close'].pct_change()        # Calculate daily returns

    # Figure 1: Line Plot (Close Price)
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Close'], label='Close Price')
    plt.title(f'Figure 1: {TICKER} Historical Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{FIGURES_DIR}/fig1_close_price.png')
    plt.close()
    print("Saved Figure 1")

    # Figure 2: Bar Plot (Volume)
    plt.figure(figsize=(10, 5))
    plt.bar(df.index, df['Volume'], color='gray')
    plt.title(f'Figure 2: {TICKER} Trading Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.savefig(f'{FIGURES_DIR}/fig2_volume.png')
    plt.close()
    print("Saved Figure 2")

    # Figure 3: Candlestick (Last 6 months)
    df_recent = df.tail(120) 
    df_subset = df.tail(60).copy()
    
    plt.figure(figsize=(12, 6))
    up = df_subset[df_subset.Close >= df_subset.Open]
    down = df_subset[df_subset.Close < df_subset.Open]

    col1 = 'green'
    col2 = 'red'
    
    plt.vlines(up.index, up.Low, up.High, color=col1, linewidth=1)
    plt.vlines(down.index, down.Low, down.High, color=col2, linewidth=1)
    
    plt.vlines(up.index, up.Open, up.Close, color=col1, linewidth=6)
    plt.vlines(down.index, down.Open, down.Close, color=col2, linewidth=6)
    
    plt.title(f'Figure 3: {TICKER} Candlestick Chart (Last 60 Days) - Pure Matplotlib')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True, alpha=0.3)
    
    plt.savefig(f'{FIGURES_DIR}/fig3_candlestick.png')
    plt.close()
    print("Saved Figure 3")

    # Figure 4: Bollinger Bands Visualization
    plt.figure(figsize=(12, 6))
    plt.plot(df_recent.index, df_recent['Close'], label='Close', alpha=0.6)
    plt.plot(df_recent.index, df_recent['Upper'], label='Upper Band', linestyle='--', color='green')
    plt.plot(df_recent.index, df_recent['Lower'], label='Lower Band', linestyle='--', color='green')
    plt.fill_between(df_recent.index, df_recent['Upper'], df_recent['Lower'], color='green', alpha=0.1)
    plt.title(f'Figure 4: Bollinger Bands (20-day, 2-SD)')
    plt.legend()
    plt.savefig(f'{FIGURES_DIR}/fig4_bollinger_bands.png')
    plt.close()
    print("Saved Figure 4")

    # Figure 5: Extreme Values Scatter Plot
    extremes = detect_extreme_values(df)
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Close Price', alpha=0.5, color='gray')
    plt.scatter(extremes.index, extremes['Close'], color='red', label='Extreme Values', zorder=5)
    plt.title(f'Figure 5: Identified Extreme Values (Outside 2-SD Bands)')
    plt.legend()
    plt.savefig(f'{FIGURES_DIR}/fig5_extremes_scatter.png')
    plt.close()
    print("Saved Figure 5")

    # Figure 6: Returns Distribution (Histogram)
    plt.figure(figsize=(10, 6))
    plt.hist(df['Returns'].dropna(), bins=50, color='purple', alpha=0.7, edgecolor='black')
    plt.title('Figure 6: Distribution of Daily Returns (Fat Tails Check)')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.savefig(f'{FIGURES_DIR}/fig6_returns_hist.png')
    plt.close()
    print("Saved Figure 6")

    # Figure 7: Sensitivity Analysis (Bar Chart)
    sd_levels = [1.5, 2.0, 2.5]
    counts = []
    for sd in sd_levels:
        temp_bands = calculate_bollinger_bands(df['Close'], num_std_dev=sd)
        temp_df = df[['Close']].join(temp_bands)
        count = len(detect_extreme_values(temp_df))
        counts.append(count)
    
    plt.figure(figsize=(8, 6))
    plt.bar([str(x) for x in sd_levels], counts, color=['orange', 'red', 'darkred'])
    plt.title('Figure 7: Sensitivity Analysis - Extreme Days vs. SD Threshold')
    plt.xlabel('Standard Deviation Threshold')
    plt.ylabel('Number of Extreme Days')
    plt.savefig(f'{FIGURES_DIR}/fig7_sensitivity.png')
    plt.close()
    print("Saved Figure 7")

    # Figure 8: Trend Analysis (SMA 50 vs 200)
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Price', color='lightgray', alpha=0.5)
    plt.plot(df.index, df['SMA_50'], label='SMA 50 (Short-term)', color='blue')
    plt.plot(df.index, df['SMA_200'], label='SMA 200 (Long-term)', color='orange')
    plt.title('Figure 8: Trend Analysis (Golden/Death Cross)')
    plt.legend()
    plt.savefig(f'{FIGURES_DIR}/fig8_trend_sma.png')
    plt.close()
    print("Saved Figure 8")

if __name__ == "__main__":
    main()
