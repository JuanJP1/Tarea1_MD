# Uso de solid en el ejercicio 2 

## Pincipio S 

El principio S se utilizo de gran manera durante el ejercicio 2, a la hora de definir las clases se busco que cada clase se encargara de una funcion y tarea en concreto, se creo una clase para cada tipo de error, asi como una clase que se encargue solo de obtener los datos de la persona y otra que se encargue solo de usar la informacion proporcionada, posteriormente una clase se encargara de obtener los resultados del factor para la informacion de esta persona, asimismo una clase independiente se encarga de hacer calculos de cambio de moneda y finalmente una clase se encarga de la salida de el resultado, en general cada clase se encarga de una sola tarea.

## Prinipio O 

Se  busco que cada clase ceada sea capaz de añadir mas variables sin necesidad de modificarse mediante la implementacion de procesos concretos que puedan interferir a funciones o clases secundarias.

## Principio L

Todas las clases padres mantienen propiedades o atributos especificos tal que al usar herencia, las clases hijas no generen errores por atributos que no poseen o alteren estos atributos, principalmente se usa a la hora de el calculo de los factores donde la clase hija para Mujeres y para hombres poseen el mismo atributo pero de manera distinta, es por eso que en la clase padre no se especifican atributos especificos solo la propiedad.

## Pincipio I

En gran medida se busco hacer uso de variables "pequeñas" en vez de variables mas generales que puedan ocasionar algun conflicto a las demas variables 

## Principio D

En general no fue necesario usar en gran medida este principio, sin embargo, se busco que los modulos de alto nivel no fuesen afectados por los de bajo nivel, mediante la implementacion de una varibale intermedia que evite esto.

---

# Uso de solid en el ejercicio 3

## Principio S 

Para este principio nos aseguramos de que cada clase tuviera una sola tarea bien definida. Como la clase TextNormalizer que solo se encarga de limpiar el texto quitando puntos, comas, números y acentos mediante el método normalize(). Y como la clase HashTable que de dedica únicamente a guardar las palabras, evitar que se repitan usando buckets y llevar el conteo de frecuencias mediante add_or_increment().

## Principio O 

Aqui aplicamos este principio creando una clase base abstracta SorterStrategy con el método abstracto sort (). Gracias a esta clase base tenemos como subclases MergeSortStrategy y QuickSortStrategy. Como el código está abierto a extenderse pero cerrado a modificaciones, cuando necesitemos agregar otro algoritmo solo tendremos que crear una nueva subclase que herede de SorterStrategy y asi no tendremos que modificar la lógica general del programa.

## Principio L

Este principio se cumple pues al ser MergeSortStrategy y QuickSortStrategy subclases de SorterStrategy van a hacer exactamente lo que la clase base define, es decir, recibir una lista de palabras y regresarla ordenada alfabéticamente. Lo que nos puede permitir intercambiar MergeSortStrategy por QuickSortStrategy en cualquier momento de la ejecución para tomar los tiempos sin que el programa falle o altere el resultado.

## Principio I

Para este principio nos encargamos de dividir las responsabilidades en partes pequeñas, en lugar de crear una clase gigante que haga todo. Por ejemplo, el módulo que mide los tiempos de ejecución solo interactúa con la interfaz de ordenamiento (SorterStrategy) para tomar las lecturas de forma rapida, pues no necesita saber cómo funciona la limpieza del texto en TextNormalizer ni cómo la tabla hash (HashTable) cuenta las palabras y elimina los duplicados.

## Principio D

Este principio se utilizó en la estructura principal que coordina el diccionario, pues evitamos que dependiera directamente de los modulos de bajo nivel como lo son los algoritmos concretos. En lugar de instanciar QuickSortStrategy() dentro de la clase, esta recibe el algoritmo de ordenamiento desde afuera como una abstracción (SorterStrategy). Gracias a que le podemos "pasar" el algoritmo que queramos al momento de usarla, se facilita probar tanto MergeSortStrategy como QuickSortStrategy para tomar los tiempos sin tener que modificar ni una sola línea del código principal.


