// Dia 12 de octubre
// Calculadora que +,-,*,/ dos numeros como argumentos
// Creando una clase en la cual se crean las operaciones y el menu de opciones para realizar
void main(List<String> args) {
  calculadora calc = calculadora(); // Se crea una instancia(copia) de la clase calculadora
  calculadora miSuperCalcu = calculadora();
  if (args.length == 3){ // Se evalua la longitud de los parametros que se colocan al momento de ejecutar el programa en la terminal
    var a = int.parse(args[0]); // Se asigna el valor a una varianle se usa .parse para canvertir el caracter a un numero entero
    var b = int.parse(args[1]);
    calc.calcular(a, b,args[2]); // se realiza la operacion que se ingrese en la terminal al momento de ejecutar el programa
  }  
  else{ // se crea la parte falsa de la condicion
    print("Error de argumentos.");
    print("Ejemplo: datr main.dart 4 5");
  }
print(args);
for (var i = 0; i < args.length; i++) { // imperativo
print(args[i].runtimeType);
}
args.forEach((e) => print(e.runtimeType)); // declarativa
calculadora miCalcu = calculadora();
miCalcu.a = 5;
miCalcu.b = 10;
var n1 = 6;
var n2= 10;
int res = miCalcu.suma(miCalcu.a,miCalcu.b); // se realizan las operaciones dependiendo de la funcion y la instancia
print("${miCalcu.a} + ${miCalcu.b} = $res");
print("$n1 + $n2 = ${miSuperCalcu.suma(n1,n2)}");
int resul = miCalcu.resta(miCalcu.a, miCalcu.b);
print("${miCalcu.a} - ${miCalcu.b} = $resul");
print("$n1 + $n2 = ${miSuperCalcu.resta(n1,n2)}");
int resu = miCalcu.multi(miCalcu.a,miCalcu.b);
print("${miCalcu.a} * ${miCalcu.b} = $resu");
var re = miCalcu.div(miCalcu.a,miCalcu.b);
print("${miCalcu.a} / ${miCalcu.b} = $re");
}
class calculadora{ // se crea la clase calculadora en la cual se hacen las operaciones y se realiza el menu de operaciones
  int a = 0;
  int b = 0;
  int suma(int a, int b) => a + b; // forma declarativa. Se crean las funciones las cuales realizan las operaciones
  int resta(int a, int b) => a - b;
  int multi(int a, int b) => a * b;
  double div(int a, int b) => a / b;

  void calcular(int a, int b, String ope){ // se crea una funcion la cual realiza el menu de operaciones 
  calculadora cal = calculadora(); // se crea una instancia de la clase calculadora
  cal.a = a;
  cal.b = b;
  switch (ope) {
    case '+':
        print(suma(a,b));
      break;
    case '-':
        print(resta(a,b));
        break;  
    case '*':
        print(multi(a,b));
        break;
    case '/':
        print(div(a,b));
        break;            
    default:
        print("OPERACION INVALIDA.");
  }
}  
}
