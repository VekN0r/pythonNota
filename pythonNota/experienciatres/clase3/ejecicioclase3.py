"""Ejercicio 1: Información Personal
Objetivo: Practicar la creación y acceso a elementos de tuplas.
1. Crea una tupla llamada `informacion` que contenga los siguientes elementos en orden: tu
nombre, tu edad, y tu ciudad de residencia.
2. Accede e imprime cada elemento de la tupla utilizando índices.
3. Utiliza el desempaquetado de tuplas para asignar los valores a variables individuales y
luego imprime estas variables.
Ejercicio 2: Operaciones con Tuplas Numéricas
Objetivo: Practicar el uso de funciones y métodos con tuplas.
1. Crea una tupla llamada `numeros` que contenga los números del 1 al 10.
2. Utiliza la función `sum()` para calcular la suma de los elementos de la tupla.
3. Utiliza las funciones `max()` y `min()` para encontrar el valor máximo y mínimo en la tupla.
4. Utiliza el método `count()` para contar cuántas veces aparece el número 5 en la tupla.
Ejercicio 3: Rebanado de Tuplas
Objetivo: Practicar el rebanado (slicing) para obtener sub-tuplas.
1. Crea una tupla llamada `letras` que contenga las letras del alfabeto de la 'a' a la 'j'.
2. Utiliza el rebanado (slicing) para obtener una sub-tupla con las primeras 5 letras e
imprímela.
3. Utiliza el rebanado para obtener una sub-tupla con las últimas 3 letras e imprímela.
4. Utiliza el rebanado con pasos (saltos) para obtener una sub-tupla con cada segunda letra
e imprímela."""

informacion = ('Juan', 22, 'Puerto Varas')

print("Accediendo a elementos de la tupla usando índices:")
print("Nombre:", informacion[0])
print("Edad:", informacion[1])
print("Ciudad de residencia:", informacion[2])

nombre, edad, ciudad = informacion

print("\nDesempaquetando la tupla:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad de residencia:", ciudad)

#segundo ejercicio

num = (1,2,3,4,5,6,7,8,9,10)
print(sum(num))
print(f"Valor maximo {max(num)} Valor minimo: {min(num)}")
print(num.count(5))

#Tercer ejercicio

letras = ("a","b","c","d","e","f","j")
print(letras[0:5])
print(letras[-4:-1])
print(letras[0::2])