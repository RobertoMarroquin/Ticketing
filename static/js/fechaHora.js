//para la fecha
document.getElementById("fechaForm").value=document.getElementById("initial-id_fecha").value;

document.getElementById("fechaActBtn").addEventListener("click",function(){
  let anioF=new Date();
  let diaF=Number(anioF.getDate());
  let mesF=Number(anioF.getMonth())+1;
  anioF=Number(anioF.getFullYear());

  if (diaF<10){diaF="0"+diaF;}
  if (mesF<10){mesF="0"+mesF;}

  document.getElementById("fechaForm").value=anioF+"-"+mesF+"-"+diaF;
});

document.getElementById("fechaAntBtn").addEventListener("click",function(){
  document.getElementById("fechaForm").value=document.getElementById("initial-id_fecha").value;
});

/////////////////////////////////////////////////////////////////////////////////

//para la hora
let horaForm=document.getElementById("horaForm");
let horaCampo=document.getElementById("horas");
let minutosCampo=document.getElementById("minutos");
let tipoHoraSwitch=document.getElementById("tipoHoraSwitch");
let ampm=document.getElementById("ampm");

let horaAnt=horaForm.value;
let minutosAnt=horaAnt.slice(horaAnt.indexOf(":")+1);
horaAnt=horaAnt.slice(0,horaAnt.indexOf(":"));

minutosCampo.setAttribute("min",0);
minutosCampo.setAttribute("max",59);

reset();
maxMin(0,23);//min hora, max hora

/////////// Eventos
tipoHoraSwitch.addEventListener("click",ampmcambio);
document.getElementById("horaAntBtn").addEventListener("click",function(){
  maxMin(0,23);
  reset();
  ampm.value="0";
  tipoHoraSwitch.checked=false;
});

//asignando valores iniciales
function reset(){minutosCampo.value=minutosAnt; horaCampo.value=horaAnt;}
//seteando Max/min
function maxMin(minH,maxH){
  horaCampo.setAttribute("min",minH);
  horaCampo.setAttribute("max",maxH);
}
function ampmcambio(){
  if(tipoHoraSwitch.checked){ //de 24 a 12
    ampm.removeAttribute("disabled");
    if (Number(horaCampo.value)>=12){ampm.value=2;}
    else {ampm.value=1;}
    horaCampo.value=convierteHoras(2,horaCampo.value,0);
    maxMin(1,12);
  }
  else{ //de 12 a 24
    horaCampo.value=convierteHoras(1,horaCampo.value,ampm[ampm.value].textContent);
    ampm.value="0";
    ampm.setAttribute("disabled","true");
    maxMin(0,23);
  }
}

function convierteHoras(bandera,horaP,amPmDt){
  bandera=Number(bandera);
  horaP=Number(horaP);
  // bandera=1 -> de 12 a 24 horas
  // bandera=2 -> de 24 a 12 horas
  if (bandera==1){
    if (horaP==12){
      if (amPmDt=="AM"){return 0;}
      else {return horaP;}
    }
    else{
      if (amPmDt=="PM"){return horaP+12;}
      else{return horaP;}
    }
  }
  else if (bandera==2){
    if (horaP==0){return 12;}
    else{
      if (horaP>12){return horaP-12;}
      else{return horaP;}
    }
  }
}
