import pandas as pd

'''groupby() to replicate the value_counts() function''' 
print(f'\n\n******************groupby() to replicate the value_counts() function******************\n')
tips = pd.read_csv('tips.csv')
print(tips.groupby('tip')['tip'].count(),'\n')

'''groupby() function to calculate the mean tip of males and females'''
print('\n\n******************groupby() function to calculate the mean tip of males and females******************\n')
print(tips.groupby('tip').apply(lambda df: df.total_bill.iloc[0], include_groups=False),'\n\n')     #include group must be false to avoid error

'''groupwise analysis for wine reviews'''
reviews = pd.read_csv('winemag-data-130k-v2.csv')
print('\n\n******************groupwise analysis for wine reviews******************\n')
print(reviews.head())
print('\n')
#prints the titles of the first wine in every winery
print('\n\n******************the titles of the first wine in every winery******************\n')
print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0], include_groups=False))
print('\n')
#prints the data of the wine with highest points in each country's each province
print("\n\n******************data of the wine with highest points in each country's each province******************\n")
print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()], include_groups=False))
print('\n')
#prints the length, minimum and maximum prices of the groups sorted by country
print('\n\n******************length, minimum and maximum prices of the groups sorted by country******************\n')
print(reviews.groupby(['country']).price.agg([len, 'min', 'max']))
print('\n')
#makes a df which is grouped by country and province and then prints the no of descriptions in that data frame
print('\n\n******************df grouped by country and province and then prints the no of descriptions in that data frame******************\n')
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)
print('\n')
#creates a series whose index is taster_twitter_handle and value is number of reviews
print('\n\n******************series whose index is taster_twitter_handle and value is number of reviews******************\n')
reviews_written = reviews.groupby('taster_twitter_handle').size()
print(reviews_written,'\n')
#Series whose index is wine prices and whose values is the maximum number of points a wine costing that much was given in a review. Sort the values by price, ascending
print('\n\n******************Series whose index is wine prices and values is max no. of points of that wine (sorted by price)******************\n')
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
print(best_rating_per_price)
#DataFrame whose index is the variety category from the dataset and whose values are the min and max values
print('\n\n******************DataFrame whose index is the variety category from the dataset and whose values are the min and max values******************\n')
price_extremes = reviews.groupby('variety').price.agg(['min', 'max'])
print(price_extremes)
#df where varieties are sorted in descending order based on minimum price, then on maximum price (to break ties)
print('\n\n******************varieties are sorted in descending order based on minimum price, then on maximum price (to break ties)******************\n')
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
print(sorted_varieties)
#Series whose index is a MultiIndexof {country, variety} pairs.
print('\n\n******************Series whose index is a MultiIndexof {country, variety} pairs.******************\n')
country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending=False)
print(country_variety_counts)