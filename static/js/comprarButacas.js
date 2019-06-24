const tablaButacas=document.getElementById("tablaButacas");
const confirmar=document.getElementById("confirmar");
const boletosRestantes=document.getElementById("boletosRestantes");
let salaButacas;
let boletosDisponibles=ninos+adultos+mayores;
let butacasImagenes=[];
let token = $('input[name=csrfmiddlewaretoken]').val();

confirmar.disabled=true;
confirmar.addEventListener("click",confirmarCompra);
boletosRestantes.textContent="Boletos Restantes: "+boletosDisponibles;

$.ajax({
  url: p,
  type: "POST",
  data : {
    csrfmiddlewaretoken: token,
    mensaje1:aidi,
  },
  success: function(smg){
    salaButacas=JSON.parse(smg);
    artista();
  },
  error: function (msg, textStatus, errorThrown) {alert("fail");console.log(msg);console.log(textStatus);console.log(errorThrown);}
});

$.ajax({
  url: ocu,
  type: "POST",
  data : {
    csrfmiddlewaretoken: token,
    mensaje1:aidi,
    mensaje2:funcionID,
  },
  success: function(smg){
    if (smg!="nain"){
      salaButacas=JSON.parse(smg);
      liquidPaper();
    }
  },
  error: function (msg, textStatus, errorThrown) {alert("fail");console.log(msg);console.log(textStatus);console.log(errorThrown);}
});

if(boletosDisponibles===1){
  boletosRestantes.hidden="true";
  document.getElementById("peticion").textContent="Por favor elija su butaca";
}

function numeroLetra(numero){return String.fromCharCode(numero+65);}
function letraNumero(letra){return letra.charCodeAt(0)-65;}

function artista(){
  for (let i=0;i<filas;i++){
    let filaTr=document.createElement("tr");
    let headerFila=document.createElement("td");
    let letraFila="";
    let flagFila=0;

    let hFContainer=document.createElement("div");
    hFContainer.setAttribute("class","containerF");
    headerFila.appendChild(hFContainer);
    filaTr.appendChild(headerFila);

    for (let j=0;j<columnas;j++){
      let divContenedor=document.createElement("div");
      divContenedor.setAttribute("class","containers");

      /////buscando si hay alguna butaca en la fila y si hay, se asigna la letra
      if (salaButacas[i*columnas+j].fields.fila!="-"&&flagFila==0){
        letraFila=salaButacas[i*columnas+j].fields.fila;
        flagFila=1;
      }
      let butacaIcon=document.createElement("img");
      let nAsiento=salaButacas[i*columnas+j].fields.numero_asiento;

      if (!salaButacas[i*columnas+j].fields.clase){
        butacaIcon.setAttribute("src","/static/Media/ButacasGrid/transparente.png");
        divContenedor.classList.add("caminoTD");
        divContenedor.setAttribute("numero",0);
        butacaIcon.setAttribute("id",0);
      }else if(salaButacas[i*columnas+j].fields.disponibilidad){
        butacaIcon.setAttribute("src","/static/Media/ButacasGrid/disponible.png");
        divContenedor.setAttribute("numero",nAsiento);
        divContenedor.classList.add("butacaTD");
        butacaIcon.setAttribute("class","asientoImg");
        butacaIcon.setAttribute("reservada","false");
        butacaIcon.setAttribute("idDB",salaButacas[i*columnas+j].pk);
        butacaIcon.setAttribute("id",nAsiento);
        divContenedor.addEventListener("click",ev=>reservar(ev));
      }else{
        butacaIcon.setAttribute("src","/static/Media/ButacasGrid/ocupada.png");
        divContenedor.classList.add("butacaTD");
        divContenedor.setAttribute("numero",0);
        butacaIcon.setAttribute("class","asientoImg");
        butacaIcon.setAttribute("idDB",salaButacas[i*columnas+j].pk);
        butacaIcon.setAttribute("id",nAsiento);
      }

      let datoTd=document.createElement("td");
      divContenedor.appendChild(butacaIcon);

      if (nAsiento!=0){
        let numeroA=document.createElement("div");
        numeroA.setAttribute("class","numero");
        numeroA.textContent=nAsiento;
        divContenedor.appendChild(numeroA);
      }
      datoTd.appendChild(divContenedor);
      filaTr.appendChild(datoTd);
    }
    let fCon=document.createElement("div");
    fCon.setAttribute("class","letra");
    hFContainer.appendChild(fCon);
    filaTr.setAttribute("id",letraFila);
    fCon.textContent=letraFila;
    filaTr.appendChild(headerFila.cloneNode(true));
    tablaButacas.appendChild(filaTr);
  }
  salaButacas=[];//ahora ésta variable guardará las butacas del cliente, se vacía
}

