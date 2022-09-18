############## Dia 24 de Agosto ################
"""def suma(a,b):
    return a+b

#Entrada de datos
if __name__ == "__main__":
    print(suma(5,9))


 x = 10
 print(x,"addr:",id(x))
 x = "Hola"
 print(x,"addr:",id(x))
 y = 10
 print(y,"addr:",id(y))
 z="HOla"
 print(z,"addr:",id(z))
x = 1
print(x,":",id(x))
x = x + 1
print(x,":",id(x))
x = x + 1
print(x,":",id(x))
x = x + 1
print(x,":",id(x))
x = x + 1
print(x,":",id(x))
x = x + 1
print(x,":",id(x))
x = x + 1
print(x,":",id(x))
x = x + 1
print(x,":",id(x))
x = x + 1
print(x,":",id(x))
x = x + 1
print(x,":",id(x))
x = x + 1
print(x,":",id(x))
x = x + 1
def suma1(a,b):
    return a+b

def suma2(a:int,b:int)->int:
    return a+b

print(suma1(2,2))
print(suma2(3,3))

1._Escibir una funcion que reciba un mensaje y un nombre y escriba en pantalla "<mensaje> <nombre>
def saludar(mensaje:str, nombre:str)->str: #Asignar como valores de entrada mensaje y nombre con tipo de dato string(str) y arroje una salida de tipo string
   print(f"{mensaje} {nombre}")

2._ Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de salida tiene
que ser: "Hola <nombre> tienes <edad> años
def mensaje(nombre:str, edad:int)->str: #Asignar como valores de entrada nombre de tipo string y edad de tipo int y arroje una salida de tipo string
   print("Hola", (nombre), "tienes", (edad), "años")

3._ Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior
enviando esta como argumento obtenga el mensaje: "Hola <nombre> tienes <edad> años
def calcular_edad(año_actual:int, año_nacimiento:int, nombre:str)->str: #Asignar como valores de entrada año_actual y año_nacimiento que son tipo integer(int) y un tercer parametro nombre de tipo string el cual se usa para llamar la funcion como parametro y arroje una salida de tipo string
   edad = año_actual - año_nacimiento
   return mensaje(nombre,edad) #Llamado de la funcion calcular_edad como parametro de la funcion calcular_edad


if __name__ == "__main__":
   print("Escibir una funcion que reciba un mensaje y un nombre y escriba en pantalla <mensaje> <nombre>")
   saludar("Hola","Victor")
   print("Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de salida tiene que ser: Hola <nombre> tienes <edad> años")
   mensaje("Victor", "20")
   print("Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: Hola <nombre> tienes <edad> años")
   calcular_edad(2022,2002,"Victor")

"""
################## Dia 26 de Agosoto ################
#Dia 26 de Agosto
"""import sumar as s
import restar as r
import multiplicar as m
import dividir as d
import cuadrado as c


if __name__ == "__main__":
   print( s.sumar(5,6))
   print( r.restar(6,10))
   print(m.multiplicar(6, 10))
   print(d.dividir(6, 10))
   print(c.cuadrado(6))

#Importar modulos desde otros archivos en una cierta carpeta
import ops.operaciones as op #Importar el modulo con (import) de una carpeta de operaciones con un punto(.) y (as) para hacer referencia al modulo. Es una forma general para trabajar los diferentes modulos dentro de la carpeta de operaciones
import ops.sumar as s #Importar el modulo con (import) de una carperta de operaciones(ops) con un punto(.) y (as) para hacer referencia al modulo. Es una forma para solo importar un solo modulo de la carpeta
from ops.operaciones import multiplicar #Importar el modulo de operaciones con (from) luego se importa el nombre del modulo y despues (import) y el nombre del archivo para asi obtener una funcion como si fuera nativa


if __name__ == "__main__":
    a = 11 #Asignamos a la variable (a) como tipo int con valor 11
    b = 6 #Asignamos a la variable (b) como tipo int con valor 6
    print(op.cuadrado(a)) #Se imprime el resultado de mandar a llamar la funcion importada dando sus parametros que fueron previamente asignados
    print(op.dividir(a,b))
    print(s.sumar(a,b))
    print(multiplicar(a,b))
"""

