## 1. Recap ##

import pandas as pd
import numpy as np
np.random.seed(1)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings.info()

## 2. Removing features ##

columns_remove = ["room_type", "city", "state", "latitude", "longitude", "zipcode", "host_response_rate", "host_acceptance_rate", "host_listings_count"]

# axis parameters is set to 1 so Pandas only drops across columns not rows
dc_listings = dc_listings.drop(columns_remove, axis = 1)

## 3. Handling missing values ##

dc_listings = dc_listings.drop(["cleaning_fee", "security_deposit"], axis=1)
dc_listings = dc_listings.dropna(axis=0)
dc_listings.isnull().sum()

## 4. Normalize columns ##

# Normalize columns to prevent any single column from having too much of an impact on the distance. Normalizing the values in each columns to the standard normal distribution (mean of 0, standard deviation of 1) preserves the distribution of the values in each column while aligning the scales.
normalized_listings = (dc_listings - dc_listings.mean()) / (dc_listings.std())
normalized_listings["price"] = dc_listings["price"]
normalized_listings.iloc[:3, :]

## 5. Euclidean distance for multivariate case ##

from scipy.spatial import distance

# Calculate the Euclidean distance using only the accommodates and bathrooms features between the first row and fifth row in normalized_listings using the distance.euclidean() function.

first_listing = normalized_listings.iloc[0][["accommodates", "bathrooms"]]
fifth_listing = normalized_listings.iloc[4][["accommodates", "bathrooms"]]

first_fifth_distance = distance.euclidean(first_listing, fifth_listing)

## 7. Fitting a model and making predictions ##

from sklearn.neighbors import KNeighborsRegressor

train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]

knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')

# Matrix-like object, containing just the 2 columns of interest from training set.
train_features = train_df[["accommodates", "bathrooms"]]

# List-like object, containing just the target column "price"
train_target = train_df["price"]

# Pass everything into the fit method
knn.fit(train_features, train_target)

# Call the predict method to make predictions on the accommodates and bathrooms columns from test_df
predictions = knn.predict(test_df[["accommodates", "bathrooms"]])

print(predictions)

## 8. Calculating MSE using Scikit-Learn ##

from sklearn.metrics import mean_squared_error

train_columns = ['accommodates', 'bathrooms']
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute', metric='euclidean')
knn.fit(train_df[train_columns], train_df['price'])
predictions = knn.predict(test_df[train_columns])

two_features_mse = mean_squared_error(test_df["price"], predictions)
two_features_rmse = two_features_mse ** (1/2)

## 9. Using more features ##

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')

knn.fit(train_df[features], train_df["price"])
four_predictions = knn.predict(test_df[features])

four_mse = mean_squared_error(test_df["price"], four_predictions)
four_rmse = four_mse ** (1/2)

## 10. Using all features ##

from sklearn.neighbors import KNeighborsRegressor

features = train_df.columns.tolist()
features.remove("price")

knn = KNeighborsRegressor(n_neighbors=5, algorithm="brute")
knn.fit(train_df[features], train_df["price"])

all_features_predictions = knn.predict(test_df[features])
all_features_mse = mean_squared_error(test_df["price"], all_features_predictions)
all_features_rmse = all_features_mse ** (1/2)

print(all_features_mse)
print(all_features_rmse)