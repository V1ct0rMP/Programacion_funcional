// Dia 14 de octubre
// Se empieza a trabajar con clases, propiedades y metodos
  class User{ //Se crea la clase
    //Propiedades
    String? _name; //Se crea una variable la cual tendra el valor de la propiedad de la clase con _ hace que la propiedad sea propia de esa clase
    int? _age;
    //Metodos
    set Nombre(String Nombre) => _name = Nombre; //Con Setter se estable el valor de la propiedad de la clase
    set Edad(int Edad)=> _age = Edad;
    void reporte(){ //Se crea una funcion la cual imprimira las propiedades de la clase
      print("Nombre:  ${_name}");
      print("Edad:    ${_age}");
    }
  }

  class Estudiante{ //Se crea una clase de Estudiante
  String? carrera; //Se crea una variable la cual tendra el valor de la propiedad de la clase
  int? semestre;
  String? No_Cuenta;
  void reporte(){
  print("Carrera: $carrera"); //Se crea una funcion la cual imprimira las propiedades de la clase
  print("Semestre: $semestre");
  print("Numero de cuenta: $No_Cuenta");
  }
  }
  void main() {
  User usuario1 = User(); //Se crea una instancia de la clase User
  usuario1.Nombre = "Victor"; //Se le asigna los valores de las propiedades de la clase
  usuario1.Edad = 20;
  print(usuario1._name); //Se imprimen los valores de las propiedades de la clase
  print(usuario1._age);
  usuario1.reporte(); //Se manda a llamar la funcion que muestra por pantallas las propiedades de la clase
  var usuario2 = User(); // Se crea una instancia de la clase User
  usuario2._name = "Victor"; //Se le asigna los valores de las propiedades de la clase
  usuario2._age = 20;
  usuario2.reporte(); //Se manda a llamar la funcion que muestra por pantallas las propiedades de la clase
  var alumno = Estudiante(); //Se crea una instancia de la clase Estudiante
  alumno.No_Cuenta = "20173430"; //Se le asigna los valores de las propiedades de la clase
  alumno.carrera = "ICI";
  alumno.semestre = 3;
  alumno.reporte(); //Se manda a llamar la funcion que muestra por pantallas las propiedades de la clase
  }
  // encapsulamiento
  //- ocultar los atributos de la clase
  //- hacerlos locales dentro de la clase
  //- el simbolo _
