import RPi.GPIO as GPIO
from time import sleep
import pygame
from array import array
from math import *

MIXER_FREQ=44100
MIXER_SIZE=-16
MIXER_CHANS=1
MIXER_BUFF=1024

# Class for bounding each note to a key
class Note(pygame.mixer.Sound):
    def __init__(self,frequency,volume,wave):
        self.frequency=frequency
        self.wave=wave
        pygame.mixer.Sound.__init__(self,buffer=self.build_samples())
        self.set_volume(volume)
    
    # Determines the wave for each note
    def build_samples(self):
        period=int(round(MIXER_FREQ/self.frequency))
        amplitude=2**(abs(MIXER_SIZE)-1)-1
        samples=array("h",[0]*period)
        
        # Square Wave
        if(self.wave=="square"):
            for t in range(period):
                if(t<period/2):
                    samples[t]=amplitude
                else:
                    samples[t]=-amplitude
                    
        # Triangle Wave
        elif(self.wave=="triangle"):
            slope=round(amplitude/(period/4))
            for t in range(period):
                if(t<period/4):
                    samples[t]=t*slope
                elif(t<period*(0.75)):
                    samples[t]=((round(period/2))-t)*slope
                else:
                    samples[t]=((period-t)*slope)-amplitude

        # Sawtooth Wave   
        elif(self.wave=="sawtooth"):
            slope=round(amplitude/(period/2))
            for t in range(period):
                if(t<period/2):
                    samples[t]=t*slope
                else:
                    samples[t]=((period-t)*slope)-amplitude
                    
        # Sinusoidal Wave
        elif(self.wave=="sinusoidal"):
            s=360/period
            for t in range(period):
                if(t<period/2):
                    samples[t]=int(amplitude*(sin(radians(t*s))))
                else:
                    samples[t]=-int(amplitude*(sin(radians(t*s))))
                
        return samples
    
# Waits for the key to be pushed and play the corresponding note
def wait_for_note_start():
    while(True):
        for key in range(len(keys)):
            if(GPIO.input(keys[key])):
                return key
        sleep(0.01)
        
# Waits for a key to not be pressed
def wait_for_note_stop(key):
    while(GPIO.input(key)):
        sleep(0.1)
    
# Initilizes the pygame library functions for sounds
pygame.mixer.pre_init(MIXER_FREQ,MIXER_SIZE,MIXER_CHANS,MIXER_BUFF)
pygame.init()
GPIO.setmode(GPIO.BCM)

keys=[20,16,12,26]
freq=261.6
notes=[]
waves=["square","triangle","sawtooth","sinusoidal"]

GPIO.setup(keys,GPIO.IN,GPIO.PUD_DOWN)

for n in range(len(keys)):
    notes.append(Note(freq,1,waves[n]))

###########
# Main
###########
print("Welcome Grape Piano")
print("Use ctrl+c to exit...")

try:
    while(True):
        key=wait_for_note_start()
        notes[key].play(-1)
        wait_for_note_stop(keys[key])
        notes[key].stop()
except KeyboardInterrupt:
    GPIO.cleanup
    print("EXITED")