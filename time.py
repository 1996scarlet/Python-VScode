# from pandas import Series

# from pandas import DataFrame

# # load dataset

# series = Series.from_csv('seasonally_adjusted.csv', header=None)

# # reframe as supervised learning

# dataframe = DataFrame()

# for i in range(12,0,-1):

#     dataframe['t-'+str(i)] = series.shift(i)

# dataframe['t'] = series.values

# print(dataframe.head(13))

# dataframe = dataframe[13:]

# # save to new file

# dataframe.to_csv('lags_12months_features.csv', index=False)

from pandas import read_csv

from sklearn.ensemble import RandomForestRegressor

from matplotlib import pyplot

# load data

dataframe = read_csv('lags_12months_features.csv', header=0)

array = dataframe.values

# split into input and output

X = array[:,0:-1]

y = array[:,-1]

# fit random forest model

model = RandomForestRegressor(n_estimators=500, random_state=1)

model.fit(X, y)

# show importance scores

print(model.feature_importances_)

# plot importance scores

names = dataframe.columns.values[0:-1]

ticks = [i for i in range(len(names))]

pyplot.bar(ticks, model.feature_importances_)

pyplot.xticks(ticks, names)

pyplot.show()