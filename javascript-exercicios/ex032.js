const prompt = require("prompt-sync")();

const ano = parseInt(prompt("Digite um ano qualquer: "));

// Verifica se é bissexto
if ((ano % 4 === 0 && ano % 100 !== 0) || (ano % 400 === 0)) {
    console.log(`${ano} é bissexto`);
} else {
    console.log(`${ano} não é bissexto`);
}
