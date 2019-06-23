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
    artista();
  },
  error: function (msg, textStatus, errorThrown) {alert("fail");console.log(msg);console.log(textStatus);console.log(errorThrown);}
});

function numeroLetra(numero){return String.fromCharCode(numero+65);}
function letraNumero(letra){return letra.charCodeAt(0)-65;}

function artista(){
  for (let i=0;i<filas;i++){
    let filaTr=document.createElement("tr");
    let letraFila=numeroLetra(i);
    filaTr.setAttribute("id",letraFila);
    tablaButacas.appendChild(filaTr);

    for (let j=0;j<columnas;j++){
      let butacaIcon=document.createElement("img");

      if (salaButacas[i*columnas+j].fields.clase){
        butacaIcon.setAttribute("src","/static/Media/ButacasGrid/butacaEditor.png");
        butacaIcon.setAttribute("class","butacaTD");
        butacaIcon.setAttribute("clase",true);
      }else{
        butacaIcon.setAttribute("src","/static/Media/ButacasGrid/caminoEditor.png");
        butacaIcon.setAttribute("class","caminoTD");
        butacaIcon.setAttribute("clase",false);
      }
      butacaIcon.setAttribute("id",j+1);
      butacaIcon.setAttribute("title",j+1);
      butacaIcon.addEventListener("click",ev=>clickear(ev));
      let datoTd=document.createElement("td");
      datoTd.appendChild(butacaIcon);
      filaTr.appendChild(datoTd);
    }
  }
}
