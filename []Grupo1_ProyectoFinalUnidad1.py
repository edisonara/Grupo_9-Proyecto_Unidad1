import re
import holidays
import argparse
from datetime import date, datetime
import requests
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________

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
    
    def __repr__(self):# imprimir objeto como cadena 
	    return f'nombre {self.nombreMedic}:: codigo {self._codigoMedic}:: precio {self.precioMedic} '
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
class Lugar(Medicamentos):
    '''
    nomenclatura de los medicamentos en 
    http://pre.esteve.org/wp-content/uploads/2018/01/137014.pdf
a c o                Antinflamatorios del grupo del ibufenaco [38]
a d o                Analgésicos [38]
a n tel              Antihelmínticos que no forman parte de un grupo definido [15]
a s a                Enzimas [18]
a s t                Antiasmáticos y antialérgicos de acción preferentemente no antihistamínica [34]
a s tina             Antihistamínicos [23]
a z epam             Fármacos del grupo del diazepam [49]
a z ocina            Antagonistas y agonistas opiáceos relacionados con el 6,7-benzomorfano [17]
a z olina            Antihistamínicos o vasoconstrictores locales del grupo de la antazolina [18]
b a rb-,-barb-       Barbitúricos de actividad hipnótica [28]
b e ndazol           Antihelmínticos del grupo del tiabendazol [17]
b o l-, -bol-,-bol   Esteroides anabolizantes [22]
___________________________________________________________________________________________________________
c a ína              Anestésicos locales [59]
c a in-              Antiarrítmicos del grupo I, químicamente emparentados
                        con la procainamida y la lidocaína [31]
c e f-                Antibióticos derivados del ácido cefalosporánico (cefalosporinas) [62]
c i clina            Antibióticos del grupo de la tetraciclina [25]
c i lina             Antibióticos derivados del ácido 6-aminopenicilánico (penicilinas) [63]
c o nazol            Antifúngicos sistémicos del grupo del miconazol [33]
c o rt-, -cort-       Corticosteroides, excepto los del grupo de la prednisolona [23]
d i l-, -dil-, -dil   Vasodilatadores [55]
d i pino             Antagonistas del calcio del grupo del nifedipino [23]
d r ina              Simpaticomiméticos [18]
e r g-, -erg-         Alcaloides derivados del cornezuelo de centeno [28]
e s tr-, -estr-       Estrógenos [33]
f i brato            Fármacos del grupo del clofibrato [32]
f i lina             Derivados de la teofilina [40]
g e st-               Progestágenos [40]
g l i-                Hipoglucemiantes sulfamídicos [30]
g r el-, -grel       Antiagregantes plaquetarios [18]
g u an-               Antihipertensores derivados de la guanidina [15]
i o -                 Medios de contraste yodados [55]
m i cina             Antibióticos obtenidos de Micromonospora o Streptomyces [113]
m i to-               Antineoplásicos nucleotóxicos [18]
m u stina            Antineoplásicos alquilantes derivados de la β-cloroetilamina [20]
n i dazol            Antiparasitarios del grupo del metronidazol [24]
n i fur-              Derivados del 5-nitrofurano [26]
o l ol               Bloqueantes adrenérgicos β [90]
o n ida              Esteroides de uso tópico que contienen un grupo acetal [21]
o r ex               Anorexígenos [23]
o x acino            Antibióticos del grupo del ácido nalidíxico [27]
p e rona             Derivados de la 4’-fluoro-4-piperidinobutirofenona, tranquilizantes, neurolépticos [32]
p r amina            Fármacos del grupo de la imipramina [19]
p r ed-, -pred-       Derivados de la prednisolona y la prednisona [25]
p r ida              Derivados de la sulpirida [41]
p r il               Inhibidores de la enzima conversiva de la angiotensina [27]
p r ofeno            Antinflamatorios del grupo del ibuprofeno [41]
p r ost-,             Prostaglandinas [52]
q u i(n)-, -qui(n)-   Derivados quinolínicos [64]
s a l-, -sal-, -sal   Derivados del ácido salicílico [57]
s u lfa-              Antibióticos sulfamídicos [53]
t e rol              Broncodilatadores, derivados de la fenetilamina [29]
t i dina             Antagonistas de los receptores H2 del grupo de la cimetidina [22]
v e rina             Espasmolíticos de acción similar a la de la papaverina [42]
v i n-, -vin-         Alcaloides derivados de la Vinca [24]
cuando nos referimos en ordeanr no es ordenar los productos ingresados 
si no imprimir el lugar especifico de cada medicamento

'''
    def Pasillo(self, codigo):
        '''
        esta parte nos encontramos con el lugar del pasillo 
        - recibe como parametro el codigo 
         retorna el numero del pasillo donde se encuentra el medicamento
         '''
        self.codigo1= codigo[:1]
        
        ###__________ pasillo ___________________________
        if self.codigo1=='a':
            return 1
        if self.codigo1=='b':
            return 2
        if self.codigo1=='c':
            return 3
        if self.codigo1=='d':
            return 4
        if self.codigo1=='e':
            return 5
        if self.codigo1=='d':
            return 6
        if self.codigo1=='e':
            return 7
        if self.codigo1=='f':
            return 8
        if self.codigo1=='g':
            return 9
        if self.codigo1=='i':
            return 10
        if self.codigo1=='m':
            return 11
        if self.codigo1=='n':
            return 12
        if self.codigo1=='o':
            return 13
        if self.codigo1=='p':
            return 14
        if self.codigo1=='q':
            return 15
        if self.codigo1=='s':
            return 16
        if self.codigo1=='t':
            return 17
        if self.codigo1=='v':
            return 18
        
    def seccion(self,codigo):
        self.codigo2=codigo[1:2]
        ###________________________ seccion___________
        if self.codigo2=='a':
            return 1
        if self.codigo2=='c':
            return 2
        if self.codigo2=='d':
            return 3
        if self.codigo2=='e':
            return 4
        if self.codigo2=='i':
            return 5
        if self.codigo2=='l':
            return 6
        if self.codigo2=='o':
            return 7
        if self.codigo2=='r':
            return 8
        if self.codigo2=='s':
            return 9
        if self.codigo2=='u':
            return 10
        if self.codigo2=='x':
            return 11
        if self.codigo2=='z':
            return 12
        
