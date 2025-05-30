#include <stdio.h>
#include <stdlib.h>

#define MAX 5

// Estrutura da fila
typedef struct
{
    int elementos[MAX];
    int inicio, fim;
}Fila;

//inicializar a fila
void inicializarFila(Fila *f){
    f->inicio=0;
    f->fim=-1;
}

//Verificar fila cheia
int estaCheia(Fila *f){
    // se a posição final for igual ao valor máximo dentro da fila, retorne verdadeiro
    return f->fim == MAX-1;
}

//verificar fila vazia
int estaVazia(Fila *f){
    return f->fim < f->inicio;
}

// inserção de elemento na fila
void enQueue(Fila *f,int valor){
    if(estaCheia(f)){
        printf("A fila está cheia! não foi possível inserir o valor %d",valor);
    }else{
        f->elementos[++f->fim]=valor; // no elemento específico no fim será adicionado o valor 
        printf("elemento inserido\n");
    }
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

int main(){
    Fila f;
    inicializarFila(&f);
    enQueue(&f,1);
    enQueue(&f,2);
    enQueue(&f,3);
    enQueue(&f,4);
    enQueue(&f,5);

    printf("elemento removído %d\n",deQueue(&f));

    return 0;
}