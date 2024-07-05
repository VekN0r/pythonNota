"""5) Cree un sistema de ventas de supermercado en el cual se pueda agregar productos
al carro de compras, las opciones del menú serán.
1. Agregar productos
2. Ver canasta
3. Ver total
4. Salir
 En agregar productos deberá mostrar un menú con 5 productos y sus
precios (creado por usted), cada vez que se seleccione un producto
quedará agregado en la lista.
 Ver canasta, es mostrar todos los productos seleccionados.
 Ver total, es mostrar el total a pagar por el cliente"""
productos = {}
while True:
    print("1.-Agregar productos")
    print("2.-Ver canasta")
    print("3.-Ver total")
    print("4.-Salir")
    opc = input()

    if opc == "1":
        produc = input("Añada producto: ")
        valor = float(input("Añada el valor del producto: ")) 
        productos[produc] = valor  
        print(f'{produc} agregado a la canasta.')
    elif opc == "2":
        for clave, valor in productos.items():
            print(f'Prodcuto: {clave}, Valor: {valor}')
    elif opc == "3":
        total = sum(productos.values())
        print(f'Total de la canasta: ${total: }')     
    elif opc == "4":
        break    
print(productos)    