import pandas as pd

#DataFrame
print('\n\nA DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.')
df = pd.DataFrame({'one':[1,1,1,1], 'two':[2,2,2,2]})
print(f'\n{df}')


print("\nThe 0,1,2,3 are called column index. They're as shown by default but can be changed as required:\n")
df = pd.DataFrame({'one':[1,1,1,1], 'two':[2,2,2,2]}, index=['a','b','c','d'])
print(df)


print('\nA Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:')
series = pd.Series([1,2,3,4,5])
print(f'\n{series}\n')
series = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(f'{series}\n')


print('\nWe can read a csv file in the following way:\n')
tips = pd.read_csv("./tips.csv")
print(tips)


print('\nWe can use the shape attribute to check how large the resulting DataFrame is:')
print(tips.shape)


print('\nWe can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:')
print(tips.head())


print('''\nThe pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify. 
For example, you can see in this dataset that the CSV file has a built-in index, which pandas did not pick up on automatically. 
To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.''')
tips = pd.read_csv("./tips.csv",index_col='tip')
print(f'\n{tips.head()}')