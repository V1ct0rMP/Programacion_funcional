#Hecho por: Victor Jesus Martinez Perez
#1._Escibir una funcion que reciba un mensaje y un nombre y escriba en pantalla "<mensaje> <nombre>
def saludar(mensaje:str, nombre:str)->str: #Asignar como valores de entrada mensaje y nombre con tipo de dato string(str) y arroje una salida de tipo string
   print(f"{mensaje} {nombre}")
#
# 2._ Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de salida tiene
# que ser: "Hola <nombre> tienes <edad> años
def mensaje(nombre:str, edad:int)->str: #Asignar como valores de entrada nombre de tipo string y edad de tipo int y arroje una salida de tipo string
   print("Hola", (nombre), "tienes", (edad), "años")
#
#3._ Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior
#  enviando esta como argumento obtenga el mensaje: "Hola <nombre> tienes <edad> años
def calcular_edad(año_actual:int, año_nacimiento:int, nombre:str)->str: #Asignar como valores de entrada año_actual y año_nacimiento que son tipo integer(int) y un tercer parametro nombre de tipo string el cual se usa para llamar la funcion como parametro y arroje una salida de tipo string
   edad = año_actual - año_nacimiento
   return mensaje(nombre,edad) #Llamado de la funcion calcular_edad como parametro de la funcion calcular_edad


# if __name__ == "__main__":
   print("Escibir una funcion que reciba un mensaje y un nombre y escriba en pantalla <mensaje> <nombre>")
   saludar("Hola","Victor")
   print("Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de salida tiene que ser: Hola <nombre> tienes <edad> años")
   mensaje("Victor", "20")
   print("Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: Hola <nombre> tienes <edad> años")
   calcular_edad(2022,2002,"Victor")
