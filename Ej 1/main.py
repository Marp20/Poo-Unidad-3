from ManejaFacultades import ManejadorFacultades
import os

os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
	Manejador = ManejadorFacultades()
	Manejador.CargaLista()

	opcion = None
	while opcion != '0':
		print("\nMenu opciones")
		print("1- Ingresar el código  de una facultad: ")
		print("2- Ingresar nombre de la carrera: ")
		print("0- Salir")

		opcion = input("\nIngrese opcion: ")

		if opcion == '1':
			codigo = int(input("Ingrese codigo de facultad: "))
			Manejador.BuscaFacultad(codigo)

		if opcion == '2':
			nomCarrera = input("Ingrese nombre de la carrera: ")
			Manejador.BuscaCarrera(nomCarrera)

		if opcion == '3':
			print("Saliendo...")