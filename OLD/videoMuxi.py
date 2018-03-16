import pandas as pd
import urllib.request
res = []
for i in range(3400,5000):
    try:
        status = urllib.request.urlopen("http://data1.cache.directory/media/videos/iphone/%d.mp4" %i).code
    except:
        continue

    if status==200:
        res.append(i)
        print (i)

df = pd.DataFrame(res)
df.to_csv("D:\\abc.csv")