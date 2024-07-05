"""
Objetivo del programa: Un programa funcional que, dada una lista de números
ingresada por el usuario, identifica y muestra los números pares e impares de
manera clara y organizada.
Reglas de negocio:
1. Solicitar al usuario que ingrese una lista de números enteros
separados por espacios.
2. Implementar una función llamada validar_lista_numeros que verifique
que todos los elementos ingresados sean números enteros. Si se
ingresa algún valor no válido, solicitar nuevamente la lista.
3. la función validar_lista_numeros debe utilizar un bucle y maneja
excepciones para asegurar que todos los elementos ingresados sean
números enteros.
4. Utilizar el operador de módulo % (MOD) para determinar si un
número es par o impar en la lista de números a ingresar. Considerar
que un número es par cuando el mod es igual a 0, en caso contrario,
es impar
5. Crear dos listas separadas: una para los números pares y otra para
los impares.
6. Mostrar al usuario las listas resultantes, indicando los números
pares, e indicando los números impares
"""

def numParoImpar(lista):
    listaPar = []
    listaImpar = []
    for num in lista:    
        if num % 2 == 0:
            listaPar.append(num)
        else:
            listaImpar.append(num)
    return listaPar, listaImpar
def validarListaNumeros(lista): 
        try:
            numerosVal = [int(i) for i in lista]
            print("La lista se ingreso correctamente")
            return numerosVal, False
        except:
            print("Se encontro un dato incorrecto")
            return None, True    
while True:
    try:
        numerosEntrada = input("Ingrese una lista de números separados por espacios: ")
        numeros = numerosEntrada.split()
        numerosValidados, errorEncontrado = validarListaNumeros(numeros)
        if errorEncontrado:
            continue         
    except ValueError as r:
        print(f"Error: {r}")
        continue
    else:
        listaPar, listaImpar = numParoImpar(numerosValidados)
        print(f"\nNúmeros pares: {listaPar}")
        print(f"Números impares: {listaImpar}")                
        res = input("¿Desea otra lista? (S/N)").upper()
        if res == "S":
            continue
        else:
            print("Hasta la próxima")
            break