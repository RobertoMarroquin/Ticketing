let filtros=document.getElementsByClassName("form-control");
let divCards=document.getElementsByClassName("card col-3");
let peliculas=document.getElementsByClassName("card-body");
let pelisTam=peliculas.length;
let filtrosTam=filtros.length;
let aux=[];

let llenarOpciones=[
  function(){
    filtros[0].querySelectorAll("option").forEach(function(x){if (x.value!=-1){x.parentNode.removeChild(x);}});
    for (let i=0;i<pelisTam;i++){
      let flag=0;
      let horario=peliculas[i].childNodes[3].textContent.slice(9,-6);
      aux.forEach(function(horarioElem){if(horarioElem===horario){flag=1;}});
      if (flag===1){continue;}
      aux.push(horario);
    }aux.sort((a=fechaNumero(a),b=fechaNumero(b))=>a-b);
    for (let i=0;i<aux.length;i++){
      let opcion=document.createElement("option");
      opcion.setAttribute("value",i+1);
      opcion.textContent=aux[i];
      filtros[0].appendChild(opcion);
    }aux=[];
  },
  function(){
    filtros[1].querySelectorAll("option").forEach(function(x){if (x.value!=-1){x.parentNode.removeChild(x);}});
    for (let i=0;i<pelisTam;i++){
      let flag=0;
      let nombrePeli=peliculas[i].childNodes[1].textContent;
      if (divCards[i].style.display==="none"){continue;}
      aux.forEach(function(nombreElem){if(nombreElem===nombrePeli){flag=1;}});
      if (flag===1){continue;}
      aux.push(nombrePeli);
    }aux.sort();
    for (let i=0;i<aux.length;i++){
      let opcion=document.createElement("option");
      opcion.setAttribute("value",i+1);
      opcion.textContent=aux[i];
      filtros[1].appendChild(opcion);
    }aux=[];
  },
  function(){
    filtros[2].querySelectorAll("option").forEach(function(x){if (x.value!=-1){x.parentNode.removeChild(x);}});
    for (let i=0;i<pelisTam;i++){
      let flag=0;
      let formato=peliculas[i].childNodes[5].textContent.slice(9,peliculas[i].childNodes[5].textContent.indexOf("Lenguaje")-1);
      if (divCards[i].style.display==="none"){continue;}
      aux.forEach(function(formatoElem){if(formatoElem===formato){flag=1;}});
      if (flag===1){continue;}
      aux.push(formato);
    }aux.sort();
    for (let i=0;i<aux.length;i++){
      let opcion=document.createElement("option");
      opcion.setAttribute("value",i+1);
      opcion.textContent=aux[i];
      filtros[2].appendChild(opcion);
    }aux=[];
  },
  function(){
    filtros[3].querySelectorAll("option").forEach(function(x){if (x.value!=-1){x.parentNode.removeChild(x);}});
    for (let i=0;i<pelisTam;i++){
      let flag=0;
      let idioma=peliculas[i].childNodes[5].textContent.slice(peliculas[i].childNodes[5].textContent.lastIndexOf(":")+1);
      if (divCards[i].style.display==="none"){continue;}
      aux.forEach(function(idiomaElem){if(idiomaElem===idioma){flag=1;}});
      if (flag===1){continue;}
      aux.push(idioma);
    }aux.sort();
    for (let i=0;i<aux.length;i++){
      let opcion=document.createElement("option");
      opcion.setAttribute("value",i+1);
      opcion.textContent=aux[i];
      filtros[3].appendChild(opcion);
    }aux=[];
  },
  function(){
    filtros[4].querySelectorAll("option").forEach(function(x){if (x.value!=-1){x.parentNode.removeChild(x);}});
    for (let i=0;i<pelisTam;i++){
      let flag=0;
      let horas=peliculas[i].childNodes[3].textContent.slice(-6);
      if (divCards[i].style.display==="none"){continue;}
      aux.forEach(function(horasElem){if(horasElem===horas){flag=1;}});
      if (flag===1){continue;}
      aux.push(horas);
    }aux.sort();
    for (let i=0;i<aux.length;i++){
      let opcion=document.createElement("option");
      opcion.setAttribute("value",i+1);
      opcion.textContent=aux[i];
      filtros[4].appendChild(opcion);
    }aux=[];
  }
];

//para la primera lista
reestablecer(0);
llenarOpciones[0]();

////eventos
filtros[0].setAttribute("onchange","ocultarPelis(0);");
filtros[1].setAttribute("onchange","ocultarPelis(1);");
filtros[2].setAttribute("onchange","ocultarPelis(2);");
filtros[3].setAttribute("onchange","ocultarPelis(3);");
filtros[4].setAttribute("onchange","ocultarPelis(4);");

