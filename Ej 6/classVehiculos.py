import json
from pathlib import Path

class Vehiculo:
    def __init__(self,modelo,puertas,color,preciob):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__preciob = preciob
    
class VehiculoNuevo(Vehiculo):
    def __init__(self,version):
        self.__version = version     
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                modelo = self.__modelo,
                puertas = self.__puertas,
                color = self.__color,
                preciob = self.__preciob,
                version = self.__version
            )
        )
        return d
    
class VehiculoUsado(Vehiculo):
    def __init__(self,patente,anio,KM):
        self.__patente = patente
        self.__anio = anio 
        self.__KM = KM

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                modelo = self.__modelo,
                puertas = self.__puertas,
                color = self.__color,
                preciob = self.__preciob,
                patente = self.__patente,
                anio = self.__anio,
                KM = self.__KM,
            )
        )
        return d
             
    
    
    

