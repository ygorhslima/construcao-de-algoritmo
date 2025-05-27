import os
import math

velocidade = 1
tam_array = 1000

os.system("cls")
print(f"tamanho array: {tam_array} elementos, velocidade: {velocidade} operação(ões) por segundo")

print(f"O(log n): {round(math.log2(tam_array)/velocidade,1)} segundos")
print(f"O(n): {tam_array} segundos")
print(f"O(n log n): ")
print(f"O(n²): ")
print(f"O(n!): ")

