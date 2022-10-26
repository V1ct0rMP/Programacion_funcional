// Dia 19 de octubre 
// Creacion de una clase principal y las demas contendran las propiedades de la clase principal
// Se usa la herencia para poder usar las propiedades de la clase principal en las demas clases 
void main(List<String> args) {
  Animal Perro = new Animal(); // Se crea una instancia de la clase Animal
  Perro.patas = 4; // Se asigna el valor a la propiedad del objeto
  Perro.nombre = "Pocho";
  Perro.showAnimal(); //Se llama a la funcion que se encarga de mostrar las propiedades del objeto
  Perro.caminar(); //Se llama el metodo del objeto
  perro Pitbull = perro.caractereristicas("Pitbull"); //Se crea una instancia de la clase hijo
  Pitbull.patas=4;//Se le asigna el valor de las propiedades de la clase hijo
  Pitbull.nombre="Pocho";
  Pitbull.info(); //Se llama a la funcion que se encarga de mostrar las propiedades del objeto
  Pitbull.ladra(); //Se llama el metodo del objeto
  Pitbull.camina(); //Se llama el metodo del objeto
  Avestrus ave = Avestrus.carac("DESIERTO"); //Se crea una instancia de la otra clase hijo
  ave.patas=2; //Se le asigna el valor de las propiedades de la clase hijo
  ave.nombre="POPEYE";
  ave.info(); //Se llama a la funcion que se encarga de mostrar las propiedades del objeto
  ave.vuela(); //Se llama el metodo del objeto
  ave.aletea();
}

class Animal{ //Se crea la clase principal
  int? patas;//Se crea la variable que contiene las propiedades del objeto, se coloca ? para poder crear variables con valor nulo
  String? nombre;

  void caminar()=>print("Empieza a caminar"); //Se crea el metodo del objeto

  Animal({this.nombre,this.patas}); //Se crea el constructor que se encarga de crear las propiedades del objeto

  void showAnimal(){ //Se crea una funcion que se encargara de mostrar las propiedades del objeto
    print("Patas:    ${patas}");
    print("Nombre:   ${nombre}");
  }

}

class perro extends Animal{ //Se crea una clase hijo la cual heredara las propiedades de la clase principal
  String? _raza; //Se crea la variable que contiene las propiedades del objeto, se coloca ? para poder crear variables con valor nulo

  void ladra(){  //Se crea el metodo del objeto
    print("gua gua ladra el perrito.");}

  void camina(){
    print("Camina el perrito.");}

  perro.caractereristicas(this._raza); //Se crea el constructor que se encarga de crear las propiedades del objeto

  void info(){ //Se crea una funcion que se encargara de mostrar las propiedades del objeto
    print("EL ANIMAL ${_raza} TIENE ${patas} patas y se llama ${nombre}");
  }
}
class Avestrus extends Animal{  //Se crea otra clase hijo la cual heredara las propiedades de la clase principal
  String? _habitad; //Se crea la variable que contiene las propiedades del objeto, se coloca ? para poder crear variables con valor nulo

  void vuela()=>print("Empieza a volar el ave."); //Se crea el metodo del objeto
  void aletea()=>print("Empieza a aletear.");

  Avestrus.carac(this._habitad); //Se crea el constructor que se encarga de crear las propiedades del objeto

  void info(){ //Se crea una funcion que se encargara de mostrar las propiedades del objeto
    print("El AVESTRUZ HABITA EN ${_habitad} TIENE ${patas} Y SE LLAMA ${nombre}");
  }
}
