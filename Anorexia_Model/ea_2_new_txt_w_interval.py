#!/usr/bin/python
#Eiko Alzamora
#v1.0
#Fri Feb 24 11:53:36 PM EST 2023


import sys
import os.path
import matplotlib.pyplot as plt
import numpy as np
  
GRAPH_MIN_X=0
GRAPH_MAX_X=120   ;# range 0-8
GRAPH_MIN_Y=-20
GRAPH_MAX_Y=30 ;# range 0-170

prog=sys.argv[0]
if len(sys.argv) < 3:
    print("Error: Missing Arguments.\n\t\aUsage: ",prog," text_file(*.txt) num_of_intervals(Ex 500) ")
    exit(1)
txtFile=sys.argv[1]
num_of_int= int(sys.argv[2])
txtFileOut=txtFile.replace(".txt","_" + str(num_of_int)+".txt")

#arrX = np.ones((500,), dtype=int)
#arrY = np.ones((500,), dtype=int)
arrX = np.array( [] , dtype=np.float32 )
arrY = np.array( [] , dtype=np.float32 )
arrNX = np.array( [] , dtype=np.float32 )
arrNY = np.array( [] , dtype=np.float32 )

cnt=0;
IN  = open(     txtFile, 'r')
OUT = open( txtFileOut , 'wb')


for line in IN:
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
        delta_t=round( (GRAPH_MAX_X-GRAPH_MIN_X)/num_of_int , 4 )

    if cnt > 2:
        x_range=x_bot-x_top
        y_range=y_bot-y_top
        x_min=GRAPH_MIN_X
        x_max=GRAPH_MAX_X
        y_min=GRAPH_MIN_Y
        y_max=GRAPH_MAX_Y

        fx=round( (x_max-x_min)/x_range*(x-x_top) , 3)
        fy=round( (y_max-y_min)/y_range*(y_range-(y-y_top)) +y_min , 3)


#        print(f'x={x} y={y} new values fx={fx} fy={fy} ')
        arrX = np.append( arrX , fx )
        arrY = np.append( arrY , fy )
#        print(f'arrX ={arrX} ')

print(f"Creating new txt file {txtFileOut} with {num_of_int} pairs delta_t = {delta_t}")

for i in range(len(arrX)-1): 


    if i == 0:
        arrNX = np.append( arrNX , arrX[i] )
        arrNY = np.append( arrNY , arrY[i] )
        nextX=arrX[i]+delta_t

    #y = m * x + b
    m=(arrY[i+1] - arrY[i])/(arrX[i+1] - arrX[i])
    b = arrY[i] - m * arrX[i]


    while nextX <= arrX[i+1] :
        y = m *  nextX + b
        arrNX = np.append( arrNX , nextX )
        arrNY = np.append( arrNY ,   y   )
        nextX = nextX + delta_t

while nextX <= GRAPH_MAX_X :
    y = m *  nextX + b
    arrNX = np.append( arrNX , nextX )
    arrNY = np.append( arrNY ,   y   )
    nextX = nextX + delta_t

for i in range(len(arrNX)): 
    xypair=str( f"{round(arrNX[i],3)},{round(arrNY[i],3)}\n" )
#    print(f"pair={xypair}")
    OUT.write( xypair.encode('ascii') )

print(f"The input file had {len(arrX)} points.\nThe new file {txtFileOut} has {len(arrNX)} points, last is ({round(arrNX[-1],3)},{round(arrNY[-1],3)}) with delta_t {delta_t}.")

plt.plot(arrX, arrY ,'bo',arrNX,arrNY,'r' )
  
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Normal Model for Glucose Homeostasis')
plt.show()
