nombre=input("Ingresa tu nombre completo: ")
inicio=input("Ingresa tu modelo de automovil, marca de vehículo y año de este (separado por comas), Por favor: ")
problema=input("Que problema tiene su automovil?")
print(inicio)
print("Rellena lo siguiente para darte un estimado sobre el costo de tu reparación")
def menu():
    print("1.- Tipo de reparaciones")
    print("2.- Elegir reparaciones")
    print("3.- Cancelar una reparacion")
    print("4.- Imprimir recibo")
    print("5.- Salir")
    print("")
    opcion = int(input("Opción: "))
    print("")
    return opcion

def mostrar_reparaciones(l_productos, l_precio):
    listp1 = len(l_productos)
    # print("No.      Reparacion      Precio")
    print("{:<5s}{:<15s}{:>16s}".format("No.", "Nombre", "Precio"))
    for i in range(listp1):
        print("{:<5d}{:<15s}{:>16.2f}".format(i + 1, l_productos[i], l_precio[i]))


def reparacionesadicionales():

    mostrar_reparaciones(lista_de_reparaciones, lista_de_precio)

    print("------------------------")
    num_reparaciones = int(input("Ingresa la opcion de la reparacion que ocupas: "))
    cant_reparaciones = int(input("Cuantas reparaciones quieres de este tipo: "))
    carrito_reparaciones.append(num_reparaciones - 1)
    cantidad_reparaciones.append(cant_reparaciones)


#Lista de las reparaciones
lista_de_reparaciones = ["Raspon ", "Abolladura leve ", "Abolladura grave", "Cambio de pieza ", "Llantas ", "Pintura  "]
#Lista de los precios de reparacion
lista_de_precio =    [900,      2400,         3500,      6500,   1500,      10000]
#Lista de las reparaciones actuales
carrito_reparaciones = []
#Lista de la cantidad de reparaciones
cantidad_reparaciones = []

#Opción del menu
opcion = 0

#Mientras la opción  no sea igual a 5 repetir el menu
#Mientras la opción sea diferente a 5 repetir el menu
while opcion != 5:

    opcion = menu()

    if opcion == 1:
        mostrar_reparaciones(lista_de_reparaciones, lista_de_precio)
    elif opcion == 2:
        reparacionesadicionales()
    elif opcion == 3:
        listp1 = len(carrito_reparaciones)
        print("---------- estimado -----------")
        print("Opcion     Tipo de reparacion      Precio($mx)       No. Reparaciones")
        for i in range(listp1):
            print(i+1,". ", lista_de_reparaciones[ carrito_reparaciones[i] ],"    ",lista_de_precio[ carrito_reparaciones[i] ], "   ", cantidad_reparaciones[i])
        print("------------------------")
        #Se ve que reparacion se quiere cancelar
        num_producto = int(input("Ingresa la opcion de la reparacion que quieres cancelar: "))
        #Sustituir por un 0 el valor de la reparacion a cancelar
        carrito_reparaciones[ num_producto-1 ] = -1
        cantidad_reparaciones[ num_producto-1 ] = -1
        #Removerlo de la lista de reparaciones
        carrito_reparaciones.remove(-1)
        cantidad_reparaciones.remove(-1)

    elif opcion == 4:
        total = 0.0
        listp1 = len(carrito_reparaciones)
        for i in range(listp1):
            total = total + lista_de_precio[ carrito_reparaciones[i] ] * cantidad_reparaciones[i]
        print("Su estimado ha llegado a un total de: ", total)
        print("")
        print(":)")
    elif opcion == 5:
        print("Gracias por usar el programa")
    else:
        print("Opción invalida.")








