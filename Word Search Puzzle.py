# # Question
# #
# # A time series of daily readings of mercury levels in a river is provided to you.
# # In each test case, the day's highest level is missing for certain days. By analyzing the data,
# # try to identify the missing mercury levels for those days. Each row of data contains two tab-separated values:
# # a time-stamp and the day's highest reading.
# #
# # There are exactly twenty rows marked missing in each input file.
# # The missing values are marked as "Missing_1", "Missing_2", ..., "Missing_20". These missing records have been randomly
# # dispersed in the rows of data.
# #
# # Constraints
# #
# # Mercury levels are all < 400.
# #
# # Function Description
# #
# # Complete the calcMissing function in the editor below. It should print 20 rows, one for each missing value, as floats.
#
# # !/bin/python3
# import math
# import os
# import random
# import re
# import sys
#
# #
# # Complete the 'calcMissing' function below.
# #
# # The function accepts STRING_ARRAY readings as parameter.
# #
#
# def calcMissing(readings):
#     # Write your code here
#     import datetime as dt
#
#     import pandas as pd
#     import numpy as np
#     import random
#     dates = []
#     temp_values = []
#     for x in readings:
#         temp_list = x.split('\t')
#         dates.append(temp_list[0])
#         temp_values.append(temp_list[1])
#
#     df = pd.DataFrame(list(zip(dates, temp_values)),
#                       columns=['X', 'Y'])
#     df['X'] = pd.to_datetime(df['X'])
#
#     missing_indices = df.Y.str.contains('^Missing')
#     missing_dates = df.X[missing_indices]
#
#     b = df.index[missing_indices]
#     df1 = df.drop(b)
#
#     df1['Date'] = df1['X'].map(dt.datetime.toordinal)
#     df1['Y'] = pd.to_numeric(df1['Y'])
#
#     x = df1[['Date']]
#     y = np.asarray(df1['Y'])
#
#     from sklearn.ensemble import GradientBoostingRegressor
#     lr = GradientBoostingRegressor()
#     lr.fit(x, y)
#
#     x_test = df.X[b]
#     x_test1 = x_test.map(dt.datetime.toordinal)
#     y_pred = lr.predict(np.array(x_test1).reshape(-1, 1))
#     for p in y_pred:
#         print(p)
#
#
# if __name__ == '__main__':
#     readings_count = int(input().strip())
#
#     readings = []
#
#     for _ in range(readings_count):
#         readings_item = input()
#         readings.append(readings_item)
#
#     calcMissing(readings)

# import pandas as pd
#
# def attributesSet(numberOfAttributes, supportThreshold):
#     # Write your code here
#     census_list = []
#     dataset = pd.read_csv('census.csv')
#     census_dict = dict()
#     list1 = ['age', 'sex', 'education', 'native_country','race','marital-status','workclass','occupation','hours-per-week','income','capital-gain','capital-loss']
#     for x in range(len(dataset)):
#         for y in dataset.columns:
#             newlist = dataset.loc[x, y].split("=")
#             census_dict[newlist[0]] = newlist[1]
#         census_list.append(census_dict)

# !/bin/python3











