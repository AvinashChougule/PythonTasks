import pandas as pd
data = pd.read_csv('E:/Python Data/Daily_Flash1.csv', index_col = 0)
print(data)

# Fetched column name with index
# for itrData in pd.read_csv('E:/Python Data/Daily_Flash1.csv', index_col = 0, chunksize = 5):
#     newData = pd.DataFrame(columns=itrData.columns)
#     print(newData)


# fetch data with perticular size using chinksize function
# for itrData in pd.read_csv('E:/Python Data/Daily_Flash1.csv', index_col = 0, chunksize = 5):
#     print(itrData)
# group by columns with sorted int values only.
# mean_data = data.groupby(['name']).mean().sort_values(['reviews'])
# sum_data = data.groupby(['name']).sum().sort_values(['reviews'])
# count_data = data.groupby(['name']).count().sort_values(['reviews'])
# print(count_data)
# print(mean_data)
# print(sum_data)

# retrive filtered columns and data
# datas = data.loc[(data['name']=='Avinash') & (data['salary'] == 5000) ]
# retrive data from columns
# b = data.loc[data['name'].str.contains('Avinash')]
# print(b)

# Retrive data for perticular words like Amol 'mol' and (flags = re.I) methos ignore case sensitve words
# c = data.loc[data['name'].str.contains('Avinash|Amol', flags = re.I, regex =True)]
# print(c)
# # set index for filtered data
# a = datas.reset_index()
# # load into CSV
# a.to_csv('E:/Python Data/All_data.csv')

# Add 2 columns and sum the values
# data['Total'] = data['id'] + data['salary']
# print(data.head(3))

# Add 2 or more columns
# cols = list(data.columns)
# data = data[cols[0:3]+[cols[-2]]+ cols[3:4]]
# print(data.head(8))

#drop the column
# dropped = data.drop(columns=['salary'])
# print(dropped)

# # Adding two columns
# #data['Maths'] = data['id'] + data['salary']
# #print(data['Maths'])
# # Adding two or more columns
# data['Total'] = data.iloc[:,4:6].sum(axis=0)
# print(data.head(4))
# # ways of changing the column positions
#
# # Dropping a specific column
#
# #print(data.sort_values('designation', ascending = True))
# # sort 2 columns at a time, 'designation' is ascending  another one is decending
# #print(data.sort_values(['designation', 'id'], ascending = [False,True]))
#
# # a = data.columns
# # print(len(a))
#
# #print(data.describe())
# # Reading Headers
# # a = data.columns
# # print(data['salary'][2])
# # data_value = data.loc[data['salary'] == 6000]
# # print(data_value)
# # Read specific column and a range of column