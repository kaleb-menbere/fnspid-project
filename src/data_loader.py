import pandas as pd
import numpy as np
import re
from datetime import datetime

class FinancialDataLoader:
    """Load and clean financial news data with mixed date formats"""
    
    def __init__(self, data_path="../data/raw/"):
        self.data_path = data_path
        self.df = None
    
    def load_news_data(self, filename="raw_analyst_ratings.csv"):
        """Load and clean the main news dataset"""
        filepath = f"{self.data_path}/{filename}"
        self.df = pd.read_csv(filepath)
        print(f"✅ Loaded dataset shape: {self.df.shape}")
        return self.df
    
    def clean_dates(self):
        """Clean mixed date formats - your existing logic as a method"""
        if self.df is None:
            raise ValueError("No data loaded. Call load_news_data() first.")
        
        # Ensure 'date' is string type
        self.df['date'] = self.df['date'].astype(str)

        # Detect rows with timezone
        mask_tz = self.df['date'].str.contains(r"[+-]\d{2}:\d{2}", na=False)
        
        # Parse rows WITH timezone
        self.df.loc[mask_tz, 'date'] = pd.to_datetime(
            self.df.loc[mask_tz, 'date'], utc=True, errors='coerce'
        )
        
        # Parse rows WITHOUT timezone
        self.df.loc[~mask_tz, 'date'] = pd.to_datetime(
            self.df.loc[~mask_tz, 'date'], format="%Y-%m-%d %H:%M:%S", utc=True, errors='coerce'
        )
        
        # Final conversion
        self.df['date'] = pd.to_datetime(self.df['date'], utc=True, errors='coerce')
        
        print(f"✅ Date cleaning complete. NaT values: {self.df['date'].isna().sum()}")
        return self.df
    
    def extract_text_features(self):
        """Extract textual features from headlines"""
        self.df['headline_len_chars'] = self.df['headline'].astype(str).str.len()
        self.df['headline_len_words'] = self.df['headline'].astype(str).str.split().apply(len)
        return self.df
    
    def get_basic_stats(self):
        """Return basic dataset statistics"""
        if self.df is None:
            raise ValueError("No data loaded")
        
        stats = {
            'total_articles': len(self.df),
            'date_range': (self.df['date'].min(), self.df['date'].max()),
            'publishers_count': self.df['publisher'].nunique(),
            'stocks_count': self.df['stock'].nunique()
        }
        return stats