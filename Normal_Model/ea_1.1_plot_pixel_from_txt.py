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
    print("Error: Missing Arguments.\n\t\aUsage: ",prog," text_file")
    exit(1)

#arrX = np.ones((500,), dtype=int)
#arrY = np.ones((500,), dtype=int)
txtFile=sys.argv[1]
arrX = np.array( [] , dtype=np.float32 )
arrY = np.array( [] , dtype=np.float32 )

cnt=0;
f = open(txtFile, 'r')
for line in f:
    cnt+=1
#    print(repr(line))
    line = line.strip()
    columns = line.split(",")
    x=float(columns[0])
    y=float(columns[1])
    fx=0
    fy=0

    if cnt == 1:
        x_top=x
        y_top=y

    if cnt == 2:
        x_bot=x
        y_bot=y

    if cnt > 2:
        x_range=x_bot-x_top
        y_range=y_bot-y_top
        x_min=0
        x_max=8
        y_min=0
        y_max=170
        fx=round( (x_max-x_min)/x_range*(x-x_top) , 1)
        fy=round( (y_max-y_min)/y_range*(y_range-(y-y_top)) , 1)

#        print(f'x={x} y={y} new values fx={fx} fy={fy} ')
        arrX = np.append( arrX , fx )
        arrY = np.append( arrY , fy )
#        print(f'arrX ={arrX} ')





#    print( f'y[k]={y[k]}' )
  
plt.plot(arrX, arrY  )
  
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My graph!')
plt.show()
