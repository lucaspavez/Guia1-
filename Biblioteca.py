from Libro import Libro
import os


Libro1 = None


titulo = ["1984" , "El retrato de Dorian Grey" , "POO"]	
autor = ["George Orwell","Oscar Wilde","Algun sujeto"]
prestados1=0
prestados2=0
prestados3=0


while True:
	ejemplares=10
	print ("    Menu   ")
	print ("1. ver informacion de los libros")
	print ("2. Pedir un libro")
	print ("3. Devolver un libro")
	opcion = int(input("Elija una opcion: "))
	
	Libro1=Libro(ejemplares,ejemplares,ejemplares)
	
	if (opcion == 1):
		
		for i in range(len(titulo)):
					
			print i+1,"Libro: ",titulo[i],". Autor: ",autor[i]
		 
	elif (opcion == 2):
		
		print "escoja el libro que desea llevar: "
		print "1. 1984"
		print "2. El retrato de Dorian Grey"
		print "3.POO"
		opcion2 = int(input("Elija una opcion: "))	
		
		if (opcion2 == 1):
			prestados1 = prestados1 + 1
			ejemplares = ejemplares - prestados1
			
			Libro1.setEjemplares1(ejemplares)
			print  "quedan: ",ejemplares, "ejemplares"	
		
		if (opcion2 == 2):
			prestados2 = prestados2 + 1
			ejemplares = ejemplares - prestados2
			
			Libro1.setEjemplares2(ejemplares)
			print  "quedan: ",ejemplares, "ejemplares"			
		
		if (opcion2 == 3):
			prestados3 = prestados3 + 1
			ejemplares = ejemplares - prestados3
			
			Libro1.setEjemplares3(ejemplares)
			print "quedan: ",ejemplares, "ejemplares"	
		
	elif (opcion == 3):
		
		print "escoja el libro que desea devolver"
		print "1. 1984"
		print "2. El retrato de Dorian Grey"
		print "3.POO"
		opcion2 = int(input("Elija una opcion: "))	
		
		if (opcion2 == 1):
			prestados1 = prestados1 - 1
			ejemplares = ejemplares - prestados1
			
			Libro1.setEjemplares1(ejemplares)
			print  "quedan: ",ejemplares, "ejemplares"	
		
		if (opcion2 == 2):
			prestados2 = prestados2 - 1
			ejemplares = ejemplares - prestados2
			
			Libro1.setEjemplares2(ejemplares)
			print  "quedan: ",ejemplares, "ejemplares"			
		
		if (opcion2 == 3):
			prestados3 = prestados3 - 1
			ejemplares = ejemplares - prestados3
			
			Libro1.setEjemplares3(ejemplares)
			print "quedan: ",ejemplares, "ejemplares"			
			
	
	print ""
	



