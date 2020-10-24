import time
import random
stunum1 = input('please input num of class1:')
stunum2 = input('please input num of class2:')

lst = [int(stunum1), int(stunum2)]
cls = [1, 2]

k = 0
while( k < 1000):
    for i in cls:
        for stu in range(lst[i - 1]):
            print("class:", i , "num:", stu+1)
            time.sleep(0.1)
    k+=1

