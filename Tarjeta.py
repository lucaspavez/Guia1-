

class Tarjeta():
	nombre=""
	saldo=0
	
	def __init__(self, nombre, saldo):
		
		self.nombre = nombre
		self.saldo = saldo
		
	def getNombre(self):
		return self.nombre
		
	def getSaldo(self):
		return self.saldo
		
	def setNombre(self,nuevoNombre):
		self.nombre = nuevoNombre
		
	def setSaldo(self, nuevoSaldo):
		self.saldo = nuevoSaldo
