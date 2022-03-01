import pandas as pd

data = pd.read_csv("ufc.csv")
data[['cidade','pais']] = data.pop('local').str.split(",",n=1, expand=True)
print(data)
print(data['pais'].value_counts())
print(data['idade'].value_counts())