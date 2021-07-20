const peso = document.querySelector('#peso')
const botao = document.querySelector('.btn')
const resul = document.querySelector('.resul')
let resultado = 0
const agua = 30

function litrosPorPeso(event){
    event.preventDefault()
    resultado = Number(peso.value) * agua
    resul.innerText = `${resultado} Lts`;
    peso.value = ' ' 
}
botao.addEventListener('click', litrosPorPeso)

function sumir(){
    resul.innerText = ' '
}
peso.addEventListener('focusin', sumir)


