import pandas
import numpy as np
import matplotlib.pyplot as plt

# Load the data into a DataFrame
df = pandas.read_csv('hits.csv')
by_user = df.groupby('user')

def avg_number_of_visits_per_user():
    rows = len(df.index)
    user_size = by_user['user'].size()
    cumsum_of_user_size = user_size.cumsum()
    avg_number_of_visits_per_user = cumsum_of_user_size.tail(1)/rows
    return round(avg_number_of_visits_per_user,10)
    
def avg_number_of_visits_per_user_with_condition():
    user_size = by_user['user'].size()
    # Create a new DataFrame from the Series category_mean 
    df = pandas.Series(user_size)
    df = df[df != 1] 
    rows = len(df.index)
    cumsum_of_user_size = df.cumsum()
    avg_number_of_visits_per_user_with_condition = cumsum_of_user_size.tail(1)/rows
    return round(avg_number_of_visits_per_user_with_condition,10)

def avg_categories_visited():
    rows = len(df.index)
    cumsum_of_category_mean = by_user['category'].mean().cumsum()
    avg_categories_visited = (cumsum_of_category_mean.tail(1)/rows)
    return round(avg_categories_visited,10)
    
def avg_categories_visited_with_condition1():
    category_size = by_user['category'].size()
    # Create a new DataFrame from the Series category_size with given condition that user visited more than one page
    pdf = pandas.Series(category_size)
    pdf = pdf[pdf != 1] 
    prows = len(pdf.index)
    cumsum_of_category_size = pdf.cumsum()
    avg_categories_visited_over_one_page = (cumsum_of_category_size.tail(1)/prows)
    return round(avg_categories_visited_over_one_page,10)

def avg_categories_visited_with_condition2():
    category_mean = by_user['category'].mean()
    # Create a new DataFrame from the Series category_mean with given condition that user visited more than one category
    ndf = pandas.Series(category_mean)
    ndf = ndf[ndf != 1.000000]
    new_rows = len(ndf.index)
    new_cumsum_of_category_mean = ndf.cumsum()
    avg_categories_visited_over_one_category = (new_cumsum_of_category_mean.tail(1)/new_rows)
    return round(avg_categories_visited_over_one_category,10)

print "Average number of visits per user is: ", avg_number_of_visits_per_user()
print ""
print "Average number of visits per user given they visited more than a single page is: ", avg_number_of_visits_per_user_with_condition()
print ""
print "Average number of categories visited per user is: ", avg_categories_visited()
print ""
print "Average number of categories visited per user given they visited more than a single page is: ", avg_categories_visited_with_condition1()
print ""
print "Average number of categories visited per user given they visited more than one category is: ", avg_categories_visited_with_condition2()