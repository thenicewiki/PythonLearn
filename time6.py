import pandas as pd
import test5 as re
import time

df = re.read_excel('class1.xlsx', 'class2.xlsx')

for i in df.iloc: 
    for j in i.index:
        print(j, ':', i[j])

    time.sleep(0.3)
    print('----------------------我是一条分割线-------------------------')
