from machine import Pin
import time
inr1=Pin(5,Pin.OUT)
inr2=Pin(4,Pin.OUT)
inr3=Pin(27,Pin.OUT)
inr4=Pin(12,Pin.OUT)

pos=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
for o in range(1000):
    for i in pos:
        inr1.value(i[0])
        inr2.value(i[1])
        inr3.value(i[2])
        inr4.value(i[3])
        time.sleep(0.005)
        
inr1.value(0)
inr2.value(0)
inr3.value(0)
inr4.value(0)
