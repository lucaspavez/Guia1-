from Clase4 import Clase4

while True:
	
	numero_amigos = int(input("ingrese el numero de personas que se dividiran la cuenta: "))
	cuenta = int(input("ingrese el total de la cuenta: "))
			
	Clase4=Clase4(numero_amigos,cuenta)
	Clase4.agregar()
	Clase4.dividir()
	Clase4.comprobar()
	
	
	
	break


