import sys
import pandas as pd

print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"A_parameter": [1, 2], "B_parameter": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_month_{sys.argv[1]}.parquet")
print(f"hello pipeline, month {month}")

