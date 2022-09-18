# Unidad I: Tópicos Avanzados de Programación
## Problemas resueltos en clase con Python3
### Ejercicio 1.1. Escribir una funcion que reciba dos argumentos de tipo string e imprima en pantalla "Hola {argumento1} tienes {argumento2} años"
### 1.1 Descripcion del ejercicio
  Se necesita crear una funcion que en sus argumentos los hints sean argumento1 como tipo de dato str y arugmento2 como tipo de dato str y el valor de salida será de tipo string y posteriormente mandarla a llamar introduciendole sus argumentos.  Y finalmente imprimirá en pantalla "Hola {nombre} tienes {edad} años".
#### 1.2 Código
```python
def funcion1(a: str, b: str) -> str:
    return f"<{a}> <{b}>"
```
 #### 1.3 Implementación
 ```python
print(funcion1("Hola", "Victor")
 ```
#### 1.4 Salida
```
Hola Victor
```

### Ejercicio 1.2 Escribir una funcion que reciba el nombre y la edad de una persona. EL mensaje de saluda tiene que ser: "Hola {nombre} tienes {edad} años"
#### 1.1 Descripcion del ejercicio
Se necesita crear una funcion que en sus argumentos los hints sean argumento1 como tipo de dato str y arugmento2 como tipo de dato int y el valor de salida será de tipo string y posteriormente mandarla a llamar introduciendole sus argumentos.  Y finalmente imprimirá en pantalla "Hola {nombre} tienes {edad} años".
#### 1.2 Código
```python
def funcion2(a: str, b: int) -> str:  
    return f"Hola {a} tienes {b} años"
```
#### 1.3 Implementación
```python
print(funcion2("Victor", 20))
```
#### 1.4 Salida
```
Hola Victor tienes 20 años
```

### Ejercicio 1.3 Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: "Hola {nombre} tienes {edad} años"
#### 1.1 Descripcion del ejercicio
Se necesita crear una funcion que en sus argumentos los hints sean argumento1 como tipo de dato int, argumento2 como tipo de dato int y argumento3 como tipo de dato str y el valor de salida sea de tipo string, se debe usar la funcion del anterior ejercicio dentro de esta funcion para hacer el proceso. Y finalmente imprimirá en pantalla "Hola {nombre} tienes {edad} años".
#### 1.2 Código
```python
def mensaje(a: int, b: int, c: str) -> str:
    Edad = a - b
    return funcion2(c, Edad)
```
#### 1.3 Implementación
```python
print(mensaje(2022, 2002, "Victor"))
```
#### 1.4 Salida
```
Hola Victor tienes 20 años
```

### Ejercicio 1.4 Importacion de modulos
#### 1.1 Descripcion del ejercicio
Conocer el uso de la importacion de modulos desde otros archivos para tener una presentacion mas limpia y facilitar la lectura del codigo.
#### 1.2 Código
```python
import ops.operaciones as op
import ops.sumar as s
import ops.cuadrado as c
from ops.operaciones import multiplicar
```
#### 1.3 Implementación
```python
a = 10    
b = 5     
print(s.sumar(a,b))  
print(op.restar(a,b))
print(op.dividir(a,b))
print(c.cuadrado(a))
print(multiplicar(a,b))
```
#### 1.4 Salida
```
15
5
2.0
100
50
```
### Ejercicio 1.5 Hacer una funcion que reciba el nombre de una persona y el año de nacimiento de una persona el año de nacimiento y el año actual retornando el mensaje "Hola {nombre}, tienes {edad} años"
#### 1.1 Descripcion del ejercicio
Se necesita crear una funcion que en sus argumentos los hints sean argumento1 como tipo de dato int, argumento2 como tipo de dato int y argumento3 como tipo de dato int y el valor de retorne un valor de tipo str. La funcion imprimira en pantalla el mensaje "Hola {nombre}, tienes {edad} años".
#### 1.2 Código
```python
def funcion1(nombre:str, año_actual:int, año_nac:int)->str
    edad=año_actual - año_nac
    return f"Hola {nombre}, tienes {edad} años"

def funcion2(nombre:str, año_actual:int, año_nac:int)->str:
    return f"Hola {nombre}, tienes {año_actual-año_nac} años"

def calcular_edad(año_actual:int, año_nac:int)->int:
    return año_actual - año_nac

def funcion3(nombre:str, año_actual:int, año_nac:int)->str
    return f"Hola {nombre}, tienes {calcular_edad(año_actual-año_nac) años"
```
#### 1.3 Implementación
```python
print(funcion1("Victor", 2022, 2002))
print(funcion2("Victor", 2022, 2002))  
respuesta = funcion1("Victor", 2022, 2002)   
print(respuesta)
print(funcion3("Victor", 2022, 2002))
```
#### 1.4 Salida
```
Hola Victor, tienes 20 años
Hola Victor, tienes 20 años
Hola Victor, tienes 20 años
Hola Victor, tienes 20 años
```

