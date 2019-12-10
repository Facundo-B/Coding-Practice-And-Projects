import pandas as pd

df = pd.read_csv('data.csv')

df[column_name].value_counts('value_name', dropna=False) #Counts appearances of every value in a given column. 'dropna = False' counts NaN values.

#Bar Plots for discrete, Histograms for continuous. Scatter for two numeric columns.

df.boxplot(column='column1, by='column2')

#-----------------------------------------------------------------------------------------------------------------------------------------

#Tidy Data Principles:

# Columns == Variables
# Rows == Observations
# Observational units form tables

#Melting: Takes a group of columns into a single column

pd.melt(dataframe, id_vars = [columns_not_to_melt], value_vars = [columns_to_melt], value_name='Name_for_Value_Column', var_name='Name_for_Variable_Column')

#Pivoting: Creates a new column for every unique value in a given column

pd.pivot_table(dataframe, index = [columns_not_to_pivot], columns = [columns_to_pivot], values = [values_to_use_when_pivoting], aggfunc=function_to_use_for_conflicts)

#python has a built-in .split(delim), which splits a strings into parts separated by "delim" (returns a list)

#-----------------------------------------------------------------------------------------------------------------------------------------

#Concatenating Data

pd.concat([dataframe1, dataframe2], ignore_index = True) #axis = 1 for column-wise concatenation.

import glob #for finding files based on patterns

glob.glob("*.csv")

#Merging Data (SQL join)

pd.merge(left = df1, right = df2, on = column, left_on = column_left, right_on =column_right) #left/right only if key column is not the same in both df's
