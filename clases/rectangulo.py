class Rectangulo:
	def __init__(self, base, altura):
		self.base=base
		self.altura=altura
	def area(self):
		return f"el area es{self.base * self.altura }"
	def perimetero(self):
		return f"el area es{ 2*(self.base + self.altura) }"
