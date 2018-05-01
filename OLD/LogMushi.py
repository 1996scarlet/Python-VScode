import pandas as pd
import urllib.request
# import requests

import os

path = os.path.abspath(os.curdir) + "/logs"

if not os.path.exists(path):
    os.makedirs(path)

import datetime
begin = datetime.date(2018,1,10)
end = datetime.date.today()

for i in range((end - begin).days+1):
    day = begin + datetime.timedelta(days=i)

    if str(day) == "2018-01-15":
        print (str(day) + "该文件编码错误 跳过")
        continue

    url = "http://yppf.hljda.gov.cn/images/log/maltrail/%s.log" %day

    try:
        status = urllib.request.urlopen(url).code
    except:
        continue

    if status==200:

        from urllib import request
        with request.urlopen(url) as web:
            with open("%s/%s.log" %(path, day), 'wb') as outfile:
                outfile.write(web.read())

        # urllib.request.urlretrieve(url, "%s/%s.log" %(path, day))
        # r = requests.get(url) 
        # with open("%s/%s.log" %(path, day), "wb") as code:
        #     code.write(str(r.content))
        print (str(day))