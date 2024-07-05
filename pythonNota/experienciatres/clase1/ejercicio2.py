"""2) Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para
nombres y una 1 lista para apellidos), el sistema deberá mostrar de forma ordenada
los nombres y apellidos."""

nombres = []
apellidos = []
x = 0

while x < 3:
    x+=1
    nombre = input("Ingrese nombre")
    apellido = input("Ingrese apellido")
    nombres.append(nombre)
    apellidos.append(apellido)
for i in range(3):
    print(f"Nombre: {nombres[i]} Apellido: {apellidos[i]}")
