import os
import math

velocidade = 1
tam_array = 10

os.system("cls")
print(f"tamanho array: {tam_array} elementos, velocidade: {velocidade} operação(ões) por segundo")

print(f"O(log n): {round(math.log2(tam_array)/velocidade,1)} segundos") # Busca Binária
print(f"O(n): {tam_array} segundos") # Percorrer um vetor
print(f"O(n log n): {round((tam_array * math.log2(tam_array)) / velocidade, 1)} segundos") # QuickSort
print(f"O(n²): {round(math.pow(tam_array/velocidade,2),1)} segundos") # Ordenação por seleção
print(f"O(n!): {round(math.factorial(tam_array)/velocidade,1)} segundos") # Caixeiro viajante

