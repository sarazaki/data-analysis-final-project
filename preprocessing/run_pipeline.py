from pipeline import BikeSharePipeline

raw_path = "C:/Users/Test/Desktop/DataAnalysisFinal/data-analysis-final-project/data/raw/fordgobike-tripdataFor201902.csv"

output_path = "C:/Users/Test/Desktop/DataAnalysisFinal/data-analysis-final-project/data/processed/fordgobike-tripdataFor201902_cleaned.csv"

pipeline = BikeSharePipeline(raw_path)

pipeline.load_data() \
        .clean_data() \
        .engineer_features() \
        .encode_and_scale()

df_cleaned = pipeline.get_data()

df_cleaned.to_csv(output_path, index=False)

print("Cleaned file saved successfully.")
