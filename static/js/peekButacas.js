const tablaButacas=document.getElementById("tablaButacas");
let salaButacas;
let token = $('input[name=csrfmiddlewaretoken]').val();

$.ajax({
  url: p,
  type: "POST",
  data : {
    csrfmiddlewaretoken: token,
    mensaje1:aidi,
  },
  success: function(smg){
    salaButacas=JSON.parse(smg);
    if (salaButacas!=""){artista();}
    else {tostada("Ésta sala no dispone de butacas en la base de datos, favor actualizarla","#f8d7da","#721c24",6000);}
  },
  error: function (msg, textStatus, errorThrown) {alert("fail");console.log(msg);console.log(textStatus);console.log(errorThrown);}
});

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
      divContenedor.setAttribute("class","container");

      /////buscando si hay alguna butaca en la fila y si hay, se asigna la letra
      if (salaButacas[i*columnas+j].fields.fila!="-"&&flagFila==0){
        letraFila=salaButacas[i*columnas+j].fields.fila;
        flagFila=1;
      }
      let butacaIcon=document.createElement("img");
      let nAsiento=salaButacas[i*columnas+j].fields.numero_asiento;

      if (salaButacas[i*columnas+j].fields.clase){
        butacaIcon.setAttribute("src","/static/Media/ButacasGrid/butacaEditor.png");
        butacaIcon.setAttribute("class","butacaTD");
        butacaIcon.setAttribute("clase",true);
        butacaIcon.setAttribute("id",nAsiento);
      }else{
        butacaIcon.setAttribute("src","/static/Media/ButacasGrid/transparente.png");
        butacaIcon.setAttribute("class","caminoTD");
        butacaIcon.setAttribute("clase",false);
        butacaIcon.setAttribute("id",0);
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
}