////////////////////////////////////////////////////////////////////////////////////////
function ocultarPelis(filtroF) {
  for (let p=0;p<pelisTam;p++){divCards[p].style.display="";}
  for (let i=0;i<=filtroF;i++){
    let id=filtros[i].value;
    if (id!=-1){filtrosFunc[i](filtroF,id);}
    else{reestablecer(filtroF);}
  }
}

function reestablecer(filtroFin){
  for (let g=0;g<pelisTam;g++){
    if (filtroFin===0){divCards[g].style.display="";}
    else{for (let k=0;k<filtroFin;k++){filtrosFunc[k];}}
  }
  resetFiltros(filtroFin);
}

function resetFiltros(t){
  for (let f=filtrosTam-1;f>t;f--){
    filtros[f].setAttribute("disabled","");
    filtros[f].querySelectorAll("option").forEach(function(x){if (x.value!=-1){x.parentNode.removeChild(x);}});
  }
}

let filtrosFunc=[
  function(filtroFinal,opcionID){
    for (let g=0;g<pelisTam;g++){
      let horario=peliculas[g].childNodes[3].textContent.slice(9,-6);
      if (filtros[0][opcionID].textContent!==horario){divCards[g].style.display="none";}
      else if (divCards[g].style.display!="none"){divCards[g].style.display="";}
      if(filtroFinal!=(filtrosTam-1))
      {resetFiltros(filtroFinal+1);filtros[filtroFinal+1].removeAttribute("disabled");}
    }if(filtroFinal!=(filtrosTam-1)){llenarOpciones[filtroFinal+1]()};
  },
  function(filtroFinal,opcionID){
    for (let g=0;g<pelisTam;g++){
      let nombrePeli=peliculas[g].childNodes[1].textContent;
      if (filtros[1][opcionID].textContent!==nombrePeli){divCards[g].style.display="none";}
      else if (divCards[g].style.display!="none"){divCards[g].style.display="";}
      if(filtroFinal!=(filtrosTam-1))
      {resetFiltros(filtroFinal+1);filtros[filtroFinal+1].removeAttribute("disabled");}
    }if(filtroFinal!=(filtrosTam-1)){llenarOpciones[filtroFinal+1]()};
  },
  function(filtroFinal,opcionID){
    for (let g=0;g<pelisTam;g++){
      let formato=peliculas[g].childNodes[5].textContent.slice(9,peliculas[g].childNodes[5].textContent.indexOf("Lenguaje")-1);
      if (filtros[2][opcionID].textContent!==formato){divCards[g].style.display="none";}
      else if (divCards[g].style.display!="none"){divCards[g].style.display="";}
      if(filtroFinal!=(filtrosTam-1))
      {resetFiltros(filtroFinal+1);filtros[filtroFinal+1].removeAttribute("disabled");}
    }if(filtroFinal!=(filtrosTam-1)){llenarOpciones[filtroFinal+1]()};
  },
  function(filtroFinal,opcionID){
    for (let g=0;g<pelisTam;g++){
      let idioma=peliculas[g].childNodes[5].textContent.slice(peliculas[g].childNodes[5].textContent.lastIndexOf(":")+1);
      if (filtros[3][opcionID].textContent!==idioma){divCards[g].style.display="none";}
      else if (divCards[g].style.display!="none"){divCards[g].style.display="";}
      if(filtroFinal!=(filtrosTam-1))
      {resetFiltros(filtroFinal+1);filtros[filtroFinal+1].removeAttribute("disabled");}
    }if(filtroFinal!=(filtrosTam-1)){llenarOpciones[filtroFinal+1]()};
  },
  function(filtroFinal,opcionID){
    for (let g=0;g<pelisTam;g++){
      let horas=peliculas[g].childNodes[3].textContent.slice(-6);
      if (filtros[4][opcionID].textContent!==horas){divCards[g].style.display="none";}
      else if (divCards[g].style.display!="none"){divCards[g].style.display="";}
      if(filtroFinal!=(filtrosTam-1))
      {resetFiltros(filtroFinal+1);filtros[filtroFinal+1].removeAttribute("disabled");}
    }if(filtroFinal!=(filtrosTam-1)){llenarOpciones[filtroFinal+1]()};
  }
];

function fechaNumero(leFecha) {
  let dia=leFecha.slice(0,leFecha.indexOf("d")-1);
  let mes=leFecha.slice(leFecha.indexOf("e")+2,leFecha.lastIndexOf("d")-1).toLowerCase();
  let year=leFecha.slice(leFecha.lastIndexOf("e")+2);
  switch (mes){
    case "enero":mes=1;break;
    case "febrero":mes=2;break;
    case "marzo":mes=3;break;
    case "abril":mes=4;break;
    case "mayo":mes=5;break;
    case "junio":mes=6;break;
    case "julio":mes=7;break;
    case "agosto":mes=8;break;
    case "septiembre":mes=9;break;
    case "octubre":mes=10;break;
    case "noviembre":mes=11;break;
    case "diciembre":mes=12;break;
  }
  return new Number(dia+mes+year);
}
