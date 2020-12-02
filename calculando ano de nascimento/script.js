function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('#res')
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert('ERRO')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ' '
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 10) {
                //criança
                img.setAttribute('src', 'menino.png')
            }else if (idade < 21) {
                //jovem
                img.setAttribute('src', 'jovem-homem.png')
            }else if (idade < 50) {
                // adulto
                img.setAttribute('src', 'homem-adulto.png')
            }else{
                // idoso
                img.setAttribute('src', 'idoso-homem.png')
            }
        }
        
            //Mulher

            else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 10) {
                //criança
                img.setAttribute('src', 'menina.png')
            }else if (idade < 21) {
                //jovem
                img.setAttribute('src', 'jovem-mulher.png')
            }else if (idade < 50) {
                //adulto
                img.setAttribute('src', 'mulher-adulta.png')
            }else{
                // idoso
                img.setAttribute('src', 'idoso-mulher.png')
            }
        }  
        res.innerHTML = `Detectamos ${genero} com ${idade} anos.`
        res.appendChild(img)
    }
}