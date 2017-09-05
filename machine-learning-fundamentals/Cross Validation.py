## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
   
shuffled_index = np.random.permutation(dc_listings.index)
dc_listings = dc_listings.reindex(shuffled_index)

split_one = dc_listings[0:1862]
split_two = dc_listings[1862:]

## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

# Train a k-nearest neighbors model using the default algorithm (auto) and the default number of neighbors (5)
knn = KNeighborsRegressor(n_neighbors=5)
# Uses the accommodates column from train_one for training
knn.fit(train_one[["accommodates"]], train_one["price"])
# Tests it on test_one.
predictions = knn.predict(test_one[["accommodates"]])
mse = mean_squared_error(predictions, test_one["price"])
iteration_one_rmse = mse ** (1/2)

# Train a k-nearest neighbors model using the default algorithm (auto) and the default number of neighbors (5)
knn = KNeighborsRegressor(n_neighbors=5)
# Use the accommodates column from train_two for training
knn.fit(train_two[["accommodates"]], train_two["price"])
# Test it on test_two
predictions = knn.predict(test_two[["accommodates"]])
mse = mean_squared_error(predictions, test_two[["price"]])
iteration_two_rmse = mse ** (1/2)

avg_rmse = np.mean([iteration_one_rmse, iteration_two_rmse])




## 3. K-Fold Cross Validation ##

dc_listings.set_value(dc_listings.index[0:744], "fold", 1)
dc_listings.set_value(dc_listings.index[744:1488], "fold", 2)
dc_listings.set_value(dc_listings.index[1488:2232], "fold", 3)
dc_listings.set_value(dc_listings.index[2232:2976], "fold", 4)
dc_listings.set_value(dc_listings.index[2976:3723], "fold", 5)

## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

# Training
train_one = dc_listings[dc_listings["fold"] != 1]
test_one = dc_listings[dc_listings["fold"] == 1]
knn = KNeighborsRegressor()
knn.fit(train_one[['accommodates']], train_one['price'])

# Predicting
labels = knn.predict(test_one[['accommodates']])
mse = mean_squared_error(labels, test_one['price'])
iteration_one_rmse = mse ** (1/2)

## 5. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]

def train_and_validate(df, folds):
    fold_rmses = []
    for fold in folds:
        # Training
        train = df[df["fold"] != fold]
        test = df[df["fold"] == fold]
        knn = KNeighborsRegressor()
        knn.fit(train[['accommodates']], train['price'])

        # Predicting
        labels = knn.predict(test[['accommodates']])
        mse = mean_squared_error(labels, test['price'])
        rmse = mse ** (1/2)
        fold_rmses.append(rmse)
    return fold_rmses
               
rmses = train_and_validate(dc_listings, fold_ids)
avg_rmse = np.mean(rmses)
               
print(rmses)
print(avg_rmse)

## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

import numpy as np
from sklearn.model_selection import cross_val_score, KFold
from sklearn.neighbors import KNeighborsRegressor

kf = KFold(5, shuffle=True, random_state=1)
mses = cross_val_score(KNeighborsRegressor(), dc_listings[["accommodates"]], dc_listings["price"], scoring="neg_mean_squared_error", cv = kf)
rmses = np.sqrt(np.abs(mses))
avg_rmse = np.mean(rmses)

## 7. Exploring Different K Values ##

from sklearn.model_selection import cross_val_score, KFold

num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="neg_mean_squared_error", cv=kf)
    rmses = np.sqrt(np.absolute(mses))
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))