import pandas as pd

# შეცვალე ფაილის სახელი შესაბამისით!
df = pd.read_parquet("train-00000-of-00001 (1).parquet")
print(df.head())  # პირველი 5 ჩანაწერი

# ასევე შეგიძლია მეორე ფაილიც ასე წაიკითხო
df_test = pd.read_parquet("test-00000-of-00001.parquet")
print(df_test.head())
