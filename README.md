# FinalProjects_Snow_CMSC6950

Student name: Thi Tuyet Nhi Nguyen

Student ID: 202398785


# Statistical Analysis and Extreme Value Detection in Financial Time-Series: A Case Study of Apple Inc.

## Project Overview
This project focuses on the processing and analysis of historical stock data for **Apple Inc. (AAPL)**. The goal is to identify meaningful extreme values and market trends using statistical methods, specifically **Bollinger Bands** and **Simple Moving Averages (SMA)**.

The analysis is performed on a time-series dataset containing over 1,200 data points (5 years of daily OHLCV data).

## Data Source
The data is sourced from **Yahoo Finance** (an original citable resource) using the `yfinance` Python library.
- **Ticker:** AAPL
- **Period:** Daily data from 2020 to 2025.
- **Attributes:** Open, High, Low, Close, Volume.

## Methodology
1. Bollinger Bands (Meaningful Function): A function calculate_bollinger_bands was developed to compute volatility bands (20-day SMA ± 2 standard deviations).

2. Extreme Value Detection: "Extreme days" are defined as days where the closing price falls outside the upper or lower Bollinger Bands.

3. Sensitivity Analysis: The project explores how the number of extreme days changes when the standard deviation threshold varies (1.5, 2.0, and 2.5 SD).

4. Trend Analysis: Long-term trends are identified using the interaction between 50-day and 200-day Simple Moving Averages (Golden Cross/Death Cross).

## Project Structure
The repository is organized as follows:

```text
├── data/                   # Contains the raw CSV data (auto-downloaded)
├── figures/                # Output directory for the 8 generated figures
├── src/                    # Source code for analysis logic
│   ├── __init__.py
│   ├── analysis_functions.py   # Core logic (Bollinger Bands, SMA, Extreme detection)
│   └── data_loader.py          # Data retrieval and cleaning
├── test_analysis.py        # Unit tests for the analysis functions
├── main.py                 # Main script to reproduce all figures
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

**Setup Instructions:**

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/snoween/FinalProjects_Snow_CMSC6950.git
    cd FinalProjects_Snow_CMSC6950
    ```
2. Ensure you have Python 3.8 or higher installed.

3. Install the required packages (once `requirements.txt` is available):
    ```bash
    pip install -r requirements.txt
    ```

### Running the Main File

To execute the primary script, open a terminal in the root directory of this repository and use the following command (replace `main.py` with the actual main file name if different):

```bash
python main.py
```

- Ensure that any required input files are present in the appropriate directories before running the script.
- Command-line arguments, if required, will be described in individual project documentation.

## Acknowledgments
- Any third-party libraries and data sources used are acknowledged within individual project documentation.

