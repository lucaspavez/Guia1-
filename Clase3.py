
class Clase3():
	
	
	def __init__(self, numero):
		
		self.numero = numero 
		print "el numero ingresado es: ", numero
		
	def transformar(self):
		
		miles = self.numero/1000 
		cientos = (self.numero/100)-miles*10
		decenas = (self.numero/10)-(miles*100+cientos*10)
		unidad = (self.numero%10)
		
		primero = miles
		segundo = (primero + cientos)%10
		tercero = (segundo + decenas)%10
		cuarto = (tercero + unidad)%10
		
		print miles,cientos,decenas,unidad		
		print primero,segundo,tercero,cuarto
		
		miles = (tercero + 7)%10
		cientos= (cuarto + 7)%10
		decenas = (primero + 7)%10
		unidad = (segundo + 7)%10
		
		print miles, cientos, decenas, unidad
		
		final = miles*1000+cientos*100+decenas*10+unidad
		print "El numero modificado es: ",final
		
		
		
		
