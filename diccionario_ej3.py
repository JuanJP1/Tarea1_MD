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
