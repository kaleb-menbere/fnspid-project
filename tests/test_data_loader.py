import pytest
import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.data_loader import FinancialDataLoader

class TestFinancialDataLoader:
    def test_initialization(self):
        loader = FinancialDataLoader()
        assert loader.data_path == "../data/raw/"
        assert loader.df is None
    
    def test_load_data(self):
        loader = FinancialDataLoader()
        # You would mock this in real implementation
        # df = loader.load_news_data("test_sample.csv")
        # assert df.shape[0] > 0
    
    def test_clean_dates_requires_loaded_data(self):
        loader = FinancialDataLoader()
        with pytest.raises(ValueError):
            loader.clean_dates()