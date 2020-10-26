import pandas as pd

def read_excel(*file):
    df = pd.DataFrame(columns=pd.read_excel(file[0]).columns) # 读取Excel表表头 File[0]：其中一个文件 
    for i in file:
        df = df.append(pd.read_excel(i), ignore_index=True)
    df.to_excel('my.xlsx')
    print(df)
    return df