################ Dia 31 de Agosto ###############
"""n = 10
msg = "Hola"

print(n,msg)
print(str(n)+msg)
#fstrings
print(f"{n} {msg}")
Hacer una funcion que reciba el nombre de una persona
el año de nacimiento y el año actual retornando el mensaje
"Hola <nombre>, tienes <edad> años"

def mensaje(nombre:str, año_nacimiento:int, año_actual:int)->str:
   edad = año_actual - año_nacimiento
   return f"Hola {nombre}, tienes {edad} años"

def mensaje2(nombre:str, a_nac:int, a_actual:int)-> str:
   return f"Hola {nombre}, tienes {a_actual-a_nac} años"

def calcular_edad(a_nac:int, a_actual:int)->int:
   return a_actual - a_nac

def mensaje3(nombre:str, a_nac:int,a_actual:int)->str:
   return f"Hola {nombre}, tienes {calcular_edad(a_nac,a_actual)} años"

if __name__ == "__main__":
   print(mensaje("Victor",2002,2022))
   res=mensaje2("Victor",2002,2022)
   print(res)
   print(mensaje3("Victor",2002,2022))

listas
alumnos=["Hugo", "Paco", "Luis", "Lupita"] #Se crea una lista con elementos de tipo string(str)
print(f"Alumnos: {alumnos}") #Se imprime la lista completa con todos sus elementos

Tuplas
alumnos= ("Hugo", "Paco", "Luis", "Lupita") #Se crea una Tupla con elementos de tipo string(str)
print(f"Alumnos: {alumnos}") #Se imprime la tupla completa con todos sus elementos

sets
alumnos= {"Hugo", "Paco", "Luis", "Lupita"} #Se crea un Set con elementos de tipo string(str)
print(f"Alumnos: {alumnos}") #Se imprime el Set con todos sus elementos

diccionarios
alumnos = {"nombre":"Hugo", "Materia1":10, "Materia2":5} #Se crea un diccionario con elementos y claves de tipo string(str), las claves sirven para poder llamar un cierto valor
print(f"alumnos: {alumnos}") #Se imprime el diccionario completo con claves y valores
print(f"alumnos: {alumnos['Materia1']}") #Imprime del diccionario el valor que tiene por clave Materia1

numeros_list = [1,2,1,2,4,3,4,3,2,2,1,4,6,5,5,2,1,5] #Se crea una lista de numeros de tipo entero. La razon por lo que se crea esta lista es para encontrar la diferencia entre una lista y un set
numeros_set = {1,2,1,2,4,3,4,3,2,2,1,5,6,5,5,2,4,5} #Se crea un Set con numero de tipo entero de forma repetitiva
print(numeros_list) #Se imprime la Lista con todos sus elementos
print(numeros_set) #Se imprime el Set para asi poder encontrar la diferencia entre un Set y una lista


e = ["Nombre", "Est Dat", "Prog Func", "Ingles"] #Se crea una lista con elementos de tipo string(str) para asi poder crear una base de datos pequeña
alumnos=["Hugo Alberto", "Paco", "Luis", "Lupita"] #Se crea una lista con elementos de tipo string(str) en el cual almacenamos nombres para la base de datos
m_e_d = [9,7,9,8] #Se crea una lista con elementos de tipo entero(int) la cual almacena calificaciones de una materia para la base de datos
m_p_f = [8,9,7,8] #Se crea una lista con elementos de tipo entero(int) la cual almacena calificaciones de una materia
m_i = [6,7,9,8] #Se crea una lista con elementos de tipo entero(int) la cual almacena calificaciones de una materia

ancho=15 #Se le asigna el valor de separacion entre elementos a una variable que se encarge de acomodar de la mejor forma los elementos

print(f"{e[0]:^{ancho}}{e[1]:^{ancho}}{e[2]:^{ancho}}{e[3]:^{ancho}}") #Se imprime mediante fstring nuestra pequeña base de datos, se utiliza la variable de separacion para hacer mas estetica la base de datos
for i in range(len(alumnos)): #Se recorre la lista de alumnos para ingresar a cada elemento de ella}
   print(f"{alumnos[i]:<{ancho}}{m_e_d[i]:^{ancho}}{m_p_f[i]:^{ancho}}{m_i[i]:^{ancho}}") #Se asigna mediante fstring el valor de la calificacion a cada alumno y al final se imprime la base de datos
"""
################## Dia 02 de Septiembre ###################
"""
m_e_d = [9,7,9,8] #Se crea una lista con elementos de tipo entero(int) la cual almacena calificaciones de una materia para la base de datos
m_p_f = [8,9,7,8] #Se crea una lista con elementos de tipo entero(int) la cual almacena calificaciones de una materia
m_i = [6,7,9,8] #Se crea una lista con elementos de tipo entero(int) la cual almacena calificaciones de una materia

def reporte(fmt:int):
   print(f"{e[0]:^{fmt}}{e[1]:^{fmt}}{e[2]:^{fmt}}{e[3]:^{fmt}}")
   for i in range(len(alumnos)):
      print(f"{alumnos[i]:*<{fmt}}{m_e_d[i]:+^{fmt}}{m_p_f[i]:#>{fmt}}{m_i[i]:-^{fmt}}")


if __name__=="__main__":
   reporte(15)

Separacion con coma
numeroBig= 12123456789123456787 #Se le asigna a una variable un numero aleatorio
print(f"{numeroBig:,d}") #Se imprime con fstring el numero pero se separa el numero mediante un separador el cual es ,
# #Fijar con decimales
numeroPI= 3.1415926785478589658565 #Se le asigna a una variable (PI) su valor
print(f"{numeroPI: .3f}") #Se imprime con fstring la variable pero se utiliza la separacion(.) para asi decidir la cantidad de decimales que van a aparecer en la pantalla
# #Notacion cientifica
numeroPI= 314.15926785478589658565 #Se le asiga a una variable para PI su valor matematico
print(f"{numeroPI:e}") #Se imprime con fstring y con (e) el valor de la variable pero con valor en notacion cientifica
print(f"{numeroPI: .2e}") #Se imprime fstring y con (e) el valor de la variable pero con valor en notacion centifica y se utiliza la separacion(.) para asi contralar el numero de decimales
# #Porcentaje
numeroPorciento= 0.258478585 #Se asigna a una variable de porciento un valor en decimal aleatorio
print(f"{numeroPorciento:%}") #Se imprime con fstring el valor de la variable pero con el convertidor (%d) para asi mostrar el valor de la variable en porcentaje
print(f"{numeroPorciento:.2%}") #Se imprime con fstring el valor de la variable pero con el convertidor (%d) para asi mostrar el valor de la variable en porcentaje y con el separador(.) para contralar el numero de decimales

#Numeros Binarios
print(f"{25:b}{35:b}") #Se imprime con fstring y con el formato (b) para convertir un numero entero a su equivalente en binario
# #Unicodes Codigo ASCII
print(f"{80:c}") #Se imprime con fstring y con el formato (c) para imprimir el valor de una cierta tecla pero con el codigo ASCII
# #Hexadecimal
print(f"{255:x}") #Se imprime con fstring y con el formato (x) para convertir un numero a su equivalente en hexadecimal
# #Octal
print(f"{255:o}") #Se imprime con fstring y con el formato (o) para convertir un numero a su equivalente en octal

Escriba una funcion que genere una tabla de multiplicar
recibiendo como argumento la cantidad de numero y la tabla
a generar
def tablas_mult(m:int,n:int,fmt:int): #Se crea una funcion de apoyo la cual se encargara de generar las tablas que recibe como parametros el valor de las tablas, asi como el maximo de multiplicaciones y el formato de separacion entre cada elementos de las tablas. Todos los valores son de tipo integer(int)
   for i in range(1,m+1): #Se crea un ciclo for que se encarga de generar las tablas con un rango desde uno hasta el numero maximo de tablas mas 1
      tablas(n,i,fmt) #Se retorna una funcion que se encarga de imprimir las tablas, pasando como parametros, el valor maximo, el valor de las tablas y el formato de seaparacion de cada elementos de las tablas

def tablas(can_num:int, numero:int,fmt:int): #Se crea una funcion una funcion que se encargar de imprimir las tablas la cual recibe como parametros el valor de las tabla, asi como el maximo de multiplicaciones y el formato de separacion entre cada elementos de las tablas. Todos los valores son de tipo integer(int)
   print(f"tabla del {numero}") #Se muestra como titulo de cada tabla en pantalla el valor de la tabla de multiplicar
   for x in range(1,can_num+1): #Se crea un ciclo for que se encargara de recorrer cada elemento de las tablas que con un rango que inicia en 1 y termina hasta el valor maximo de tablas mas 1
      print(f"{numero:^{fmt}}x{x:^{fmt}} = {(x*numero):^{fmt}}") #Se imprime con fstring cada elemento de las tablas con formatos de separacion y al final hace la operacion de multiplicar para asi mostrar el resultado.
      # print("") #Se imprime un espacio en blanco al final de cada ciclo paraa asi separar una tabla de otra

if __name__=="__main__":
   tablas_mult(5,10,5) #Se manda a llamar la funcion que genera las tablas de multiplicar dando como parametros el numero el valor de las tablas, el numero maximo de multplicaiones y el formato de separacion entre cada elemento
"""

