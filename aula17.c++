#include <iostream>
using namespace std;

#define tam 10

/**
 * Função que implementa o algoritmo de ordenação por seleção (Selection Sort).
 * Ordena os elementos de um array de inteiros em ordem crescente.
 * 
 * @param arr - Ponteiro para o array que será ordenado.
 * @param n - Quantidade de elementos no array.
 */
void ordenacaoSelecao(int *arr, int n){
    // O loop externo percorre cada posição do array (exceto a última, que já estará ordenada ao final).
    for(int i = 0; i < n - 1; i++){ 
        int iMin = i; // Assume que o menor elemento está na posição atual (i)

        // O loop interno percorre os elementos à frente da posição i
        // para encontrar o índice do menor valor entre eles.
        for(int j = i + 1; j < n; j++){ 
            if(arr[j] < arr[iMin]){ 
                iMin = j; // Atualiza iMin se encontrar um valor menor
            }
        }

        // Se o menor valor encontrado não estiver na posição i, troca os valores
        if(iMin != i){
            int tmp = arr[i];       // Armazena temporariamente o valor de arr[i]
            arr[i] = arr[iMin];     // Move o menor valor encontrado para a posição i
            arr[iMin] = tmp;        // Coloca o valor original de arr[i] na posição de iMin
        }
    }
}


void imprimirArray(int *arr, int n){
    printf("[");
    for(int i = 0; i < n; i++){
        printf("%d",arr[i]);
        if(i < n - 1){
            printf(", ");
        }
    }
    printf("]\n");
}

int main(){
    int arr[tam] = {4,2,10,90,67,5,43,100,6,5};
    
    cout << "array original" << endl;
    imprimirArray(arr, tam);
    
    cout << "Array ordenado" << endl;
    ordenacaoSelecao(arr,tam);

    cout << "depois da ordenação" << endl;

    imprimirArray(arr, tam);

    return 0;
}