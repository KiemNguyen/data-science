## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])
most_bars_country = flags["name"][flags["bars"].idxmax()]


pop_sort = flags.sort_values("population", ascending=[0])
highest_population_country = pop_sort["name"].iloc[0]

## 2. Calculating probability ##

total_countries = flags.shape[0]
orange_flag = flags[flags["orange"] == 1]
orange_probability = len(orange_flag) / total_countries

stripe_flag = flags[flags["stripes"] > 1]
stripe_probability = len(stripe_flag) / total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5

ten_heads = .5 ** 10

hundred_heads = .5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
red = flags[flags["red"]==1].shape[0]
total = flags.shape[0]

three_red = red/total * (red-1)/(total-1) * (red-2)/(total-2)

## 5. Disjunctive probability ##

start = 1
end = 18000

def count_divisible(start, end, div):
    divisible = 0
    for i in range(start, end + 1):
        if i % div == 0:
            divisible += 1
    return divisible

hundred_prob = count_divisible(start, end, 100) / 18000
seventy_prob = count_divisible(start, end, 70) / 18000

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None

red = flags[flags["red"]==1]
orange = flags[flags["orange"]==1]
red_orange = flags[flags["red"]==1][flags["orange"]==1]

red_or_orange = (red.shape[0]/flags.shape[0] + orange.shape[0]/flags.shape[0]) - red_orange.shape[0]/flags.shape[0]

stripes = flags[flags["stripes"]>0]
bars = flags[flags["bars"]>0]
stripes_bars = flags[(flags["stripes"] > 0) & (flags["bars"]>0)]

stripes_or_bars = (stripes.shape[0]/flags.shape[0] + bars.shape[0]/flags.shape[0]) - stripes_bars.shape[0]/flags.shape[0]

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None

three_flips = 1/2 * 1/2 * 1/2

heads_or = 1 - three_flips