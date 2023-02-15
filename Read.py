#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#try:
 #   id, text = reader.read()
  #  print(id)
   # print(text)
#finally:
    #GPIO.cleanup()
   
def readcard(x):
     #print("Attempting to read NFC")
     id, text = x.read()
     #print(f"ID  :  {id}")
     text = text.strip()
     '''if (text == "1"):
          print("Drawer 1 open")
     if (text == "2"):
          print("Drawer 2 open")
     if (text == "3"):
          print("Drawer 3 open")'''

     return text

#if __name__ == "__main__":
 #    try:
  #        reader = SimpleMFRC522()
   #       print("Initialized Reader")
    #      readcard(reader)
     #     GPIO.cleanup()
     #except KeyboardInterrupt:
      ##    print("Keyboard Interrupt")
        #  GPIO.cleanup()

