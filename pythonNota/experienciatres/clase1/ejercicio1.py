"""Se requiere dar solución a los casos que se verán a continuación, para ello los
estudiantes deberán formar grupos de trabajos de un mínimo de 2 alumnos y un
máximo de 3 alumnos.
1) Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en
una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de
caracteres en un mensaje de salida por pantalla.
2) Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para
nombres y una 1 lista para apellidos), el sistema deberá mostrar de forma ordenada
los nombres y apellidos.
3) Cree una lista y comience a almacenar nombres, cada vez que se agregue un
nombre nuevo, el sistema preguntará si desea agregar otro nombre, deberá agregar
nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” (use funciones lower()
y upper() ) .
Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de
caracteres.
4) Cree un menú para registrar usuarios e iniciar sesión, también el menú tendrá la
opción de eliminar usuarios, para ello, utilice el nombre de usuario, además para
confirmar la eliminación, deberán escribir la contraseña correspondiente de cada
usuario.
1. Inicio sesión.
2
2. Registrar usuario
3. Eliminar usuario.
4. Salir.
La opción 1 solo mostrará un mensaje exitoso si ha iniciado correctamente,
o un error de caso contrario.
5) Cree un sistema de ventas de supermercado en el cual se pueda agregar productos
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
x = 0
nombreGrande = ""
while x < 3:
    nombre = input(f"Ingrese el nombre número {x+1}")
    x+=1
    if len(nombre) > len(nombreGrande):
        nombreGrande = nombre
print(f"El nombre más grande es {nombreGrande}")    