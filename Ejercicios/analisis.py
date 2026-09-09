
from abc import ABC, abstractmethod


# ==============================================================================
# 1. VALIDACIÓN ROBUSTA (Excepciones y Captura)
# [PRINCIPIO SOLID: SRP - Single Responsibility Principle]
# Cada función de captura tiene una única responsabilidad: validar y devolver un único dato.
# ==============================================================================

class EdadInvalidaError(Exception):
    """Excepción personalizada para cuando la edad no está en el rango [18, 99]."""
    pass


class SexoInvalidoError(Exception):
    """Excepción personalizada para entradas de sexo distintas a 'M' o 'F'."""
    pass


class FumadorInvalidoError(Exception):
    """Excepción personalizada para respuestas de fumador distintas a 'Si' o 'No'."""
    pass


class ExtraPrimaInvalidaError(Exception):
    """Excepción personalizada para respuestas de extra-prima distintas a 'Si' o 'No'."""
    pass


class SumaAseguradaInvalidaError(Exception):
    """Excepción personalizada para sumas aseguradas fuera de [$500,000, $3,000,000]."""
    pass


def solicitar_edad() -> int:
    """Solicita e ingresa la edad del asegurado con manejo de excepciones."""
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


def solicitar_sexo() -> str:
    """Solicita e ingresa el sexo ('M'/'F') con validación robusta."""
    while True:
        try:
            sexo = input("Ingrese el sexo (M/F): ").strip().upper()
            if sexo not in ("M", "F"):
                raise SexoInvalidoError("Solo se acepta M o F.")
            return sexo
        except SexoInvalidoError as e:
            print(f"Error: {e}")


def solicitar_fumador() -> bool:
    """Solicita si el asegurado fuma o no."""
    while True:
        try:
            fumador = input("¿Es fumador? (Si/No): ").strip().lower()
            if fumador not in ("si", "no"):
                raise FumadorInvalidoError("Solo se acepta Si o No.")
            return fumador == "si"
        except FumadorInvalidoError as e:
            print(f"Error: {e}")


def solicitar_extra_prima() -> bool:
    """Solicita si el asegurado cuenta con recargo de extra-prima."""
    while True:
        try:
            extra_prima = input("¿Tiene extra-prima? (Si/No): ").strip().lower()
            if extra_prima not in ("si", "no"):
                raise ExtraPrimaInvalidaError("Solo se acepta Si o No.")
            return extra_prima == "si"
        except ExtraPrimaInvalidaError as e:
            print(f"Error: {e}")


def solicitar_suma_asegurada() -> float:
    """Solicita e ingresa la suma asegurada en MXN dentro del rango permitido."""
    while True:
        try:
            entrada = input("Ingrese la suma asegurada ($500,000 - $3,000,000): ")
            entrada = entrada.replace(",", "").replace("$", "").strip()
            sa = float(entrada)
            if sa < 500000 or sa > 3000000:
                raise SumaAseguradaInvalidaError(
                    "Debe estar entre $500,000 y $3,000,000 MXN."
                )
            return sa
        except ValueError:
            print("Error: ingresa un número válido.")
        except SumaAseguradaInvalidaError as e:
            print(f"Error: {e}")


# ==============================================================================
# 2. PROCESAMIENTO POR LOTES Y REPORTE ESTADÍSTICO
# Controla la captura secuencial de N asegurados y el despliegue del reporte.
# ==============================================================================

