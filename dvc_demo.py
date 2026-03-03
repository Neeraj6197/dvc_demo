import pandas as pd
import os

#create a directory in data folder
os.makedirs("data", exist_ok=True)

#create a dataframe
sample_data = {
    "Name": ["Adam", "Bob", "Charlie"],
    "Car": ["Audi", "BMW", "Mercedes"]
}

df = pd.DataFrame(sample_data)

#save the dataframe
df.to_csv("data/abc_data.csv", index=False)
print("Data ingested successfully!")










# #adding a new row
# idx = len(df.index)
# df.loc[idx] = {"name":"David",
#                 "age":38,
#                 "car":"Dodge"}

