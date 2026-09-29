import unicodedata
import time
from abc import ABC, abstractmethod

# ==========================================
# 1. NORMALIZACIÓN DE TEXTO (Single Responsibility)
# ==========================================
class TextNormalizer:
    @staticmethod
    def normalize(text: str) -> list[str]:
        if not text or not text.strip():
            raise ValueError("El texto de entrada está vacío.")
        
        # Eliminar acentos mediante NFD
        text_decomp = unicodedata.normalize('NFD', text.lower())
        text_clean = ''.join(c for c in text_decomp if unicodedata.category(c) != 'Mn')
        
        # Extraer únicamente secuencias alfabéticas
        words = []
        current_word = []
        for char in text_clean:
            if 'a' <= char <= 'z':
                current_word.append(char)
            else:
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
        if current_word:
            words.append(''.join(current_word))
            
        return words

# ==========================================
# 2. TABLA HASH PROPIA (Single Responsibility)
# ==========================================
class HashTable:
    """
    Tabla Hash con encadenamiento por buckets (lista de listas).
    Maneja el conteo de frecuencias y la eliminación de duplicados.
    Resuelve colisiones mediante listas asociativas [clave, valor] dentro de cada bucket.
    """
    def __init__(self, capacity: int = 1007):
        self.capacity = capacity
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key: str) -> int:
        hash_val = 0
        for char in key:
            hash_val = (hash_val * 31 + ord(char)) % self.capacity
        return hash_val

    def add_or_increment(self, key: str):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for pair in bucket:
            if pair[0] == key:
                pair[1] += 1
                return
        bucket.append([key, 1])

    def get_unique_words_and_counts(self) -> list[tuple[str, int]]:
        result = []
        for bucket in self.buckets:
            for key, count in bucket:
                result.append((key, count))
        return result

# ==========================================
# 3. ESTRATEGIAS DE ORDENAMIENTO (Strategy, Open/Closed, Liskov Substitution)
# ==========================================
class SorterStrategy(ABC):
    @abstractmethod
    def sort(self, items: list[tuple[str, int]]) -> list[tuple[str, int]]:
        pass

class MergeSortStrategy(SorterStrategy):
    def sort(self, items: list[tuple[str, int]]) -> list[tuple[str, int]]:
        if len(items) <= 1:
            return items
        
        mid = len(items) // 2
        left = self.sort(items[:mid])
        right = self.sort(items[mid:])
        
        return self._merge(left, right)

    def _merge(self, left: list[tuple[str, int]], right: list[tuple[str, int]]) -> list[tuple[str, int]]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

class QuickSortStrategy(SorterStrategy):
    def sort(self, items: list[tuple[str, int]]) -> list[tuple[str, int]]:
        if len(items) <= 1:
            return items
        
        pivot = items[len(items) // 2][0]
        left = [x for x in items if x[0] < pivot]
        middle = [x for x in items if x[0] == pivot]
        right = [x for x in items if x[0] > pivot]
        
        return self.sort(left) + middle + self.sort(right)
# ==========================================
# 4. Conteo de frecuencias (Reporte)
# ==========================================

def generar_reporte_frecuencias(texto: str, estrategia: SorterStrategy):

    palabras_limpias = TextNormalizer.normalize(texto)
    tabla_hash = HashTable()
    for palabra in palabras_limpias:
        tabla_hash.add_or_increment(palabra)
        
    lista_desordenada = tabla_hash.get_unique_words_and_counts()
    lista_ordenada = estrategia.sort(lista_desordenada)
    print(f"--- Reporte de Frecuencias ({estrategia.__class__.__name__}) ---")
    print(f"Total de palabras distintas: {len(lista_ordenada)}")
    for palabra, frecuencia in lista_ordenada:
        print(f"{palabra}: {frecuencia}")
# ==========================================
# 5. Comparacion empirica de estrategias de ordenamiento
# ==========================================

texto_100_palabras = """
La probabilidad es una herramienta matemática fundamental para modelar la incertidumbre y analizar fenómenos aleatorios. En el estudio de variables aleatorias continuas y discretas, buscamos comprender la distribución subyacente de los datos. Por ejemplo, procesos estocásticos como el movimiento browniano o los procesos de Poisson nos permiten describir eventos dinámicos en el tiempo. Además, mediante la inferencia estadística, podemos realizar contrastes de hipótesis para validar nuestros modelos teóricos. Pruebas no paramétricas, como la de Kolmogorov-Smirnov o la prueba de rangos de Wilcoxon, son esenciales cuando no asumimos normalidad. Así, las distribuciones predictivas bayesianas, combinando modelos como el Gamma-Poisson, ofrecen estimaciones robustas frente a la variabilidad inherente.
"""
texto_1000_palabras = texto_100_palabras * 10
texto_10000_palabras = texto_100_palabras * 100

def ejecucion_comparacion():
    textos = {
        "~100 palabras": texto_100_palabras,
        "~1,000 palabras": texto_1000_palabras,
        "~10,000 palabras": texto_10000_palabras
    }
    
    estrategias = {
        "Merge Sort": MergeSortStrategy(),
        "Quick Sort": QuickSortStrategy()
    }
    print(f"{'Tamaño del texto':<20} | {'Merge Sort (segundos)':<25} | {'Quick Sort (segundos)':<25}")
    print("")
    for etiqueta, texto in textos.items():
        palabras = TextNormalizer.normalize(texto)
        tabla = HashTable()
        for l in palabras:
            tabla.add_or_increment(l)
        lista_base = tabla.get_unique_words_and_counts()
        tiempos = {}
        for nombre_algoritmo, estrategia in estrategias.items():
            # Pasamos una copia para que la lista original no se ordene en la primera pasada
            datos_a_ordenar = lista_base.copy() 
            inicio = time.perf_counter()
            lista_ordenada = estrategia.sort(datos_a_ordenar)
            fin = time.perf_counter()
            tiempos[nombre_algoritmo] = fin - inicio
        print(f"{etiqueta:<20} | {tiempos['Merge Sort']:<25f} | {tiempos['Quick Sort']:<25f}")
ejecucion_comparacion()