def procesar_lote_asegurados():
    """Ejecuta el procesamiento por lotes para N asegurados y genera el reporte general."""
    print("=" * 50)
    print("      CALCULADORA DE PRIMAS POR LOTES (ASEGURADORA)")
    print("=" * 50)

    while True:
        try:
            n = int(input("Ingrese la cantidad de asegurados a procesar (N >= 1): "))
            if n < 1:
                print("Debe ingresar al menos 1 asegurado.")
                continue
            break
        except ValueError:
            print("Error: Ingresa un número entero válido.")

    lista_asegurados = []

    # Bucle de captura por lotes
    for idx in range(1, n + 1):
        print(f"\n---> CAPTURA DE DATOS - ASEGURADO #{idx} <---")
        edad = solicitar_edad()
        sexo = solicitar_sexo()
        fumador = solicitar_fumador()
        extra_prima = solicitar_extra_prima()
        sa = solicitar_suma_asegurada()

        # Se instancian los objetos usando las clases correspondientes
        if sexo == "F":
            asegurado = AseguradoFemenino(idx, edad, sa, fumador, extra_prima)
        else:
            asegurado = AseguradoMasculino(idx, edad, sa, fumador, extra_prima)

        lista_asegurados.append(asegurado)

    # Cálculo de métricas requeridas
    primas = [a.calcular_prima() for a in lista_asegurados]
    prima_promedio = sum(primas) / len(primas)
    prima_maxima = max(primas)
    prima_minima = min(primas)

    # Búsqueda del asegurado con la extra-prima más alta
    asegurados_ep = [a for a in lista_asegurados if a.extra_prima]
    if asegurados_ep:
        max_ep_val = max(a.calcular_prima() for a in asegurados_ep)
        asegurados_max_ep = [
            f"Asegurado #{a.id_asegurado} (${a.calcular_prima():,.2f} MXN)"
            for a in asegurados_ep
            if a.calcular_prima() == max_ep_val
        ]
        info_extra_prima = ", ".join(asegurados_max_ep)
    else:
        info_extra_prima = "Ningún asegurado cuenta con extra-prima"

    # Despliegue de reporte estadístico
    print("\n" + "=" * 50)
    print("           REPORTE GENERAL DEL LOTE")
    print("=" * 50)
    print(f"Total de asegurados procesados : {n}")
    print(f"Prima Promedio                  : ${prima_promedio:,.2f} MXN")
    print(f"Prima Máxima                    : ${prima_maxima:,.2f} MXN")
    print(f"Prima Mínima                    : ${prima_minima:,.2f} MXN")
    print(f"Asegurado(s) c/ extra-prima alta: {info_extra_prima}")
    print("=" * 50)

    # Integración con Servicios de Conversión y Persistencia (Módulos 4 y 5)
    conversor = Conversor_de_moneda(tasa_cambio=21.13)
    exportar_carnet(lista_asegurados, conversor)


# ==============================================================================
# 3. DISEÑO EXTENSIBLE Y JERARQUÍA DE CLASES
# [PRINCIPIOS SOLID:]
# - OCP (Open/Closed Principle): Permite agregar nuevas categorías de edad/factor
#   extendiendo la clase abstracta sin alterar el cálculo central de la prima.
# - LSP (Liskov Substitution Principle): Subclases como AseguradoFemenino pueden 
#   sustituir a la clase base Asegurado sin alterar el funcionamiento del sistema.
# - DIP (Dependency Inversion Principle): La clase Asegurado depende de la 
#   abstracción FactorEdadStrategy y no de una implementación concreta.
# ==============================================================================

class FactorEdadStrategy(ABC):
    """Interfaz abstracta (Estrategia) para calcular el factor K de edad."""

    @abstractmethod
    def obtener_factor_edad(self, edad: int) -> float:
        pass


class FactorFemenino(FactorEdadStrategy):
    """Estrategia concreta de factores actuariales para asegurados de sexo femenino."""

    def obtener_factor_edad(self, edad: int) -> float:
        if 18 <= edad <= 25:
            return 1.5
        elif 25 < edad <= 45:
            return 1.7
        elif 45 < edad <= 65:
            return 2.0
        else:
            return 2.2


class FactorMasculino(FactorEdadStrategy):
    """Estrategia concreta de factores actuariales para asegurados de sexo masculino."""

    def obtener_factor_edad(self, edad: int) -> float:
        if 18 <= edad <= 25:
            return 2.0
        elif 25 < edad <= 45:
            return 2.3
        elif 45 < edad <= 65:
            return 2.5
        else:
            return 3.0


class Asegurado:
    """Clase principal que representa a un asegurado y aplica las reglas de ajuste actuarial."""

    def __init__(
        self,
        id_asegurado: int,
        edad: int,
        sexo: str,
        suma_asegurada: float,
        fumador: bool,
        extra_prima: bool,
        estrategia_factor: FactorEdadStrategy,
    ):
        self.id_asegurado = id_asegurado
        self.edad = edad
        self.sexo = sexo
        self.suma_asegurada = suma_asegurada
        self.fumador = fumador
        self.extra_prima = extra_prima
        self.estrategia_factor = estrategia_factor

    def calcular_edad_ajustada(self) -> int:
        """Calcula la edad ajustada basándose en hábitos y recargos, acotada a [18, 99]."""
        edad_ajustada = self.edad
        if not self.fumador:
            edad_ajustada -= 5
        if self.sexo == "F":
            edad_ajustada -= 10
        if self.extra_prima:
            edad_ajustada += 10

        return max(18, min(99, edad_ajustada))

    def obtener_factor_edad(self) -> float:
        """Obtiene el factor K delegando el cálculo a la estrategia asignada."""
        edad_ajustada = self.calcular_edad_ajustada()
        return self.estrategia_factor.obtener_factor_edad(edad_ajustada)

    def calcular_prima(self) -> float:
        """Calcula la prima anual mediante la fórmula (SA * K) / 1000."""
        factor = self.obtener_factor_edad()
        return (self.suma_asegurada * factor) / 1000


