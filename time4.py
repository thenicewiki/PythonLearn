import pandas as pd
import time

df = pd.read_excel('test.xlsx')

while(1):
    for i in df.iloc:
        print("班级", i[0],  "姓名:", i[1])
        time.sleep(0.1)

