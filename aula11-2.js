/** 
 *  em uma lista de 128 valores inteiros ordenados. qual será o  número máximo de etapas 
 * que se levaria para encontrar o valor desejado, usando pesquisa simples e binária
*/

let lista = Array.from({length: 128}, (v,i)=>i)

function pesquisaSimples(valor, procurado){
    for(let i = 0; i < lista.length; i++){
        if(valor[i] === procurado){
            return i;
        }
    }
    return -1;
}

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

let ps = pesquisaSimples(lista, 100)
console.log(ps)