from classNodo import Nodo

class Lista:
    def __init__(self):
        self.__comienzo = None
    
    def agregarVehiculo(self,vehiculo):
        nodo = Nodo(vehiculo)
        nodo.setSig(self.__comienzo)
        self.__comienzo=nodo
        
    def agregaVehiculo_Pos(self,vehiculo,sig):
        nodo = Nodo(vehiculo)
        if self.__comienzo == None:
            nodo.setSig(self.__comienzo)
            self.__comienzo = nodo
            print('Se ha establecido el primer elemento de la lista')
        else:
            if sig == '1':
                aux = self.__comienzo
                nodo.setSig=aux
                self.__comienzo = nodo
                print('su nuevo elemento esta en el comienzo de la lista')
            else:
                i=1
                aux = self.__comienzo
                while i < (int(sig)-1) and nodox != None:
                        nodox = aux.getSig()
                        aux = nodox
                        i+=1
                if nodox == None:
                    print('hubo un error en al intentar agregar el elemento')
                else:
                    aux = nodox.getSig()
                    nodox.setSig(nodo)
                    nodo.setSig(aux)

                
                        
                