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
