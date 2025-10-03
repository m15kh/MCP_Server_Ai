import pandas as pd
# Read the CSV
df = pd.read_csv("sample.csv")
# Save as Parquet
df.to_parquet("sample.parquet", index=False)