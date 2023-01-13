# Import libraries
import RPi.GPIO as GPIO
from time import sleep

#set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Plugged into 17 on breadboard
GPIO.setup(11,GPIO.OUT) #The 2 servos will you one pin per row
GPIO.setup(13,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse
servo2 = GPIO.PWM(13, 50)
servo1.start(0)
servo2.start(0)

#Test
answer = input("Servo Test Proceed: Y/N: ")
print(answer)

if answer == 'Y' :
    servo1.ChangeDutyCycle(5) #Makes servos go in a clockwise direction
    servo2.ChangeDutyCycle(10)
    sleep(5) #Controls length of time the servo will go on
    # Also, length of shelf will determine how long the servo needs to go for

    servo1.ChangeDutyCycle(10) #Makes serovs go in a counter-clockwise direction
    servo2.ChangeDutyCycle(5)
    sleep(5)
else:
    servo1.stop()
    servo2.stop()
GPIO.cleanup()