class AseguradoFemenino(Asegurado):
    """Especialización para asegurados femeninos con su estrategia correspondiente."""

    def __init__(self, id_asegurado, edad, suma_asegurada, fumador, extra_prima):
        super().__init__(
            id_asegurado,
            edad,
            "F",
            suma_asegurada,
            fumador,
            extra_prima,
            FactorFemenino(),
        )


class AseguradoMasculino(Asegurado):
    """Especialización para asegurados masculinos con su estrategia correspondiente."""

    def __init__(self, id_asegurado, edad, suma_asegurada, fumador, extra_prima):
        super().__init__(
            id_asegurado,
            edad,
            "M",
            suma_asegurada,
            fumador,
            extra_prima,
            FactorMasculino(),
        )


# ==============================================================================
# 4. CONVERSIÓN DE MONEDA DESACOPLADA
# [PRINCIPIO SOLID: ISP - Interface Segregation Principle]
# Servicio aislado e independiente. Permite cambiar la tasa de cambio o conectar
# una API externa sin tocar la lógica del cálculo de las primas.
# ==============================================================================

class Conversor_de_moneda:
    """Servicio independiente para realizar la conversión de divisa (MXN a USD)."""

    def __init__(self, tasa_cambio: float = 21.13):
        if tasa_cambio <= 0:
            raise ValueError("La tasa de cambio debe ser un número mayor a cero.")
        self.tasa_cambio = tasa_cambio

    def mxn_a_usd(self, monto_mxn: float) -> float:
        """Convierte un monto en MXN a USD según la tasa configurada."""
        return monto_mxn / self.tasa_cambio


# ==============================================================================
# 5. PERSISTENCIA EN ARCHIVO DE TEXTO
# [PRINCIPIO SOLID: SRP - Single Responsibility Principle]
# Modulo exclusivo para el formateo y exportación física de datos en disco.
# ==============================================================================

def exportar_carnet(
    asegurados: list,
    conversor: Conversor_de_moneda,
    ruta_archivo: str = "carnet_asegurados.txt",
):
    """Exporta los detalles actuariales e individuales de cada asegurado a un archivo texto."""
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            for a in asegurados:
                prima_mxn = a.calcular_prima()

                try:
                    prima_usd = conversor.mxn_a_usd(prima_mxn)
                    prima_usd_str = f"${prima_usd:,.2f} USD"
                except Exception:
                    prima_usd_str = "Error al convertir a USD"

                es_fumador = "Sí" if a.fumador else "No"
                tiene_extra_prima = "Sí" if a.extra_prima else "No"

                print(f"--- Carnet Asegurado #{a.id_asegurado} ---", file=archivo)
                print(f"Sexo: {a.sexo}", file=archivo)
                print(f"Edad Real: {a.edad} años", file=archivo)
                print(f"Edad Ajustada: {a.calcular_edad_ajustada()} años", file=archivo)
                print(f"Fumador: {es_fumador}", file=archivo)
                print(f"Extra-prima: {tiene_extra_prima}", file=archivo)
                print(f"Suma Asegurada (SA): ${a.suma_asegurada:,.2f} MXN", file=archivo)
                print(f"Prima Anual (MXN): ${prima_mxn:,.2f} MXN", file=archivo)
                print(f"Prima Anual (USD): {prima_usd_str}", file=archivo)
                print("-" * 45 + "\n", file=archivo)

        print(f"\n[Éxito] El carnet por lotes se ha guardado en: '{ruta_archivo}'")

    except PermissionError:
        print(f"Error de permisos: No se puede escribir en la ruta '{ruta_archivo}'.")
    except FileNotFoundError:
        print(f"Error de ruta: La ubicación especificada no existe: '{ruta_archivo}'.")
    except OSError as e:
        print(f"Error de E/S del sistema al guardar el archivo: {e}")
    except Exception as e:
        print(f"Error inesperado al exportar los datos: {e}")


# Entry point ejecutable del programa
if __name__ == "__main__":
    procesar_lote_asegurados()