const prompt = require('prompt-sync')();

const nome = prompt("Não \n escreva \n pare ");
const texto = "ola, ";
const mensagem = console.log(texto+nome);
const erro = "erro\n".repeat(100);
console.log(erro)