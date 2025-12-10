import pandas as pd
t = pd.read_csv('titanic.csv')
#всего пассажиров
a = t.shape[0]
print(a)
# не заполнен возраст
b = t['Age'].isna().sum()
print(b)