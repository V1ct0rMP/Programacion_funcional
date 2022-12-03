# Unidad III: Programación Funcional Con Elixir
##  Problemas resueltos en clase con el Lenguaje De Programacion Funcional Elixir
##  Ejercicio 1.1. Crear una calculadora con excepciones
## 1.1 Descripción del ejercicio
Se necesita crear una calculadora que al darle un argumento vacío u 0, no provoque fallas al momento de ejecucion
### 1.2 Código
defmodule Calculadora do
  def div(_,0) do
    {:error, "No se puede dividir por 0"}
  end
  def div(n1,n2) do
    {:ok, "El resultado es: #{n1/n2}"}
  end
end
### 1.3 Implementacion
IO.inspect(Calculadora.div(5,0))
IO.inspect(Calculadora.div(5,3))
### 1.4 salida
>elixir main.ex
{:error, "No se puede dividir por 0"}
{:ok, "El resultado es: 1.6666666666666667"}
