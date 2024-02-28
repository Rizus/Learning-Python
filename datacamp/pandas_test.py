import pandas as pd


# dict = {
#     "country":["Brazil","Ukraine", "India", "China", "South Africa"],
#     "capital":["Brasilia", "Kiev", "New Delhi", "Beijing", "Pretoria"],
#     "area":[8.516, 7.545, 3.286, 9.597, 1.221],
#     "population":[200.4, 48.3, 1252, 1357, 52.98]
#     }

# cap = ["BR", "UA", "IN", "CH", "SA"]


# cars.loc['RU']
# cars.iloc[4]

# cars.loc[['RU']]
# cars.iloc[[4]]

# cars.loc[['RU', 'AUS']]
# cars.iloc[[4, 1]]

# # Print out drives_right column as Series
# print(cars.loc[:,'drives_right'])

# # Print out drives_right column as DataFrame
# print(cars.loc[:, ['drives_right']])

# # Print out cars_per_cap and drives_right as DataFrame
# print(cars.loc[:, ['cars_per_cap', 'drives_right']])


# brics = pd.DataFrame(dict)
# brics.index = cap
# # print(brics[["country", "capital"]]) # Column access
# # print(brics[1:4]) # Row access
# # print(brics.loc[["UA", "IN", "CH"], ["country", "capital"]])
# # print(brics.loc[:, ["country", "population"]])
# # print(brics)
# print(brics.iloc[[1, 2, 3], [0, 1]])

# # Extract drives_right column as Series: dr
# dr = cars['drives_right']

# # Use dr to subset cars: sel
# sel = cars[dr]

# # Print sel
# print(sel)


# np.logical_and(brics['area'] > 8, brics['area'] < 10)
# brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)]
# sel = cars[cars['drives_right']]


# for lab, row in dict.iterrows():
#     print(f'{lab} : {row['capital']}')
#     # - Creating Series on every iteration
#     dict.loc[lab, 'name_length'] = len(row['country'])

# dict['name_length'] = dict['country'].apply(len)



df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Aritra'],
                   'Age': [25, 30, 35],
                   'Location': ['Seattle', 'New York', 'Kona'],
                   'date_of_birth': ['2015-12-31', '2001-10-28', '1988-06-26']},
                  )

df.head()
df.info()
df.shape
df.describe()
df.values
df.columns
df.index
df.sort_values("Age", ascending=False)
df.sort_values(["Age", "Name"], ascending=[True, False])
df["Name"]
df[["Name", "Location"]]
df["Age"] >= 30
df[df["Age"] >= 30 ]
df[df["Location"] == "Kona"]
df[df["date_of_birth"] < "2001-12-31"]

val1 = df['Age'] == 25
val2 = df['Age'] == 30
df[val1 & val2]
df[ (df['Age'] == 25) & (df['Age'] == 30) ]

is_age = df["Age"].isin([25, 30])
print(df[is_age])

df["Age_m"] = df["Age"] / 100
print(df)



# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness['indiv_per_10k'] = (homelessness['individuals'] / homelessness['state_pop']) * 10000

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state','indiv_per_10k']]

# See the result
print(result)