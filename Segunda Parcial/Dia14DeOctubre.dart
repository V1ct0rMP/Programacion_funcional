// Dia 14 de octubre
// Crear objetos mediante una clase la cual contiene las propiedades y metodos del objeto
// Se hace el implemento de constructores para poder crear las propiedades del objeto
void main(List<String> args) {
  Vehiculo auto = new Vehiculo(4, "Rojo", "Versa 2022","Nissan"); // se crea el objeto mediante un constructor
  auto.showAuto(); //Se manda a llamar la funcion que muestra la informacion del objeto
  auto.arrancar(); // Se manda a llamar el metodo arrancar del objeto
  auto.correr(); // Se manda a llamar el metodo correr del objeto
  auto.frenar(); // Se manda a llamar el metodo frenar del objeto
  Vehiculo Raptor = new Vehiculo(4, "Blanco", "Ford", "Raptor 2022");
  Raptor.showAuto();
  Raptor.arrancar();
  Raptor.frenar();
  Raptor.correr();
  Vehiculo Lambo = new Vehiculo(4, "rojo", "Huracan Perfomant", "Lamborghini");
  Lambo.showAuto();
}

class Vehiculo{ // Se crea la clase del objeto donde vendran las propiedades y metodos del objeto
  int? _Llantas; // Se crea una variable para almacenar la propiedad del objeto y se hace una propiedad propio con _, se coloca ? para asi poder crear variables con valores nulos
  String? _color;
  String? _modelo;
  String? _marca;
  
  void set Llantas(int Llantas)=> _Llantas = Llantas; // Con Setter se establece el valor de las propiedades de objeto
  void set Color(String Color) => _color = Color;
  void set Modelo(String Modelo)=> _modelo = Modelo;
  void set Marca(String Marca)=> _marca = Marca;

  int get Llantas =>_Llantas!; //Con Getter se obtiene el valor de un campo o propiedad del objeto
  String get color => _color!;
  String get modeolo => _modelo!;
  String get marca=> _marca!;

  Vehiculo(int Nollantas,String color,String marca,String modelo){ //Creacion del constructor que no servira para poder varios objetos en un mismo programa
    this._Llantas = Nollantas; //Se crea las propiedades del objeto
    this._color = color;
    this._marca = marca;
    this._modelo = modelo;
  }

  void arrancar()=>print("Ya prendio tu."); //Se crea una funcion la cual contendra el metodo del objeto
  void correr()=> print("Soy veloz dijo el mcaquin.");
  void frenar()=>print("Frenale padrino.");

  void showAuto(){ // Se crea una funcion la cual mostrara la informacion del objeto
    print("Llantas:   ${_Llantas}");
    print("Color:     ${_color}");
    print("Modelo:    ${_modelo}");
    print("Marca:     ${_marca}");
  }
}
