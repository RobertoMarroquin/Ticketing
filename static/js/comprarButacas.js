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
        butacaIcon.setAttribute("id",0);
      }else if(salaButacas[i*columnas+j].fields.disponibilidad){
        butacaIcon.setAttribute("src","/static/Media/ButacasGrid/disponible.png");
        divContenedor.classList.add("butacaTD");
        butacaIcon.setAttribute("class","asientoImg");
        butacaIcon.setAttribute("reservada","false");
        butacaIcon.setAttribute("id",nAsiento);
        divContenedor.addEventListener("click",ev=>reservar(ev));
      }else{
        butacaIcon.setAttribute("src","/static/Media/ButacasGrid/ocupada.png");
        divContenedor.classList.add("butacaTD");
        butacaIcon.setAttribute("class","asientoImg");
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



function reservar(ev){
  let filButaca="";
  let numButaca="";
  let imagen;
  objetivoClic=ev.target.getAttribute("class");
  if (objetivoClic=="asientoImg"){
    numButaca=ev.target.id;
    filButaca=ev.target.parentNode.parentNode.parentNode.id;
    imagen=ev.target;
  }else if (objetivoClic=="numero"){
    numButaca=ev.target.textContent;
    filButaca=ev.target.parentNode.parentNode.parentNode.id;
    imagen=ev.target.previousSibling;
  }

  if (filButaca!="" && numButaca!=""){
    if (imagen.getAttribute("reservada")=="false")
    {
      if(boletosDisponibles!=0){
        imagen.src="/static/Media/ButacasGrid/reserva.png";
        imagen.setAttribute("reservada","true");
        salaButacas.push(new ButacaClase(numButaca,filButaca));
        butacasImagenes.push(imagen);
        boletosDisponibles--;
        if (boletosDisponibles==0){confirmar.removeAttribute("disabled");}
      }else{
        imagen.src="/static/Media/ButacasGrid/reserva.png";
        imagen.setAttribute("reservada","true");
        salaButacas.push(new ButacaClase(numButaca,filButaca));
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
        if (sisha.numero_asiento==numButaca && sisha.fila==filButaca){
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
            mensaje2:adultos,
            mensaje3:ninos,
            mensaje4:mayores,
          },
          success: function (msg) {
            alert(msg);
            let vencimiento=new Date();
            let tiempoEnMinutos=5;
            vencimiento.setTime(vencimiento.getTime()+tiempoEnMinutos*60*1000);
            let expira ="expires="+vencimiento.toUTCString();
            document.cookie = "reservaCarrito="+vencimiento.getTime()+";"+expira+";path=/";
            setMinutos(tiempoEnMinutos);
            window.location.href=redirecto;
          },
          error: function (msg, textStatus, errorThrown) {alert("fail");console.log(msg);console.log(textStatus);console.log(errorThrown);}
        });
      }
  }
  });
}

function ButacaClase(numero_asiento,fila){
  this.numero_asiento=numero_asiento;
  this.fila=fila;
}
