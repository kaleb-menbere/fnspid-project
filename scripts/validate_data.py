#!/usr/bin/env python3
"""
Data validation script for financial news analytics project
"""

import pandas as pd
import os
import sys

def validate_data_structure():
    """Validate the structure and quality of the dataset"""
    
    data_path = "../data/raw_analyst_ratings.csv"
    
    if not os.path.exists(data_path):
        print(f"❌ Data file not found: {data_path}")
        sys.exit(1)
    
    try:
        # Load data
        df = pd.read_csv(data_path)
        
        print("✅ Data file loaded successfully")
        print(f"📊 Dataset shape: {df.shape}")
        
        # Check required columns
        required_columns = ['headline', 'date', 'publisher']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"❌ Missing required columns: {missing_columns}")
            sys.exit(1)
        else:
            print("✅ All required columns present")
        
        # Check for null values
        null_counts = df[required_columns].isnull().sum()
        if null_counts.any():
            print("⚠️  Null values found:")
            for col, count in null_counts.items():
                if count > 0:
                    print(f"   - {col}: {count} nulls")
        else:
            print("✅ No null values in required columns")
        
        # Check date format
        try:
            pd.to_datetime(df['date'], errors='raise')
            print("✅ Date format is valid")
        except Exception as e:
            print(f"❌ Invalid date format: {e}")
            sys.exit(1)
        
        # Basic statistics
        print("\n📈 Basic Data Statistics:")
        print(f"   - Total articles: {len(df):,}")
        print(f"   - Unique publishers: {df['publisher'].nunique():,}")
        print(f"   - Date range: {df['date'].min()} to {df['date'].max()}")
        
        # Check headline length
        df['headline_length'] = df['headline'].str.len()
        avg_length = df['headline_length'].mean()
        print(f"   - Average headline length: {avg_length:.1f} characters")
        
        if avg_length < 10:
            print("⚠️  Warning: Very short average headline length")
        
        print("\n🎉 Data validation completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during data validation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    validate_data_structure()