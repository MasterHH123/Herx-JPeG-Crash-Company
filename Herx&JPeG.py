#Se inicia el programa
#Se le pide al usuario que ingrese su modelo de auto y nombre completos
inicio=input("Ingresa tu modelo de automovil, marca de vehículo y tu nombre completo (separado por comas), Por favor: ")

print("Rellena lo que se te pide para darte un estimado sobre el costo de reparación")

opcion = int(input("Opción: "))

print(inicio)

#Se imprime una lista de tipos de reparaciones que se ofrecen
#Se le pide al usuario que introduzca cuantas reparaciones necesita o si su tipo de reparacion no aparece en la lista seleccione "otra"
#Se le pregunta al usuario si necesita alguna otra reparación
#Sino se imprime el cobro total por las reparaciones requeridas
def menu():
    print("")
    print("-------------------------------------")
    print("1. Mostrar productos")
    print("2. Mostrar el carrito")
    print("3. Agregar al carrito")
    print("4. Borrar un producto del carrito")
    print("5. Cantidad a pagar")
    print("6. Salir")
    print("")
    opcion = int(input("Opción: "))
    print("")
    return opcion