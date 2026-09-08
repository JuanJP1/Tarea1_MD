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
