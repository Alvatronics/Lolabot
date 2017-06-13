import RPi.GPIO as GPIO    #Importamos la librería GPIO
import time                #Importamos time (time.sleep)
from gpiozero import DistanceSensor #Importamos libreria del sensor de distancia
import pygame
import consola_io

ESC = '\x1B'

GPIO.setmode(GPIO.BCM)     #Ponemos la placa en modo BCM
ultrasonic = DistanceSensor(echo=23, trigger=24, threshold_distance=0.2, max_distance=2)

MotorDA = 5    #29 board 
MotorDB = 6    #31 board
MotorDE = 13   #33 board

MotorIA = 27   #13 board
MotorIB = 17   #11 board
MotorIE = 18   #12 board

offset = 0 #offset entre ruedas
vmax = 100 #velocidad maxima
vel_actual = 0	#variable para conocer la velocidad actual del robot

GPIO.setup(MotorIA,GPIO.OUT)
GPIO.setup(MotorIB,GPIO.OUT)
GPIO.setup(MotorIE,GPIO.OUT)
GPIO.setup(MotorDA,GPIO.OUT)
GPIO.setup(MotorDB,GPIO.OUT)
GPIO.setup(MotorDE,GPIO.OUT)
  

pwmIzq = GPIO.PWM(MotorIE, 500)   # Creamos el objeto de control PWM para el motor izquierdo
pwmDch = GPIO.PWM(MotorDE, 500)     # Creamos el objeto de control PWM para el motor derecho
  
pwmIzq.start(0)              # Iniciamos el objeto 'white' al 0% del ciclo de trabajo (completamente apagado)  
pwmDch.start(0)



def arranca_alante(vel=100):
	global vel_actual
	if vel>100: return
	else: 
		GPIO.output(MotorIA,GPIO.HIGH) #Motor izquierdo hacia delante
		GPIO.output(MotorIB,GPIO.LOW)
		GPIO.output(MotorDA,GPIO.HIGH)
		GPIO.output(MotorDB,GPIO.LOW)
		pause_time = 0.005
		vel_actual=vel+1
		#for i in range(0,vel_actual):            # Recta de aceleracion
			#if (i-offset)<0: pwmIzq.ChangeDutyCycle(i) #Para no pasarle un valor menor que 0 a la salida
			#else: pwmIzq.ChangeDutyCycle(i-offset) 
		pwmIzq.ChangeDutyCycle(vel-offset)     
		pwmDch.ChangeDutyCycle(vel)  
		time.sleep(pause_time)
    

def arranca_atras(vel=80):
	global vel_actual
	vel_actual=vel
	GPIO.output(MotorIA,GPIO.LOW) #Motor izquierdo hacia delante
	GPIO.output(MotorIB,GPIO.HIGH)
	GPIO.output(MotorDA,GPIO.LOW)
	GPIO.output(MotorDB,GPIO.HIGH)
	pause_time = 0.01
	for i in range(30,vel_actual+1):            # De i=0 hasta i=101 (101 porque el script se detiene al 100%)
			pwmIzq.ChangeDutyCycle(i-offset)      # LED #1 = i
			pwmDch.ChangeDutyCycle(i)  # LED #2 resta 100 - i
			time.sleep(pause_time)

def arranca_atras_giro():
    GPIO.output(MotorIA,GPIO.LOW) #Motor izquierdo hacia delante
    GPIO.output(MotorIB,GPIO.HIGH)
    GPIO.output(MotorDA,GPIO.LOW)
    GPIO.output(MotorDB,GPIO.HIGH)
    pause_time = 0.01
    giro = 30
    for i in range(20,60):            # De i=0 hasta i=101 (101 porque el script se detiene al 100%)
            pwmIzq.ChangeDutyCycle(20)      # LED #1 = i
            pwmDch.ChangeDutyCycle(i)  # LED #2 resta 100 - i
            time.sleep(pause_time)
    pwmIzq.ChangeDutyCycle(0)      # LED #1 = i
    pwmDch.ChangeDutyCycle(0)  # LED #2 resta 100 - i

def giro_si_mismo_izq(vel=80):
	global vel_actual
	GPIO.output(MotorIA,GPIO.LOW) #Motor izquierdo hacia delante
	GPIO.output(MotorIB,GPIO.HIGH)
	GPIO.output(MotorDA,GPIO.HIGH)
	GPIO.output(MotorDB,GPIO.LOW)
	#pause_time = 0.001
	vel_actual=vel

	pwmIzq.ChangeDutyCycle(vel_actual)      # LED #1 = i
	pwmDch.ChangeDutyCycle(vel_actual)

