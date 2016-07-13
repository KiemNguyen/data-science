## 1. Introduction ##

import pandas as pd
titanic_survival = pd.read_csv("titanic_survival.csv")

## 2. Finding the Missing Data ##

age = titanic_survival["age"]
print(age.loc[10:20])
age_is_null = pd.isnull(age)
age_null_true = age[age_is_null]
age_null_count = len(age_null_true)
print(age_null_count)

## 3. Whats the big deal with missing data? ##

age_is_null = pd.isnull(titanic_survival["age"])
#Create a vector that only contains values from the "age" column that aren't NaN
good_ages = titanic_survival["age"][age_is_null == False]

correct_mean_age = sum(good_ages) / len(good_ages)

## 4. Easier Ways to Do Math ##

correct_mean_age = titanic_survival["age"].mean()

correct_mean_fare = titanic_survival["fare"].mean()

## 5. Calculating Summary Statistics ##

passenger_classes = [1, 2, 3]
fares_by_class = {}
for item in passenger_classes: 
    pclass_rows = titanic_survival[titanic_survival["pclass"] == item]
    new_fare_column = pclass_rows["fare"]
    mean_result = new_fare_column.mean()
    fares_by_class[item] = mean_result

print(fares_by_class)

## 6. Making Pivot Tables ##

passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived")
passenger_age = titanic_survival.pivot_table(index="pclass", values="age")
print(passenger_age)

## 7. More Complex Pivot Tables ##

import numpy as np
port_stats = titanic_survival.pivot_table(index="embarked", values=["fare", "survived"], aggfunc=np.sum)
print(port_stats)

## 8. Drop Missing Values ##

drop_na_rows = titanic_survival.dropna(axis=0)
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0, subset=["age", "sex"])

## 9. Using iloc to Access Rows by Position ##

# We have already sorted new_titanic_survival by age
first_five_rows = new_titanic_survival.iloc[0:5]

first_ten_rows = new_titanic_survival.iloc[0:10]
row_position_fifth = new_titanic_survival.iloc[4]
row_index_25 = new_titanic_survival.loc[25]