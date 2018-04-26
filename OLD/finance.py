from datetime import datetime
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import numpy as np

start = datetime(2015, 2, 9)

end = datetime(2017, 5, 24)

DAX = web.DataReader('F', 'iex', start, end)

# f['close'].plot(figsize=(8, 5), grid=True)
# plt.show()

DAX['return'] = np.log(DAX['close'] / DAX['close'].shift(1))

# DAX[['close', 'return', 'return']].tail()

# DAX[['close', 'return']].plot(
#     subplots=True, style='b', figsize=(8, 5), grid=True)

DAX['smooth'] = pd.rolling_mean(DAX['close'], window=42)
# DAX['252d'] = pd.rolling_mean(DAX['close'], window=152)

# DAX[['close', '42d', '252d']].plot(figsize=(8, 5), grid=True)
DAX[['close', 'smooth']].plot(figsize=(8, 5), grid=True)
# 标签: dax_trends
# 标题: DAX 指数以及移动平均值

# import math
# DAX['Mov_Vol'] = pd.rolling_std(DAX['return'], window=42) * math.sqrt(42)
# DAX[['close', 'Mov_Vol', 'return']].plot(
#     subplots=True, style='b', figsize=(8, 7), grid=True)

plt.show()