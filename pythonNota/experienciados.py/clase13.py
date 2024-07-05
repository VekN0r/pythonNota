"""
El programa debe tener un menú de opciones de donde se pueda realizar el pago
del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
una vez sumadas se resten al cupo disponible.
Las opciones disponibles deben estar construidas de la siguiente forma:
1. Pago de Tarjeta de Crédito:
a. El usuario comienza con una deuda de $100.000
b. El usuario puede ingresar un monto para realizar un pago en la
tarjeta de crédito.
c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
d. Se debe verificar que el monto a pagar no exceda el saldo actual de
la tarjeta.
e. Al pagar el sistema debe descontar de la deuda total
f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
saldo de la tarjeta.
2. Simulación de Compras:
a. El usuario puede simular realizar un número ilimitado de compras.
b. Para cada compra, se solicita al usuario ingresar el monto de la
compra. El programa suma los montos de cada compra.
c. Se verifica que el monto de la compra sea mayor o igual a cero.
d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
iteración del bucle for.
3. Salir:
a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
A considerar:
1. Manejo de Errores:
a. Se utilizan bloques try y except para manejar posibles errores al
ingresar datos, validar valores no numéricos y errores inesperados.
2
b. Se debe programar mensajes de error específicos para guiar al
usuario sobre posibles problemas"""
deudaT = 100000
opc = ""
while True:
    print("1.-Pagar tarjeta")
    print("2.-Comprar")
    print("3.-Salir")
    opc == input("Ingrese una opción")

    if opc == "1":
        try:
            pagar = int(input("Ingrese caunto desea pagar."))
            if pagar > 0 and pagar <= deudaT:
                deudaT -= pagar
                print(f"Haz canceleado {pagar} te quedan {deudaT} de la deutatoal")
            else:
                print("Valor fuera de rango")   
        except ValueError:
            print("Valor ingresado invalido")    
    elif opc == "2":
        try:
            try:
                num_compras = int(input("Ingrese la cantidad de compras a simular: "))
                for i in range(num_compras):
                    compra = int(input("El monto de la compra debe ser mayor o igual a cero."))
                    if compra > 0:
                        print("El monto de la compra debe ser mayor o igual a cero.")
                    else:
                        deudaT += compra
                        print(f"Compra realizada por {compra}. Deuda total actualizada: {deudaT}.")
                        break
            except ValueError:
                print("Valor ingresado inválido para el monto de la compra.")
        except ValueError:
            print("Valor ingresado inválido para la cantidad de compras.")        
    elif opc == "3":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Por favor, ingrese una opción válida (1, 2 o 3).")

print("Programa finalizado.")
