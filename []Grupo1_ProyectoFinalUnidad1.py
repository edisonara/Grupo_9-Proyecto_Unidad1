'''
Analgésicos. ...
Antiácidos y antiulcerosos. ...
Antialérgicos. ...
Antidiarreicos y laxantes. ...
Antiinfecciosos. ...
Antiinflamatorios. ...
Antipiréticos. ...
Antitusivos y mucolíticos.
'''
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
    def __repr__(self):
	    return f'nombre {self.nombreMedic}:: codigo {self._codigoMedic}:: precio {self.precioMedic} '
####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________
class Lugar(Medicamentos):
    '''
a c o                Antinflamatorios del grupo del ibufenaco [38]
a d ol, -adol-       Analgésicos [38]
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
v i n-, -vin-         Alcaloides derivados de la Vinca [24]'''
    def Pasillo(self, codigo):
        self.codigo1= codigo[:1]
        
        ###__________ pasillo ___________________________
        if self.codigo1=='a':
            return 1
        if self.codigo1=='b':
            return 2
        if self.codigo1== 'c':
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
        if self.codigo2=='r':
            return 7
        if self.codigo2=='s':
            return 8
        if self.codigo2=='u':
            return 9
        if self.codigo2=='x':
            return 10
        if self.codigo2=='z':
            return 11
        



####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________

####_____________________________________________________________________________________________________
####_____________________________________________________________________________________________________

def printLugar(pasillo, seccion):
    print(f'se encunetra en el pasillo {pasillo}, seccion {seccion}')

####_____________________________________________________________________________________________________
def imprimirRalla(palabra):
    '''
    impresion de extras para evitar la fatiga '''
    print(f'______________________________________\n      {palabra}\n'
        , '______________________________________')
####_____________________________________________________________________________________________________
if __name__ == '__main__':
    medicamento=Lugar('', '', 0.00)
    while True:
        print('1. guardar los los datos del medicamento')
        print('2. ver la ubicacion del medicamento.')
        print('3. ver los medicamentos')
        print('4. precio del medicamento(segun).')
        print('5. salir...')
        opcionPrincipal= int(input('ingrese opcion(#): '))
        if opcionPrincipal==1:
           imprimirRalla('INGRESO DE DATOS ')
           medicamento.nombreMedic=input('ingrese nombre del medicamento: ')
           medicamento.codigoMedic= input('ingrese el condgo del medicamento: ')
           medicamento.precioMedic= float(input('ingrese el precio del medicamento (#.##): '))
        elif opcionPrincipal==2:
            imprimirRalla('UBICACION DEL MEDICAMENTO ')
            printLugar(medicamento.Pasillo(medicamento.codigoMedic),medicamento.seccion(medicamento.codigoMedic))
        elif opcionPrincipal==3:
            imprimirRalla(' DATOS ')
        elif opcionPrincipal==4:
            imprimirRalla(' PRECIOS ')
        elif opcionPrincipal== 5:
            print('usted salio ;)')
            break
        else:
            print('error de numero (#)')

