def startupmenu():
    print("Rellena lo que se te pide para darte un estimado sobre el costo de reparación")
    input("")
opcion = int(input("Opción: "))
print("")
    return opcion

#Se inicia el programa
#Se le pide al usuario que ingrese su modelo de auto y nombre completos
inicio=input("Ingresa tu modelo de automovil, marca de vehículo y su nombre completo (separado por comas), Por favor: ")
#Se imprime una lista de tipos de reparaciones que se ofrecen
#Se le pide al usuario que introduzca cuantas reparaciones necesita o si su tipo de reparacion no aparece en la lista seleccione "otra"
#Se le pregunta al usuario si necesita alguna otra reparación
#Sino se imprime el cobro total por las reparaciones requeridas
print(inicio)