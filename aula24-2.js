function quickSort(arr){
    if(arr.length <= 1){
        return arr
    }else{
        const pivo = arr[Math.floor(arr.length /2)];
        const esquerda = arr.filter(x => x < pivo);
        const meio = arr.filter(x => x == pivo);
        const direita = arr.filter(x => x > pivo);

        return quickSort(esquerda).concat(meio, quickSort(direita));
    }
}

let arr = [10, 7, 8, 9, 1, 5,89,5,4,8,6,412,3,5,3]
let arr_ordenado = quickSort(arr)

console.log(arr_ordenado)
