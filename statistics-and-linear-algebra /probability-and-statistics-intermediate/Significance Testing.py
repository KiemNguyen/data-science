## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)

mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)

plt.hist(weight_lost_a)
plt.show()

plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a

print(mean_difference)

## 5. Permutation test ##

import numpy as np
import matplotlib.pyplot as plt

mean_difference = 2.52
print(all_values)
mean_differences = []

for i in range(1000):
    group_a = []
    group_b = []
    for value in all_values:
        random_val = np.random.rand()
        if random_val >= 0.5:
            group_a.append(value)
        else:
            group_b.append(value)
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)
    
plt.hist(mean_differences)
plt.show()

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}

for i in mean_differences:
    if sampling_distribution.get(i, False):
        # If in the dictionary, grab the value, increment by 1, reassign.
        val  = sampling_distribution.get(i)
        inc = val + 1
        sampling_distribution[i] = inc
    else:
         # If not in the dictionary, assign `1` as the value to that key.
        sampling_distribution[i] = 1
        
print(sampling_distribution)

## 8. P value ##

import numpy as np

frequencies = []
for sp in sampling_distribution.keys():
    if sp > 2.52:
        frequencies.append(sampling_distribution[sp])
        
p_value = np.sum(frequencies)/1000 

# Since the p value of 0 is less than the threshold we set of 0.05, we conclude that the difference in weight lost can't be attributed to random chance alone. We therefore reject the null hypothesis and accept the alternative hypothesis
        