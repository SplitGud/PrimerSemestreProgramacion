"""
Autor: Santiago Villa Salazar
Fecha: 29/Abril/2022
Descripcion: Programa bucle con FOR
"""
n = int(input("Digite el numero: "))
if n >= 1:
    for i in range (1, n+1):
        for j in range (1, i+1):
            print (j, end=" ")
        print (" ")
else:
    print ("Valor dado no valido")
    