## 2. Calculating differences ##

female_diff = (10771 - 16280.5) / 16280.5
male_diff = (21790 - 16280.5) / 16280.5

## 3. Updating the formula ##

female_diff = (10771 - 16280.5) ** 2 / 16280.5
male_diff = (21790 - 16280.5) ** 2 / 16280.5

gender_chisq = male_diff + female_diff

## 4. Generating a distribution ##

import numpy as np
import matplotlib.pyplot as plt

chi_squared_values = []
for i in range(1000):
    sequence = np.random.random(32561,)
    sequence[sequence < 0.5] = 0
    sequence[sequence >= 0.5] = 1
    
    male_count = len(sequence[sequence == 0])
    female_count = len(sequence[sequence == 1])
    
    male_diff = (male_count - 16280.5) ** 2 / 16280.5
    female_diff = (female_count - 16280.5) ** 2 / 16280.5
    
    male_female_diff = male_diff + female_diff
    chi_squared_values.append(male_female_diff)

print(chi_squared_values)
plt.hist(chi_squared_values)
plt.show()

## 6. Smaller samples ##

female_diff = (107.71 - 162.805) ** 2 / 162.805
male_diff = (217.90 - 162.805) ** 2 / 162.805

gender_chisq = male_diff + female_diff

## 7. Sampling distribution equality ##

import numpy as np
import matplotlib.pyplot as plt

chi_squared_values = []

for i in range(1000):
    sequence = numpy.random.random(300,)
    # For each of the numbers, if it is less than .5, replace it with 0, otherwise replace it with 1.
    sequence[sequence < 0.5] = 0
    sequence[sequence >= 0.5] = 1
    
    # Count up how many times 0 occurs (Male frequency), and how many times 1 occurs (Female frequency).
    male_count = len(sequence[sequence == 0])
    female_count = len(sequence[sequence == 1])
    
    #Compute male_diff by subtracting the expected Male count (150) from the observed Male count, squaring  it, and dividing by the expected Male count.
    male_diff = (male_count - 150) ** 2 / 150
    female_diff = (female_count - 150) ** 2 / 150
    male_female_diff = male_diff + female_diff
    chi_squared_values.append(male_female_diff)
    
plt.hist(chi_squared_values)
plt.show()
    
    

## 9. Increasing degrees of freedom ##

diffs = []
observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

for i, j in enumerate(observed):
    exp = expected[i]
    diff = (j - exp) ** 2 / exp
    diffs.append(diff)
race_chisq = sum(diffs)


## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]
chisquare_value, race_pvalue = chisquare(observed, expected)