def giro_si_mismo_der(vel=80):
	global vel_actual
	GPIO.output(MotorIA,GPIO.HIGH) #Motor izquierdo hacia delante
	GPIO.output(MotorIB,GPIO.LOW)
	GPIO.output(MotorDA,GPIO.LOW)
	GPIO.output(MotorDB,GPIO.HIGH)
	vel_actual=vel

	pwmIzq.ChangeDutyCycle(vel_actual)      # LED #1 = i
	pwmDch.ChangeDutyCycle(vel_actual)
    

def para():
	global vel_actual
	pause_time = 0.001
	print (vel_actual)
	for i in range(vel_actual-1,0,-1):        # Desde i=100 a i=0 en pasos de -1  
		pwmIzq.ChangeDutyCycle(i)      # LED #1 = i
		pwmDch.ChangeDutyCycle(i)  # LED #2 resta 100 - i 
        #print(i) 
		time.sleep(pause_time)             # Pequeña pausa para no saturar el procesador

	pwmIzq.ChangeDutyCycle(0)      # lo paro
	pwmDch.ChangeDutyCycle(0)
	vel_actual=0
    
            
def automatico():
    try:
        while True:
            ultrasonic.when_in_range = para
            arranca_alante ()
            #ultrasonic.when_in_range=para()
            #ultrasonic.wait_for_in_range()
            while (ultrasonic.distance >= 0.5):
                print(ultrasonic.distance)
            
            while (ultrasonic.distance <= 0.5):
                giro_si_mismo_der()
                print(ultrasonic.distance)
            arranca_alante ()
            while (ultrasonic.distance >= 0.5):
                print(ultrasonic.distance)
            while (ultrasonic.distance <= 0.5):
                giro_si_mismo_izq()
                print(ultrasonic.distance)
    
    except KeyboardInterrupt:                #Si el usuario pulsa CONTROL+C...
        print ("quit")                         #Avisamos del cierre al usuario
        pwmIzq.stop()            # Detenemos el objeto 'white'
        pwmDch.stop()
        GPIO.cleanup()
    
def teclado():
	try:
		pygame.init()
		screen = pygame.display.set_mode((640, 480)) #inicializamos le interfaz de pygame
		pygame.display.set_caption('Robot!')
		pygame.mouse.set_visible(1)
 
		val = '-'
 
		while val != 'stop':
			#events = pygame.event.get()
			#for event in events:
			#inicial=time.time() #establezco tiempos para evitar rebotes de las teclas
			event=pygame.event.wait()
			
			
			
			if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						tecla_anterior=event.key
						vel_deseada=100
						if vel_actual!=vel_deseada:
							arranca_alante(vel_deseada)
							print("alante")
					elif event.key == pygame.K_LEFT:
						tecla_anterior=event.key
						vel_deseada=80
						if vel_actual!=vel_deseada:
							giro_si_mismo_izq(vel_deseada)
							print("izquierda")
					elif event.key == pygame.K_RIGHT:
						tecla_anterior=event.key
						vel_deseada=80
						if vel_actual!=vel_deseada:
							giro_si_mismo_der(vel_deseada)
							print("derecha")
					elif event.key == pygame.K_DOWN:
						tecla_anterior=event.key
						vel_deseada=80
						if vel_actual!=vel_deseada:
							arranca_atras(vel_deseada)
							print("atras")
					elif event.key == pygame.K_ESCAPE:
						print("salir")
						val = 'stop'
			elif event.type == pygame.KEYUP:
						time.sleep(0.001)
						event=pygame.event.poll()				#compruebo que no ha llegado ningun evento nuevo durante los
						if (event.type == pygame.KEYDOWN):
							if 	(event.key == tecla_anterior):
								print("rebotes")
						else:
							print("ha soltado")	
							print("para")
							para()
		
        


	except KeyboardInterrupt:                #Si el usuario pulsa CONTROL+C...
		print ("quit")                         #Avisamos del cierre al usuario
		pwmIzq.stop()            # Detenemos el objeto 'white'
		pwmDch.stop()
		GPIO.cleanup()

#-----------------
#-- Sacar el menu
#-----------------
def menu():
  print ("""
  
     Menu de opciones
     ----------------
     
     1.- Automatico
     2.- Teclado
	 Espacio.- Volver a sacar el menu
	 ESC.- Terminar
		""")

#---------------------
#- Comienzo programa
#---------------------

try:

	menu()
    
	while 1:
		#-- Leer tecla
		
		c=input()
		#-- Procesar tecla
		if   c=='1': print ("Automatico")
		elif c=='2': 
			print ("Control con teclado")
			teclado()
		elif c==' ': menu()
		elif c==ESC: break   #-- Salir del bucle
		menu()
        

except KeyboardInterrupt:                #Si el usuario pulsa CONTROL+C...
    print ("quit")                         #Avisamos del cierre al usuario
    pwmIzq.stop()            # Detenemos el objeto 'white'
    pwmDch.stop()
    GPIO.cleanup()

