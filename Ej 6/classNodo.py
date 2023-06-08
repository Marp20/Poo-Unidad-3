from classVehiculos import Vehiculo

class Nodo:
    __vehiculo: Vehiculo
    __siguiente: object
    
    def __init__(self,vehiculo):
        self.__vehiculo = vehiculo
        self.__siguiente = None
        
    def setSig(self,siguiente):
        self.__siguiente=siguiente
    
    def getSig(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__vehiculo