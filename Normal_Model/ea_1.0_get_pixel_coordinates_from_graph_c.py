#!/usr/bin/python

import sys
import os.path
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib.backend_bases import MouseButton

def onclick(event):
    global xypair
    global f
    xypair=str( f"{round(event.xdata,1)},{round(event.ydata,1)}\n" )
    print(f"{event.xdata} {event.ydata} pair={xypair}")
    f.write( xypair.encode('ascii') )


#imgFile="model.png"

prog=sys.argv[0]

if len(sys.argv) < 2:
    print("Error: Missing Arguments.\n\t\aUsage: ",prog," picture_with_graph")
    exit(1)

imgFile=sys.argv[1]

if os.path.exists(imgFile):
    fname=imgFile
else:
    print("Error: Missing file\n");
    exit(1)

#s = '12345'
#with open(f'{imgFile}.txt', 'wb') as f:
#    ascii = s.encode('ascii')
#    f.write(ascii)
f = open(f'{imgFile}.txt', 'wb')

img = img.imread( imgFile )

#global xypair
xypair="";

fig, ax = plt.subplots()

connection_id = fig.canvas.mpl_connect('button_press_event', onclick)

plt_image=plt.imshow(img)

plt.tight_layout()

plt.show()
