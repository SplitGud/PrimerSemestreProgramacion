#Aplicacion para hacer el calculo del IVA de un producto
"""
Autor: Santiago Villa Salazar
Fecha: 01/Marzo/2022
Descripcion: Programa dia del IVA
"""

print("TIPOS DE PRODUCTOS A COMPRAR: \n1)Tipo alimentos \n2)Tipo ropa \n3)Tipo tecnologia \n4)Tipo medicamentos")
tipo_producto = int(input("Digite la opcion a elegir: "))
precio_producto = float(input("Digite el precio del producto: "))

def descuento_producto (producto, precio):
    if precio_producto <= 1500000:
        print("El IVA no aplica a su producto")
    else:
        if tipo_producto > 4 and tipo_producto > 1:
            precio_final = 0
        else:
            if tipo_producto == 1:
                precio = precio_producto * 0.05
                if precio > 200000:
                    precio_final = precio - 20000 - (precio*0.02)
                else: precio_final = precio
            elif tipo_producto == 2:
                precio = precio_producto * 0.19
                if precio > 200000:
                    precio_final = precio - 20000 - (precio*0.02)
                else: precio_final = precio
            elif tipo_producto == 3:
                precio = precio_producto * 0.08
                if precio > 200000:
                    precio_final = precio - 20000 - (precio*0.02)
                else: precio_final = precio
            elif tipo_producto == 4:
                precio = precio_producto * 0.12
                if precio > 200000:
                    precio_final = precio - 20000 - (precio*0.02)
                else: precio_final = precio
            else:
                print("El tipo de producto no existe")
            return precio_final

precio_final = descuento_producto (tipo_producto, precio_producto)
precio_total = (precio_producto + precio_final)
print(f"Su descuento es de {precio_final} y su producto quedo con un valor de {precio_total}")


        