import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial

#initialize serial port
ser = serial.Serial()
ser.port = 'COM14' #Arduino serial port
ser.baudrate = 115200
ser.timeout = 10 #specify timeout when using readline()
ser.open()
if ser.is_open==True:
	print("\nAll right, serial port now open. Configuration:\n")
	print(ser, "\n") #print serial parameters

# Create figure for plotting
fig = plt.figure()
plt.title('Serial teste')
plt.xlabel('tempo')    
plt.ylabel('Variável')
#plt.legend()
ax = fig.add_subplot(1, 1, 1)
xs = [] #store trials here (n)
ys = [] #store relative frequency here


# This function is called periodically from FuncAnimation
def animate(i, xs, ys, limit = 100): 
    # Add x and y to lists
    try:
        a = float(ser.readline().decode('UTF-8').replace("\r\n",""))    
        xs.append(i)
        ys.append(a)   
        
        if len(xs) > limit:
            # Limit x and y lists to 10 items
            xs = xs[-limit:]
            ys = ys[-limit:]
    except:
        None
    finally:
        ax.clear()
        ax.set_ylim([-1, 1])        
        ax.plot(xs, ys, label="Sin")        

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()