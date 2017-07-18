## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

riders = bikes[bikes["cnt"] > 5000].shape[0]
prob_over_5000 = riders/bikes["cnt"].shape[0]


## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))

def compute_probability(N, k, p, q):
    term1 = (p ** k) * (q ** (N-k))
    term2 = math.factorial(N) / (math.factorial(k) * math.factorial(N - k))
    return (term1 * term2)

p = .39
q = 0.61

outcome_probs = [compute_probability(30, i, p, q) for i in outcome_counts]
print(len(outcome_probs))

## 5. Plotting the distribution ##

import matplotlib.pyplot as plt

# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, outcome_probs)
plt.show()

## 6. Simplifying the computation ##

import matplotlib.pyplot as plt
import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)

# Generate a binomial distribution, and then find the probabilities for each value in outcome_counts. Use N=30, and p=.39, as we're doing this for the bikesharing data.
dist = binom.pmf(outcome_counts, 30, 0.39)
plt.bar(outcome_counts, dist)
plt.show()

## 8. Computing the mean of a probability distribution ##

dist_mean = None
# Compute the mean for the bikesharing data, where N = 30, and p = .39 
N = 30
p = .39
dist_mean = N * p 

## 9. Computing the standard deviation ##

dist_stdev = None
import math
# Compute the standard deviation of a probability distribution. This helps us find how much the actual values will vary from the mean when we take a sample.
N = 30
p = .39
q = 1 - .39

dist_stdev = math.sqrt(N * p * q)


## 10. A different plot ##

# Enter your answer here.
from scipy.stats import binom

outcome_counts = linspace(0,10,11)
outcome_probs = binom.pmf(outcome_counts,10,0.39)
plt.bar(outcome_counts, outcome_probs)
plt.show()

outcome_counts = linspace(0,100,101)
outcome_probs = binom.pmf(outcome_counts,100,0.39)
plt.bar(outcome_counts, outcome_probs)
plt.show()


## 11. The normal distribution ##

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = scipy.linspace(0,100,101)

# Create a probability mass function along the outcome_counts.
outcome_probs = binom.pmf(outcome_counts,100,0.39)

# Plot a line, not a bar chart.
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 12. Cumulative density function ##

outcome_counts = linspace(0,30,31)
# Create a cumulative distribution where N = 30 and p = .39  and generate a line plot of the distribution.
outcome_probs = binom.cdf(outcome_counts,30,0.39)
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 14. Faster way to calculate likelihood ##

from scipy.stats import binom

left_16 = None
right_16 = None

# The sum of all the probabilities to the left of k, including k.
k = 16
N = 30
p = 0.39

left_16 = binom.cdf(k, 30, 0.39)
right_16 = 1 - left_16