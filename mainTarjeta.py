from Tarjeta import Tarjeta
import os


tarjeta1 = None

while True:
	
	print ("    Menu   ")
	print ("1. Agregar tarjeta")
	print ("2. Modificar saldo")
	print ("3. Salir de aplicacion")
	
	opcion = raw_input("Seleccione una opcion: ")
	
	if (opcion == "1"):
		nombre = raw_input("escribe nombre: ")
		saldo = int(input("escribe saldo: "))
		tarjeta1 = Tarjeta(nombre,saldo)
		print "se ha agregado la tarjeta correctamente"
		
	if (opcion == "2"):
		compra=0
		compra = int(input("escribe el valor de la compra: "))
		
		saldo = saldo - compra
		tarjeta1.setSaldo(saldo)
		print "ha realizado una compra de ",compra,"$"
		print "A la tarjeta de ",nombre,"Le queda ",saldo,"$ dinero en su tarjeta"
		
	if (opcion == "3"):
		break
	
		

	
	
