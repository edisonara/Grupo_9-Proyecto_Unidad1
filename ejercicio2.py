
from ast import While
from asyncio.windows_events import NULL
import holidays
from datetime import date
class Medicamentos():
    def __init__(self, nombre, codigo, precio):
        self.nombreMedic= nombre
        self._codigoMedic= codigo
        self.precioMedic= float( precio)
    def __repr__(self):
	    return f'nombre {self.nombreMedic}:: codigo {self._codigoMedic}:: precio {self.precioMedic} '


class Ordenar(Medicamentos):
    '''
    aqui ordenaremos los medicametos en tipo 
    para poder saber en que estan esta
    1. recibir los productos
    2. ordenarlos segun codigos
    3. mostrar en seccion
    '''
    def recibir(self):
        pass

class NewCountryHolidays(holidays.HolidayBase):
    def _populate(self, year):
        # Set default subdiv if not provided
        if self.subdiv == None:
            self.subdiv = 'SantoDomingo'
        self[date(year, 1, 2)] = "Some Federal Holiday"
        if self.subdiv == 'SantoDomingo':
            self[date(year, 2, 3)] = "Special XX subdiv-only holiday"
        if self.subdiv == 'SantoDomingo':
            self[date(year, 3, 4)] = "Special YY subdiv-only holiday"


hdays = NewCountryHolidays()
print(hdays._populate(2022))
medicamento=Medicamentos('', '', 0.00)
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
            if lista==NULL:
                lista.append(medicamento)
    elif opcionPrincipal==2:
        print(repr(lista))
    elif opcionPrincipal== 3:
        print('usted salio ;)')
        break
    else:
        print('error de numero (#)')
    



'''
import holidays
from datetime import date
class NewCountryHolidays(holidays.HolidayBase):
    
    _________________________________________________________________________________________
    También podemos heredar de la clase HolidayBase que tiene un _populate()método vacío,
     por lo que comenzamos sin días festivos y debemos definirlos todos nosotros.
      Así es como crearíamos una clase de vacaciones para un país que aún no es compatible
      _______________________________________________________________________________________
    
    def _populate(self, year):
        self[date(year, 1, 2)] = "Some Federal Holiday"
        self[date(year, 2, 3)] = "Another Federal Holiday"
fiestaNUll = NewCountryHolidays()
print(fiestaNUll)
'''