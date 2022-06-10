import re
import holidays
import argparse
from datetime import date, datetime
import requests
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________

class Medicamentos():
    '''clase medicamento para poder hacer lo que 
    medicamentos. 
    Este se comporta como una clase padre ya que este heredara los atributos a la clase Lugar.

    Parámetros
    -----

    atributos
    --------
     - nombre - del medicamento como string 
     - codigo - del medicameto, en base de la tabla propuesta por Navarro como string, en 
                http://pre.esteve.org/wp-content/uploads/2018/01/137014.pdf
     - precio - del medicamento como flotante

     metodos
     --------
     - constructor- en cual pasa como parametros todos los atributos del a clase Medicamentos
    '''
    def __init__(self, nombre, codigo, precio):
        self.nombreMedic= nombre
        self.codigoMedic= codigo
        self.precioMedic= float( precio)
    
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
class Lugar(Medicamentos):
    '''
    Esta clase se encarga de retornar el lugar donde estan ubicados los medicamentos.\n
    Pasa los datos por ejemplo en este formato (XX##), primera o X letra nos da el pasillo, y la segunda X nos indica la seccion, para poderlo encontar.\n
    Nomenclatura de los medicamentos en 
    http://pre.esteve.org/wp-content/uploads/2018/01/137014.pdf
    --------------------------------------------------------
    --------------------------------------------------------
    --------------------------------------------------------
    - X X        ----------------------------        [ ## ]
    --------------------------------------------------------
    ---------------------------------------------------------
    ---------------------------------------------------------
    - a c       ------          Antinflamatorios del grupo del ibufenaco [38]
    - a d       ------          Analgésicos [38]
    - a n       ------          Antihelmínticos que no forman parte de un grupo definido [15]
    - a s       ------          Enzimas [18]
    - a s       ------          Antiasmáticos y antialérgicos de acción preferentemente no antihistamínica [34]
    - a s       ------          Antihistamínicos [23]
    - a z       ------          Fármacos del grupo del diazepam [49]
    - a z       ------          Antagonistas y agonistas opiáceos relacionados con el 6,7-benzomorfano [17]
    - a z       ------          Antihistamínicos o vasoconstrictores locales del grupo de la antazolina [18]
    - b a       ------          Barbitúricos de actividad hipnótica [28]
    - b e       ------          Antihelmínticos del grupo del tiabendazol [17]
    - b o       ------          Esteroides anabolizantes [22]
    ____________------_______________________________________________________________________________________________
    - c a       ------          Anestésicos locales [59]
    - c a       ------          Antiarrítmicos del grupo I, químicamente emparentados
                ------              con la procainamida y la lidocaína [31]
    - c e       ------          Antibióticos derivados del ácido cefalosporánico (cefalosporinas) [62]
    - c i       ------          Antibióticos del grupo de la tetraciclina [25]
    - c i       ------          Antibióticos derivados del ácido 6-aminopenicilánico (penicilinas) [63]
    - c o       ------          Antifúngicos sistémicos del grupo del miconazol [33]
    - c o       ------          Corticosteroides, excepto los del grupo de la prednisolona [23]
    - d i       ------          Vasodilatadores [55]
    - d i       ------          Antagonistas del calcio del grupo del nifedipino [23]
    - d r       ------          Simpaticomiméticos [18]
    - e r       ------          Alcaloides derivados del cornezuelo de centeno [28]
    - e s       ------          Estrógenos [33]
    - f i       ------          Fármacos del grupo del clofibrato [32]
    - f i       ------          Derivados de la teofilina [40]
    - g e       ------          Progestágenos [40]
    - g l       ------          Hipoglucemiantes sulfamídicos [30]
    - g r       ------          Antiagregantes plaquetarios [18]
    - g u       ------          Antihipertensores derivados de la guanidina [15]
    - i o       ------          Medios de contraste yodados [55]
    - m i       ------          Antibióticos obtenidos de Micromonospora o Streptomyces [113]
    - m i       ------          Antineoplásicos nucleotóxicos [18]
    - m u       ------          Antineoplásicos alquilantes derivados de la β-cloroetilamina [20]
    - n i       ------          Antiparasitarios del grupo del metronidazol [24]
    - n i       ------          Derivados del 5-nitrofurano [26]
    - o l       ------          Bloqueantes adrenérgicos β [90]
    - o n       ------          Esteroides de uso tópico que contienen un grupo acetal [21]
    - o r       ------          Anorexígenos [23]
    - o x       ------          Antibióticos del grupo del ácido nalidíxico [27]
    - p e       ------          Derivados de la 4’-fluoro-4-piperidinobutirofenona, tranquilizantes, neurolépticos [32]
    - p r       ------          Fármacos del grupo de la imipramina [19]
    - p r       ------          Derivados de la prednisolona y la prednisona [25]
    - p r       ------          Derivados de la sulpirida [41]
    - p r       ------          Inhibidores de la enzima conversiva de la angiotensina [27]
    - p r       ------          Antinflamatorios del grupo del ibuprofeno [41]
    - p r       ------          Prostaglandinas [52]
    - q u       ------          Derivados quinolínicos [64]
    - s a       ------          Derivados del ácido salicílico [57]
    - s u       ------          Antibióticos sulfamídicos [53]
    - t e       ------          Broncodilatadores, derivados de la fenetilamina [29]
    - t i       ------          Antagonistas de los receptores H2 del grupo de la cimetidina [22]
    - v e       ------          Espasmolíticos de acción similar a la de la papaverina [42]
    - v i       ------          Alcaloides derivados de la Vinca [24]
    ------
    OJO
    ----------
    Cuando nos referimos en ordenar no es ordenar los productos ingresados 
    si no imprimir el lugar especifico de cada medicamento
        '''
    def Pasillo(self, codigo):
        '''
        esta parte nos encontramos con el lugar del pasillo

        Parametros
        ----------- 
        - recibe como parametro el - codigo 
        ----------
        Retorna
        ---------
        - retorna el numero del pasillo donde se encuentra el medicamento
         '''
        self.codigo1= codigo[:1]
        
        ###__________ pasillo ___________________________
        if self.codigo1=='a':
            return 1 # recibe X y retorna el numero de pasillo 
        if self.codigo1=='b':
            return 2 # recibe X y retorna el numero de pasillo
        if self.codigo1=='c':
            return 3 # recibe X y retorna el numero de pasillo
        if self.codigo1=='d':
            return 4 # recibe X y retorna el numero de pasillo
        if self.codigo1=='e':
            return 5 # recibe X y retorna el numero de pasillo
        if self.codigo1=='d':
            return 6 # recibe X y retorna el numero de pasillo
        if self.codigo1=='e':
            return 7 # recibe X y retorna el numero de pasillo
        if self.codigo1=='f':
            return 8 # recibe X y retorna el numero de pasillo
        if self.codigo1=='g':
            return 9 # recibe X y retorna el numero de pasillo
        if self.codigo1=='i':
            return 10 # recibe X y retorna el numero de pasillo
        if self.codigo1=='m':
            return 11 # recibe X y retorna el numero de pasillo
        if self.codigo1=='n':
            return 12 # recibe X y retorna el numero de pasillo
        if self.codigo1=='o':
            return 13 # recibe X y retorna el numero de pasillo 
        if self.codigo1=='p':
            return 14 # recibe X y retorna el numero de pasillo 
        if self.codigo1=='q':
            return 15 # recibe X y retorna el numero de pasillo
        if self.codigo1=='s':
            return 16 # recibe X y retorna el numero de pasillo
        if self.codigo1=='t':
            return 17 # recibe X y retorna el numero de pasillo
        if self.codigo1=='v':
            return 18 # recibe X y retorna el numero de pasillo
        
    def seccion(self,codigo):
        '''
        Esta parte nos encontramos con la seccion definida con un retorno el cual es el numero de seccion.

        Parametros
        ----------- 
        - recibe como parametro el - codigo 
        ----------
        Retorna
        ---------
        - retorna el numero de la seccion en el quese encuentrael medicameto donde se encuentra el medicamento
         '''
        self.codigo2=codigo[1:2]
        ###________________________ seccion___________
        if self.codigo2=='a':
            return 1 # recibela letra ...X y retorna la seccion respectiva a esa letra  
        if self.codigo2=='c':
            return 2 # recibe la letra ...X y reotorma sección correspondiente
        if self.codigo2=='d':
            return 3 # recibe la letra ...X y reotorma sección correspondiente
        if self.codigo2=='e':
            return 4 # recibe la letra ...X y reotorma sección correspondiente
        if self.codigo2=='i':
            return 5 # recibe la letra ...X y reotorma sección correspondiente
        if self.codigo2=='l':
            return 6 # recibe la letra ...X y reotorma sección correspondiente
        if self.codigo2=='o':
            return 7 # recibe la letra ...X y reotorma sección correspondiente
        if self.codigo2=='r':
            return 8 # recibe la letra ...X y reotorma sección correspondiente
        if self.codigo2=='s':
            return 9 # recibe la letra ...X y reotorma sección correspondiente
        if self.codigo2=='u':
            return 10 # recibe la letra ...X y reotorma sección correspondiente
        if self.codigo2=='x':
            return 11 # recibe la letra ...X y reotorma sección correspondiente
        if self.codigo2=='z':
            return 12 # recibe la letra ...X y reotorma sección correspondiente
        
