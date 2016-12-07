## 1. Introduction to Scales ##

car_speeds = [10,20,30,50,20]
earthquake_intensities = [2,7,4,5,8]

mean_car_speed = sum(car_speeds) / len(car_speeds)
mean_earthquake_intensities = sum(earthquake_intensities) / len(earthquake_intensities)

## 2. Discrete and Continuous Scales ##

day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]
cars_in_parking_lot = [5,6,4,2,1,7,8]

import matplotlib.pyplot as plt
plt.plot(day_numbers, snail_crawl_length)
plt.show()

plt.plot(day_numbers, cars_in_parking_lot)
plt.show()

## 3. Understanding Scale Starting Points ##

fahrenheit_degrees = [32, 64, 78, 102]
yearly_town_population = [100,102,103,110,105,120]

degrees_zero = [f + 459.67 for f in fahrenheit_degrees]
population_zero = yearly_town_population

## 4. Working With Ordinal Scales ##

# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]
survey_scale = ["none", "a few", "some", "a lot"]

# Assign a number to each survey response that corresponds with its position on the scale
survey_numbers = [survey_scale.index(response) for response in survey_responses]

# Compute the average value of all the survey responses
average_smoking = sum(survey_numbers) / len(survey_numbers)

## 5. Grouping Values with Categorical Scales ##

# Let's say that these lists are both columns in a matrix.  Index 0 is the first row in both, and so on.
gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]

# Compute the average savings for everyone who is "male".
male_saving_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "male"]
male_savings = sum(male_saving_list) / len(male_saving_list)
print(male_saving)

# Compute the average savings for everyone who is "female".
female_saving_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "female"]
female_savings = sum(female_saving_list) / len(female_saving_list)

print(female_saving)

## 6. Visualizing Counts with Frequency Histograms ##

# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]
survey_scale = ["none", "a few", "some", "a lot"]

# Assign a number to each survey response that corresponds with its position on the scale
survey_numbers = [survey_scale.index(response) for response in survey_responses]

# Compute the average value of all the survey responses
average_smoking = sum(survey_numbers) / len(survey_numbers)

## 7. Aggregating Values with Histogram Bins ##

# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]
survey_scale = ["none", "a few", "some", "a lot"]

# Assign a number to each survey response that corresponds with its position on the scale
survey_numbers = [survey_scale.index(response) for response in survey_responses]

# Compute the average value of all the survey responses
average_smoking = sum(survey_numbers) / len(survey_numbers)

## 8. Measuring Data Skew ##

# We've already loaded in some numpy arrays. We'll make some plots with them.
# The arrays contain student test scores that are on a 0-100 scale.
import matplotlib.pyplot as plt

# See how there's a long slope to the left?
# The data is concentrated in the right part of the distribution, but some people also scored poorly.
# This plot has a negative skew.
plt.hist(test_scores_negative)
plt.show()

# This plot has a long slope to the right.
# Most students did poorly, but a few did really well.
# This plot has a positive skew.
plt.hist(test_scores_positive)
plt.show()

# This plot has no skew either way. Most of the values are in the center, and there is no long slope either way.
# It is an unskewed distribution.
plt.hist(test_scores_normal)
plt.show()

# We can test how skewed a distribution is using the skew function.
# A positive value means positive skew, a negative value means negative skew, and close to zero means no skew.
from scipy.stats import skew
positive_skew = skew(test_scores_positive)
negative_skew = skew(test_scores_negative)
no_skew = skew(test_scores_normal)

## 9. Checking for Outliers with Kurtosis ##

# We've already loaded in some numpy arrays. We'll make some plots with them.
# The arrays contain student test scores that are on a 0-100 scale.
import matplotlib.pyplot as plt

# See how there's a long slope to the left?
# The data is concentrated in the right part of the distribution, but some people also scored poorly.
# This plot has a negative skew.
plt.hist(test_scores_negative)
plt.show()

# This plot has a long slope to the right.
# Most students did poorly, but a few did really well.
# This plot has a positive skew.
plt.hist(test_scores_positive)
plt.show()

