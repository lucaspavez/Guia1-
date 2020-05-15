
class Perro():
	
	
	def __init__(self):
		
		self.color = ""
		self.raza = ""
		self.edad = 0
		self.sexo = ""
		self.peso = 0
		self.accion = 0 
		
		
	def agregar_perro(self):
		
		self.color = raw_input("ingrese el color del perro: ")
		self.raza = raw_input("ingrese raza del perro: ")
		self.edad = int(input("ingrese la edad del perro: "))
		self.sexo = raw_input("ingrese el sexo del perro: ")
		self.peso = int(input("ingrese el peso del perro: "))
		
		
		print "se han guardado los atributos de tu perro"
		print ""
		print "su perro es de color:", self.color
		print "es de raza: ", self.raza
		print "su edad es de :  ", self.edad ,"anos"
		print "su sexo es :", self.sexo
		print "su peso es de ",self.peso,"kg" 
		print ""
	def acciones(self):
		
		while True:
			print "      Menu de acciones    "
			print "1. Ladrar "
			print "2. Correr "
			print "3. Pelear con otro perro "
			print "4. Morder a una persona"
			print "5. Salir"
			
			
			self.accion = int(input("seleccione la accion que quiere que el perro efectue: "))-1
			
			print ""
			
			accion_elegida = ["El perro esta ladrando, puede que los recidentes cercanos se enojen, intente hacer que se calle",
							  "El perro se fue corriendo... creo que no volvera",
							  "Se comieron a su perro... lo siento",
							  "Su perro ataco a una persona, sera sacrificado",
							  "Que tenga un buen dia "]
							  
			print accion_elegida[self.accion]
			print ""
			if self.accion == 4:
				break
			
		
		
