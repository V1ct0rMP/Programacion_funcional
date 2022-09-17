#Hecho por: Victor Jesus Martinez Perez
#Array es una estrucutra de datos primitiva, que almacena cualquier tipo de dato y tiene una longitud
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
