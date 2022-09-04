#listas
alumnos=["Hugo", "Paco", "Luis", "Lupita"] #Se crea una lista con elementos de tipo string(str)
print(f"Alumnos: {alumnos}") #Se imprime la lista completa con todos sus elementos

#Tuplas
alumnos= ("Hugo", "Paco", "Luis", "Lupita") #Se crea una Tupla con elementos de tipo string(str)
print(f"Alumnos: {alumnos}") #Se imprime la tupla completa con todos sus elementos

#sets
alumnos= {"Hugo", "Paco", "Luis", "Lupita"} #Se crea un Set con elementos de tipo string(str)
print(f"Alumnos: {alumnos}") #Se imprime el Set con todos sus elementos

#diccionarios
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
m_p_f = [10.5,8.34,7.92,9.11] #Se crea una lista con elementos de tipo entero(int) la cual almacena calificaciones de una materia
m_i = [6,9,7,10] #Se crea una lista con elementos de tipo entero(int) la cual almacena calificaciones de una materia

ancho=15 #Se le asigna el valor de separacion entre elementos a una variable que se encarge de acomodar de la mejor forma los elementos
print(f"{e[0]:^{ancho}}{e[1]:^{ancho}}{e[2]:^{ancho}}{e[3]:^{ancho}}") #Se imprime mediante fstring nuestra pequeña base de datos, se utiliza la variable de separacion para hacer mas estetica la base de datos
for i in range(len(alumnos)): #Se recorre la lista de alumnos para ingresar a cada elemento de ella}
   print(f"{alumnos[i]:<{ancho}}{m_e_d[i]:^{ancho}}{m_p_f[i]:^{ancho}}{m_i[i]:^{ancho}}") #Se asigna mediante fstring el valor de la calificacion a cada alumno y al final se imprime la base de datos
