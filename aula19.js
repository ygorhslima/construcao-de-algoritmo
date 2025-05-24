function calc_fat(numero){
    if (numero == 0 || numero == 1){
        return 1;
    }else{
        return numero * calc_fat(numero - 1);
    }
}
let resultado = calc_fat(5)
console.log(`o resultado é ${resultado}`)