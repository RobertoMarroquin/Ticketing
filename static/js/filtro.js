let filtros=document.getElementsByClassName("form-control");
let peliculas=document.getElementsByClassName("card-body");
let pelisTam=peliculas.length;

let aux=[];

for (let i=0;i<pelisTam;i++){
  let flag=0;
  let horario=peliculas[i].childNodes[3].textContent.slice(9,-6);
  aux.forEach(function(horarioElem){if(horarioElem===horario){flag=1;}});
  if (flag===1){continue;}
  aux.push(horario);
}

aux.sort((a=fechaNumero(a),b=fechaNumero(b))=>a-b);

for (let i=0;i<aux.length;i++){
  let opcion=document.createElement("option");
  opcion.setAttribute("value",i);
  opcion.textContent=aux[i];
  filtros[0].appendChild(opcion);
}

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
