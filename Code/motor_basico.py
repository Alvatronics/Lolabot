
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
MotorDA = 29
MotorDB = 31
MotorDE = 33

MotorIA = 13
MotorIB = 11
MotorIE = 12
 
GPIO.setup(MotorIA,GPIO.OUT)
GPIO.setup(MotorIB,GPIO.OUT)
GPIO.setup(MotorIE,GPIO.OUT)
GPIO.setup(MotorDA,GPIO.OUT)
GPIO.setup(MotorDB,GPIO.OUT)
GPIO.setup(MotorDE,GPIO.OUT)

 

 
print ("Stopping motor")
GPIO.output(MotorIE,GPIO.LOW)
GPIO.output(MotorDE,GPIO.LOW)
sleep(0.5)

print ("Turning motor on Backguards")
GPIO.output(MotorIA,GPIO.LOW)
GPIO.output(MotorIB,GPIO.HIGH)
GPIO.output(MotorIE,GPIO.HIGH)
GPIO.output(MotorDA,GPIO.LOW)
GPIO.output(MotorDB,GPIO.HIGH)
GPIO.output(MotorDE,GPIO.HIGH)

sleep(0.5)

print ("Turning motor on forward")
GPIO.output(MotorIA,GPIO.HIGH)
GPIO.output(MotorIB,GPIO.LOW)
GPIO.output(MotorIE,GPIO.HIGH)
GPIO.output(MotorDA,GPIO.HIGH)
GPIO.output(MotorDB,GPIO.LOW)
GPIO.output(MotorDE,GPIO.HIGH)
sleep(0.5)

print ("GIRAR SOBRE SI MISMO")
GPIO.output(MotorIA,GPIO.HIGH)
GPIO.output(MotorIB,GPIO.LOW)
GPIO.output(MotorIE,GPIO.HIGH)
GPIO.output(MotorDA,GPIO.LOW)
GPIO.output(MotorDB,GPIO.HIGH)
GPIO.output(MotorDE,GPIO.HIGH)
sleep(2)
GPIO.cleanup()
