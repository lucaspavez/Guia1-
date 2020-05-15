class Libro():
	
	ejemplares1 = 10
	ejemplares2 = 10
	ejemplares3 = 10
	
	def __init__(self, ejemplares1, ejemplares2, ejemplares3 ):
		
		self.ejemplares1 = ejemplares1
		self.ejemplares2 = ejemplares2
		self.ejemplares3 = ejemplares3

	
	def getEjemplares1(self):
		return self.ejemplares1
		
	def setEjemplares1(self, nuevosEjemplares):
		self.ejemplares1 = nuevosEjemplares
		
		
	def getEjemplares2(self):
		return self.ejemplares2
		
	def setEjemplares2(self, nuevosEjemplares):
		self.ejemplares2 = nuevosEjemplares
		
	def getEjemplares3(self):
		return self.ejemplares3
		
	def setEjemplares3(self, nuevosEjemplares):
		self.ejemplares3 = nuevosEjemplares		
	

	
