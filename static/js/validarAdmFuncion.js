let forma=document.getElementById("forma");

let pelicula=document.getElementById("id_pelicula");
let sala=document.getElementById("id_sala");
let formato=document.getElementById("id_formato");
let lenguaje=document.getElementById("id_lenguaje");
let fecha=document.getElementById("fechaForm");
let hora=document.getElementById("horaForm");
let estado=document.getElementById("id_estado");

let horas=document.getElementById("horas");
let minutos=document.getElementById("minutos");

let boton=document.getElementById("postGuardar");
let token = $('input[name=csrfmiddlewaretoken]').val();
let flag=1; //1 guardar

//////////////////////////////////////////////////////////////////////////
//ASIGNACIÓN DE EVENTOS
//////////////////////////////////////////////////////////////////////////
boton.addEventListener("click",guardar);
horas.setAttribute("onchange","validar(this)");
minutos.setAttribute("onchange","validar(this)");
fecha.setAttribute("onchange","validarFecha(this)");

//////////////////////////////////////////////////////////////////////////
//VALIDACIONES DE LOS CAMPOS
//////////////////////////////////////////////////////////////////////////
function validar(esto){
  let valorEsto=esto.value;
  let minEsto=Number(esto.getAttribute("min"));
  let maxEsto=Number(esto.getAttribute("max"));
  if(valorEsto<minEsto){
    esto.value=minEsto;
    tostada("¡El valor es demasiado bajo!","#f8d7da","#721c24");
  }else if (valorEsto>maxEsto){
    esto.value=maxEsto;
    tostada("¡El valor es demasiado alto!","#f8d7da","#721c24");
  }else if (valorEsto%1!==0){
    esto.value=Math.floor(valorEsto);
    tostada("¡No se permiten fracciones!","#f8d7da","#721c24");
    }
}

function validarFecha(esto){
  let anioF=new Date();
  let diaF=Number(anioF.getDate());
  let mesF=Number(anioF.getMonth())+1;
  anioF=Number(anioF.getFullYear());

  if (diaF<10){diaF="0"+diaF;}
  if (mesF<10){mesF="0"+mesF;}
  if (esto.value==""){
    esto.value=anioF+"-"+mesF+"-"+diaF;
    tostada("¡No se permiten fechas vacías!","#f8d7da","#721c24");
  }
  let dia=esto.value;

  let indice=dia.indexOf("-");
  let anio=Number(dia.slice(0,indice)); indice+=1;
  let mes=Number(dia.slice(indice,dia.lastIndexOf("-"))); indice=dia.lastIndexOf("-")+1;
  dia=Number(dia.slice(indice));

  if (dia<10){dia="0"+dia;}
  if (mes<10){mes="0"+mes;}

  indice=new Date(anio,mes-1,dia+1, 0, 0, 0, 0);
  if (indice-Date.now()<0){
    esto.value=anioF+"-"+mesF+"-"+diaF;
    tostada("¡No se permiten fechas pasadas!","#f8d7da","#721c24");
  }
}

//////////////////////////////////////////////////////////////////////////
//GUARDAR
//////////////////////////////////////////////////////////////////////////
function guardar(){
  if (
    pelicula.value==""||
    sala.value==""||
    formato.value==""||
    lenguaje.value==""||
    fecha.value==""||
    horas.value==""||
    minutos.value==""
  ){flag=0; tostada("¡Uno o más campos están vacíos!","#f8d7da","#721c24");}

  if (flag==1){
    let horaD=horas.value;
    if(tipoHoraSwitch.checked){
      horaD=convierteHoras(1,horaCampo.value,ampm[ampm.value].textContent);
    }
    hora.value=horaD+":"+minutos.value;
    forma.submit();
  }
}
