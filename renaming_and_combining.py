import pandas as pd
reviews = pd.read_csv('winemag-data-130k-v2.csv')
#The changes are not permanent and should be stores in a variable
'''Renames the columns'''
print(reviews.rename({'points':'score'}))
'''Renames the index'''
df = reviews.rename(index={0:'score'})
print(df)
'''Renames the index's name attribute'''
print(reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns'))