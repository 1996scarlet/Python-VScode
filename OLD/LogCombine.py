# -*- coding: utf-8 -*-  
import os

path = os.path.abspath(os.curdir) + "/logs"

filenames=os.listdir(path)

f=open('CombinedLogs.log','w',encoding="utf-8")

for filename in filenames:
    filepath = path+'/'+filename

    print (filename)
    
    for line in open(filepath,mode='r',encoding="utf-8"):
        f.writelines(line)

f.close()