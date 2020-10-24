import time
import random
stunum1 = input('please input num of class1:')
stunum2 = input('please input num of class2:')

lst = [int(stunum1), int(stunum2)]

i = 0
while(i < 1000):
    time.sleep(0.12)
    cls = random.randint(0, 1)
    print('class:', cls + 1, 'num:', random.randint(1, lst[cls]))
    i+=1
