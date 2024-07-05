from funcionesCAL import sumar, resta, mul, div, validarNum
while True:
    print("*" * 30)
    print("\t1.-Sumar")
    print("2.-Restar")
    print("3-Multiplicar")
    print("4.-Dividir")
    print("5.-Salir")
    opc = input("Ingrese su opcion")
    if opc == "5":
        print("Hasta la proxima")
        break
    elif opc in ["1","2","3","4"]:
        try:
            numero1 = validarNum(input("Ingrese primer valor: "))
            numero2 = validarNum(input("Ingrese segundo valor: "))
            if numero1 is None or numero2 is None:
                raise ("Uno de los valores ingresados no es un número válido.")
        except :
            print(f"Error")
            continue
        if opc == "1":
            resulSum = sumar(numero1,numero2)
            print(f"El resultado de la suma es: {resulSum}") 
        elif opc == "2":
            resulRes = resta(numero1,numero2)
            print(f"El resultado de la resta es: {resulRes}")        
        elif opc == "3":
            resulMul = mul(numero1,numero2)
            print(f"El resultado de la multiplicacion es: {resulMul}")            
        elif opc == "4":
            try: 
                resulDiv = div(numero1,numero2)
                print(f"El resultado de la division es: {resulDiv}")
            except ZeroDivisionError as zde: 
                print("No se puede dividir por cero")          
    else:
        print("Opcion incorrecta")
                        