from Cuenta import Cuenta

nombre = raw_input("ingrese su nombre: ")
numero_cuenta = int(input("ingrese el numero de su cuenta: "))
saldo = float(input("ingrese su saldo (es de tipo flotante): "))

Cuenta1 = Cuenta(nombre, numero_cuenta,saldo)

