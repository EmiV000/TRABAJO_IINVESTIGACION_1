from funciones import gotoxy, borrarPantalla
import time

class Menu:
    def __init__(self,titulo="",opciones=[],col=1,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col+5,self.fil);print(self.titulo)
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones))) 
        return opc   

if __name__ == '__main__':
    borrarPantalla()    
    menu = Menu("Menu Cuentas Por Cobrar",["1) Cliente","2) Factura","3) Credito","4) Pagos","5) Consulta Generales","6) Salir"],2,2)
    menu.menu()