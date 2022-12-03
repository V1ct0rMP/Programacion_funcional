#Victor Jesus Martinez Perez
#Apuntes Elixir
# Importaciones
# • Creamos un archivo fuente main.ex
# • Escribimos el siguiente código:
importar  Modulo Importado

defmodule  ModuloMain  do
  def  principal  do
    IO.puts( "Funcion principal" )
    funcion_importada( "Esta funcion es importada" )
  final
final

# • Creamos el Módulo a importar modsec.ex
# • Escribimos el siguiente código:
defmodule  ModuloImportado  do
  def  funcion_importada ( msg )  hacer
    IO _ pone ( mensaje )
  final
final

# • Compilamos en iex la función a importar
"""
iex> c("modsec.ex")
[Módulo Importado]
"""

# • Compilamos en iex la función que va a importar
"""
iex> c("principal.ex")
[Módulo Principal]
"""

# • Ejecutamos la función principal
"""
iex> MóduloPrincipal.main()
Función principal
Esta función es importada
:OK
"""

# Si no se quiere importar el módulo, se puede utilizar de manera directa indicando
# el módulo y la función esto es:

defmodule  ModuloMain  hacer
  def  principal  hacer
    IO _ puts ( "Funcion principal" )
    ModuloImportado  funcion_importada ( "Esta funcion es importada" )
  final
final

# • Es necesario volver a compilar la función principal
"""
iex(7)> c("principal.ex")
advertencia: redefiniendo módulo ModuloMain (versión actual definida en memoria)
principal.ex:3
[Módulo Principal]
iex(8)> MóduloPrincipal.main()
Función principal
Esta función es importada
:OK
"""

# Alias
# • Se puede utilizar alias como alternativa a import, permite hacer una referencia a
# un módulo con otro nombre

defmodule  ModuloMain  hacer
  alias  Módulo Importado ,  como  MI

  def  principal  hacer
    IO _ puts ( "Funcion principal" )
    MI . funcion_importada ( "Esta funcion es importada con alias" )
  final
final

# • golpe
"""
iex(10)> c("principal.ex")
advertencia: redefiniendo módulo ModuloMain (versión actual definida en memoria)
principal.ex:1
[Módulo Principal]
iex(11)> MóduloPrincipal.main()
Función principal
Esta función es importada con alias
:OK
"""
