import pytest
import pandas as pd
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.analysis_function import calculate_bollinger_bands

def test_bollinger_bands_logic():
    data = pd.Series([10]*5 + [20]*5)       # Create fake data: 5 days with price 10, 5 days with price 20
    bands = calculate_bollinger_bands(data, window=5, num_std_dev=2)        # Calculate with a 5-day window
    
    assert bands['Middle'].iloc[4] == 10.0
    assert bands['Upper'].iloc[4] == 10.0
    assert bands['Middle'].iloc[9] == 20.0

def test_input_validation():
    with pytest.raises(TypeError):
        calculate_bollinger_bands([1, 2, 3])