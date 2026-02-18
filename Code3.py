inr1 = Pin(5, Pin.OUT)
inr2 = Pin(4, Pin.OUT)
inr3 = Pin(27, Pin.OUT)
inr4 = Pin(12, Pin.OUT)
pos = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
steps = 500
yo = 0.005

while True:
  
    for step in range(steps):
        for i in pos:
            inr1.value(i[0])
            inr2.value(i[1])
            inr3.value(i[2])
            inr4.value(i[3])
            time.sleep(yo)

    
    for step in range(steps):
        for i in reversed(pos):
            inr1.value(i[0])
            inr2.value(i[1])
            inr3.value(i[2])
            inr4.value(i[3])
            time.sleep(yo)
