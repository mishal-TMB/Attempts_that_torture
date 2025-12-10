import pandas as pd
t = pd.read_csv('titanic.csv')
#кол-во выживших
survived_count = t[t['Survived'] == 1].shape[0]
print(survived_count)
#%
survived_percent = survived_count / t.shape[0] * 100
print(f"{survived_percent:.2f}")
#вимены
women = t[t['Sex'] == 'female']
women_survived = women[women['Survived'] == 1].shape[0]
women_percent = women_survived / women.shape[0] * 100
print(f"{women_percent:.2f}")
#мен
men = t[t['Sex'] == 'male']
men_survived = men[men['Survived'] == 1].shape[0]
men_percent = men_survived / men.shape[0] * 100
print(f"{men_percent:.2f}")