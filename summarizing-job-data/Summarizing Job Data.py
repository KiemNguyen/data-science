## 2. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv") 
print(all_ages.head(5))
print(recent_grads.head(5))

## 3. Summarizing Major Categories ##

import numpy as np

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

#aa_cat_counts = dict()
#rg_cat_counts = dict()

aa_cat_counts = all_ages.pivot_table(index = "Major_category", values = "Total", aggfunc = np.sum)
rg_cat_counts = recent_grads.pivot_table(index = "Major_category", values = "Total", aggfunc = np.sum)

print(aa_cat_counts)
print("")
print(rg_cat_counts)

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0

low_wage_jobs_sum = recent_grads['Low_wage_jobs'].sum()
recent_grads_sum = recent_grads['Total'].sum()

low_wage_percent = low_wage_jobs_sum / recent_grads_sum
print(low_wage_percent)
