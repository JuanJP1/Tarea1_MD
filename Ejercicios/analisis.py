


#Ejercicio 2 parte 1 

# Creamos los errores personalizados
class EdadInvalidaError(Exception):
    pass


class SexoInvalidoError(Exception):
    pass


class FumadorInvalidoError(Exception):
    pass


class ExtraPrimaInvalidaError(Exception):
    pass


class SumaAseguradaInvalidaError(Exception):
    pass


# Validamos la edad
def solicitar_edad():
    while True:
        try:
            edad = int(input("Ingrese la edad (18-99): "))

            if edad < 18 or edad > 99:
                raise EdadInvalidaError("Edad fuera de rango.")

            return edad

        except ValueError:
            print("Error: ingresa un número entero.")
        except EdadInvalidaError as e:
            print(f"Error: {e}")


# Validamos el sexo
def solicitar_sexo():
    while True:
        try:
            sexo = input("Ingrese el sexo (M/F): ").strip().upper()

            if sexo not in ("M", "F"):
                raise SexoInvalidoError("Solo se acepta M o F.")

            return sexo

        except SexoInvalidoError as e:
            print(f"Error: {e}")


# Validamos si fuma
def solicitar_fumador():
    while True:
        try:
            fumador = input("¿Es fumador? (Si/No): ").strip().lower()

            if fumador not in ("si", "no"):
                raise FumadorInvalidoError("Solo se acepta Si o No.")

            return fumador

        except FumadorInvalidoError as e:
            print(f"Error: {e}")


# Validamos la extra-prima
def solicitar_extra_prima():
    while True:
        try:
            extra_prima = input("¿Tiene extra-prima? (Si/No): ").strip().lower()

            if extra_prima not in ("si", "no"):
                raise ExtraPrimaInvalidaError("Solo se acepta Si o No.")

            return extra_prima

        except ExtraPrimaInvalidaError as e:
            print(f"Error: {e}")


# Validamos la suma asegurada
def solicitar_suma_asegurada():
    while True:
        try:
            entrada = input("Ingrese la suma asegurada: ")
            entrada = entrada.replace(",", "").replace("$", "")

            sa = float(entrada)

            if sa < 500000 or sa > 3000000:
                raise SumaAseguradaInvalidaError(
                    "Debe estar entre $500,000 y $3,000,000."
                )

            return sa

        except ValueError:
            print("Error: ingresa un número.")
        except SumaAseguradaInvalidaError as e:
            print(f"Error: {e}")


# Ajustamos la edad según las condiciones
def ajustar_edad(edad, fumador, sexo, extra_prima):
    edad_ajustada = edad

    if fumador == "no":
        edad_ajustada -= 5

    if sexo == "F":
        edad_ajustada -= 10

    if extra_prima == "si":
        edad_ajustada += 10

    # Mantenemos la edad entre 18 y 99
    edad_ajustada = max(18, min(99, edad_ajustada))

    return edad_ajustada


# Obtenemos el factor según edad y sexo
def obtener_factor(edad, sexo):

    if sexo == "F":
        if 18 <= edad < 25:
            return 1.5
        elif 25 <= edad < 45:
            return 1.7
        elif 45 <= edad < 65:
            return 2.0
        else:
            return 2.2

    else:
        if 18 <= edad < 25:
            return 2.0
        elif 25 <= edad < 45:
            return 2.3
        elif 45 <= edad < 65:
            return 2.5
        else:
            return 3.0


# Calculamos la prima
def calcular_prima(sa, factor):
    return (sa * factor) / 1000


# Programa principal
def main():

    print("=" * 40)
    print("      CALCULADORA DE SEGURO")
    print("=" * 40)

    # Pedimos todos los datos
    edad = solicitar_edad()
    sexo = solicitar_sexo()
    fumador = solicitar_fumador()
    extra_prima = solicitar_extra_prima()
    sa = solicitar_suma_asegurada()

    # Ajustamos la edad
    edad_ajustada = ajustar_edad(
        edad, fumador, sexo, extra_prima
    )

    # Buscamos el factor
    factor = obtener_factor(edad_ajustada, sexo)

    # Calculamos la prima
    prima = calcular_prima(sa, factor)

    # Mostramos los resultados
    print("\n========== RESULTADOS ==========")
    print(f"Edad original: {edad}")
    print(f"Sexo: {sexo}")
    print(f"Fumador: {'Sí' if fumador == 'si' else 'No'}")
    print(f"Extra-prima: {'Sí' if extra_prima == 'si' else 'No'}")
    print(f"Suma asegurada: ${sa:,.2f} MXN")
    print(f"Edad ajustada: {edad_ajustada}")
    print(f"Factor K: {factor}")
    print(f"Prima anual: ${prima:,.2f} MXN")
    print("================================")


# Iniciamos el programa
if __name__ == "__main__":
    main()
    
    




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

#Ejercicios 2 parte 5
def exportar_carnet(asegurados, conversor, ruta_archivo="carnet_asegurados.txt"):
    """
    Exporta el carnet de cada objeto 'Asegurado' a un archivo de texto.
    Maneja excepciones de escritura mediante try/except.
    """
    try:
        with open(ruta_archivo, "w") as archivo:
            for a in asegurados:
                prima_mxn = a.calcular_prima()

                # Uso de try/except para manejar posibles errores en la conversión de moneda
                try:
                    prima_usd = conversor.mxn_a_usd(prima_mxn)
                    prima_usd_str = f"${prima_usd} USD"
                except Exception:
                    prima_usd_str = "Error al convertir a USD"

                es_fumador = "Sí" if a.fumador else "No"
                tiene_extra_prima = "Sí" if a.extra_prima else "No"

                print("--- Asegurado ---", file=archivo)
                print(f"Edad Real: {a.edad} años", file=archivo)
                print(f"Edad Ajustada: {a.calcular_edad_ajustada()} años", file=archivo)
                print(f"Fumador: {es_fumador}", file=archivo)
                print(f"Extra-prima: {tiene_extra_prima}", file=archivo)
                print(f"Suma Asegurada (SA): ${a.suma_asegurada} MXN", file=archivo)
                print(f"Prima Anual (MXN): ${prima_mxn} MXN", file=archivo)
                print(f"Prima Anual (USD): {prima_usd_str}", file=archivo)
                print("-" * 45 + "\n", file=archivo)

        print(f"\nEl carnet se ha guardado en: '{ruta_archivo}'")

    except PermissionError:
        print(f"Error de permisos: No se puede escribir en la ruta '{ruta_archivo}'.")
    except FileNotFoundError:
        print(f"Error de ruta: La ubicación especificada no existe: '{ruta_archivo}'.")
    except OSError as e:
        print(f"Error de E/S del sistema al guardar el archivo: {e}")
    except Exception as e:
        print(f"Error inesperado al exportar los datos: {e}")