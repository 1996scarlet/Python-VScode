# import os

# print (dir(os))

# print (help(os))

import shutil

# print (dir(shutil))

import sys

# sys.stderr.write('OJBKKKK')

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

# from urllib.request import urlopen
# with urlopen('https://www.google.com') as response:
#     for line in response:
#         line = line.decode('utf-8')  # 解码.
#         if 'EST' in line or 'EDT' in line:  # 查看是否是EST或EDT时间
#             print(line)

# from datetime import date
# now = date.today()
# # print (now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# import zlib
# s = b'ojbkk ojbk ojbkk wtf wtf just eurobeat baka baka'
# print (len(s))

# t = zlib.compress(s)
# print (len(t))

# print (zlib.decompress(t))

import textwrap
doc = """The wrap() method is just like fill() except that it returns 
a list of strings instead of one big string with newlines to separate 
the wrapped lines."""

# print(textwrap.fill(doc, width=40))

# import threading, zipfile

# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile

#     def run(self):
#         f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print('后台解压文件完成:', self.infile)

# background = AsyncZip('CombinedLogs.log', 'myarchive.zip')
# background.start()
# print('主程序持续执行.')

# background.join()    # Wait for the background task to finish
# print('主程序等待后台任务结束.')

# import logging
# logging.debug('Debugging information')
# logging.info('Informational message')
# logging.warning('Warning:config file %s not found', 'server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')

import heapq
data = random.sample(range(1000), 50)
heapq.heapify(data)
heapq.heappush(data, -1)
heapq.heappush(data, -99)

print([heapq.heappop(data) for i in range(5)])
