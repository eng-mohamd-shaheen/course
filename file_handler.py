import pandas as pd

df = pd.read_csv("addresses.csv", header=None)
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

print(df)