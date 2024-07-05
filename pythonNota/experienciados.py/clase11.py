"""Deberás construir un programa que está diseñado para ayudar en la venta
de pasajes. Inicia preguntándote cuántos pasajes deseas vender. Luego,
utiliza un proceso organizado (llamado bucle for) para pedirte el precio de
cada pasaje por separado. Si ingresas un valor que no es un número, te
indica que necesitas proporcionar un valor numérico válido. Al final, muestra
el monto total que se ha obtenido por la venta de todos los pasajes
 Solicita al usuario la cantidad de pasajes a vender.
 Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
 Dentro del bucle, se solicita al usuario el precio de cada pasaje y se
acumula en la variable totalIngresos.
 Si el usuario ingresa un valor no numérico para el precio del pasaje,
el programa muestra un mensaje y sale del bucle usando break.
 Finalmente, se imprime el total de ingresos por la venta de pasajes"""

total = 0
while True:
    try:
        cantPa = int(input("Ingrese la cantidad de pasajes a vender: "))
        break 
    except ValueError:
        print("Valor ingresado inválido. Intente nuevamente.")

for i in range(cantPa):
    while True:
        try:
            valorPasaje = int(input(f"Ingrese valor del pasaje {i+1}: "))
            total += valorPasaje
            break  
        except ValueError:
            print("El valor ingresado es inválido. Intente nuevamente.")
            break
print(total)        
       
