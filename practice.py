import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print(df.head())

print(df.groupby(pd.cut(df['Fare'], bins=[0, 10, 30, 100, 600]))['Survived'].mean())

