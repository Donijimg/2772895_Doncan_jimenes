from cuadrado import Cuadrado


cuadro = Cuadrado(2)
print (f"El perimetro del cuadrado es: {cuadro.perimetro()}")
print (f"El area del cuadrado es: {cuadro.area()}")

print (f"Lado actual: {cuadro.lado}")
cuadro.lado = 4
print (f"Nuevo lado: {cuadro.lado}\n")