class FeriadosTsachilas(holidays.HolidayBase):
    provincia=['EC-SD']

    '''def __init__(self, years: Union[int, Iterable[int]] = None, expand: bool = True, observed: bool = True, subdiv: Optional[str] = None, prov: Optional[str] = None, state: Optional[str] = None) -> None:
        super().__init__(years, expand, observed, subdiv, prov, state)'''
    def __init__(self ,**lista):
        '''declaramos las funciones necesarias para tener nuestrosferiados a la mano'''
        self.country = 'ECU'
        self.provincia1=lista.pop('prov', 'ON')
        holidays.HolidayBase.__init__(self, **lista)

    def _populate(self, year):
        '''
            La documetacion se puede encontrar en: 
            https://www.eluniverso.com/noticias/ecuador/ecuador-calendario-de-feriados-nacionales-y-por-provincias-para-el-ano-2022-nota/
            -Cantonización de Santo Domingo: domingo 3 de julio (pasa al lunes 4)
            -Provincialización: domingo 6 de noviembre (pasa al lunes 7)
            '''
        # Set default subdiv if not provided
        #if self.subdiv == None:
        self[date(year, 7, 3)] = "Cantonización de Santo Domingo" # año mes y dia 
        self[date(year, 11, 6)] = "Provincialización de SAnto Domingo"