class FeriadosTsachilas(holidays.HolidayBase):
    ''' Esta clase se encarga de definir nuevas fiestas personalisadas ante la necesidad de nosotros.\n
        recibe parametros de Holiday base para poder hacer todo lo necesario en esta clase.\n
        ------------------
        Atributos
        -----------------
        - country - el cual lo heredamos de holiday base, el cual da la forma para definir un pais.
        - provincia1 - el cual es una lista definido en la libreria builtins.pyi
        -  '''
    provincia=['EC-SD'] # guia de nuestro paso de dato 
    def __init__(self ,**lista): # será un diccionario con los argumentos ingresados, con ** hace que la función acepte infinitos argumentos, pero hay que aclarar primero el nombre del argumento.
        '''declaramos las funciones necesarias para tener nuestrosferiados a la mano'''
        self.country = 'ECU'
        self.provincia1=lista.pop('prov', 'ON')
        holidays.HolidayBase.__init__(self, **lista)

    def _populate(self, year):
        '''
            La documetacion se puede encontrar en: 
            https://www.eluniverso.com/noticias/ecuador/ecuador-calendario-de-feriados-nacionales-y-por-provincias-para-el-ano-2022-nota/
            - Cantonización de Santo Domingo: domingo 3 de julio (pasa al lunes 4)
            - Provincialización: domingo 6 de noviembre (pasa al lunes 7)
            ---------
            Parametros
            ----------
            El parametro que pasa a este metodo es el --year-- o año el cual servira para declarar nuevas fiestas con años dinamicos.
            '''
        self[date(year, 7, 3)] = "Cantonización de Santo Domingo" #  los parametros son año, mes y dia. 
        self[date(year, 11, 6)] = "Provincialización de SAnto Domingo"


