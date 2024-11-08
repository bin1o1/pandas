import pandas as pd
tips = pd.read_csv('./tips.csv')
print('\nThe sample data is:\n')
print(tips.head())
print(
      '\nIn Python, we can access the property of an object by accessing it as an attribute. \
A book object, for example, might have a title property, which we can access by calling book.title. \
Columns in a pandas DataFrame work in much the same way.\n'
)
print(tips.tip)
print(
    '\nIf we have a Python dictionary, we can access its values using the indexing ([]) operator. We can do the same with columns in a DataFrame:\n'
)
print(tips['tip'])
print(
    '\nPandas has its own accessing operators as well : loc(non-index based) and iloc(index based). Both loc and iloc are row first, column second. This is the opposite of python indexing operators\n'
)
print(
    "\nThis means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns. To get a column with iloc, we can do the following:\n"
)
print(tips.iloc[:,0])
print(
    '\nTo select the first three entries:\n'
)
print(tips.iloc[:3, 0])
print(
    '\nIt is also possible to pass a list.\n'
)
print(tips.iloc[[1,2,4], :],'\n\n')
print(tips[1:2][0:4],'\n\n')
print("You cant do print(tips[:]['4']) as it returns a key error, as there are no rows named 4")
print(
    '\n\nTo select the last five elements of the db:\n\n'
)
print(tips[-5:])
print(
    '\n\n*****LABEL BASED SELECTION*****\n\n'
)
print(tips.loc[:, ['tip','total_bill']] )

'''
When choosing or transitioning between loc and iloc, there is one "gotcha" worth keeping in mind, which is that the two methods use slightly different indexing schemes.
iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, 
meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

Why the change? Remember that loc can index any stdlib type: strings, for example. If we have a DataFrame with index values Apples, ..., Potatoes, ..., 
and we want to select "all the alphabetical fruit choices between Apples and Potatoes", then it's a lot more convenient to index df.loc['Apples':'Potatoes'] 
than it is to index something like df.loc['Apples', 'Potatoet'] (t coming after s in the alphabet).
'''

print(
    '\n\n***MANIPULATING THE INDEX***\n\n'
)
print(
    'The set_index() method can be used to do the job. Here is what happens when we set_index to the title field:'
)
print(tips.set_index('tip'))

print(
    '\n\n***CONDITIONAL SELECTION***\n\n'
)
print(
    'If the sex is Female'
)
print(tips.sex == 'Female')
print(
    '\nThis result can then be used inside of loc to select the relevant data:'
)
print(tips.loc[tips.sex == 'Female'])
print(
    'If the sex is Female and the tip is more than 2'
)
print(tips.loc[(tips.sex == 'Female') & (tips.tip>2)])
print(
    '''\n\nPandas comes with a few built-in conditional selectors, two of which we will highlight here.
The first is isin. isin is lets you select data whose value "is in" a list of values\n\n'''
)
print(tips.loc[tips.day.isin(['Sun','Fri', 'Sat'])])
print(
    '''\n\nThe second is isnull (and its companion notnull). 
These methods let you highlight values which are (or are not) empty (NaN).\n\n
eg: reviews.loc[reviews.price.notnull()]'''
)
print('\n\n***ASSIGNING DATA***')
tips['tip']=1
print(tips)
tips['tip'] = range(0, len(tips['tip']))
print(tips)