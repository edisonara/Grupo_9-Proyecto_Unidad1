
import holidays
from datetime import date
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


hdays = NewCountryHolidays(subdiv='SantoDomingo')
print(hdays._populate(2022))
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