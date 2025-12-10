import pandas as pd
t = pd.read_csv('titanic.csv')
t['FamilySize'] = t['SibSp'] + t['Parch'] + 1
print(t.loc[887, 'FamilySize'])