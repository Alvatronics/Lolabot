#! /usr/bin/python
#---------------------------------------------------------------------------
#--  (C)2007 Juan Gonzalez
#--
#--  Pruebas del modulo consola_io.py. Se saca un menu de opciones
#--
#--  LICENCIA GPL
#---------------------------------------------------------------------------

import consola_io

#-- Caracter de escape
ESC = '\x1B'

#-----------------
#-- Sacar el menu
#-----------------
def menu():
  print """
  
     Menu de opciones
     ----------------
     
     1.- Opcion 1
     2.- Opcion 2
     
  SP.- Volver a sacar el menu
  ESC.- Terminar
  """

#---------------------
#- Comienzo programa
#---------------------

#-- Sacar menu
menu()

#-- bucle principal
while 1:

  #-- Leer tecla
  c = consola_io.getkey()
  
  #-- Procesar tecla
  if   c=='1': print "Opcion 1"
  elif c=='2': print "Opcion 2"
  elif c==' ': menu()
  elif c==ESC: break   #-- Salir del bucle
 
#-- Terminar 
print "-- FIN --"
