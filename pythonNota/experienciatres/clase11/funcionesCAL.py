def sumar(num1, num2):
    suma = num1 + num2
    return suma
def resta(num1,num2):
    restar = num1 - num2
    return restar
def mul(num1,num2):
    multi = num1*num2
    return multi
def div(num1,num2):
    if num2 == 0:
        raise ZeroDivisionError
    else:
        dividir = num1 / num2
        return dividir
def validarNum(num):
    try:
        return float(num)
    except ValueError:
        None