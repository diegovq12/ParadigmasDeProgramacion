import os

class Cuenta:
    def __init__(self,numero_cuenta, titular, cantidad):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.cantidad = cantidad
        
    def depositar(self,cantidad):
        self.cantidad += cantidad
        print(f"Deposito realizado, su saldo actual es de: {self.cantidad}")
    
    def retirar(self,cantidad):
        if self.cantidad < cantidad:
            print("No cuenta con saldo suficiente")
        else:
            self.cantidad -= cantidad
            print(f"Retiro realizado, su saldo actual es de: {self.cantidad}")
            
    def transferir(self,destino,monto):
        if self.cantidad < monto:
            print("No cuenta con saldo suficiente")
        else:
            self.cantidad -= monto
            destino.cantidad += monto
            print(f"Transferencia realizada, su saldo actual es de: {self.cantidad} \n")
    
    def __str__(self):
        return f"Numero de cuenta: {self.numero_cuenta}\nTitular: {self.titular}\nCantidad: {self.cantidad}"
    
class CuentaAhorros(Cuenta):
    def __init__(self, numero_cuenta, titular, cantidad, interes):
        super().__init__(numero_cuenta, titular, cantidad)
        self.interes = interes
        
    
    def calcular_interes(self):
        self.cantidad += self.cantidad * self.interes
        return self.cantidad
    
    def __str__(self):
        informacion_base = super().__str__()
        return f"{informacion_base}\nInteres: {self.interes} \nSaldo con interes: {self.calcular_interes()}"
    
class Banco:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cuentas = []
        self.numero_cuentas = 0
        
    def crear_cuenta(self,titular,cantidad):
        self.numero_cuentas += 1
        nueva_cuenta = Cuenta(self.numero_cuentas,titular,cantidad)
        self.cuentas.append(nueva_cuenta)
        print(f"Cuenta creada con exito, su numero de cuenta es: {self.numero_cuentas}")
        return nueva_cuenta
    
    def crear_cuenta_ahorros(self,titular,cantidad,interes):
        self.numero_cuentas += 1
        nueva_cuenta = CuentaAhorros(self.numero_cuentas,titular,cantidad,interes)
        self.cuentas.append(nueva_cuenta)
        return nueva_cuenta
    
    def getCuenta(self,numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None
    
    def __str__(self):
        result = f"Banco: {self.nombre}\n"
        for cuenta in self.cuentas:
            result += str(cuenta) + "\n"
            result += "----------------------------\n"
        return result
            

banco = Banco("Bancoppel QVDD")



def menu():
    while True:
        print("Bienvenido al Banco")
        print("1. Crear cuenta")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Transferir")
        print("5. Consultar saldo")
        print("6. Imprimir todas las cuentas del banco")
        print("7. Imprimir una cuenta en especifico")
        print("8. Salir")
        
        opcion = input("Ingrese el numero de la opcion que desea realizar: ")
        
        if opcion == "1":
            #preguntar al usuario si es cuenta de ahorros o cuenta normal
            tipo_cuenta = input("Ingrese el tipo de cuenta que desea crear (1. Cuenta normal, 2. Cuenta de ahorros): ")
            if tipo_cuenta == "1":
                titular = input("Ingrese el nombre del titular: ")
                cantidad = float(input("Ingrese la cantidad inicial: "))
                cuenta = banco.crear_cuenta(titular, cantidad)
            elif tipo_cuenta == "2":
                interes = input("Ingrese el interes de la cuenta de ahorros 1 - [0.5] 2 - [0.1] 3 - [0.05]: ")
                if interes == "1":
                    interes = 0.5
                elif interes == "2":
                    interes = 0.1
                elif interes == "3":
                    interes = 0.05
                titular = input("Ingrese el nombre del titular: ")
                cantidad = float(input("Ingrese la cantidad inicial: "))
                cuenta = banco.crear_cuenta_ahorros(titular, cantidad, interes)
            else:
                print("Opcion invalida")
        elif opcion == "2":
            numero_cuenta = int(input("Ingrese el numero de cuenta: "))
            cuenta = banco.getCuenta(numero_cuenta)
            if cuenta:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cuenta.depositar(cantidad)
            else:
                print("Cuenta no encontrada")
        
        elif opcion == "3":
            numero_cuenta = int(input("Ingrese el numero de cuenta: "))
            cuenta = banco.getCuenta(numero_cuenta)
            if cuenta:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad)
            else:
                print("Cuenta no encontrada")
        
        elif opcion == "4":
            numero_cuenta_origen = int(input("Ingrese el numero de cuenta origen: "))
            cuenta_origen = banco.getCuenta(numero_cuenta_origen)
            if cuenta_origen:
                numero_cuenta_destino = int(input("Ingrese el numero de cuenta destino: "))
                cuenta_destino = banco.getCuenta(numero_cuenta_destino)
                if cuenta_destino:
                    cantidad = float(input("Ingrese la cantidad a transferir: "))
                    cuenta_origen.transferir(cuenta_destino, cantidad)
                else:
                    print("Cuenta destino no encontrada")
            else:
                print("Cuenta origen no encontrada")
        
        elif opcion == "5":
            numero_cuenta = int(input("Ingrese el numero de cuenta: "))
            cuenta = banco.getCuenta(numero_cuenta)
            if cuenta:    
                print(cuenta)

        elif opcion == "6":
            print(banco)
        
        elif opcion == "7":
            numero_cuenta = int(input("Ingrese el numero de cuenta: "))
            cuenta = banco.getCuenta(numero_cuenta)
            if cuenta:
                print(cuenta)
            else:
                print("Cuenta no encontrada")
        
        elif opcion == "8":
            print("Gracias por utilizar nuestros servicios. ¡Hasta luego!")
            break
        
        else:
            print("Opcion invalida. Por favor, ingrese una opcion valida.")
        
        input("Presione cualquier tecla para continuar...")
        os.system("cls")
        
menu()

# menu()

# banco = Banco("Bancoppel")

# cuenta1 = banco.crear_cuenta("Juan Perez",1000)

# cuenta2 = banco.crear_cuenta_ahorros("Maria Lopez",5000,0.05)

# print(banco)

# cuenta1.depositar(500)
# cuenta1.retirar(350)

# cuenta2.depositar(1000)
# cuenta2.retirar(500)

# print(banco)

# cuenta1.transferir(cuenta2,250)

# print(banco)