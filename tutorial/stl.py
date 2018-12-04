# import os

# print (dir(os))

# print (help(os))

import shutil

# print (dir(shutil))

import sys

sys.stderr.write('OJBKKKK')

import math

# print(math.log(2048, 4))

import random

random.choice([
    'akl',
    'medusa',
])

random.sample(range(100), 10)  # 不重复抽样

import statistics as st

data = random.sample(range(100), 20)
# print(st.mean(data), st.median(data), st.variance(data))


from urllib.request import urlopen
with urlopen('https://www.google.com') as response:
    for line in response:
        line = line.decode('utf-8')  # 解码.
        if 'EST' in line or 'EDT' in line:  # 查看是否是EST或EDT时间
            print(line)