### Ejercicio 1.6 Escriba una funcion que genere una tabla de multiplicar recibiendo como argumento la cantidad de numeros y la tabla a generar
#### 1.1 Descripcion del ejercicio
Se necesita crear una funcion que en sus argumentos los hints sean dos valores de tipo de dato int y retorne la multiplicacion de uno por el otro. Posteriormente Escribir una funcion que haga uso de la funcion anterior y que en sus argumentos los hints sean 3 argumentos de tipo de dato int y retorne y tipo de dato int. Y finalmente imprimirá en pantalla una tabla de multiplicar de algun numero hasta n numero.
#### 1.2 Código
```python
def multiplicar_numeros(x:int,y:int)->int: 
    return x*y

def tabla_multiplicar(num:int,total:int)->int:
    print(f"Tabla de multiplicar del {num}")
    for i in range(1, total+1):           
        print(f"{num:<3}x{i:^4}={multiplicar_numeros(i,num):>4}")
    return 0
```
#### 1.3 Implementación
```python
tablamultiplicar(1, 10)
```
#### 1.4 Salida
```
Tabla de multiplicar del 1
1  x 1  =   1
1  x 2  =   2
1  x 3  =   3
1  x 4  =   4
1  x 5  =   5
1  x 6  =   6
1  x 7  =   7
1  x 8  =   8
1  x 9  =   9
1  x 10 =  10
```

### Ejercicio 1.7 Hacer una funcion que haga n tablas de multiplicar de n hasta n numeros con n numeros de la tabla de multiplicar de la misma
### 1.1 Descripcion del ejercicio
Crear una funcion que en sus hints los argumentos sean 3 de tipo de dato int y retorne un valor de tipo de dato int. La funcion hará uso de la anterior funcion del ejercicio pasado. Y finalmente tendrá que imprimir una lista de tablas de multiplicar hasta n numero, de algun numero hasta n numero.
### 1.2 Código
```python
def multitablas(num_tablas:int,num:int,total:int)->int:    
    print(f"Tablas de multiplicar de 1 hasta {num_tablas})
    for i in range(1, num_tablas+1):
        tabla_multiplicar(num,total)
        print()  
        num+=1   
    return 0
```
### 1.3 Implementación
```python
multitablas(3, 1, 10)
```
### 1.4 Salida
```
Tablas de multiplicar de 1 hasta 3
Tabla de multiplicar del 1
1  x 1  =   1
1  x 2  =   2
1  x 3  =   3
1  x 4  =   4
1  x 5  =   5
1  x 6  =   6
1  x 7  =   7
1  x 8  =   8
1  x 9  =   9
1  x 10 =  10

Tabla de multiplicar del 2
2  x 1  =   2
2  x 2  =   4
2  x 3  =   6
2  x 4  =   8
2  x 5  =  10
2  x 6  =  12
2  x 7  =  14
2  x 8  =  16
2  x 9  =  18
2  x 10 =  20

Tabla de multiplicar del 3
3  x 1  =   3
3  x 2  =   6
3  x 3  =   9
3  x 4  =  12
3  x 5  =  15
3  x 6  =  18
3  x 7  =  21
3  x 8  =  24
3  x 9  =  27
3  x 10 =  30
```
