def quickSort(arr):
    # Caso Base
    if len(arr) <= 1:
        return arr
    else:
        # Caso Recursivo
        pivo = arr[len(arr) // 2]

        esquerda = [x for x in arr if x < pivo]
        meio = [x for x in arr if x == pivo]
        direita = [x for x in arr if x > pivo]
        
        return quickSort(esquerda) + meio + quickSort(direita)

arr = [10, 7, 8, 9, 1, 5,89,5,4,8,6,412,3,5,3]
arr_ordenado = quickSort(arr)
print(arr_ordenado)
