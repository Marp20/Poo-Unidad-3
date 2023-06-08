from ManejaHelados import ManejaHelados
from ManejaSabores import ManejaSabores
from claseHelado import Helado

def menu(self):
    manSabores = ManejaSabores
    manHelados = ManejaHelados
    archivo = input('Ingresar nombre del archivo con sabores disponibles')
    archivo = archivo + '.csv'
    manSabores.carga_sabores(archivo)
    print('       Bienvenido al menu principal.\n   Ingresar una opcion:\n1#Registrar helado\n2#Mostrar helados mas vendidos\n3# Gramos vendidos\n')
    op = input()
    
    if op == '1':
        tipo = input('     Ingresar tipo vendido de entre las opciones.\n A-100gr.  B-150gr    C-250gr.    D-500gr.    E-1000gr')
        if tipo == 'A':
            gramos = 100.00
            precio = 340.00
        elif tipo == 'B':
            gramos = 150.00
            precio = 400.00
        elif tipo == 'C':
            gramos = 250.00
            precio = 500.00
        elif tipo == 'D':
            gramos = 500.00
            precio = 750.00
        elif tipo == 'E':
            gramos = 1000.00
            precio = 1350.00
        helado = Helado(gramos,precio,sabor)
        manHelados.registrar_helado(helado)
    
    elif op == '2':
        