# This plot has no skew either way. Most of the values are in the center, and there is no long slope either way.
# It is an unskewed distribution.
plt.hist(test_scores_normal)
plt.show()

# We can test how skewed a distribution is using the skew function.
# A positive value means positive skew, a negative value means negative skew, and close to zero means no skew.
from scipy.stats import skew
positive_skew = skew(test_scores_positive)
negative_skew = skew(test_scores_negative)
no_skew = skew(test_scores_normal)

## 10. Modality ##

# Let's plot the mean and median side-by-side in a negatively skewed distribution.
# Unfortunately, arrays don't have a nice median method, so we have to use a numpy function to compute it.
import numpy
import matplotlib.pyplot as plt

# Plot the histogram
plt.hist(test_scores_negative)
# Compute the median
median = numpy.median(test_scores_negative)

# Plot the median in blue (the color argument of "b" means blue)
plt.axvline(median, color="b")
# Plot the mean in red
plt.axvline(test_scores_negative.mean(), color="r")

# Notice how the median is further to the right than the mean.
# It's less sensitive to outliers, and isn't pulled to the left.
plt.show()

# Plot a histogram for test_scores_positive
plt.hist(test_scores_positive)
# Compute the median
median = numpy.median(test_scores_positive)

# Plot the median in blue
plt.axvline(median, color="b")
# Plot the mean in red
plt.axvline(test_scores_positive.mean(), color="r")

plt.show()

## 11. Measures of Central Tendency ##

# We've already loaded in some numpy arrays. We'll make some plots with them.
# The arrays contain student test scores that are on a 0-100 scale.
import matplotlib.pyplot as plt

# See how there's a long slope to the left?
# The data is concentrated in the right part of the distribution, but some people also scored poorly.
# This plot has a negative skew.
plt.hist(test_scores_negative)
plt.show()

# This plot has a long slope to the right.
# Most students did poorly, but a few did really well.
# This plot has a positive skew.
plt.hist(test_scores_positive)
plt.show()

# This plot has no skew either way. Most of the values are in the center, and there is no long slope either way.
# It is an unskewed distribution.
plt.hist(test_scores_normal)
plt.show()

# We can test how skewed a distribution is using the skew function.
# A positive value means positive skew, a negative value means negative skew, and close to zero means no skew.
from scipy.stats import skew
positive_skew = skew(test_scores_positive)
negative_skew = skew(test_scores_negative)
no_skew = skew(test_scores_normal)

## 12. Calcultaing the Median ##

import matplotlib.pyplot as plt

# This plot has one mode. It is unimodal.
plt.hist(test_scores_uni)
plt.show()

# This plot has two peaks. It is bimodal.
# This could happen if one group of students learned the material and another learned something else, for example.
plt.hist(test_scores_bi)
plt.show()

# More than one peak means that the plot is multimodal.
# We can't easily measure the modality of a plot, like we can with kurtosis or skew.
# Often, the best way to detect multimodality is to examine the plot visually.

# This plot has four peaks
plt.hist(test_scores_multi)
plt.show()

## 14. Removing Missing Data ##

# We've loaded the clean version of the data into the variable new_titanic_survival
import matplotlib.pyplot as plt
import numpy

plt.hist(new_titanic_survival["age"])

median_age = numpy.median(new_titanic_survival["age"])
mean_age = new_titanic_survival["age"].mean()

plt.axvline(median_age, color="b")
plt.axvline(mean_age, color="r")
plt.show()

## 15. Plotting Age ##

# We've loaded the clean version of the data into the variable new_titanic_survival
import matplotlib.pyplot as plt
import numpy

plt.hist(new_titanic_survival["age"])

median_age = numpy.median(new_titanic_survival["age"])
mean_age = new_titanic_survival["age"].mean()

plt.axvline(median_age, color="b")
plt.axvline(mean_age, color="r")
plt.show()

## 16. Calculating Indexes for Age ##

import numpy
from scipy.stats import skew
from scipy.stats import kurtosis

mean_age = new_titanic_survival["age"].mean()
median_age = numpy.median(new_titanic_survival["age"])
skew_age = skew(new_titanic_survival["age"])
kurtosis_age = kurtosis(new_titanic_survival["age"])