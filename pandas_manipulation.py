#Indexing

dataframe[col_label][row_label]

dataframe.col_label[row_label]

dataframe[[col1, col2]] #returns a dataframe with subselected labels

#It is more efficient and reusable to use accessors

df.loc[row_label, col_label]

df.iloc[row_nbr, col_nbr]

#Slicing

#A column is actually a series, a onne-dimensional array with a labeled index

