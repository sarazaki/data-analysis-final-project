import pandas as pd

# 1. Load and prepare data
# تحميل وتجهيز البيانات

def load_data():
    df = pd.read_csv(
        r'C:\Users\zbookg6\data_analysi\data-analysis-final-project\data\processed\fordgobike-tripdataFor201902_cleaned.csv'
    )

# Mapping for weekends to make labels clearer
# تحويل قيم الويك إيند لأسماء واضحة في الرسم

    df['day_type'] = df['weekend_flag'].map({0: 'Weekday', 1: 'Weekend'})
    return df

