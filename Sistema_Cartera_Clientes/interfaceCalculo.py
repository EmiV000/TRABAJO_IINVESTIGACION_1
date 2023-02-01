from abc import abstractmethod, ABC
from datetime import date
from persona import Factura, Cliente


class calculo(ABC): 

    @abstractmethod
    def realizarPago(self):
        pass

class Pago(calculo):
    _secuencia = 0
    def __init__(self, valor):
        Pago._secuencia += 1 
        self.__idPago = Pago._secuencia
        self.valor = valor
        self.fechapago = date.today()

    @property
    def idPago(self):
        return self.__idPago

    def mostrarDatosPago(self):
        # print(f''' 
        # Numero de pago: {self.__idPago}
        # Fecha de pago: {self.fechapago} 
        # Valor cancelado: {self.valor}''')
        return [str(self.idPago), str(self.fechapago), str(self.valor)]

    def realizarPago(self):
        return "Pago realizado"


class detalleCredito: 
    _secuencia = 0
    def __init__(self, aamm, cuota, estCredito):
        detalleCredito._secuencia += 1 
        self.__idDetcredito = detalleCredito._secuencia
        self.aamm = aamm
        self.cuota = cuota
        self.estadoCredito = "Credito aprobado" if estCredito else "Credito denegado"
        self.detallePago = []
    
    @property
    def iddetCredito(self):
        return self.__idDetcredito

    def mostrarDatosDT(self):
        # print(f'''
        # Id del credito: {self.__idDetcredito} 
        # AAMM: {self.aamm} 
        # Cuota: {self.cuota} 
        # Estado del credito: {self.estadoCredito} 
        # ''')
        # for det in self.detallePago:
        #     print(f''' Fecha del pago: {det.fechapago} \n Valor de pago:  {det.valor}''')
        return [str(self.iddetCredito), str(self.aamm), str(self.cuota), self.estadoCredito]


    def agregarPago(self,valor):
        detalle = Pago(valor)
        #calculos
        self.detallePago.append(detalle)


class cabCredito:
    _secuencia = 0
    def __init__(self, factura, deuda, numcuotas, cuota, aammInitial, estado):
        cabCredito._secuencia += 1
        self.__idCabCredito = cabCredito._secuencia
        self.factura = factura
        self.fecha = date.today()
        self.deuda = deuda
        self.numeroCuotas = numcuotas
        self.cuota = cuota
        self.aammInicial = aammInitial
        self.estado = estado
        self.detalleCredito = []

    @property
    def idcabCredito(self):
        return self.__idCabCredito

    @staticmethod
    def getInteres():
        return  "Credito Aprobado"

    def agregardetalleCredito(self,aamm, cuota, estCredito):
        detalle = detalleCredito(aamm, cuota, estCredito)
        self.detalleCredito.append(detalle)

    def mostrarDatosCabCredito(self):
        print(f''' 
        Id cabCredito: {self.__idCabCredito}
        Factura a nombre: {self.factura.cliente.nombre}  Cedula: {self.factura.cliente.cedula}
        Fecha: {self.fecha}
        Deuda: {self.deuda}
        Numero de cuotas: {self.numeroCuotas}
        Cuota: {self.cuota}
        Fecha Inicial: {self.aammInicial}
        Estado: {self.estado}
        ''')
        for detCabCredi in self.detalleCredito:
            print(f'''
        Fecha del datalle credito: {detCabCredi.aamm} 
        Cuotas del datalle credito: {detCabCredi.cuota}
        Estado del detalle del credito: {detCabCredi.estadoCredito} ''')

if __name__ == '__main__':
    c = Cliente("Alejandro", 953456084, True)
    fac = Factura(c, 200, True)
    # fac.mostrarDatosFactura()
    pago = Pago(200)
    #pago.mostrarDatosPago()
    det = detalleCredito("2023/01", 20, True)
    # det.agregarPago(200)
    # det.mostrarDatosDT()
    cabcredit = cabCredito(fac, 500, 10, 50, "2023/01", True)
    cabcredit.agregardetalleCredito("2023/01", 20, True)
    cabcredit.mostrarDatosCabCredito()
    #print(cabcredit.getInteres())
