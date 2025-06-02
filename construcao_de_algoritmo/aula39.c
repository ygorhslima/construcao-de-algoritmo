#include <stdio.h>
#include <stdlib.h>
#define MAX 5

typedef struct 
{
    int topo;
    int elementos[MAX];
}Pilha;

void inicializarPilha(Pilha *p){
    p->topo=-1;
}

int estaVazia(Pilha *p){
    return p->topo == -1;
}

int estaCheia(Pilha *p){
    return p->topo == MAX-1;
}

void push(Pilha *p, int valor){
    if(estaCheia(p)){
        printf("a pilha está cheia, não é possível inserir\n");
    }else{
        p->elementos[++p->topo]=valor;
        printf("Valor %d inserido na pilha\n",valor);
    }
}

int pop(Pilha *p){
     if(estaVazia(p)){
        printf("a pilha está vazia, não é possível remover\n");
        return -1;
    }else{
        int valor=p->elementos[p->topo--];
        printf("valor retirado da pilha %d\n",valor);
        return valor;
    }
}

int peek(Pilha *p){
    if(estaVazia(p)){
        printf("não é possível vizualizar elementos, pois a pilha está vazia");
        return -1;
    }else{
        return p->elementos[p->topo];
    }
}

int main(){
    Pilha p;
    inicializarPilha(&p);
    push(&p,10);
    push(&p,20);
    push(&p,30);
    push(&p,40);
    push(&p,50);

    printf("elemento no topo da Pilha: %d",peek(&p));
    pop(&p);
    pop(&p);
    pop(&p);
    pop(&p);
    pop(&p);
    return 0;
}