############### Dia 7 de septiembre ##################
"""
#Array es una estrucutra de datos primitiva, que almacena cualquier tipo de dato y tiene una longitud
lista1=[1, 2, 3, 4]
print(lista1)
lista2 = [1, 3.14, "a", True, [4,5,6],(1,2,3),{8, "a", 5.4}]
print(lista2)

# Len para medir la longitud de una lista. Una lista es considera como un objeto
print(len(lista1))
print(len(lista2))
#Indexacion para un elemento de una lista
print(lista2[6])

# #Lista Vacia
lista_calif = []
print(lista_calif)
lista_calif.append(5) #Agregar elementos a una lista, con el metodo append
print(lista_calif)
lista_calif.append(8)
print(lista_calif)
lista_calif.insert(0,6) #Insert sirve para insestar un dato a una lista mediante su indice

#Rellenar una lista con los numeros naturales del 1 al 10
lista_n = []
for i in range(1,11):
    lista_n.append(i)

print(lista_n)
#Indices negativos
print(lista1[-2]) #Forma para recorre la lista de manera inversa, con indices negativos

#Slices (rebandas), forma para imprimir o recorrer una lista iniciando desde un cierto punto
lista1 = [1,2,3,4,5,6,7,8,9,10]
print(lista1)
print(lista1[:])
print(lista1[0:10])

print(lista1[int(len(lista1)/2):])
print(lista1[:int(len(lista1)/2)])
print(lista1[0:-1])
print(lista1[3:7])
print(lista1[-7:-3])

lista1 = [1,"dos", 3, "cuatro"]
print(lista1)
lista1[1] = 2
print(lista1)
lista2=lista1
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
lista2[1] = 2
print("-----------")
print(f"Direccion: {id(lista1)},Lista 1: {lista1}")
print(f"Direccion : {id(lista2)},Lista 2: {lista2}")
print("Forma Correcta")
lista1 = [1,"dos", 3, "cuatro"]
lista2 = lista1[:]
print(f"Direccion: lista1: {id(lista1)}")
print(f"Direccion lista2: {id(lista2)}")
lista2[1] = 2
lista2[3] = 4
print(f"Direccion: {id(lista1)}, lista1: {lista1}")
print(f"Direccion: {id(lista2)}, Lista2: {lista2}")

lista1 = [0,1,2,3,4]
lista2 = [5,6,7]
Insertar varios elementos al final de una lista
lista1[5:] = lista2
lista1[len(lista1):] = lista2
print(lista1)

#Insertar al inicio de una lista varios elementos (en una lista)
lista1[:0] = lista2
print(lista1)

lista1.extend(lista2) #Agregar con el formato extend elementos a una lista
lista1.append(lista2)
print(lista1)
#Como eleminar elementos de una lista
del(lista1[0])
print(lista1)

del(lista1[2:5])
print(lista1)

lista2 = [1, 3.14, "a", True, [4,5,6],(1,2,3),{8, "a", 5.4}] #Se crea una lista que puede almacenar: numeros enteros o flotantes, caracteres, valores booleanos e inclusive listas
print(lista2) #Se imprime cada elemento de la lista

#Len para medir la longitud de una lista. Una lista es considera como un objeto
print(len(lista2)) #Con la funcion len se obtiene el largo o longitud de la lista, es decir cuantos elementos contiene
# Indexacion para un elemento de una lista
print(lista2[6]) #Indexar es agregar un elemento en un cierto indice o posicion de una lista, se imprime la lista con el valor indexado
# #Lista Vacia
lista_calif = [] #Se crea una lista sin elementos para asi poder agregar elementos a esa lista
print(lista_calif) #Se imprime la lista, en este caso como es una lista vacia no se imprime nada
lista_calif.append(5) #Agregar elementos a una lista, con el metodo append
print(lista_calif) # Se imprime la lista con el nuevo elemento agregado
lista_calif.append(8) #Se agrega otro elemento con ele metodo append, cabe recalcar que append ingresa los elementos al final de la lista no al principio
print(lista_calif) # Se imprime la lista con el element anterior y el nuevo elemento agregado
lista_calif.insert(0,6) #Insert sirve para insestar un dato a una lista mediante su indice, con este metodo se pueden ingresar elemento al principio o entre medias en una lista

# Actividad: Rellenar una lista con los numeros naturales del 1 al 10
lista_n = [] #Se crea una lista sin elementos, en la cual se van a agregar los numeros naturales del 1 al 10
for i in range(1,11): #Se crea un ciclo for que se va a encargar de recorrer la lista, el cual va tener un rango que va iniciar en 1 y va a terminar en 11
    lista_n.append(i) #Se va agregando mediante la variable iteradora del ciclo, los elementos a nuestra lista vacia
print(lista_n) #Se imprime nuestra lista vacia ya con elementos agregados por el ciclo for

#Indices negativos
print(lista2[-2]) #Forma para recorre la lista de manera inversa, con indices negativos

#Slices (rebandas), forma para imprimir o recorrer una lista iniciando desde un cierto indice y terminando en cierto indice y asi obtener un trozo de elementos de una lista
lista1 = [1,2,3,4,5,6,7,8,9,10] #Se crea una lista con elementos de tipo int
print(lista1) #Se imprime nuestra lista de manera tradicional
print(lista1[:]) #Se imprime nuestra lista pero ahora con el metodo slice, el cual al no indicar en que indice empieza y en cual termina, se toma que se va imprimir la lista de inicio a fin
print(lista1[0:10]) #Se imprime la lista con slice pero ahora si se le indica el indice de inicion y de fin

print(lista1[int(len(lista1)/2):]) #Se imprime mediante slice la mitad de la lista, para ello se obtiene su longitud y se divide entre dos, con esto el slicing comenzara desde la mitad de la lista y terminar hasta el final
print(lista1[:int(len(lista1)/2)]) #Se imprime mediante slice la mitad de la lista, para ello se obtiene su longitud y se divide entre dos, con esto el slicing comenzara desde la mitad de la lista y terminar hasta el principio
print(lista1[0:-1]) #Se imprime mediante slices un trozo de la lista, el cual va a comenzar desde el principio de la lista y va a terminar en el penultimo indice de la lista, para ello se usa los indices negativos para recorrer de izquierda a derecha la lista
print(lista1[3:7]) #Se imprime mediante slices un trozo de la lista, el cual comienza en un cierto punto y termina en cierto indice del final de la lista
# print(lista1[-7:-3]) #Se imprime mediante slices y indices negativos un trozo de la lista

lista1 = [1,"dos", 3, "cuatro"] #Se crea una lista que almacena elementos de tipo int y string
print(lista1) #Se imprime la lista
lista1[1] = 2 #Mediante indices se cambia el valor del elemento, cabe recalcar que al momento de cambiar el valor el valor antiguo se destruye
print(lista1) #Se imprime la lista ya con el nuevo valor del elemento que fue cambiado mediante indices
lista2=lista1 #Se crea una variable de lista la cual tiene el mismo valor que la lista 1, esto se hace para asi tener una copia de la lista 1 para asi poder modificar los elementos sin destruir los valores antiguos
print(f"Lista 1: {lista1}") #Se imprime mediante fstring los elementos de la lista 1, la cual no tiene el valor modificado mediante indices
print(f"Lista 2: {lista2}") #Se imprime mediante fstring la copia de la lista 1, la cual contiene el valor modificado
lista2[1] = 2 #Se modifica el valor mediante indice un elemento de la lista
print("-----------")#Separar un bloque de otro
print(f"Direccion: {id(lista1)},Lista 1: {lista1}") #Se imprime la direccion de memoria y los elementos de la lista 1
print(f"Direccion : {id(lista2)},Lista 2: {lista2}") #Se imprime la direccion de memoria y los elementos de la copia de lista 1, por lo tanto como es una copia esta tiene la misma direccion que la lista 1
print("Forma Correcta") #Se muestra la forma correcta de crear copias de una lista
lista1 = [1,"dos", 3, "cuatro"] #Se crea una lista que almacena elementos de tipo int y string
lista2 = lista1[:] #Se crea una variable que va a almacenar la copia de la lista 1 la cual se va a generar recorriendo la lista mediante slices, con esto es suficiente para asi tener dos listas con los mismos elementos pero con diferente direccion de memoria
print(f"Direccion: lista1: {id(lista1)}") #Se imprime la direccion de memoria de la lista 1
print(f"Direccion lista2: {id(lista2)}") #Se imprime la direccion de memoria de la copia de la lista 1, pero como esta fue obtenida recorriendo la lista mediante slices y gracias a eso se obtiene una copia de la lista 1 pero con diferente ID
lista2[1] = 2 #Se modifica mediante indices un elemento de la lista 1
lista2[3] = 4 #Se modifica mediante indices un elemento de la copia de la lista 1
print(f"Direccion: {id(lista1)}, lista1: {lista1}") #Se imprime mediante fstring la ID y la lista 1 con el elemento modificado
print(f"Direccion: {id(lista2)}, Lista2: {lista2}") #Se imprime mediante fstring la ID y la copia de la lista 1 con elemento modificado, como son dos listas distintas tienen diferente ID

lista1 = [0,1,2,3,4] #Se crea una lista con elementos de tipo int
lista2 = [5,6,7] #Se crea una lista con elementos de tipo int
#Insertar varios elementos al final de una lista
lista1[5:] = lista2 #Se recorre la lista 1 con slices y ese recorrido se guarda en la lista 2
lista1[len(lista1):] = lista2 #Se inserta mediante slices los elementos de la lista 2 a la lista 1 y de esa forma se insertan varios elementos al final de una lista
print(lista1) #Se imprime la lista 1 con los elementos agregados de la lista 2

#Insertar al inicio de una lista varios elementos (en una lista)
lista1[:0] = lista2 #Se recorre la lista 1 con slices y ese recorrido se guarda en la lista 2, y asi se insertan los elementos de la lista 2 al principio de la lista 1
print(lista1) #Se imprime la lista 1 con los elementos agregados de la lista 2

lista1.extend(lista2) #Agregar con el formato extend elementos a una lista, el extend lo que hace es sacar los elementos de una lista para asi poder agregarlos a otra
lista1.append(lista2) #Se agregan con append todos los elemetos de la lista 2 a la lista 1
print(lista1) #Se imprime la lista 1 con los elementos de la lista 1
#Como eleminar elementos de una lista
del(lista1[0]) #Se elemina con el metodo del un elemento de la lista 1 mediante su indice
print(lista1) #Se imprime la lista 1 sin elemento que fue eleminado

del(lista1[2:5]) #Se elemina con el metod del y slice un cierto trozo de elementos de la lista 1 que inicia en cierto indice y termina en otro cierto indice
print(lista1) #Se imprime la lista sin el trozo de elementos que fueron eleminados.
"""
