import pandas as pd

reviews = pd.read_csv('winemag-data-130k-v2.csv')

'''prints the data type(s) of the columns in the dataframe'''
print(reviews.dtypes)
print(reviews.winery.dtype)
'''is null gives boolean output for whether the data in the given column is null'''
print(reviews[pd.isnull(reviews.designation)])
'''fills nan values with the given argument'''
print(reviews.winery.fillna("unknown"))
'''replaces the value'''
print(reviews.winery.replace("Nicosia", "replaced value"))
