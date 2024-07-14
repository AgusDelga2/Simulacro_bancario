# %%
import re

class Banco:
    
    #Creamos el constructor de la clase Banco
    def __init__(self, clientes):
        self.clientes = clientes
  
    """ def totalDep(self):
        for x in range(len(clientes.datos_clientes)):
            self.cantDepositada += clientes.totalDepositado
            print("El total depositado en el Banco es de $", self.cantDepositada)
    """
    
class Agenda:
    
    def __init__(self):
        self.nombre = input("Ingrese el nombre del cliente: ")
        #Solicitar y validar el dni del cliente
        while True:
            dni = input("Ingrese el DNI del cliente: ")
            if dni.isdigit() and (len(dni) == 7 or len(dni) == 8):
                self.dni = int(dni)
                break
            else:
                print("Por favor, ingrese un DNI válido.")
        # Solicitar y validar el telefono
        while True:
            telefono = input("Ingrese el teléfono del cliente: ")
            if telefono.isdigit():
                self.telefono = telefono
                break
            else:
                print("Por favor, ingrese un número de teléfono válido (sólo números).")

        # Solicitar y validar el email
        while True:
            email = input("Ingrese el email del cliente: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                self.email = email
                break
            else:
                print("Por favor, ingrese un email válido.")
        
        #Creamos un diccionario para almacenar a los clientes
        self.datos_clientes = {}

#clase Clientes que hereda de Agenda
class Clientes(Agenda):
    
    #Contructor de la clase Clientes
    def __init__(self):
        super().__init__()
        self.cantidad = 0
        self.CajaAhorro = CajaAhorro(self.nombre, self.cantidad)
        self.PlazoFijo = PlazoFijo(self.nombre, 0,0,0.0)
        #se actualiza el diccionario
        self.datos_clientes[self.dni] = [self.nombre, self.cantidad]
        
    #Método depositar
    def depositar(self):
        #Solicitar el monto y verificar que sea valido
        while True:
            monto = input("Ingrese el monto a depositar: ")
            if monto.replace('.', '', 1).isdigit() and float(monto) > 0:
                self.cantidad += float(monto)
                break
            else:
                print("Por favor, ingrese un monto válido (un número positivo).")
        #monto = int(input("Ingrese el monto a depositar: "))
        #acumula los montos depositados por el cliente
        #self.cantidad += monto
        #se actualiza el diccionario
        self.datos_clientes[self.dni] = [self.nombre, self.cantidad]
    
    #Método extraer, controlamos que la extracción sea menor al saldo de la cuenta
    def extraer(self):
        importe = int(input("Ingrese el importe a extraer $"))
        #el monto a extraer debe ser menor al saldo xq no puede quedar la cuenta en $0
        while importe > self.cantidad:
            print("Saldo insuficiente: $",self.cantidad)
            importe = int(input("Ingrese el importe a extraer $"))
        #ingresado el monto correcto, se descuenta del saldo de la cuenta del cliente
        self.cantidad -= importe
        print("****Retire su dinero****")
        #se actualiza el diccionario
        self.datos_clientes[self.dni] = [self.nombre, self.cantidad]
        
    #Método mostrar Total
    def imprimirTotal(self):
        total = self.cantidad
        print("Su saldo actual es de $", total)
        
        

# %%
#clase Padre, que será heredada de Caja de Ahorro y Plazo Fijo   
class Cuentas:
    
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        
    def imprimir(self):
        print("Titular de la Cuenta ", self.titular)
        print("Saldo de la Cuenta ", self.cantidad)
        
#clase hija de Cuentas
class CajaAhorro(Cuentas):
    
    #constructor de la clase, hereda el constructor de Cuentas
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
    
    #Método para impirmir los datos de la Caja de Ahorro
    def imprimir(self):
        print("***Caja de Ahorro***")
        super().imprimir()
        
class PlazoFijo(Cuentas):
    #constructor de la clase, hereda el constructor de Cuentas
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes
        
    def importeInteres(self):
        interesTotal = self.cantidad * self.interes/100
        return interesTotal
    
    #Método para impirmir los datos del Plazo Fijo
    def imprimir(self):
        print("***Plazo Fijo***")
        super().imprimir()
        print("El plazo fijo es a ", self.plazo, "días, con tasa de interés de ", self.interes, "%")
        print("El interés total es de ", self.importeInteres())
        
            

# %%
cliente = Clientes()
print(cliente.datos_clientes)
banco = Banco(cliente)
cliente.depositar()
cliente.extraer()
cliente.imprimirTotal()


# %%
cliente.CajaAhorro.imprimir()
print(cliente.PlazoFijo.importeInteres())


