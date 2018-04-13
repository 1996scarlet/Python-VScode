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

DAX[['close', 'return']].plot(
    subplots=True, style='b', figsize=(8, 5), grid=True)

plt.show()
