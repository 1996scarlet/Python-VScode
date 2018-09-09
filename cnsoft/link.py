from PIL import Image
import pytesseract

import pandas as pd
# writer = pd.ExcelWriter('output.xlsx')


e_name = []
e_number = []
import os
path = os.path.abspath(os.curdir) + "/cnsoft/天猫工商信息执照"
filenames=os.listdir(path)

for filename in filenames:
    if(not filename.endswith('.png')):
        continue

    filepath = path+'/'+filename
    
    print (filename)

    im = Image.open(filepath).crop((0,0,520,238))

    text = pytesseract.image_to_string(im, lang='chi_sim').replace('\n',' ')

    print (text)

    number_start = text.find('号 : ')+4
    name_start = text.find('称 : ')+4
    name_end = text.find('公司')+2

    e_name.append(text[name_start:name_end])
    e_number.append(text[number_start:number_start+18])

# print (e_number)
# print (e_name)

df1 = pd.DataFrame(data={'企业名称':e_name, '企业注册号':e_number})

print (df1)

# df1.to_excel(writer,'Sheet1')
# writer.save()