####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
class Descuento:
    def __init__ (self, dia, API=False):
        self.dia= dia
        #self.hora= hora
        self.ApiEnLinea= API
    @property
    def dia(self):
        """
            Obtiene el valor del atributo de fecha
        """
        return self._dia
    @dia.setter
    def dia(self, numValor):
        try:
            if len(numValor)!=10:
                raise ValueError
            datetime.strptime(numValor, '%Y-%m-%d')
        except ValueError:
            raise ValueError('error ingrese en formato AAAA-MM_DD ;)') from None
        self._dia=numValor

    def __EsFiesta(self, date, enLinea ):
        ano, maso, menos = date.split('-')
        if enLinea:
            ''' 
                se importa los datos de la API conocida como abstractapi
                el cual se encuentra  en : https://app.abstractapi.com/api/holidays/documentation
                
                (ejemplo de fechas. https://www.youtube.com/watch?v=wSLbMwNyeLs)'''
            response = requests.get(f"https://holidays.abstractapi.com/v1/?api_key=91616907df7b4e8282a475d32edfa88a&country=EC&year={ano}&month={maso}&day={menos}")
            print(response.status_code)
            print(response.content)
            if response.content== b'[]':
                return False
            return True
        else:
            FiestasApi=FeriadosTsachilas(prov='EC-SD')
            return date in FiestasApi
    def ImprimirSiNo(self):
        '''este metodo llama a los metodos anteriores 
        para saber si si es ferido o no  '''
        if self.__EsFiesta(self.dia , self.ApiEnLinea):
            return True
        return False

###______________________________________________________________________________________________________________
###______________________________________________________________________________________________________
###______________________________________________________________________________________________________
###______________________________________________________________________________________________________
def printLugar(pasillo, seccion):
    print(f'se encunetra en el pasillo {pasillo}, seccion {seccion}')

####_____________________________________________________________________________________________________
def imprimirRalla(palabra):
    '''
    impresion de extras para evitar la fatiga '''
    print(f'______________________________________\n      {palabra}\n'
        , '______________________________________')
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
if __name__ == '__main__':
    medicamento=Lugar('', '', 0.00)
    parser = argparse.ArgumentParser(
        description=
        'Predictor Pico y Placa Quito: Verifique si el vehículo con la placa proporcionada puede estar en la carretera en la fecha y hora proporcionada:')

    enLinea=False
    
    while True:
        print('______________________________________________')
        print('| 1. Guardar los los datos del medicamento    |')
        print('| 2. Ver la ubicacion del medicamento.        |')
        print('| 3. Imprimir datos del medicamento.          |')
        print('| 4. Precio del medicamento(segun).           |')
        print('| 5. Salir...                                 |')
        print('______________________________________________')
        ##____________________________________________________________
        opcionPrincipal= int(input('ingrese opcion(#): '))
        if opcionPrincipal==1:
           imprimirRalla('INGRESO DE DATOS ')
           medicamento.nombreMedic=input('ingrese nombre del medicamento: ')
           medicamento.codigoMedic= input('ingrese el condigo del medicamento: ')
           medicamento.precioMedic= float(input('ingrese el precio del medicamento (#.##): '))
        elif opcionPrincipal==2:
            imprimirRalla('UBICACION DEL MEDICAMENTO ')
            printLugar(medicamento.Pasillo(medicamento.codigoMedic),medicamento.seccion(medicamento.codigoMedic))

        elif opcionPrincipal==3:
            imprimirRalla(' DATOS DEL MEDICAMENTO INGRESADOS ')
            print(f'medicamento {medicamento.nombreMedic}, \n   con codigo referencia de la tabla propuesta por Navarro # ({medicamento.codigoMedic} )\n    y precio de {medicamento.precioMedic} dolares. ',
                '\n Sobre el codigo puedes ver en: http://pre.esteve.org/wp-content/uploads/2018/01/137014.pdf')

        elif opcionPrincipal==4:
            imprimirRalla(' PRECIOS ')
            fecha=input('ingrese fecha de la compra del medicamento (AAAA-MM-DD): ')
            #hora = input('ingrese hora de la compra del medicamento (HH:mm):')
            cuantoPagas= Descuento(fecha, enLinea)
            if cuantoPagas.ImprimirSiNo():
                print(f'el cliente tiene un descuento del {medicamento.precioMedic*5/100}, por lo que pagaria {medicamento.precioMedic-(medicamento.precioMedic*5/100)} dolares. ')
            else:
                print(f'el cliente no tiene descuento, pagaria, {medicamento.precioMedic} dolares. ')

        elif opcionPrincipal== 5:
            print('usted salio ;)')
            break
        else:
            print('error de numero (#)')

