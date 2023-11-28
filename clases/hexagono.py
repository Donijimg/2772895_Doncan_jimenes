class Hexagono:
	def __init__(self,lado):
		self.lado=lado
	def area(self):
		return f"area: {3*(3**0.5)*(self.lado**2)/2}"
	def perimetro(self):
		return "perimetro: {6*self.lado}"
