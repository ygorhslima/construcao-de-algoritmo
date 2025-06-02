#include <iostream>
using namespace std;

class Ola{
    public:
        int n1,n2,n3;
        Ola(){
            cout << "objeto criado" << endl;
        }
        ~Ola(){
            cout << "Objeto deletado" << endl;
        }
};

int main(){
    Ola *ola1 = new Ola();
    Ola ola2;
    cout << sizeof(ola1) << endl;
    cout << sizeof(ola2) << endl;
    return 0;    
}