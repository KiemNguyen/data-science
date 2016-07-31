## 1. Shared Indexes ##

import pandas as pd
fandango = pd.read_csv("fandango_score_comparison.csv")
print(fandango.head(2))
print(fandango.index)

## 2. Using Integer Indexes to Select Rows ##

fandango = pd.read_csv('fandango_score_comparison.csv')
first_row = 0
last_row = fandango.shape[0] - 1

first_last = fandango.iloc[[first_row, last_row]]
print(first_last)

## 3. Using Custom Indexes ##

fandango = pd.read_csv('fandango_score_comparison.csv')
fandango_films = fandango.set_index("FILM", drop=False)
print(fandango_films.index)