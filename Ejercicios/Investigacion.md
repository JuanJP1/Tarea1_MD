# 10 Reglas Útiles de Estilo de Python (PEP 8)

Revisando la guía oficial de estilo de Python (**PEP 8**), existen directrices muy prácticas que van más allá de las reglas convencionales y ayudan a escribir un código más limpio y legible.

---

## 1. Salto de línea *antes* de un operador binario

En expresiones matemáticas o lógicas que abarcan varias líneas, PEP 8 recomienda hacer el salto de línea **antes** del operador binario (siguiendo la convención matemática propuesta por Donald Knuth). Esto permite alinear los operadores verticalmente en el margen izquierdo para identificar rápidamente cada operación.

### Antes (Incorrecto / No recomendado)
```python
# Los operadores quedan al final de cada línea
total = (precio_base +
         impuesto_estatal +
         recargo_envio -
         descuento_promocional)
```

### Después (Correcto / Conforme a PEP 8)
```python
# El operador precede al operando en la nueva línea
total = (precio_base
         + impuesto_estatal
         + recargo_envio
         - descuento_promocional)
```

---

## 2. Espaciado según la prioridad del operador

Cuando se combinan operadores con distintas prioridades dentro de una misma fórmula, PEP 8 permite omitir los espacios alrededor de los operadores de **mayor prioridad**. Esto ayuda a reflejar visualmente la jerarquía de evaluación.

### Antes (Incorrecto / No recomendado)
```python
# Se usa el mismo espaciado sin importar la prioridad
resultado = x * y + a * b
distancia = x ** 2 + y ** 2
```

### Después (Correcto / Conforme a PEP 8)
```python
# Sin espacios en multiplicaciones y potencias para marcar la jerarquía
resultado = x*y + a*b
distancia = x**2 + y**2
```

---

## 3. Uso explícito de `.startswith()` y `.endswith()`

Para verificar si una cadena comienza o termina con un texto específico, PEP 8 indica que se deben usar los métodos integrados `.startswith()` y `.endswith()` en lugar de utilizar rebanados de texto (*slicing*), evitando errores de índices y haciendo el código más claro.

### Antes (Incorrecto / No recomendado)
```python
# El slicing es menos legible y propenso a errores de índice
if archivo[-4:] == '.pdf':
    procesar(archivo)

if url[:5] == 'https':
    validar(url)
```

### Después (Correcto / Conforme a PEP 8)
```python
# Expresivo, seguro e idiomático
if archivo.endswith('.pdf'):
    procesar(archivo)

if url.startswith('https'):
    validar(url)
```

## 4.Nombres de funciones y variables
Las funciones y variables deben tener nombres en minúsculas y, si el nombre tiene varias palabras, se deben separar utilizando _. A esta forma de escribir nombres se le conoce como snake_case.

Ejemplos:

nombreUsuario= "Hannia"
calcularPromedio = 9.5


nombre_usuario = "Hannia"
calcular_promedio = 9.5


##  5.Constantes
Cuando un valor se considera una constante, su nombre debe escribirse completamente en mayúsculas y se deben utilizar _ para separar las palabras.

Ejemplo:

maxAlumnos = 50

MAX_ALUMNOS = 50

## 6. Indentación
La indentación es el espacio que se coloca al inicio de una línea para indicar que pertenece a un bloque de código. En Python se deben utilizar cuatro espacios por nivel.

Ejemplos:

if edad >= 18:
  print("Es mayor de edad")

if edad >= 18:
        print("Es mayor de edad")

## 7. Comentarios en linea
Los comentarios en la misma línea del código deben usarse solo cuando aportan valor real y no para explicar lo evidente. Para no ensuciar la lectura visual del código, PEP 8 exige separarlos del código fuente con al menos dos espacios en blanco, incluir un espacio después del símbolo "#" y comenzar el texto con mayúscula.

### ANTES (Incorrecto)
x = x + 1#incrementa x en 1
p = 0.16#tasa del IVA

### DESPUÉS (Correcto)
x = x + 1  # Compensación por el índice base cero

precio_total = subtotal * 1.16  # Aplica la tasa de impuesto estándar (16%)

## 8. Nombres de Variables Globales
Las variables globales de un módulo usan `snake_case`. Para evitar que variables internas se exporten al usar `from modulo import *`, se deben marcar como no públicas.

### Antes (Incorrecto)
Sin protección; exporta variables internas al exterior por accidente.
```python
CONFIG_INTERNA = "Dato sensible"  # Se exporta con import *
```
### Despues (Correcto)
```python
__all__ = ['CONEXION_PUBLICA']  # Solo exporta lo necesario

CONEXION_PUBLICA = "[https://api.com](https://api.com)"
_config_interna = "Dato sensible"  # Protegido con '_'
```
## 9.- Importaciones
Las importaciones en PEP 8 deben ir siempre al inicio del archivo (justo debajo del docstring del módulo y antes de variables globales), escribiendo una por línea y divididas en tres bloques de prioridad separados por una línea en blanco (librería estándar, librerías de terceros y módulos locales), priorizando importaciones absolutas y evitando el uso de asteriscos.
## Antes (Incorrecto / No recomendado)
```python
# Se tiene una forma mas limpia y se respetan reglas y recomendaciones
import os 
import pandas
import numpy

import formulas algebra 

```
## 10.- Molestias (Pet peeves)
Se establece la manera en que se deben de evitar espacios en blancos que son innecesarios que "ensucian" el codigo y algunas excepciones de espaciados.
### Antes (Incorrecto / No recomendado)
```python
# Hay demasiados espacios que son innecesarios y solo ensucian el codigo
precios_descuento = []
precios = [ 100 , 500 , 10000, 100 ] # Hay espacios de más
for i in precios:
    n = i *.8
    precios_descuento.append( n ) # Hay espacios de más
print( precios_descuento) # Hay un espacio de más
print(precios[0: 2]) # Deberia de haber mismo espaciado antes y despues de :
```
### Después (Correcto / Conforme a PEP 8)

```python
# Se eliminan los espacios que no son necesarios
precios_descuento = []
precios = [100, 500, 10000, 100]
for i in precios:
    n = i *.8
    precios_descuento.append(n)
print(precios_descuento)
print(precios[0:2])

```
