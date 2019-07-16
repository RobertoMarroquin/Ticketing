let boton=document.getElementById("postGuardar");
let nombre=document.getElementById("id_nombre");
let pais=document.getElementById("id_pais");
let anyo=document.getElementById("id_anyo");
let duracion=document.getElementById("id_duracion");
let sinopsis=document.getElementById("id_sinopsis");
let clasificacion=document.getElementById("id_clasificacion");
let genero=document.getElementById("id_genero");
let boleteria=document.getElementById("id_boleteria");
let exhibicion=document.getElementById("id_exhibicion");
let token = $('input[name=csrfmiddlewaretoken]').val();

duracion.setAttribute("min","0");
anyo.setAttribute("min","1878");

//////////////////////////////////////////////////////////////////////////
//ASIGNACIÓN DE EVENTOS
//////////////////////////////////////////////////////////////////////////
boton.addEventListener("click",guardar);
anyo.setAttribute("onchange","validar(this)");
duracion.setAttribute("onchange","validar(this)");
//////////////////////////////////////////////////////////////////////////
//VALIDACIONES DE LOS CAMPOS
//////////////////////////////////////////////////////////////////////////
function validar(esto){
  let valorEsto=esto.value;
  let minEsto=Number(esto.getAttribute("min"));
  if(valorEsto<minEsto){
    esto.value=minEsto;
    if (minEsto==1878){
      tostada("¡Antes del año "+minEsto+" no existian las películas!","#f8d7da","#721c24");
    }else{
      tostada("¡No se aceptan minutos negativos!","#f8d7da","#721c24");
    }
  }else if (valorEsto%1!==0){
    esto.value=Math.floor(valorEsto);
    tostada("¡No se permiten fracciones!","#f8d7da","#721c24");
    }
}
//////////////////////////////////////////////////////////////////////////
//GUARDAR
//////////////////////////////////////////////////////////////////////////
function guardar(){
  if (
    nombre.value==""||
    pais.value==""||
    anyo.value==""||
    duracion.value==""||
    sinopsis.value==""||
    clasificacion.value==""||
    genero.value==""||
    boleteria.value==""||
    exhibicion.value==""
  ){tostada("¡Uno o más campos están vacíos!","#f8d7da","#721c24");}
  else {forma.submit();}
}
