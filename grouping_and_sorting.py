import pandas as pd

'''groupby() to replicate the value_counts() function''' 
tips = pd.read_csv('tips.csv')
print(tips.head(),'\n')
print(tips.groupby('tip')['tip'].count(),'\n')


'''groupby() function to calculate the mean tip of males and females'''
print(tips.groupby('tip').apply(lambda df: df.total_bill.iloc[0], include_groups=False),'\n\n')     #include group must be false to avoid error


'''groupwise analysis for wine reviews'''
reviews = pd.read_csv('winemag-data-130k-v2.csv')
print(reviews.head())
print('\n')
#prints the titles of the first wine in every winery
print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0], include_groups=False))
print('\n')
#prints the data of the wine with highest points in each country's each province
print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()], include_groups=False))
print('\n')
#prints the length, minimum and maximum prices of the groups sorted by country
print(reviews.groupby(['country']).price.agg([len, 'min', 'max']))
print('\n')
#makes a df which is grouped by country and province and then prints the no of descriptions in that data frame
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)
print('\n')