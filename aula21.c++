#include <iostream>

using namespace std;

int fibonacci(int pos){
    int n1 = 0;
    int n2 = 1;
    int res = 1;
    while(pos > 1){
       res = n1 + n2;
       n1=n2;
       n2=res;
       pos-=1; 
    }
    return res;
}

int main(){
    cout << fibonacci(10) << endl;
    return 0;
}