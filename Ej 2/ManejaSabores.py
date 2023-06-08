import csv
from claseSabor import Sabor

class ManejaSabores:
    def __init__(self):
        self.__sabores = []
    
    def carga_sabores(self,filename):
        with open(filename, 'r') as archivo:
            reader= csv.reader(archivo, delimiter=';')
            for row in reader:
                sabor=Sabor(int(row[0]),row[1],row[2])
                self.__sabores.append(sabor)