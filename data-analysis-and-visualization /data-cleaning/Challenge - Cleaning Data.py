## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()

true_avengers = avengers[avengers["Year"] > 1960]

## 5. Consolidating Deaths ##

def calculate_death(row):
    columns = ["Death1", "Death2", "Death3", "Death4", "Death5"]
    death_count = 0
    
    for column in columns:
        death = row[column]
        if pd.isnull(death) or death == 'NO':
            continue
        elif death == 'YES':
            death_count += 1
    return death_count

true_avengers["Deaths"] = true_avengers.apply(calculate_death, axis=1)
print(true_avengers["Deaths"])

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()
# Calculate the number of rows where Years since joining is accurate

years_diff = 2015 - true_avengers["Year"]

correct_joined_year = true_avengers[true_avengers["Years since joining"] == years_diff]

joined_accuracy_count = len(correct_joined_year)
