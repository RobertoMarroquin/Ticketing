let boton=document.getElementById("postGuardar");
let nombre=document.getElementById("id_nombre");
let eslogan=document.getElementById("id_eslogan");
let forma=document.getElementById("forma");
let token = $('input[name=csrfmiddlewaretoken]').val();

//////////////////////////////////////////////////////////////////////////
//ASIGNACIÓN DE EVENTOS
//////////////////////////////////////////////////////////////////////////
boton.addEventListener("click",guardar);

//////////////////////////////////////////////////////////////////////////
//VALIDACIONES DE LOS CAMPOS
//////////////////////////////////////////////////////////////////////////
function guardar(){
  if (nombre.value==""){tostada("¡El nombre de la boletería no puede estar vacío!","#f8d7da","#721c24");}
  else {forma.submit();}
}
