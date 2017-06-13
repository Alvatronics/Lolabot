





LolaBot
















1. Especificaciones

1. Versión 0
Estrucutura: Base para alojar los motores, la raspi, los sensores infrarojos y modular.
Movimiento: Capacidad para evitar obstaculos mediante los sensores infrarojos.
Autonomia: Se utilizara el banco de alimentacion de 5600 mAh, 1.5 A output.

2. Version 1.0
Hacer menú de inicio con distintas opciones de ejecución (Automatico, Teclado, Shell, Mando)
Controlar el robot con teclado.
Añadir la pluma.

Version 1.1
Incluir sensor de infrarrojos para detectar presencia.
Controlar el robot con mando infrarrojos.

Version 1.1
Añadir botón para poder parar la ejecución.
Arranque automático de la aplicación al arrancar la raspi.

3. Version 2.0
Controlarlo remotamente desde red externa.
Controlarlo dentro de cualquier red sin necesidad de configurar la raspi.

Version 2.1
Incluir cámara raspi.

Version 2.2
Control de carga de la batería.

Version 2.3
Hacer un HAT con la electrónica básica.




Estructura: Incluir carcasa para proteger la electronica.
Movimiento: Añadir sensor infrarojos para controlarlo con mando, incluir acelerometros para detectar ataques, añadir cámara para telepresencia y mapeado.
Software de control remoto.

















2. Lineas de trabajo

2.1. Investigar sobre la utilización de las salidas de la raspi:

2.1.1. Control de motores DC. Requisitos: En función de los motores que elija los valores de demanda de corriente/voltaje de los mismos va a estar entre los 200 mA / 6 V y los 800 mA.
Lo máximo que pueden dar las patillas de la raspi 3 es de 16 mA, por lo que hay que utilizar un interfaz para conectarlas a los motores.
Opciones:
2.1.1.1. Controlador de motores con transistores NPN: Pros: Barato y fácil; Contras: Necesitas hacer la placa para que quede curioso. Ver http://robologs.net/2014/09/16/como-construir-un-controlador-de-motores-npn/ 

2.1.1.2. Usando el driver L293D: Chip que te permite controlar 2 motores DC o 1 paso a paso. Precio 3´26. Pros: Barato, escalable. Contras: hay que hacer la placa. Limitado a 600 mA de salida.
Ver:
https://business.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051 
https://learn.adafruit.com/adafruit-raspberry-pi-lesson-9-controlling-a-dc-motor/hardware 

2.1.1.3. Adafruit DC-Stepper Hat: Se controla por I2C y puede dar hasta 1.2 A de salida con pico de 3A. 4 motores DC o 2 paso a paso. Precio 25.87. Pros: facilidad de uso y potencia. Contra: Precio.
Ver: https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/overview?view=all 

2.1.2. Control de sensor de ultrasonidos: 
https://www.raspberrypi.org/learning/physical-computing-with-python/distance/ De la web oficial, utiliza la clase.
http://fpaez.com/sensor-ultrasonico-hc-sr04-para-raspberry-pi/ controlado a capon.

2.2. Gestión del robot: ¿Merece la pena empezar el básico con ROS?
Inicialmente programa básico de control de motores y sensor de ultrasonidos.
2.3. Estructura:
Seleccionar los motores y las ruedas.
Base a utilizar.
Interfaces entre la raspi y el hardware.


3. Especificaciones Técnicas:

3.1. Raspberry Pi 3:
Consumos: Raspi entre 700 – 1000 mA, Pins 50 mA max en total y 16 mA max individual. Camara 250 mA











4. Manos a la obra

4.1. Conexión remota a la Raspi (desde casa): Voy a usar VNC. La dirección IP actual es 192.168.0.168.
https://www.raspberrypi.org/documentation/remote-access/ Buen link donde explican varias conexiones posibles.

4.2. Conexión física con el driver de motores L293D:
BCM 5–Pin 29 > L293D–Pin 2 (1A)
BCM 6–Pin 31 > L293D–Pin 7 (2A)
BCM 13(PWM)–Pin 33 > L293D–Pin 1 (1,2 EN)
BCM 17–Pin 11 > L293D–Pin 10 (3A)
BCM 27–Pin 13 > L293D–Pin 15 (4A)
BCM 18(PWM)–Pin 12 > L293D–Pin 9 (3,4 EN)
 

