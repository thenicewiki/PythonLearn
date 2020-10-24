import pandas as pd
import time
import test5 as re

# def ReadExcel(*file):
#     df = pd.DataFrame(columns=pd.read_excel(file[0]).columns)
#     for i in file:
#         df = df.append(pd.read_excel(i), ignore_index=True)
    
#     df.to_excel('my.xlsx')
#     return df

# ReadExceal('class1.xlsx', 'class2.xlsx')


# df = pd.read_excel('class1.xlsx')
# df2 = pd.read_excel('class2.xlsx')
# df = df.append(df2, ignore_index=True)


# print(df)

df = re.read_excel('class1.xlsx', 'class2.xlsx')

for i in df.iloc: 
    for j in i.index:
        print(j, ':', i[j])

    time.sleep(0.3)
    print('----------------------我是一条分割线-------------------------')
