from menu import Menu
from funciones import borrarPantalla, gotoxy
from crudArchivos import Archivo
from persona import *
from interfaceCalculo import * 
import time

# INGRESO DE DATOS-------------------------------------------------------------------------
def cliente():
   borrarPantalla()     
   gotoxy(20,2);print("Ingresar Cliente")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Nombre: ")
   gotoxy(15,6);print("Cedula: ")
   gotoxy(23,5)
   nombre = input()
   gotoxy(23,6)
   cedula = input()
   gotoxy(15,9);print("Esta seguro de Grabar El registro del cliente(s/n):")
   gotoxy(67,9);grabar = input().lower()
   if grabar == "s":
        archiCliente = Archivo("./archivos/cliente.txt","|")
        clientes = archiCliente.leer()
        if clientes : idSig = int(clientes[-1][0])+1
        else: idSig=1
        cliente = Cliente(nombre,cedula,idSig)
        datos = cliente.mostrarDatosCliente()
        datos = '|'.join(datos)
        archiCliente.escribir([datos],"a")
   else:
        gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
def factura():
   borrarPantalla()     
   gotoxy(20,2);print("Ingresar factura")
   gotoxy(15,4);print("Cliente: ")
   gotoxy(15,5);print("Total: ")
   gotoxy(15,6);print("Estado: ")
   gotoxy(15,7);print("Fecha: ")
   gotoxy(24,4)
   nombre =input()
   gotoxy(22,5)
   total = input()
   gotoxy(15,9);print("Esta seguro de Grabar El registro de la factura(s/n):")
   gotoxy(68,9);grabar = input().lower()
   if grabar == "s":
        archiFactura = Archivo("./archivos/factura.txt","|")
        facturas = archiFactura.leer()
        if facturas : idSig = int(facturas[-1][0])+1
        else: idSig=1
        factura = Factura(nombre,total,idSig)
        datos = factura.mostrarDatosFactura()
        datos = '|'.join(datos)
        archiFactura.escribir([datos],"a")
   else:
        gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
def Dcredito():
   borrarPantalla()     
   gotoxy(20,2);print("Ingresar detalle del credito")
   gotoxy(15,4);print("AAAAMM: ")
   gotoxy(15,5);print("Cuota: ")
   gotoxy(15,6);print("Estado del credito: ")
   gotoxy(23,4)
   aaaamm =input()
   gotoxy(22,5)
   cuota = input()
   archiDCredito = Archivo("./archivos/credito.txt","|")
   creditos = archiDCredito.leer()
   if creditos : idSig = int(creditos[-1][0])+1
   else: idSig=1
   credito = detalleCredito(aaaamm, cuota, idSig)
   datos = credito.mostrarDatosDT()
   datos = '|'.join(datos)
   archiDCredito.escribir([datos],"a")

def ppago():
   borrarPantalla()     
   gotoxy(20,2);print("Ingresar pago")
   gotoxy(15,4);print("Fecha de pago: ")
   gotoxy(15,5);print("Valor: ")
#    gotoxy(33,4)
#    fecha =input()
   gotoxy(22,5)
   valor = input()
   gotoxy(15,7);print("Esta seguro de Grabar El registro del pago (s/n):")
   gotoxy(64,7);grabar = input().lower()
   if grabar == "s":
        archiPago = Archivo("./archivos/pago.txt","|")
        pagos = archiPago.leer()
        if pagos : idSig = int(pagos[-1][0])+1
        else: idSig = 1
        pago = Pago(valor)
        datos = pago.mostrarDatosPago()
        datos = '|'.join(datos)
        archiPago.escribir([datos],"a")
   else:
        gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")  

# CONSULTA DE DATOS----------------------------------------------------------------------------------
def Consultarcliente():
    borrarPantalla()     
    gotoxy(20,2);print("Consultar Clientes")
    lista = []
    with open("./archivos/cliente.txt", 'r') as datos:
        for dato in datos:
            reg = dato[:-1]
            #print(reg.split(";"))
            lista.append(reg.split(";"))
    for lis in lista:
        print(lis)
    time.sleep(5);gotoxy(27,5);print(" "*40)
    borrarPantalla()

        
    # cliente,entCliente = [],None
    # while not cliente:
    #     gotoxy(15,5);print("ID del cliente para buscarlo[  ]")
    #     gotoxy(44,5);id = input().upper()
    #     archiCliente = Archivo("./archivos/cliente.txt","|")
    #     cliente = archiCliente.buscar(id)
    #     if cliente:
    #         entCliente = Cliente(cliente[1],cliente[2]) 
    #         gotoxy(15,7);print("El cliente consultado es: ")
    #         gotoxy(15,8);print('''
    #             Nombre: {}
    #             Cedula: {}
    #             Estado: {}'''.format(entCliente.nombre, entCliente.cedula, entCliente.estado))
    #         time.sleep(3);gotoxy(27,5);print(" "*40)

    #     else: 
    #         gotoxy(27,5);print("No existe el cliente con ese codigo[{}]:".format(id))
    #         time.sleep(2);gotoxy(27,5);print(" "*40)

