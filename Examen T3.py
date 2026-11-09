import random
import math


a = float(input("Ingrese el valor de a de la elipse: "))
b = float(input("Ingrese el valor de b de la elipse: "))
c = float(input("Ingrese el valor de c de la hiperbola: "))
d = float(input("Ingrese el valor de d de la hiperbola: "))
cantidad = int(input("Ingrese la cantidad de puntos aleatorios: "))


puntosElipse = 0
puntosInterseccion = 0


for i in range(cantidad):

    
    x = -a + (2 * a) * random.random()
    y = -b + (2 * b) * random.random()

    
    elipse = (x ** 2) / (a ** 2) + (y ** 2) / (b ** 2)


    if elipse <= 1:

        puntosElipse = puntosElipse + 1

      
        hiperbola = (x ** 2) / (c ** 2) - (y ** 2) / (d ** 2)


        if hiperbola >= 1:

            puntosInterseccion = puntosInterseccion + 1


areaElipse = math.pi * a * b


if puntosElipse > 0:

    areaInterseccion = (
        areaElipse * puntosInterseccion / puntosElipse
    )

else:

    areaInterseccion = 0


print()
print("===== RESULTADOS =====")
print()

print("Puntos generados:", cantidad)

print(
    "Puntos que cayeron dentro de la elipse:",
    puntosElipse
)

print(
    "Puntos que cayeron en la interseccion:",
    puntosInterseccion
)

print(
    "Area de la elipse:",
    areaElipse
)

print(
    "Area aproximada de la interseccion:",
    areaInterseccion
)