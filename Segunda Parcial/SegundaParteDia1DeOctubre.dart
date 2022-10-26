/ Dia 12 de octubre
// Creacion de clases usando propiedades
// Se crea una clase persona en el cual sus propiedad son los datos de la persona y despues se muestran sus propiedades

void main(List<String> args) {
  persona per = new persona(); // se crea una instancia de la clase persona
  per.nombre = "Victor Jesus"; // se asigna a las variables de las propiedades
  per.aPaterno = "Martinez";
  per.aMaterno = "Perez";
  per.aNaci = 2002;
  per.showName(per.nombre,per.aPaterno,per.aMaterno); // se muestran los datos ingresados
  print("Tienes ${per.calcularEdad(per.aNaci)} años"); // se muestra la edad de la persona usando una funcion que calcula su edad
  per.showName2(); // se muestran los resultados
}

class persona{ // se crea la clase con sus propiedades
  String nombre = "";
  String aPaterno = "";
  String aMaterno = "";
  int aNaci = 0;

  int calcularEdad(int aNaci) => 2022-aNaci; // se crea la funcion para calcular la edad
  void showName(String nombre, String aPaterno, String aMaterno){ // se crea una funcion que muestra resultados
    print("Hola $nombre $aPaterno $aMaterno");
  }

  void showName2(){
    print("$nombre $aPaterno $aMaterno");
  }
}
