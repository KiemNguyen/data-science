## 2. Introduction to the data ##

import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
print(dc_listings[:0])

## 4. Euclidean distance ##

import numpy as np

# Calculate the Euclidean distance between our living space, which can accommodate 3 people, and the first living space in the dc_listings Dataframe

our_acc_value = 3
first_living_space_value = dc_listings.iloc[0]["accommodates"]

first_distance = np.abs(first_living_space_value - our_acc_value)
print(first_distance)

## 5. Calculate distance for all observations ##

import numpy as np

# Calculate the distance between each value in the accommodates column from dc_listings and the value 3 (Our listing accommodates)
our_acc_value = 3
dc_listings['distance'] = dc_listings['accommodates'].apply(lambda x: np.abs(x - our_acc_value))
print(dc_listings['distance'].value_counts())


## 6. Randomizing, and sorting ##

import numpy as np
np.random.seed(1)

# Randomize the order of the rows in dc_listings
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
dc_listings = dc_listings.sort_values("distance")
print(dc_listings.iloc[0:10]["price"])

## 7. Average price ##

# Normalize the price column
stripped_commas = dc_listings["price"].str.replace(",", "")
stripped_dollar_sign = stripped_commas.str.replace("$", "")

# Convert the new Series object containing the cleaned values to the float datatype and assign back to the price column in dc_listings
dc_listings["price"] = stripped_dollar_sign.astype(float)
mean_price = dc_listings.iloc[0:5]["price"].mean()
print(mean_price)

## 8. Function to make predictions ##

import numpy as np

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(new_listing):
    temp_df = dc_listings.copy()
    # Calculate the distance between each value in the accommodates column and the new_listing value that was passed in
    temp_df["distance"] = temp_df["accommodates"].apply(lambda x: np.abs(x - new_listing))
    # Sort temp_df by the distance column
    temp_df = temp_df.sort_values("distance")
    nearest_neighbors = temp_df.iloc[0:5]["price"]
    predicted_price = nearest_neighbors.mean()
    return(predicted_price)

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)