import re
import pandas as pd

############################################
# Loading Data into Pandas

# Load a csv file
# https://github.com/KeithGalli/pandas/blob/master/pokemon_data.csv
dataframe = pd.read_csv('pokemon_data.csv')
print(dataframe, "\n")  # Prints all
print(dataframe.head(5), "\n")  # Prints 5 rows of the dataframe from the head
print(dataframe.tail(5), "\n")  # Prints 5 rows from the tail of the data frame

# Load from excel
# https://github.com/KeithGalli/pandas/blob/master/pokemon_data.xlsx
df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))

# Load from txt file
# https://github.com/KeithGalli/pandas/blob/master/pokemon_data.txt
df = pd.read_csv('pokemon_data.txt', delimiter='\t')
# print(df.head(5))


####### READING DATA IN PANDAS #########

# Read headers
print(dataframe.columns)  # Prints the name of each column

# Read each column - df['columnname']
print(dataframe['Name'])  # Prints the pokemons name
print(dataframe['Name'][0:5])  # Prints the first 5 column
print(dataframe[['Name', 'Generation']])  # Prints 2 Columns that is specified

# Read each row - iloc means integer location/ Returns series
print(dataframe.iloc[4])  # Prints row No.4
print(dataframe.iloc[1:4])  # Prints row 1-4 Including the column names

# Prints all row
# for index, row in dataframe.iterrows():
#	print(index, row)
#	print(index, row['Name']) #prints the name column

# Prints all row with the specified value (We use loc if we specify string)
print(df.loc[df['Type 1'] == 'Fire'])

# Read Specific Column [row,column]
print(df.iloc[2, 1])

# Read Specific Rows [[row1, row2]]
print(df.iloc[[1, 2]])

# Read specific rows and a single column
print(df.iloc[[1, 2], 1])

##########################################
# Sorting/Describing Data

# Describe a dataframe
print(df.describe())

# Sort values
print(df.sort_values('Name'))  # Prints it alphabetical
print(df.sort_values('Name', ascending=False))  # Prints in descending order
# This will print name in ascending order (1=True) & (0=False) - HP in
# descending order
print(df.sort_values(['Name', 'HP'], ascending=[1, 0]))

#########Making changes to the data##########

# Making a new column named 'Total' in the last column
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + \
    df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))
# Easier way - [:] means all column/row, [4:10] means 4th col to 9th column (10 is exclusive)
# Axis 1 is always horizontal, 0 is vertica
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head(5))

# Making a list from the column names
cols = list(df.columns)
print(cols)

# Adding the 'total' to a specific place
# 0:4 is # to Type 2(4 is HP and it is exclusive)
# Then adding -1 which is the 'Total', we need to make it a list if its only one
# Then add the remaining columns
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(5))

# OR DO THIS
col = [
    '#',
    'Name',
    'Type 1',
    'Type 2',
    'Total',
    'HP',
    'Attack',
    'Defense',
    'Sp. Atk',
    'Sp. Def',
    'Speed',
    'Generation',
    'Legendary']
df = df.reindex(columns=col)
print(df.head(5))

# Dropping a specific column
#df = df.drop(columns=['Total'])
print(df.head(4))


####Saving our Data (Exporting into desired format)####

# Save as csv
# df.to_csv('modified.csv')
# df.to_csv('modified.csv', index=False) #Saves without index

# Save as excel - need to install openpyxl
# df.to_excel('modified.xlsx',index=False)

# To text file
# df.to_csv('modified.txt', index=False, sep="\t") #Using tab as
# separator, you can also use commas

###########Filtering Data###########

# Filter data (2)
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

# Filter data (or == |) 'pipe'
print(df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')])

# Filter data with condition (> or <), (>=, <=)
print(df.loc[(df['Type 1'] == 'Grass') & (
    df['Type 2'] == 'Poison') & (df['HP'] >= 70)])

# Making new data frame from a data frame(to not alter the dataframe)
new_df = df.loc[(df['Type 1'] == 'Grass') & (
    df['Type 2'] == 'Poison') & (df['HP'] >= 70)]
print(new_df.head(5))  # But its index is kinda messy
# new_df.to_csv('grasspoison.csv')

# Reset the new dataframe index
# new_df = new_df.reset_index() #Saves the old index in a new column
new_df = new_df.reset_index(drop=True)  # Doesnt save the old index
print(new_df)

# Resetting the new data frame resetted index without using a new variable
new_df.reset_index(drop=True, inplace=True)
print(new_df)

# Filtering with string.contains (containing the word mega)
print(df.loc[df['Name'].str.contains('Mega')])
# Not cointaning the word mega
print(df.loc[~df['Name'].str.contains('Mega')])

# Using regex to filter
#print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)])
# Ignores capitalization
print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])
# Prints all names that starts with pi
print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])

######CONDITIONAL CHANGES######

# Changing datas  (fire - flamer)
#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
# print(df)
# Making all fire pokemons legendary (changing data other than the one column that you gave)
#df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
# print(df)

# Changing 2 Columns(specific elements) with one data
#df.loc[df['Total'] >= 500, ['Generation', 'Legendary']] = 'Test Value'

# Changing n columns(specific elements) with n data
#df.loc[df['Total'] >= 500, ['Generation', 'Legendary']] = ['7', True]
# print(df)


#######AGGREGATE STATISTICS(GROUPBY)#######

# Get the average of each type of pokemon
print(df.groupby(['Type 1']).mean())
# To see which type have the highest average in defense
print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))

# Get the sum
print(df.groupby(['Type 1']).sum())

# Get the count
print(df.groupby(['Type 1']).count())
# Get a cleaner count
df['count'] = 1
print(df.groupby(['Type 1']).count()['count'])
# Having a subset of each type 1
print(df.groupby(['Type 1', 'Type 2']).count()['count'])

#####Working with large amount of data#####
# Printing n rows per time (5 rows in this examlle)
# for df in pd.read_csv('modified.csv', chunksize=5):
#	print(df)

# Making a new data frame with same column names with the data frame above
newDFrame = pd.DataFrame(columns=df.columns)
# Then adding data to the new dataframe
# for df in pd.read_csv('modified.csv', chunksize=5):
#	results = df.groupby(['Type 1']).count()

#	new__df = pd.concat(new__df, results)

#############MISCELLANEOUS#############
# Shows shape of the dataframe
print(df.shape)

# Shows info
print(df.info())

# Set an option to see just n rows or columns (limit) everytime, even if
# you imported a new data set
pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 80)
print(df)

# Making a dataframe with dictionaries
people = {
    "First": ['John', 'Jane', 'Jack'],
    "Last": ['Smith', 'Smath', 'Smuth'],
    "Email": ['johnsmith@c.com', 'janesmath@c.com', 'jacksmuth@c.com']
}
new = pd.DataFrame(people)
print(new)

g = new.shift(-2, axis=1)
print(g)

# Series is the rows of a single column, or simply, a single column
# Dataframe is made of rows and columns
