import random
import numpy as np
s = int(input("Кол-во строк: "))
r = int(input("Кол-во столбов: "))
m = [[random.randint(0,9) for x in range(r)] for x in range(s)]
counter = 0
count = 1
t = 0
maxj = 0
maxcount = 1                                                                                                               
 
for i in range(len(m)):
    for j in range(len(m[i])):  
        print(m[i][j], end=' ')
    print()


for j in range(r):
    if 0 in m[j]:
      counter+=1
print("%i: Кол-во столбцов с нулем." %counter)

for i in range(s):
    count = 1
    t = m[i][0]
    for j in range(r - 1):
        if t == m[i][j+1]:
            count+=1
        else:
            t = m[i][j+1]
            count = 1
        if count > maxcount:
            maxcount = count
            maxj = i
            

print('\n')
print("%i: строка с макс длиной посл-и."% maxj)


