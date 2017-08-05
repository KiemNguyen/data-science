## 2. Calculating expected values ##

males_over50k = (.241 * .669) * 32561
males_under50k = (.759 * .669) * 32561
females_over50k = (.241 * .331) * 32561
females_under50k = (.759 * .331) * 32561


## 3. Calculating chi-squared ##

observed = [6662, 1179, 15128, 9592]
expected = [5249.8, 2597.4, 16533.5, 8180.3]
values = []

for i, j in enumerate(observed):
    exp = expected[i]
    value = (exp - j) ** 2 /exp
    values.append(value)
    
chisq_gender_income = sum(values)


## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

observed = np.array([6662, 1179, 15128, 9592])
expected = np.array([5249.8, 2597.4, 16533.5, 8180.3])

chisq_value, pvalue_gender_income = chisquare(observed, expected)

## 5. Cross tables ##

import pandas

# Use a pandas.crosstab function to find the observed frequency counts

table = pandas.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding expected values ##

import numpy as np
import pandas
from scipy.stats import chi2_contingency

table = pandas.crosstab(income["sex"], [income["race"]])

# Calculate the pvalue for the sex and race columns of income
chisq_value, pvalue_gender_race, df, expected = chi2_contingency(table)