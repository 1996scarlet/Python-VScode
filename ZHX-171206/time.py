import pandas as pd
from matplotlib import pyplot
series = pd.read_csv('api_access_fix.csv', header=0)

series.plot()
pyplot.show()

class ModelDecomp(object):
    def __init__(self, file, test_size=1440):
        self.ts = self.read_data(file)
        self.test_size = test_size
        self.train_size = len(self.ts) - self.test_size
        self.train = self.ts[:len(self.ts)-test_size]
        self.test = self.ts[-test_size:]

    def _diff_smooth(self, ts):
        dif = ts.diff().dropna() # 差分序列
        td = dif.describe() # 描述性统计得到：min，25%，50%，75%，max值
        high = td['75%'] + 1.5 * (td['75%'] - td['25%']) # 定义高点阈值，1.5倍四分位距之外
        low = td['25%'] - 1.5 * (td['75%'] - td['25%']) # 定义低点阈值，同上

        # 变化幅度超过阈值的点的索引
        forbid_index = dif[(dif > high) | (dif < low)].index 
        i = 0
        while i < len(forbid_index) - 1:
            n = 1 # 发现连续多少个点变化幅度过大，大部分只有单个点
            start = forbid_index[i] # 异常点的起始索引
            while forbid_index[i+n] == start + timedelta(minutes=n):
                n += 1
            i += n - 1

            end = forbid_index[i] # 异常点的结束索引
            # 用前后值的中间值均匀填充
            value = np.linspace(ts[start - timedelta(minutes=1)], ts[end + timedelta(minutes=1)], n)
            ts[start: end] = value
            i += 1

    self.train = self._diff_smooth(self.train)
    draw_ts(self.train)