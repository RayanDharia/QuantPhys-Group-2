#!/usr/bin/python
#Eiko Alzamora
#v1.0
#Fri Feb 24 11:53:36 PM EST 2023


import sys
import os.path
import matplotlib.pyplot as plt
import numpy as np
  

prog=sys.argv[0]
if len(sys.argv) < 1:
    print("Error: Missing Arguments.\n\t\aUsage: ",prog," text_file1 [... text_fileX]")
    exit(1)

n=len(sys.argv)

#arrX = np.ones((500,), dtype=int)
#arrY = np.ones((500,), dtype=int)

for x in range(n-1):
#    print(f'x = {x} n={n}')
    txtFile=sys.argv[x+1]
    arrX = np.array( [] , dtype=np.float32 )
    arrY = np.array( [] , dtype=np.float32 )
    cnt=0;
    f = open(txtFile, 'r')
    for line in f:
        cnt+=1
#        print(repr(line))
        line = line.strip()
        columns = line.split(",")
        x=float(columns[0])
        y=float(columns[1])
        fx=0
        fy=0
    
        if cnt == cnt:
            arrX = np.append( arrX , x )
            arrY = np.append( arrY , y )
#            print(f'arrX ={arrX} ')


#    print( f'y[k]={y[k]}' )
  
    plt.plot(arrX, arrY  )
  
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My graph!')
plt.show()
