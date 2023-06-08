from ManejaSabores import ManejaSabores
from claseHelado import Helado

class ManejaHelados:
    
    def __init__(self,__helados):
        self.__helados = []
        
    def registrar_helado(self,helado):
        self.__helados.append(helado)
    
    