####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
class Descuento:
    '''
        En esta clase es donde sucede toda la magia para condicionar los descuentos, aqui hacemos las condiciones para aplicar los datos. 
        
        Parametros
        ------------
        atributos
        ----------------
        - dia - la cual pasa el año mes y dia para saber si es feriado.
        - ApiEnLiena - la cual hacemos que pase el valor de la api y poder controlar el el error ValueError
         
         Metodos
         ------------
         - constructor - contine a los atributos.
         - dia - la cual es un decorador property el cual lo que hace es interpretar la lectura, escritura y borrado de atributos.
                 la cual podemos decir que documenta los mismos.\n 
                 Tambien esta el esta el metodo settter para esta funcion, basicamente se encarga de recibir los datos cuando se escriba.
         - __EsFiesta - este comprueba si un dia es feriado o no para poder hacer losen cuentos, en el menu principal. 
                         este es privado. 
         - ImprimirSiNo - el cual me hace es retornar true o falce, true cuando si exite el feriado y false cuando no. 
                 '''
    def __init__ (self, dia, API=False):
        '''
        este el costructor.

        parametros
        ----------
            - dia - fecha ingresada
            - consideramos la API para saver si el feriado esta en los feriados personalizados o no. 
            '''
        self.dia= dia
        self.ApiEnLinea= API

    @property # primero se define el property para envolver en una funcion al atributo con funciones o codigo que tiene el mismo.
    def dia(self):
        """
            Obtiene el valor del atributo de fecha
        """
        return self._dia 
    @dia.setter ## recibe los datos cuando se escriba
    def dia(self, numValor): 
        ''' metodo para poder dar un valor al atributo dia que esta en el costructor. 
         
         Parametros
         --------------
        numValor - el cual es str 
         
         rotorna una excepcion un mensaje al encontrar el error ValueError
          '''
        try:# en este bloque es donde ejecuteremos nuestro codigo para devolver un mensaje al tener un error, en este caso ValueError.
            if len(numValor)!=10:
                raise ValueError # raice como hacer una excepcion ante este error
            datetime.strptime(numValor, '%Y-%m-%d') # tonces pasa nomas, con lo que estabas. 
        except ValueError: # este bloque se ejecutara si el bloque try nofuncina y sabremos cual es el error. 
            raise ValueError('error ingrese en formato AAAA-MM_DD ;)') from None
        self._dia=numValor # pues si no pasa normal 

    def __EsFiesta(self, date, enLinea ):
        ''' esta parte contine las condiciones para ver si hay feriado o no en un fecha indicada.
            
            parametros
            ------------
            tenemos:
            - date - el cual es la fecha que tenemos o ingresamos.
            - enLinea - el cual pasa por defecto false, es para decir que si el feriado es de la API o las personalizadas. 
            -------
            -------
            la API utilizada es:
            - abstractapi el cual se encuentra  en : https://app.abstractapi.com/api/holidays/documentation
            entrar con previo registro. 
            '''
        ano, maso, menos = date.split('-')
        if enLinea: # condicion si es enLinea true
            ''' 
                se importa los datos de la API conocida como abstractapi
                el cual se encuentra  en : https://app.abstractapi.com/api/holidays/documentation
                
                (ejemplo de fechas. https://www.youtube.com/watch?v=wSLbMwNyeLs)'''
            response = requests.get(f"https://holidays.abstractapi.com/v1/?api_key=91616907df7b4e8282a475d32edfa88a&country=EC&year={ano}&month={maso}&day={menos}")
            # pera utilizar este link utilizamos requests el cual nos ayudara a conectar con la API
            print(response.status_code) # retorna en pantalla un codigo 
            print(response.content)# retorna el contenido de dicha fecha consultada
            if response.content== b'[]':# verifica si el contenido es nulo manda una lista vacia o retorna False.
                return False
            return True # pues si no retorna true
        else: # nos conecta con los feriados personalizados o creados 
            FiestasApi=FeriadosTsachilas(prov='EC-SD') # instencia o crea un objeto de la clases feriadoTschilas con un parametro el cual es la cuadad de Santo Domingo
            return date in FiestasApi # retorna true o false dependiendo si la fecha ingresada 'date' se en cunetra en los feriados creados. 
    def ImprimirSiNo(self): # funcion que decide definitivamente
        '''este metodo llama a los metodos anteriores 
        para saber si si es ferido o no

        Datos importados
        ------
        - tenemos a la fecha - esatributo de este metodo
        - y tenemos la ApiEnLienea la cual es atributo de esta clase descuento. 
        - los datos del metodo __EsFiesta - la segunda mas importante en esta clase. '''
        if self.__EsFiesta(self.dia , self.ApiEnLinea): # retorna true dependiento del metodo __EsFiesta como pregunta este reotorna true.
            return True   
        return False # pues si no nada que ver. 

