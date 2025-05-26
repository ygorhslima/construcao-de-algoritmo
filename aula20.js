function contar(n){
    if(n <= 0){ //Caso base
        return 0;
    }else{ // Caso recursivo
        console.log(`=${n}=`);
        contar(n-1);
    }
}

function somatorio(n){
    if(n == 0){
        return 0;
    }else{
        return n+somatorio(n-1);
    }
}
let res = somatorio(5)
console.log(res)
