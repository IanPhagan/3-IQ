# Import libraries
import RPi.GPIO as GPIO
from time import sleep

#set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Plugged into 17 on breadboard
GPIO.setup(11,GPIO.OUT) #The 2 servos will you one pin per row
GPIO.setup(13,GPIO.OUT) #pin 27
GPIO.setup(15, GPIO.OUT) #pin 22
GPIO.setup(16, GPIO.OUT) #pin 23
GPIO.setup(18, GPIO.OUT) #pin 24
GPIO.setup(22, GPIO.OUT) #pin 25

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




# User-Defined functions for drawers
def BottomDrawer(x):
    if x == 1 :
        print("Opening...")
        servo1.ChangeDutyCycle(5) #Makes servos go in a clockwise direction
        servo2.ChangeDutyCycle(10)
        sleep(5) #Controls length of time the servo will go on
        # Also, length of shelf will determine how long the servo needs to go for
        print("Closing...")
        servo1.ChangeDutyCycle(10) #Makes serovs go in a counter-clockwise direction
        servo2.ChangeDutyCycle(5)
        sleep(5)
        
        

def MiddleDrawer(x):
    if x == 2 :
        print("Opening...")
        servo3.ChangeDutyCycle(5) #Makes servos go in a clockwise direction
        servo4.ChangeDutyCycle(10)
        sleep(5) #Controls length of time the servo will go on
        # Also, length of shelf will determine how long the servo needs to go for
        print("Closing...")
        servo3.ChangeDutyCycle(10) #Makes serovs go in a counter-clockwise direction
        servo4.ChangeDutyCycle(5)
        sleep(5)
    
        servo3.stop()
        servo4.stop()
        
def TopDrawer(x):
    if x == 3 :
        print("Opening...")
        servo5.ChangeDutyCycle(4) #Makes servos go in a clockwise direction
        servo6.ChangeDutyCycle(9)
        sleep(7) #Controls length of time the servo will go on
        # Also, length of shelf will determine how long the servo needs to go for
        print("Closing...")
        servo5.ChangeDutyCycle(9) #Makes serovs go in a counter-clockwise direction
        servo6.ChangeDutyCycle(4)
        sleep(7)
   
        servo5.stop()
        servo6.stop()

#Test
while True:
    answer = int((input("Which drawer would you like to open 1,2, or 3: ")))
    if (answer == 1):
        BottomDrawer(answer)
        servo1.stop()
        servo2.stop()
    elif (answer == 2):
        MiddleDrawer(answer)
    elif (answer == 3):
        TopDrawer(answer)
    else:
        pass


GPIO.cleanup()
