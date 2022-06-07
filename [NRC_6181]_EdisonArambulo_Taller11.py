'''datos=[0,0,0,0,0,0]
for i in range (1,7):
    datos[i-1]=int(input("Dime el numero {} ".format(i)))
print("los datos al reves son: ")
for i in range (6,0,-1):
    print( datos[i-1] )'''


'''datos= [3,343,453,35,43,5]
for i in range(0, 5):
    print(datos[i], end=' ')
print()
datos.remove(35)
datos[0]= -2
for i in range(0, len(datos)):
    print(datos[i], end= ' ')'''


'''listas frutas
pedir al usuario
5
guardar elementos
remover los datos ultimo y primer elemento
'''
def imprimirRalla(palabra):
    '''
    impresion de extras para evitar la fatiga '''
    print(f'______________________________________\n      {palabra}\n'
        , '______________________________________')

while True:
    '''
    En esta aparteado se encuentra un condicional el cual 
    nosserivara para definir el numeros de dato que tendra nuestra lista
        - Con lo siguiente se encuetra condicionado 
          con que si el numero ingresado tiene que ser mayor o igual a 5 '''
    cantidad= int(input('ingrese el numero de frutas que ingresara: '))
    if cantidad>=5: # while corre al infinito por lo que esto lo condiciona(salir del bucle se el # es 5 o mayor) 
        break

frutas=[]    # LISTA DE PRUEBA
for i in range(0, cantidad):    # ingreso de datos en el arreglo
    frutas.append(input('ingrese la fruta: ')) # con append de unir 
    #frutas[i]= input('ingrese fruta: ')
imprimirRalla('lista completa')
# _______________________________________________________________________________________
for i in range(0, cantidad): # primer ouput de la lista 
    print(f'la fruta {i}, es {frutas[i]}')
imprimirRalla('list') #____
print(list(frutas)) #  segundo presentacion de ouput opcional 
# _______________________________________________________________________________________
frutas.remove(frutas[0]) # remueve el primer dato (dato en la posicion 0)
print(f'la fruta en la posicion 0, {frutas[0]}')
imprimirRalla('eliminar primer dato') #____
for i in frutas: # tercero impresion de la lista
    print(i)
imprimirRalla('eliminar ultimo dato') #____
# _______________________________________________________________________________________
frutas.remove(frutas[len(frutas)-1])# borra el ultimo dato ubicando en el ultimo dato
for i in frutas: # cuarto imput de la lista 
    print(i)