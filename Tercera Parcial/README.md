# Unidad III: Programación Funcional Con Elixir
##  Problemas resueltos en clase con el Lenguaje De Programacion Funcional Elixir
##  Ejercicio 1.1. Crear una calculadora con excepciones
## 1.1 Descripción del ejercicio
Se necesita crear una calculadora que al darle un argumento vacío u 0, no provoque fallas al momento de ejecucion
### 1.2 Código
```elixir
defmodule Calculadora do
  def div(_,0) do
    {:error, "No se puede dividir por 0"}
  end
  def div(n1,n2) do
    {:ok, "El resultado es: #{n1/n2}"
  end
end
```
### 1.3 Implementacion
```elixir
IO.inspect(Calculadora.div(5,0))
IO.inspect(Calculadora.div(5,3))
```
### 1.4 salida
```
>elixir main.ex
{:error, "No se puede dividir por 0"}
{:ok, "El resultado es: 1.6666666666666667"}
```
## Ejercicio 1.2. Crear un selector de sexo al mandar un atom como argumento
## 1.1 Descripción del ejercicio
Se necesita crear un selector de sexo que al mandar el atom :m como argumento retornar  "Masculino" y cuando se mande el atom :f como argumento retornar  Femenino" de no ser asi retornar  "Sexo desconocido".
### 1.2 Código
```elixir
defmodule Persona5 do
  def sexo(sex) when sex == :m, do: "Masculino"
  def sexo(sex) when sex == :f, do: "Femenino"
  def sexo(_sex), do: "Sexo desconocido"
end
```
### 1.3 Implementacion
```
iex> c("main.ex")
iex> Persona5.sexo(:m)
iex> Persona5.sexo(:f)
iex> Persona5.sexo(:x)
```
### 1.4 salida
```
[Persona5]
"Masculino"
"Femenino"
"sexo desconocido"
```
