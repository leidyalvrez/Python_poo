# POO en python 
introduccion a la Programacion Orientada a objetos (POO) en python 

## ¿porque aprender POO?

- Imagina que quieres crear un video juego, tienes guerreros, magos, dragones... Cada uno con sus propios puntos de vida, ataques y abilidades. ¿Cómo los organizo en codigo sin repetir todo una y ota vez? 

- la **Programacion Orientada a objetos (POO)** es la respuesta. En lugar de escribir instrucciones sueltas, modelas el mundo real con *objetos* que tienen caracteristicas y comportamientos. Es la forma en que estan constridos la mayoria de los programas profesionales del mundo

![POO](img/poo.png "POO") 

## Clase y obletos 

- Una clase es un tipo de datos cuyas variables se llaman objestos o instancias 

- La clase es la definicion del concepto del mundo real y los objetos o instancias son el propio 
"objeto" del mundo real 
- Las clses estan compuestas por dos elementos: 
    - **Atributos:** informacion que almacena la clase. 
    - **Mentodos:** operaciones que pueden realizarce con la clase 

## Definicion de una clase en python 

``` python 
class nombreClase: 
    def_int_(self, variable1, variable2):
        self.atributo1 = valor 1 
        self.atributo2 = valor 2 

    def nombeMetodo(self): 
        BloqueCodigo
```

- `class` : palabra reservada en python para definir una clase.
- `NombreClase` : nombre de la clase que se quiere crear.
- `def`: palabra reservada en python que se utiliza para definir tanto el constructor de la clase (metodo que se ejecuta la primera vez que usas una clase) como los diferentes metodos que tiene. 
- `__init__` : palabra reservada en python para definir el metodo constructor de la clase. el metodo `_int_` es lo primero que se ejecuta cuando creas un objeto de una clase. 
- `(sel, variables)`: parametro del constructor de la clase. El parametro `self` es obbligatorio y despues puedes poner tantos parametros como quieras. La forma de añadir parametros es la misma que en las funciones .
-`self.atributox`: forma de utilizacion y acceso a los atributos de la clase.
- `NombreMetodo`: nombre del metodo de la clase.
- `self` : parametro del metodo. El parametro `self` es obligatorio y despues puedes tener tantos parametros como quieras. La forma de añadir parametros es la misma que en las funciones.
- `BloqueCodigo` : instrucciones que ejecutara el metodo. 

**Al definir una clase tenga en cuenta:** 
- Puedes  definir tantos atributos como necesites. 
- Puedes definir tantos metodos como necesites.
- Puedes definir tantos parametros en el constructor y en los metodos como necesitas 