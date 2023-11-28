class Triangulo:
	def __init__(self, altura, base,lado1,lado2,lado3):
		self.base=base
		self.altura=altura
		self.lado1=lado1
		self.lado2=lado2
		self.lado3=lado3
	def area(self):
		return f"area: {self.base*self.altura}"
	def perimetro(self):
		return f"perimetro: {self.lado1+self.lado2+self.lado3}"
