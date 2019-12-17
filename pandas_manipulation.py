#Indexing

dataframe[col_label][row_label]

dataframe.col_label[row_label]

dataframe[[col1, col2]] #returns a dataframe with subselected labels

#It is more efficient and reusable to use accessors

df.loc[row_label, col_label]

df.iloc[row_nbr, col_nbr]

#Slicing

#A column is actually a series, a one-dimensional array with a labeled index

dataframe.loc[] #labels (or lists of labels)

dataframe.iloc[] #index  (or list of indexes)

#Filtering

boolean_array = dataframe['column'] > int

dataframe.loc[boolean_array]

dataframe.dropna(how='any'/'all') #remove rows where any/all of these two columns contains missing data.

dataframe.dropna(thresh=1000, axis='columns') #drops columns with more thatn 1000 missing values

#Transforming Dataframes

dataframe.apply() #apply an arbitrary Python function to every element.

dataframe['column'].map(dictionary) #transform values according to a Python dictionary look-up

#apply and map are not efficient

