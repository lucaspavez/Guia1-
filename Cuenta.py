#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Cuenta():
	
	
	def __init__(self):
		
		self.__nombre = ""
		self.__numero_cuenta = 0
		self.saldo = 0.0
		
		
	def transferencia(self,monto,nombre):
		if (monto < self.saldo):
			self.saldo = self.saldo - monto
			print ("----------------------------------------------------")
			print ("se ha transferido {0:.2f} a nombre de {1}".format(monto,
																	  nombre))
			print ("Ahora su cuenta dispone de {0:.2f}".format(self.saldo))
			print ("----------------------------------------------------")
			True
		else:
			print ("Su tarjeta no dispone de ese saldo")
			False
			
	def ingreso(self,monto):
		if (0 < monto):
			self.saldo = self.saldo + monto
			print ("--------------------------------------------")
			print ("Ahora su tarjeta dispone de {0:.2f}$ de saldo".format(self.saldo))
			print ("--------------------------------------------")
			True
		else:
			print ("ingrese un valor positivo porfavor ")
			False
		
	def giro(self,monto):
		if (monto < self.saldo):
			if (0 < monto):
				self.saldo = self.saldo - monto
				print ("---------------------------------------------------------------")
				print ("Ahora usted dispone de {0:.2f}$ saldo en su tarjeta".format(self.saldo))
				print ("---------------------------------------------------------------")
				
			else:
				("Ingrese una cantidad positiva")
		else:
			print ("Usted no dispone de saldo suficiente")
			
	def mostrar_cuenta(self):
		print ("---------------Tarjeta registrada-----------------------")
		print ("Nombre: {0}, Numero de cuenta: {1}, Saldo: {2:.2f}".format(self.__nombre,
																		self.__numero_cuenta,
																		  self.saldo))
		print ("--------------------------------------------------------")
		
	def getSaldo(self):
		return self.saldo
		
	def setSaldo(self, nuevosaldo):
		self.saldo = nuevosaldo
		
	def get__nombre(self):
		return self.__nombre
		
	def set__nombre(self,nombre):
		self.__nombre = nombre
			
	def get__numero_cuenta(self):
		return self.__numero_cuenta
		
	def set__numero_cuenta(self, numero):
		self.__numero_cuenta = numero 
		
	
