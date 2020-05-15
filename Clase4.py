
class Clase4():



	def __init__(self,numero_amigos,cuenta):	
		
		self.__amigos = []
		self.__saldoamigos = [] 
		
		self.cuenta = cuenta
		self.numero_amigos = numero_amigos
		
		self.pp = 0
		self.falta = 0
		
	def agregar(self):		
		i=0
		while (i < self.numero_amigos):
		
			amigo = raw_input("ingrese un amigo: ")
			saldo = int(input("ingrese el saldo: "))
			
			self.__amigos.append(amigo)
			self.__saldoamigos.append(saldo)
			print self.__amigos
			print self.__saldoamigos
			
			i = i+1
			
	def dividir(self):		
		#se le agrega 19% de iva y 10% de propina
		self.cuenta = self.cuenta + ((self.cuenta/100)*29)		
		print "La cuenta mas IVA y propina es: ",self.cuenta
		self.pp = self.cuenta/self.numero_amigos		
		print "cada persona debe pagar: ",self.pp
	
	def comprobar(self):
		i=0
		while(i < self.numero_amigos):
			if (self.pp < self.__saldoamigos[i]):
				
				self.__saldoamigos[i] = self.__saldoamigos[i]-self.pp
				
				print self.__amigos[i],"quedo con: ",self.__saldoamigos[i],"$"
				self.cuenta = self.cuenta-self.pp
				print "Falta pagar",self.cuenta
				
				i=i+1
			else:				
				print self.__amigos[i],"no tiene saldo suficiente"
				self.cuenta = self.cuenta - self.__saldoamigos[i]
				self.falta = self.pp - self.__saldoamigos[i]
				j=0
				while(j < self.numero_amigos):
					if(self.pp < self.__saldoamigos[j]):
						self.__saldoamigos[j]=self.__saldoamigos[j]-self.falta
						self.cuenta = self.cuenta-self.falta
						print self.__amigos[j], "ha pagado lo que le faltaba a: ", self.__amigos[i]
						print self.__amigos[j], "quedo con ", self.__saldoamigos[j]
						j = self.numero_amigos + 1 
					else:
						j=j+1		
				i=i+1
		print "falta pagar",self.cuenta
		
		if(self.cuenta!=0):
			print "como no tienen dinero suficiente para pagar lo que consumieron tendran que lavar los platos y ordenar el restauratn"
		else:
			print "la cuenta esta pagada pueden retirarse"
		
		
		
		
		
			
		
		
		
		
		
	
