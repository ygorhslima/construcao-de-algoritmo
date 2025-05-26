#include <iostream>
using namespace std;

#define tam 5

int somar(int v[], int n){
    //Caso base
    if(n <= 0){
        return 0;
    }else{
        //Caso recursivo
        return v[n-1]+somar(v, n-1);
    }
}

int main(){
    int valores[tam]={65,4,9,7,10};
    int resultado = somar(valores, tam);
    cout << resultado << endl;
    return 0;
}