from abc import ABC, abstractmethod
from datetime import date

class Persona(ABC): 
    _secuencia=0
    def __init__(self, nom, estado=True):
        Persona._secuencia += 1 
        self.__idPersona = Persona._secuencia
        self.nombre = nom
        self.estado = estado

    @property
    def idPersona(self):
        return self.__idPersona

    def mostrarDatos(self):
        print(f''' 
        Codigo: {self.__idPersona}
        Nombre: {self.nombre}
        Estado: {self.estado}
        ''')

class Cliente(Persona):
    _secuencia = 0 
    def __init__(self, nom, ced, estado=True):
        super().__init__(nom, estado)
        Cliente._secuencia += 1 
        self.__idCliente = Cliente._secuencia
        self.nombre = nom
        self.cedula = ced
        self.estado = "El cliente tiene credito" if estado else 'El cliente no tiene credito'

    @property
    def idCliente(self):
        return self.__idCliente

    def mostrarDatosCliente(self):
        # print(f''' 
        # Codigo: {self.__idCliente}
        # Nombre: {self.nombre}
        # Cedula: {self.cedula}
        # Estado: {self.estado}
        # ''')
        return [str(self.idCliente), self.nombre, str(self.cedula), self.estado]


class Factura: 
    _secuencia = 0
    def __init__(self, cliente, total, estado= True):
        Factura._secuencia += 1
        self.__idFactura = Factura._secuencia
        self.cliente = cliente
        self.total = total
        self.estado = "Factura emitida" if estado else 'Factura no emitida'
        self.fecha = date.today()
    
    @property
    def idfactura(self):
        return self.__idFactura

    def mostrarDatosFactura(self):
        # print(f''' 
        # Codigo: {self.__idFactura}
        # Fecha: {self.fecha}
        # Nombre: {self.cliente.nombre}, Cedula: {self.cliente.cedula}
        # Total factura: {self.total}
        # Estado: {self.estado}
        # ''')
        return [str(self.idfactura),self.cliente ,str(self.total), self.estado,str(self.fecha)]

if __name__ == '__main__':
    c = Cliente("Alejandro", True, 953456084)
    # c.mostrarDatosCliente()
    fac = Factura(c, 200, True)
    fac.mostrarDatosFactura()