def ConsultarFactura():
    borrarPantalla()     
    gotoxy(20,2);print("Consultar facturas")
    lista = []
    with open("./archivos/factura.txt", 'r') as datos:
        for dato in datos:
            reg = dato[:-1]
            #print(reg.split(";"))
            lista.append(reg.split(";"))
    for lis in lista:
        print(lis)
    time.sleep(3);gotoxy(27,5);print(" "*40)
    borrarPantalla()

    # factura,entFactura = [],None
    # while not factura:
    #     gotoxy(15,5);print("ID de la factura para buscar[  ]")
    #     gotoxy(44,5);id = input().upper()
    #     archiFactura = Archivo("./archivos/factura.txt","|")
    #     factura = archiFactura.buscar(id)
    #     if factura:
    #         entFactura = Factura(factura[1],factura[2]) 
    #         gotoxy(15,7);print("La factura consultado es: ")
    #         gotoxy(15,8);print('''
    #             Cliente: {}
    #             Un Total de: ${}
    #             Estado: {}'''.format(entFactura.cliente, entFactura.total, entFactura.estado))
    #         time.sleep(3);gotoxy(27,5);print(" "*40)

    #     else: 
    #         gotoxy(27,5);print("No se encontro ninguna factura con el codigo ingresado[{}]:".format(id))
    #         time.sleep(2);gotoxy(27,5);print(" "*40)

def Consultarcredito():
    borrarPantalla()     
    gotoxy(20,2);print("Consultar credito")
    lista = []
    with open("./archivos/credito.txt", 'r') as datos:
        for dato in datos:
            reg = dato[:-1]
            #print(reg.split(";"))
            lista.append(reg.split(";"))
    for lis in lista:
        print(lis)
    time.sleep(3);gotoxy(27,5);print(" "*40)
    borrarPantalla()

    # credito,entCredito = [],None
    # while not credito:
    #     gotoxy(15,5);print("ID del credito para consultar[  ]")
    #     gotoxy(45,5);id = input().upper()
    #     archiCredito = Archivo("./archivos/credito.txt","|")
    #     credito = archiCredito.buscar(id)
    #     if credito:
    #         entCredito = detalleCredito(credito[1],credito[2], credito[3]) 
    #         gotoxy(15,7);print("Credito consultado: ")
    #         gotoxy(15,8);print('''
    #             Fecha: {}
    #             Diferido en: {} cuotas
    #             Estado: {}'''.format(entCredito.aamm, entCredito.cuota, entCredito.estadoCredito))
    #         time.sleep(3);gotoxy(27,5);print(" "*40)

    #     else: 
    #         gotoxy(27,5);print("No se encontro ningun credito con ese codigo[{}]:".format(id))
    #         time.sleep(2);gotoxy(27,5);print(" "*40)

def Consultarpagos():
    borrarPantalla()     
    gotoxy(20,2);print("Consultar pagos")
    lista = []
    with open("./archivos/pago.txt", 'r') as datos:
        for dato in datos:
            reg = dato[:-1]
            #print(reg.split(";"))
            lista.append(reg.split(";"))
    for lis in lista:
        print(lis)
        # gotoxy(27,5);print("No existen pagos")
    time.sleep(3);gotoxy(27,5);print(" "*40)
    borrarPantalla()

    # pago,entPago = [],None
    # while not pago:
    #     gotoxy(15,5);print("ID del pago para buscar en el archivo[  ]")
    #     gotoxy(53,5);id = input().upper()
    #     archiPago = Archivo("./archivos/pago.txt","|")
    #     pago = archiPago.buscar(id)
    #     if pago:
    #         entPago = Pago(pago[1],) 
    #         gotoxy(15,7);print("El pago consultado es: ")
    #         gotoxy(15,8);print('''
    #             Realizado el: {}
    #             Valor cancelado: {}'''.format(entPago.fechapago, entPago.valor))
    #         time.sleep(3);gotoxy(27,5);print(" "*40)

    #     else: 
    #         gotoxy(27,5);print("No existe un pago con ese codigo[{}]:".format(id))
    #         time.sleep(2);gotoxy(27,5);print(" "*40)


# Menu Proceso Principal-----------------------------------------------------------------------------
opc=''
while opc !='6':  
    borrarPantalla()      
    menu = Menu("Menu Cuentas Por Cobrar",["1) Cliente","2) Factura","3) Credito","4) Pagos","5) Consulta Generales","6) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        cliente()                
    elif opc == "2":
        factura()
    elif opc == "3":
        Dcredito()
    elif opc == "4":
        ppago()
    elif opc == "5":
        borrarPantalla()    
        menu5 = Menu("Menu Consulta Generales",["1) Consultar cliente","2) Consultar factura","3) Consultar credito","4) Consultar pago","5) Salir"],20,10)
        opc5 = menu5.menu()
        if opc5 == "1":
            Consultarcliente()
        elif opc5 == "2":
            ConsultarFactura()
        elif opc5 == "3":
            Consultarcredito()
        elif opc5 == "4":
            Consultarpagos()
        elif opc5 == "5":
                pass
    elif opc == "6":
        borrarPantalla()
        print("Gracias por usar nuestro sistema....")
    else:
        print("Opcion no valida") 
    
input("Presione una tecla para salir")
borrarPantalla()