###______________________________________________________________________________________________________________
###______________________________________________________________________________________________________
###______________________________________________________________________________________________________
###______________________________________________________________________________________________________
def printLugar(pasillo, seccion):
    '''
    hace mas sencillo imprimir los datos que obtenemos en la clase Lugar()'''
    print(f'se encunetra en el pasillo {pasillo}, seccion {seccion}')

####_____________________________________________________________________________________________________
def imprimirRalla(palabra):
    '''
    -----
    -----
    impresion de extras para evitar la fatiga 
    Parametros
    ------
    - recibe como parametros una cadena de caracteres. '''
    print(f'______________________________________\n      {palabra}\n'
        , '______________________________________')
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
if __name__ == '__main__':
    '''este es la funcion principal el cual contiene todo el codigo ejecutable
    '''
    medicamento=Lugar('', '', 0.00) ## instacia de la clase Lugar ya damos valores por defecto.
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
           medicamento.nombreMedic=input('ingrese nombre del medicamento: ') # ingresamos lo valores  - nombre del medicamento.
           medicamento.codigoMedic= input('ingrese el condigo del medicamento(XX##): ')# codigo del medicamento enformato XX##.
           medicamento.precioMedic= float(input('ingrese el precio del medicamento (#.##): '))# ingresa el precio del medicamento. 
        elif opcionPrincipal==2:
            imprimirRalla('UBICACION DEL MEDICAMENTO ')
            printLugar(medicamento.Pasillo(medicamento.codigoMedic),medicamento.seccion(medicamento.codigoMedic)) # imprime el lugar del medicamento en funcion del codigo del medicamento

        elif opcionPrincipal==3:
            imprimirRalla(' DATOS DEL MEDICAMENTO INGRESADOS ')
            print(f'medicamento {medicamento.nombreMedic}, \n   con codigo referencia de la tabla propuesta por Navarro # ({medicamento.codigoMedic} )\n    y precio de {medicamento.precioMedic} dolares. ',
                '\n Sobre el codigo puedes ver en: http://pre.esteve.org/wp-content/uploads/2018/01/137014.pdf')  # imprimimos los datos del medicamento

        elif opcionPrincipal==4:
            imprimirRalla(' PRECIOS ')
            fecha=input('ingrese fecha de la compra del medicamento (AAAA-MM-DD): ')
            cuantoPagas= Descuento(fecha, enLinea)  # isntanciamos aqui la clase Decuento, con el dato de la fecha(str) y el valor por defecto que tenemos False
            if cuantoPagas.ImprimirSiNo(): # utilizamos el ultimo metodo el mas importante el que conecta todos los metodos de la clase Descuento si es True  
                print(f'el cliente tiene un descuento del {medicamento.precioMedic*5/100}, por lo que pagaria {medicamento.precioMedic-(medicamento.precioMedic*5/100)} dolares. ')
            else: # si no lo es pues sige tu camino codigo o ejecucion ;)
                print(f'el cliente no tiene descuento, pagaria, {medicamento.precioMedic} dolares. ')

        elif opcionPrincipal== 5:
            print('usted salio ;)')
            break # para saltarme del menu o el while
        else:
            print('error de numero (#)')

