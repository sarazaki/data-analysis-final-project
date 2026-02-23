import pandas as pd

def load_data():
    path = "C:/Users/Test/Desktop/DataAnalysisFinal/data-analysis-final-project/data/processed/fordgobike-tripdataFor201902_cleaned.csv"
    df = pd.read_csv(path)

    if 'weekend_flag' in df.columns:
        df['day_type'] = df['weekend_flag'].map({0: 'Weekday', 1: 'Weekend'})
    
    return df