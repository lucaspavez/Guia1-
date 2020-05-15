

class Cuenta():
	
	
	def __init__(self,nombre, numero_cuenta, saldo):
		
		self.nombre = nombre
		self.numero_cuenta = numero_cuenta
		self.saldo = saldo
		
	def getSaldo(self):
		return self.saldo
		
	def setSaldo(self, nuevosaldo):
		self.saldo = nuevosaldo
		
	
