class Medicamentos:
	def __init__(self, nombre, codigo, precio):
		self.nombreMedic= nombre
		self.precioMedic= precio
		self._codigoMedic= codigo
	def __repr__(self):
		return f'nombre {self.nombreMedic}:: codigo {self._codigoMedic}:: precio {self.precioMedic} '


medicamento=[
	Medicamentos('tgtytg', 'fff', 23),
	Medicamentos('de', 'dede', 54)
]
print(medicamento)