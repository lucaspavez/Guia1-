#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Cuenta import Cuenta


nombre = input("ingrese su nombre: ")
numero_cuenta = int(input("ingrese el numero de su cuenta: "))
saldo = float(input("ingrese su saldo (es de tipo flotante): "))

Cuenta1 = Cuenta()
Cuenta1.set__nombre(nombre)
Cuenta1.set__numero_cuenta(numero_cuenta)
Cuenta1.setSaldo(saldo)

Cuenta1.mostrar_cuenta()
while True:
	print ("")
	print ("     Menu      ")
	print ("1. Realizar giro")
	print ("2. Ingresar dinero a su tarjeta")
	print ("3. Transferencia a terceros")
	print ("4. Salir del cajero")
	print ("")
	opcion = int(input("Seleccione la opcion que desea ejecutar: "))
	print ("")
	if (opcion == 1):
		monto = float(input("¿Cuanto desea retirar de su tarjeta?: "))
		Cuenta1.giro(monto)
	if (opcion == 2):
		monto = float(input("¿Cuanto desea ingresar en su tarjeta?: "))
		Cuenta1.ingreso(monto)
	if (opcion == 3): 	
		monto = float(input("¿Cuanto desea transferir?: "))
		nombre2 = input("A nombre de quien desea transferir: ")
		Cuenta1.transferencia(monto,nombre2)
	if (opcion == 4):
		print ("Gracias por preferir nuestros servicios")
		print ("Que tenga un buen dia")
		break

		

