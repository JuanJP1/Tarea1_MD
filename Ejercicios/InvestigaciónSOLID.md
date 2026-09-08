## 1. S — Single Responsibility Principle (Principio de Responsabilidad Única)

### Nombre completo del principio y qué problema de diseño busca resolver.
* **Nombre completo:** Single Responsibility Principle (SRP).
* **Problema de diseño que resuelve:** Este principio busca evitar que una clase se vuelva demasiado grande y termine haciendo muchas cosas al mismo tiempo.

Por ejemplo, podemos imaginar una clase que se encarga de registrar un producto, calcular su precio, mandar un correo al cliente y guardar la información en una base de datos. Aunque el programa pueda funcionar, la clase está haciendo demasiadas cosas.

El problema aparece cuando necesitamos modificar alguna de esas funciones. Por ejemplo, si cambiamos la forma en que se envían los correos, tendríamos que modificar una clase que también tiene otras responsabilidades. Esto puede hacer que el código sea más complicado de mantener y que sea más fácil cometer errores.

### Explicacion Conceptual
Se entiende ccomo que **una clase no debe encargarse de hacer demasiadas cosas diferentes**.

Puede tener varios métodos, pero todos deben estar relacionados con una misma responsabilidad. Si necesita hacer tareas diferentes, es mejor separarlas en otras clases.

Por ejemplo, una clase de una tienda puede encargarse de los productos y sus precios, pero no también de enviar correos o guardar archivos.

Así, el código queda más ordenado y es más fácil hacer cambios sin afectar otras partes del programa.


### Ejemplo en Python que viola el principio (Código malo)

Supongamos que tenemos una tienda en línea. La siguiente clase se encarga de diferentes cosas: calcular el total de una compra, enviar un mensaje al cliente y guardar la compra.

```python
class Compra:
    def __init__(self, productos):
        self.productos = productos

    def calcular_total(self):
        return sum(self.productos)

    def enviar_confirmacion(self):
        total = self.calcular_total()
        print(f"Compra confirmada. Total: ${total}")

    def guardar_compra(self):
        total = self.calcular_total()

        with open("compras.txt", "a") as archivo:
            archivo.write(f"Compra: ${total}\n")


¿Por qué NO cumple con el principio?

Porque la clase Compra está haciendo 3 cosas diferentes:

Calcula el total.
Envía una confirmación.
Guarda la compra.

Eso viola el Single Responsibility Principle, porque una sola clase está teniendo varias responsabilidades..

### Ejemplo en Python que viola el principio (Código Bueno)

class Compra:
    def __init__(self, productos):
        self.productos = productos

    def calcular_total(self):
        return sum(self.productos)


class ConfirmacionCompra:
    def enviar(self, compra):
        total = compra.calcular_total()
        print(f"Compra confirmada. Total: ${total}")


class GuardarCompra:
    def guardar(self, compra):
        total = compra.calcular_total()

        with open("compras.txt", "a") as archivo:
            archivo.write(f"Compra: ${total}\n")



Le esta manera, cada clase puede modificarse de forma independiente sin afectar las demás. Esto permite que el código sea más organizado, fácil de mantener y de modificar.


### FUENTE: DigitalOcean. SOLID: Los primeros 5  principios de diseño orientado a objetos.https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design-es






## 2. Open/Closed Principle (OCP) - Principio de Abierto/Cerrado

### Nombre completo y problema de diseño que busca resolver
* **Nombre completo:** Open/Closed Principle (Principio de Abierto/Cerrado).
* **Problema de diseño que resuelve:** Evita que tengamos que modificar el código que ya escribimos y probamos cada vez que queremos agregar una nueva función a nuestro programa. Modificar código existente es peligroso porque por error podemos romper partes del programa que ya funcionaban bien.

### Explicación conceptual
El objetivo de este principio es que podamos añadir nuevos comportamientos a un programa sin tener que editar la lógica que ya está escrita. Al estructurar las clases para que sean extensibles, evitamos modificar componentes existentes, lo cual protege el proyecto contra errores accidentales al momento de darle mantenimiento.

---

### Ejemplo en Python que viola el principio (Código malo)

Imaginemos un programa que reproduce el sonido de un animal. Si usamos un `if`, cada vez que queramos agregar un nuevo animal (como un perro), nos vemos obligados a modificar la clase existente.

```python
class Animal:
    def hacer_sonido(self, tipo: str):
        if tipo == "gato":
            print("Miau")
        # Si queremos agregar un perro, tenemos que MODIFICAR esta clase:
        # elif tipo == "perro":
        #     print("Guau")

### Ejemplo aplicando el principio (código bueno)

class Animal:
    def hacer_sonido(self):
        pass

# Clases individuales para cada animal
class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

# Agregamos un perro SIN modificar la clase Gato ni la clase Animal
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

# El reproductor ejecuta el sonido sin importar qué animal sea
class ReproductorSonido:
    def reproducir(self, animal: Animal):
        animal.hacer_sonido()
 
### Fuentes: García F. (28 de octubre de 2024), "Principios SOLID en programación orientada a objetos", Consultado el día 4 de septiembre de 2026 de https://www.arsys.es/blog/principios-solid-en-la-programacion-orientada-a-objetos#tree-2
