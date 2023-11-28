from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circulo import Circulo
from triangulo import Triangulo
from hexagono import Hexagono


cuadro = Cuadrado(2)
print (f"El perimetro del cuadrado es: {cuadro.perimetro()}")
print (f"El area del cuadrado es: {cuadro.area()}")

print (f"Lado actual: {cuadro.lado}")
cuadro.lado = 4
print (f"Nuevo lado: {cuadro.lado}\n")

circulo1=Circulo(9)
print (circulo1.perimetro())
print (circulo1.area())

hexagono1=Hexagono(9)
print (hexagono1.perimetro())
print (hexagono1.area())

triangulo1=Triangulo(9,3,3,2,2)
print (triangulo1.perimetro())
print (triangulo1.area())


rectangulo1=Rectangulo(2,1)
print (rectangulo1.perimetro())
print (rectangulo1.area())

