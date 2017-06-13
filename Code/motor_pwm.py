import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO  
from time import sleep  # cargamos la función sleep del módulo time 
  
GPIO.setmode(GPIO.BOARD)  # Ponemos la Raspberry en modo BCM

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
  

pwmIzq = GPIO.PWM(MotorIE, 100)   # Creamos el objeto 'white' en el pin 25 a 100 Hz  
pwmDch = GPIO.PWM(MotorDE, 100)     # Creamos el objeto 'red' en el pin 24 a 100 Hz 
  
pwmIzq.start(0)              # Iniciamos el objeto 'white' al 0% del ciclo de trabajo (completamente apagado)  
pwmDch.start(0)              # Iniciamos el objeto 'red' al 100% del ciclo de trabajo (completamente encendido)  
  
# A partir de ahora empezamos a modificar los valores del ciclo de trabajo
  
pause_time = 0.01           # Declaramos un lapso de tiempo para las pausas

GPIO.output(MotorIA,GPIO.HIGH) #Motor izquierdo hacia delante
GPIO.output(MotorIB,GPIO.LOW)

GPIO.output(MotorDA,GPIO.HIGH)
GPIO.output(MotorDB,GPIO.LOW)


  
try:                        # Abrimos un bloque 'Try...except KeyboardInterrupt'
    while True:             # Iniciamos un bucle 'while true'  
        for i in range(50,101):            # De i=0 hasta i=101 (101 porque el script se detiene al 100%)
            pwmIzq.ChangeDutyCycle(i)      # LED #1 = i
            pwmDch.ChangeDutyCycle(i)  # LED #2 resta 100 - i
            sleep(pause_time)             # Pequeña pausa para no saturar el procesador

        sleep(1)
            
        for i in range(100,50,-1):        # Desde i=100 a i=0 en pasos de -1  
            pwmIzq.ChangeDutyCycle(i)      # LED #1 = i
            pwmDch.ChangeDutyCycle(i)  # LED #2 resta 100 - i  
            sleep(pause_time)             # Pequeña pausa para no saturar el procesador

        pwmIzq.ChangeDutyCycle(0)      # lo paro
        pwmDch.ChangeDutyCycle(0)
        sleep(5)
            
  
except KeyboardInterrupt:   # Se ha pulsado CTRL+C!!
    pwmIzq.stop()            # Detenemos el objeto 'white'
    pwmDch.stop()              # Detenemos el objeto 'red'
    GPIO.cleanup()          # Limpiamos los pines GPIO y salimos
