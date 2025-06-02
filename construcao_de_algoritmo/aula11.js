const array = [2, 3, 10, 15, 17, 21, 28, 40, 55, 60, 61, 62, 63];

function pesquisaBinaria(valor, procurado) {
    let posLimiteInferior = 0;
    let posLimiteSuperior = valor.length - 1;

    while (posLimiteInferior <= posLimiteSuperior) {
        let posMeio = Math.floor((posLimiteInferior + posLimiteSuperior) / 2);
        let palpite = valor[posMeio];

        if (palpite === procurado) {
            return posMeio;
        }

        if (palpite > procurado) {
            posLimiteSuperior = posMeio - 1;
        } else {
            posLimiteInferior = posMeio + 1;
        }
    }

    return -1;
}

let pesquisa = pesquisaBinaria(array, 60);
console.log(pesquisa);
