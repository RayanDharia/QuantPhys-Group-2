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
arrG = np.array( [] , dtype=np.float32 )
arrA = np.array( [] , dtype=np.float32 )
arrI = np.array( [] , dtype=np.float32 )
arrB = np.array( [] , dtype=np.float32 )

for i in range(n-1):
#    print(f'x = {x} n={n}')
    txtFile=sys.argv[i+1]
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
  
#    plt.plot(arrX, arrY  )
#    print(f" x = {x}")
    if i == 0:
        arrG=np.copy(arrY)  ;# Glucose
    if i == 1:
        arrA=np.copy(arrY)  ;# Glucagon
    if i == 2:
        arrB=np.copy(arrY)  ;# Insulin

#print( f'len arrG{ arrG.shape } arrX{ arrX.shape }' )

delta_t=arrX[1]-arrX[0]
##################         ONE 
parG1=1.7 
parG2=-0.2
parA1=0.5 
parA2=0.3
parI1=-1.0 

arrI = np.zeros( arrY.shape )
arrI[0]=20
for i in range(arrX.shape[0]-1 ) :
    arrI[i+1] = arrI[i] + delta_t * ( -arrG[i]*parG2 + arrA[i]*parA2 + arrI[i]*parI1 +
        parG1*(arrG[i+1]-arrG[i])/delta_t - parA1*(arrA[i+1]-arrA[i])/delta_t )

#plt.plot(arrX, arrA,'b')
plt.figure("one")
plt.fill_between( arrX, 110, 70, color= "y", alpha= 0.2)
plt.plot(arrX, arrG,'k',arrX, arrA,'r',arrX,arrI,'purple' ,arrX,arrB,'o'  )
plt.text(1.6,  0.5, 'pG1='+str(parG1) )
plt.text(1.6, 11.5, 'pG2='+str(parG2) )
plt.text(1.6, 22.5, 'pA1='+str(parA1) )
plt.text(1.6, 32.5, 'pA2='+str(parA2) )
plt.text(1.6, 42.5, 'pI1='+str(parI1) )

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My graph!')
plt.grid(visible=True, which='major', axis='both')

plt.figure("two")

arrI = np.zeros( arrY.shape )
##################         TWO
#144.71905005531582 => pG1=1.44 pG2=-0.26 pA1=0.5 pA2=0.3 pI1=-1.0
parG1=1.44
parG2=-0.26
parA1=0.5 
parA2=0.3
parI1=-1.0 

arrI[0]=20
for i in range(arrX.shape[0]-1 ) :
    arrI[i+1] = arrI[i] + delta_t * ( -arrG[i]*parG2 + arrA[i]*parA2 + arrI[i]*parI1 +
        parG1*(arrG[i+1]-arrG[i])/delta_t - parA1*(arrA[i+1]-arrA[i])/delta_t )

plt.fill_between( arrX, 110, 70, color= "y", alpha= 0.2)
plt.plot(arrX, arrG,'k',arrX, arrA,'r',arrX,arrI,'purple' ,arrX,arrB,'o'  )
plt.text(1.6,  0.5, 'pG1='+str(parG1) )
plt.text(1.6, 11.5, 'pG2='+str(parG2) )
plt.text(1.6, 22.5, 'pA1='+str(parA1) )
plt.text(1.6, 32.5, 'pA2='+str(parA2) )
plt.text(1.6, 42.5, 'pI1='+str(parI1) )

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My graph!')
plt.grid(visible=True, which='major', axis='both')




plt.show()
