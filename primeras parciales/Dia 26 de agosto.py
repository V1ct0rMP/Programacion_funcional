#Hecho por: Victor Jesus Martinez Perez
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