4.3. Conexión física con el sensor de ultrasonidos HC-SR04:
BCM 23–Pin 16 > Echo 
BCM 24–Pin 18 > Trigger




4.4. Como controlar el robot con el teclado del ordenador: ver bibliografia.
4.5. Utilizacion del servo:
	He utilizado la librería GPIOZERO para el control del mismo a traves de la patilla BCM22
http://fpaez.com/controlar-un-servomotor-con-raspberry-pi/
Las caracteristicas del servo SG90 son:
1. Weight: 9 g
2.  Dimension: 22.2 x 11.8 x 31 mm approx.
3.  Stall torque: 1.8 kgf·cm
4.  Operating speed: 0.1 s/60 degree
5.  Operating voltage: 4.8 V (~5V)
6.  Dead band width: 10 µs
7.  Temperature range: 0 ºC – 55 ºC
 
 

Position "0" (1.5 ms pulse) is middle, "90" (~2 ms pulse) is all the way to 
the left. "-90" (~1ms pulse) is all the way to the right, "


5. Software automatico
4. 

6. Bibliografia
http://fpaez.com/    En español tutoriales basicos de uso de raspi con motores e infrarojos.
http://comohacer.eu/category/proyectos-raspberry-pi/ En español, un poco desfasada pero tiene algunos tutoriales que molan.
https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/ Pagina oficial de raspi donde explican entre otras cosas la utilización de las salidas.
https://learn.adafruit.com/simple-raspberry-pi-robot Pagina muy buena con proyectos de Raspi. Tienen un buen ejemplo de lo que quiero.  Muy buenos tutoriales.
http://www.iearobotics.com/wiki/index.php?title=Mini-Skybot Pagina de Obijuan con diferentes proyectos de robot básicos DIY con PICs y Arduino. Tambien buenos tutoriales de las herramientas de diseño libres 3D y FPGAs.
https://www.sparkfun.com/products/retired/11561 Driver para controlar los motores desde la raspi.
http://ingeniapp.com/blog/ Tutoriales en español de raspi.
http://tienda.bricogeek.com/94-raspberry-pi Tienda con bastantes componentes con 24 horas de tiempo de envio.
http://robologs.net/2014/09/16/como-construir-un-controlador-de-motores-npn/ Muy buena pagina en español con distintos tutoriales de raspi, arduino, sensores.
https://geekytheory.com/category/raspberry-pi?page=2 Muy buenos tutoriales de raspberry y arduino.
https://gpiozero.readthedocs.io/en/v1.3.1/api_input.html Explicaciones de la libreria gpiozero.
http://frambuesa-pi.blogspot.com/2015/03/raspberry-pi-primeros-pasos-con.html Buena pagina de tutoriales de raspi en español; incluye tutoriales de python, arduino, etc.
https://seminariopython.wordpress.com/2013/01/28/pygame-3-usando-el-teclado/ Como usar el teclado.
http://robots.linti.unlp.edu.ar/uploads/docs/manual_de_programacion_con_robots_para_la_escuela.pdf Manual con ejemplos de un robot parecido con arduino que al mismo tiempo enseña python, muy educativo.
http://www.iearobotics.com/personal/juan/proyectos/python/pyconsola_io/pyconsola_io.html modulo para obtener las teclas del teclado.
http://robologs.net/2015/06/20/construir-un-robot-bluetooth-con-arduino-y-python/ otro ejemplo para usar el teclado.
http://www.python-course.eu/python3_global_vs_local_variables.php manual de python 3 bastante bueno


7. Apendice

7.1. Explicación de los dos modos de configurar las salidas de raspi.
The GPIO.BOARD option specifies that you are referring to the pins by the number of the pin the the plug - i.e the numbers printed on the board (e.g. P1) and in the middle of the diagrams below.
The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number, these are the numbers after "GPIO" in the green rectangles around the outside of the below diagrams:

7.2. Como ajustar la resolucion de la pantalla para poder trabajar bien en remoto: En resumen hay que modificar las lineas “framebuffer_width” y “framebuffer_height” en el archivo “/boot/config.txt” para que tenga en cuenta esos valores en vez de los estándar. Para una explicación completa de todos los parámetros ver http://frambuesa-pi.blogspot.com/2015/03/raspberry-pi-primeros-pasos-con.html 
5. 