function liquidPaper(){
  for (let i=0;i<filas;i++){
    let tablaRow=tablaButacas.childNodes[i];
    let tablaFil=tablaRow.id;
    for (let j=0;j<columnas;j++){
      let tablaDatoN=tablaRow.childNodes[j+1].childNodes[0].getAttribute("numero");
      if (tablaDatoN!=0){
        salaButacas.forEach(function(kas){
          if (tablaDatoN==kas.fields.numero_asiento && tablaFil==kas.fields.fila){
            let primerHijoDiv=tablaRow.childNodes[j+1].childNodes[0];
            let primerHijo=primerHijoDiv.childNodes[0];
            primerHijo.setAttribute("src","/static/Media/ButacasGrid/ocupada.png");
            primerHijoDiv.removeEventListener('click',  reservar);
          }
        });
      }
    }
  }
  salaButacas=[];//ahora ésta variable guardará las butacas del cliente, se vacía
}

function reservar(ev){
  let idButacaDB="";
  let imagen;
  objetivoClic=ev.target.getAttribute("class");
  if (objetivoClic=="asientoImg"){
    imagen=ev.target;
    idButacaDB=imagen.getAttribute("idDB");
  }else if (objetivoClic=="numero"){
    imagen=ev.target.previousSibling;
    idButacaDB=imagen.getAttribute("idDB");
  }

  if (idButacaDB!=""){
    if (imagen.getAttribute("reservada")=="false")
    {
      if(boletosDisponibles!=0){
        imagen.src="/static/Media/ButacasGrid/reserva.png";
        imagen.setAttribute("reservada","true");
        salaButacas.push(idButacaDB);
        butacasImagenes.push(imagen);
        boletosDisponibles--;
        if (boletosDisponibles==0){confirmar.removeAttribute("disabled");}
      }else{
        imagen.src="/static/Media/ButacasGrid/reserva.png";
        imagen.setAttribute("reservada","true");
        salaButacas.push(idButacaDB);
        butacasImagenes.push(imagen);

        salaButacas.splice(0,1);
        butacasImagenes[0].setAttribute("src","/static/Media/ButacasGrid/disponible.png");
        butacasImagenes[0].setAttribute("reservada","false");
        butacasImagenes.splice(0,1);
      }
    }else{
      imagen.src="/static/Media/ButacasGrid/disponible.png";
      imagen.setAttribute("reservada","false");
      confirmar.setAttribute("disabled","");
      boletosDisponibles++;
      salaButacas.forEach(function(sisha,index){
        if (sisha==idButacaDB){
          salaButacas.splice(index,1);
          butacasImagenes.splice(index,1);
        }
      });
    }
  }
  boletosRestantes.textContent="Boletos Restantes: "+boletosDisponibles;
}

function confirmarCompra(){
  bootbox.confirm({
    centerVertical:"True",
    title: "Confirmación",
    message: "¿Está seguro/a de realizar la reserva?",
    buttons: {
        cancel: {label: '<i class="fa fa-times"></i> Cancelar'},
        confirm: {label: '<i class="fa fa-check"></i> Confirmar'}
    },
    callback: function (result) {
      if (result){
        mensaje1=JSON.stringify(salaButacas);

        $.ajax({
          url: a,
          type: "POST",
          data : {
            csrfmiddlewaretoken: token,
            mensaje1:mensaje1,
            mensaje2:funcionID,
            mensaje3:aidi,
            mensaje4:adultos,
            mensaje5:ninos,
            mensaje6:mayores,
          },
          success: function (msg) {
            bootbox.alert({
              centerVertical:"True",
              size: "small",
              title: "Notificación",
              message: "¡Reserva realizada con éxito!",
              closeButton: false,
              callback: function(){
                let vencimiento=new Date();
                let tiempoEnMinutos=5;
                vencimiento.setTime(vencimiento.getTime()+tiempoEnMinutos*60*1000);
                let expira ="expires="+vencimiento.toUTCString();
                document.cookie = "reservaCarrito="+vencimiento.getTime()+";"+expira+";path=/";
                setMinutos(tiempoEnMinutos);
                window.location.href=redirecto;
              }
            });
          },
          error: function (msg, textStatus, errorThrown) {alert("fail");console.log(msg);console.log(textStatus);console.log(errorThrown);}
        });
      }
  }
  });
}
