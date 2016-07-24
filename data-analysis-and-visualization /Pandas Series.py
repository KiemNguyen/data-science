## 1. Data Structures ##

import pandas as pd
fandango = pd.read_csv("fandango_score_comparison.csv")
fandango.head(2)

## 2. Integer Indexes ##

fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango['FILM']
print(series_film[0:5])

series_rt = fandango['RottenTomatoes']
print(series_rt[0:5])

## 3. Custom Indexes ##

# Import the Series object from pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values

series_custom = Series(rt_scores, film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]

## 4. Integer Index Preservation ##

series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]

fiveten = series_custom[5:10]
print(fiveten)