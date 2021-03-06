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

#Indexes

#Indexes are inmutable (you can, however, update the entire )

#Hierarchical indexing

df.setindex[col1, col2]

df.sort_index()

#accessors (loc/iloc) now can take a tuple of indexes or a single index as parameters for slicing

# Look up data for NY in month 1
sales.loc[('NY', 1), :]

# Look up data for CA and TX in month 2
sales.loc[(['CA', 'TX'], 2), :]

# Access the inner month index and look up data for all states in month 2: all_month2
sales.loc[(slice(None), 2), :]

#Pivoting

dataframe.pivot(columns=, values=, index=) #if values is not specified, all remainig columns are usad as values. 'Columns' refers to column index.

#Stacking/Unstacking

#Stack: thiner and longer

#Unstack: wider and shorter

df.stack/unstack(level = lvl_int/lvl_label)

df.swaplevels(lvl1, lvl2) #swap index levels. Might require sort_index

#Pivoting tables

df.pivot_table(columns=, values=, index=, aggfunc=) #when index/column pairs have non-unique values (default aggfunc is average)
                                                    #"see all of your variables as a function of two other variables"
                                                    # margins=True computes totals

#Grouping data

df.groupby('column') #groups of rows, using distinct values from the 'column' column.
                     #can also use Series, if they have same index as df.

series.unique() #Returns categorical (unique) values. Can be obtained with the 'astype('type')' methods.

df.agg([aggmethod1, aggmethod2]/ dict{column : method}) #agregates columns. Aggregation: Series -> Single value

df[columns].transform(function)

#you can apply a .transform() method after grouping to apply a function to groups of data independently.. Transformation: Series -> Conforming series.
#Example: z-score. Difference from mean expressed in units of std. (zscore +- 3 means outlier)

#MERGING

df.copy() #creates copy of df

df.reindex([new_index]) #creates a new dataframe with the same data, but using 'new_index' as index. If a label from the new_index is not present, it is created with NaN values.

#Arithmetic

df.divide(series, axis=)

df.pct_change() #for each value: (current value - previous value) / previous value

df.add(df, fill_value=0) # '+' operator yields NaN when indices are not present in all Dataframes.

#Appending/Concatenating 

s1.append(s2) #rows of df2 go below df1. #Maintains indexes. Needs reset_index().

pd.concat([s1, s2, s3]) #can concatenate vertical or horizontally. Can use ignore_index to avoid repeated indices. 
                        #keys=[] creates multi-index
                        #can specify join='inner'/'outer' (default)

#Merging

#Merging extends concat, making it possible to align rows using multiple columns.

pd.merge(df1, df2, on=[column1, column2], suffixes=[suf1, suf2], left_on='df1column', right_on='df2column', how='')

df1.join(df2) #left join (default) on index (default)

pd.merge_ordered(df1, df2) #outer join by default.

pd.merge_asof() #similar to a left-join except that we match on nearest key rather than equal keys. 
                #only rows from the right DataFrame whose 'on' column values are less than the left value will be kept.
  


