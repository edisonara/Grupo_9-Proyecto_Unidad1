class Medicamentos:
	def __init__(self, nombre, codigo, precio):
		self.nombreMedic= nombre
		self.precioMedic= precio
		self._codigoMedic= codigo
	def __repr__(self):
		return f'nombre {self.nombreMedic}:: codigo {self._codigoMedic}:: precio {self.precioMedic} '

'''
medicamento=[
	Medicamentos('tgtytg', 'fff', 23),
	Medicamentos('de', 'dede', 54)
]
print(medicamento)
'''


nombre= 'hola'
print(nombre[:2])



##______________________________________________________________________________________________________



import holidays
from datetime import date
class Medicamentos():
    '''clase medicamento para poder hacer lo que 
    medicamentos
    -- init
    --- repr (imprimir)
    -- codigo : A'''
    def __init__(self, nombre, codigo, precio):
        self.nombreMedic= nombre
        self.codigoMedic= codigo
        self.precioMedic= float( precio)
    def __repr__(self):
	    return f'nombre {self.nombreMedic}:: codigo {self._codigoMedic}:: precio {self.precioMedic} '


class Ordenar(Medicamentos):
    '''
    llega elproducto - y ordena 
    aqui ordenaremos los medicametos en tipo 
    para poder saber en que estan esta
    1. recibir los productos
    2. ordenarlos segun codigos
    3. mostrar en seccion
    recibe los productos (analgesico ....)--- 
    '''
    def RefProducto(self):
        '''imprimir '''
        
    def verLugar(self):
        '''Ant23'''
        self.Print=self.codigoMedic[:3]
        if self._codigoMedic=='Ant':
            print('en el pasillo 1 deizquierda a derecha')
        if self._codigoMedic='Ana':
            print('en el pasillo 2 deizquierda a derecha')
        

        '''
        A
        A: en el pasillo 1 deizquierda a derecha'''





'''class FeriadosTsachilas(holidays.HolidayBase):
    def _populate(self, year):
        
            La documetacion se puede encontrar en: 
            https://www.eluniverso.com/noticias/ecuador/ecuador-calendario-de-feriados-nacionales-y-por-provincias-para-el-ano-2022-nota/
            -Cantonización de Santo Domingo: domingo 3 de julio (pasa al lunes 4)
            -Provincialización: domingo 6 de noviembre (pasa al lunes 7)
        

        # Set default subdiv if not provided
        #if self.subdiv == None:
        self.subdiv = 'SantoDomingo'
        self[date(year, 7, 3)] = "Cantonización de Santo Domingo" # año mes y dia 
        if self.subdiv == 'SantoDomingo':
            self[date(year, 11, 6)] = "Provincialización de SAnto Domingo"

    def descuento(self, precio):
        self.PrecioFinal= precio* 50/100
        return self.PrecioFinal
    
'''


#feriado = FeriadosTsachilas()
#print(feriado)
#medicamento=Medicamentos('', '', 0.00)
lista=[]

while True:
    print('1. guardar los los datos del medicamento')
    print('2. ver los datos')
    print('3. salir...')
    opcionPrincipal= int(input('ingrese opcion(#): '))
    if opcionPrincipal==1:
        a=1
        medicamento.nombreMedic=input('ingrese nombre del medicamento: ')
        medicamento._codigoMedic= input('ingrese el condgo del medicamento: ')
        medicamento.precioMedic= float(input('ingrese el precio del medicamento (#.##): '))
        rango=int(len(lista))
        print(rango)
        for a in range (0, rango):
            if lista==None:
                lista.append(medicamento)
    elif opcionPrincipal==2:
        print(repr(lista))
    elif opcionPrincipal== 3:
        print('usted salio ;)')
        break
    else:
        print('error de numero (#)')
    
        

