#include <stdio.h>
#include <stdlib.h>


// Estrutura da fila
typedef struct
{
    int *elementos;
    int inicio, fim;
    int capacidade;
}Fila;

//inicializar a fila
void inicializarFila(Fila *f, int capacidadeInicial){
    f->inicio=0;
    f->fim=-1;
    f->capacidade = capacidadeInicial; // seria no caso o tamanho inicial da fila por exemplo 10
    f->elementos = (int *)malloc(capacidadeInicial * sizeof(int));
    if(f->elementos == NULL){
        printf("erro ao alocar memória. \n");
        exit(1);
    }
}

//verificar fila vazia
int estaVazia(Fila *f){
    return f->fim < f->inicio;
}

void redimensionarFila(Fila *f){
    f->capacidade *= 2;
    f->elementos = (int *)realloc(f->elementos, f->capacidade * sizeof(int));
    
    if(f->elementos == NULL){
        printf("erro ao redimensionar a fila. \n");
        exit(1);
    } 
    printf("fila relacionada para %d elementos \n", f->capacidade);
}

// inserção de elemento na fila
void enQueue(Fila *f,int valor){
    if(f->fim == f->capacidade - 1){
        redimensionarFila(f);
    }
    f->elementos[++f->fim] = valor;
    printf("elemento %d inserido na fila.\n",valor);
}

// remoção de elemento na fila
int deQueue(Fila *f){
    if(estaVazia(f)){
        printf("a fila está vazia, não é possível remover\n");
        return -1;
    }else{
        return f->elementos[f->inicio++];
    }
}

void liberarFila(Fila *f){
    free(f->elementos);
    f->elementos = NULL;
    f->inicio = 0;
    f->fim = -1;
    f->capacidade = 0;
}

int main(){ 
    Fila f;
    inicializarFila(&f, 2);
    enQueue(&f,1);
    enQueue(&f,2);
    enQueue(&f,3);
    enQueue(&f,4);
    enQueue(&f,5);
    enQueue(&f,6);
    enQueue(&f,7);
    enQueue(&f,8);
    enQueue(&f,9);
    enQueue(&f,10);

    printf("Elemento removido %d\n",deQueue(&f));
    printf("Elemento removido %d\n",deQueue(&f));
    printf("Elemento removido %d\n",deQueue(&f));
    printf("Elemento removido %d\n",deQueue(&f));
    printf("Elemento removido %d\n",deQueue(&f));
    printf("Elemento removido %d\n",deQueue(&f));
    printf("Elemento removido %d\n",deQueue(&f));
    printf("Elemento removido %d\n",deQueue(&f));
    printf("Elemento removido %d\n",deQueue(&f));
    printf("Elemento removido %d\n",deQueue(&f));
    return 0;
}