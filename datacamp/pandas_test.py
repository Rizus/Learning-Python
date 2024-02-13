import pandas as pd


dict = {
    "country":["Brazil","Ukraine", "India", "China", "South Africa"],
    "capital":["Brasilia", "Kiev", "New Delhi", "Beijing", "Pretoria"],
    "area":[8.516, 7.545, 3.286, 9.597, 1.221],
    "population":[200.4, 48.3, 1252, 1357, 52.98]
    }

cap = ["BR", "UA", "IN", "CH", "SA"]


cars.loc['RU']
cars.iloc[4]

cars.loc[['RU']]
cars.iloc[[4]]

cars.loc[['RU', 'AUS']]
cars.iloc[[4, 1]]

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])


brics = pd.DataFrame(dict)
brics.index = cap
# print(brics[["country", "capital"]]) # Column access
# print(brics[1:4]) # Row access
# print(brics.loc[["UA", "IN", "CH"], ["country", "capital"]])
# print(brics.loc[:, ["country", "population"]])
# print(brics)
print(brics.iloc[[1, 2, 3], [0, 1]])

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)


np.logical_and(brics['area'] > 8, brics['area'] < 10)
brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)]
sel = cars[cars['drives_right']]


for lab, row in dict.iterrows():
    print(f'{lab} : {row['capital']}')
    # - Creating Series on every iteration
    dict.loc[lab, 'name_length'] = len(row['country'])

dict['name_length'] = dict['country'].apply(len)