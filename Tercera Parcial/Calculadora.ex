#Victor Jesus Martinez Perez 
#Calculadora en programacion Funcional con elexir
defmodule Calculadora do #se crea el modulo calculadora
    def suma(a,b), do: a+b #Se crea las funciones de las operaciones de la calculadora
    def resta(a,b), do: a-b
    def multi(a,b), do: a*b
    def divi(_,b) when b==0, do: "Error division por cero" #Se valida para que no se pueda dividir entre 0
    def divi(a,b), do: a/b
    def pot(a), do: a*a

    def test() do #Se crea una funcion en la cual se llama a las funciones de las operaciones
        p suma(2,3)
        p resta(4,2) 
        p multi(5,6)
        p divi(4,5)
        p divi(4,0)
        p pot(4)
    end

    def p(funcion) do #Se crea una funcion la cual imprime en consola los resultados
        IO.puts funcion
    end
end

Calculadora.test() #Se manda a llamar el modulo principal y la funcion que realiza las operaciones
