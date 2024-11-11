import pandas as pd

df = pd.read_csv('./tips.csv')
print(df.head(), '\n\n')

#pandas has many functions which restructure data in a useful way. some examples are shown below

print(df.tip.describe(),'\n\n')    #describe generates high level summary of the attributes of a given column. it is type aware.
print(df.day.describe(),'\n\n')    #shows that describe function is type specific

#you can use attributes shown by the describe function as individual functions too:
print('mean tip =',df.tip.mean())
print('days in the day column =',df.day.unique())
print('No of times that the days occur:\n',df.day.value_counts(),'\n')

#MAPPING
tips_mean = df.tip.mean()
mapped = df.tip.map(lambda p:p-tips_mean)
print(mapped)

#the same thing can be done by simpler method that pandas provides, which are faster as well.
print(df.tip - df.tip.mean())

