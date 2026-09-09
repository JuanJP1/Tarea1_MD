# Ejercicio 2 parte 3

class Asegurado: # Una clase general para un asegurado cualquiera 
  def __init__(self, edad, suma_asegurada, fumador, extra_prima):
        self.edad = edad
        self.suma_asegurada = suma_asegurada
        self.fumador = fumador
        self.extra_prima = extra_prima
  def calcular_edad_ajustada(self):
        edad_ajustada = self.edad
        if not self.fumador:
            edad_ajustada -= 5 # Se restan 5 años si la persona no fuma
        if self.extra_prima:
            edad_ajustada += 10 # Se suman 10 años si se tiene extra prima
        
        # Nos aseguramos que la edad no pase de 99 ni baje de 18
        return max(18, min(99, edad_ajustada))
  def obtener_factor_edad(self):
        # Este método se sobreescribe en las clases hijas
        # Todo asegurado tiene factor, sin embargo, distintos
        return 1.0 # Un valor neutro con el que se calculara el factor
  def calcular_prima(self):
        factor = self.obtener_factor_edad()
        return (self.suma_asegurada * factor) / 1000

# Se desprenden dos categorias de asegurados que tienen propiedades diferentes

class AseguradoFemenino(Asegurado): # Clase propia para mujeres
    def calcular_edad_ajustada(self):
        # Las mujeres restan 10 años 
        edad = super().calcular_edad_ajustada() - 10
        return max(18, min(99, edad))

    def obtener_factor_edad(self):
        edad = super().calcular_edad_ajustada()
        if 18 <= edad <= 25: return 1.5
        elif 25 < edad <= 45: return 1.7
        elif 45 < edad <= 65: return 2.0
        else: return 2.2

class AseguradoMasculino(Asegurado): # Clase propia para hombres
    def obtener_factor_edad(self):
        edad = self.calcular_edad_ajustada()
        if 18 <= edad <= 25: return 2.0
        elif 25 < edad <= 45: return 2.3
        elif 45 < edad <= 65: return 2.5
        else: return 3.0

# Ejercicio 2 parte 4

class Conversor_de_moneda:
    def __init__(self, tasa_cambio=21.13): # Con 21.13 por defecto
        # Validar que la que el cambio sea valido
        if tasa_cambio <= 0:
            raise ValueError("La tasa de cambio debe ser un número mayor a cero.")
        self.tasa_cambio = tasa_cambio
        # si el valor es valido guardamos el dato 
# Se guarda el valor de cambio si este fue valido 
    def mxn_a_usd(self, monto_mxn): 
        return monto_mxn / self.tasa_cambio 
# Dado un monto en mxn se regresa la conversion para la tasa de cambio guardada
