# Import libraries
import RPi.GPIO as GPIO
from time import sleep

#set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Plugged into 17 on breadboard
GPIO.setup(11,GPIO.OUT) #The 2 servos will you one pin per row, servo1, bottom drawer
GPIO.setup(13,GPIO.OUT) #pin 27, servo2, bottom drawer
GPIO.setup(15, GPIO.OUT) #pin 22, servo3, middle drawer
GPIO.setup(16, GPIO.OUT) #pin 23, servo4, middle drawer
GPIO.setup(18, GPIO.OUT) #pin 24, servo5, top drawer
GPIO.setup(22, GPIO.OUT) #pin 25, servo6, top drawer

servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse
servo2 = GPIO.PWM(13, 50)
servo3 = GPIO.PWM(15, 50)
servo4 = GPIO.PWM(16, 50)
servo5 = GPIO.PWM(18, 50)
servo6 = GPIO.PWM(22, 50)

servo1.start(0)
servo2.start(0)
servo3.start(0)
servo4.start(0)
servo5.start(0)
servo6.start(0)

def Drawer1open():
    print("Opening...")
    servo5.ChangeDutyCycle(9) #Makes servos go in a clockwise direction
    servo6.ChangeDutyCycle(4)  
    sleep(1) 
    servo5.stop()
    servo6.stop()

def Drawer1close():
    print("Close...")
    servo5.ChangeDutyCycle(4) #Makes servos go in a clockwise direction
    servo6.ChangeDutyCycle(9)
    sleep(2)
    servo5.stop()
    servo6.stop()

def Drawer2open():
    print("Opening...")
    servo3.ChangeDutyCycle(9) #Makes servos go in a clockwise direction
    servo4.ChangeDutyCycle(4)  
    sleep(1) 
    servo3.stop()
    servo4.stop()

def Drawer2close():
    print("Close...")
    servo3.ChangeDutyCycle(4) #Makes servos go in a clockwise direction
    servo4.ChangeDutyCycle(9)
    sleep(2)
    servo3.stop()
    servo4.stop()

def Drawer3open():
    print("Opening...")
    servo1.ChangeDutyCycle(9) #Makes servos go in a clockwise direction
    servo2.ChangeDutyCycle(4)  
    sleep(1) 
    servo1.stop()
    servo2.stop()

def Drawer3close():
    print("Close...")
    servo1.ChangeDutyCycle(4) #Makes servos go in a clockwise direction
    servo2.ChangeDutyCycle(9)
    sleep(2)
    servo1.stop()
    servo2.stop()
