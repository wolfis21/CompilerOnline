
/* mas informacion */

window.onscroll = function(){
    if(document.documentElement.scrollTop > 100){
        document.querySelector('.container-boton-subir')
        .classList.add('show')
    }else{
        document.querySelector('.container-boton-subir')
        .classList.remove('show')
    }
}

document.querySelector('.container-boton-subir')
.addEventListener('click',()=>{
    window.scrollTo({
        top:0,
        behavior:'smooth'
    });
});