"use strict";

var prompt = require('prompt-sync')();

var nome = prompt("Não \n escreva \n pare ");
var texto = "ola, ";
var mensagem = console.log(texto + nome);
var erro = "erro\n".repeat(100);
console.log(erro);