## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")
unique_regions = cars["origin"].unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)

dummy_years = pd.get_dummies(cars["year"], prefix="year")
cars = pd.concat([cars, dummy_years], axis=1)

cars = cars.drop("year", axis=1)
cars = cars.drop("cylinders", axis=1)
print(cars.head())

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]
train_row = int(cars.shape[0] * 0.7)

train = shuffled_cars.iloc[0:train_row]
test = shuffled_cars.iloc[train_row:]

print(train)

## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}
features = [i for i in shuffled_cars if i.startswith("cyl") or i.startswith("year")]

for val in unique_origins:
    X_train = train[features]
    y_train = train["origin"] == val
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    models[val] = model
    

## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)
for val in unique_origins:
    # Select the testing features
    X_test = test[features]
    # Compute probability of observation being in the origin.
    testing_probs[val] = models[val].predict_proba(X_test)[:,1]

## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis=1)
print(predicted_origins)