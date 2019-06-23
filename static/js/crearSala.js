const tablaButacas=document.getElementById("tablaButacas");
const filasOp=document.getElementById("id_numero_filas");
const columnasOp=document.getElementById("id_numero_columnas");
const numeroSalaOp=document.getElementById("id_numero_sala");

filasOp.value="";
columnasOp.value="";
numeroSalaOp.value="";

let lastValuerF=0;
let lastValuerC=0;
let filas=0;
let columnas=0;
let bandera=true;//true==primer vez o ceroF ceroC

//////////////////////////////////////////////////////////////////////////
//ASIGNACIÓN DE EVENTOS
//////////////////////////////////////////////////////////////////////////

filasOp.setAttribute("onchange","setFilas()");
columnasOp.setAttribute("onchange","setColumnas()");
numeroSalaOp.setAttribute("onchange","validarNSala()");
document.getElementById("postGuardar").addEventListener("click",guardarSala);

//////////////////////////////////////////////////////////////////////////
//VALIDACIONES DE LOS CAMPOS
//////////////////////////////////////////////////////////////////////////

function validarNSala(){
  if (numeroSalaOp.value<1){
    numeroSalaOp.value=1;tostada("¡El número de sala tiene que ser positivo!","#f8d7da","#721c24");
  }
  else if (numeroSalaOp.value%1!==0){
    numeroSalaOp.value=Math.floor(numeroSalaOp.value);tostada("¡El número de sala no puede ser fracción!","#f8d7da","#721c24");
  }
}

function setFilas(){
  if (filasOp.value>26){
    filas=filasOp.value=26;
    tostada("¡El máximo de filas es 26!","#f8d7da","#721c24");
  }
  else if (filasOp.value<1){
    filas=filasOp.value=1;
    tostada("¡Las filas tienen que ser números positivos!","#f8d7da","#721c24");
  }
  else if (filasOp.value%1!==0){
    filas=filasOp.value=Math.floor(filasOp.value);
    tostada("¡No se admiten fracciones de filas!","#f8d7da","#721c24");
  }
  else{filas=filasOp.value;}
  if (filas>0&&columnas>0){
    if (bandera){artista();bandera=false;}
    else if (filas-lastValuerF!=0){artista(filas-lastValuerF,"F");}
  }else if (filas==0&&columnas==0){bandera=true;}
  lastValuerF=filas;
}

function setColumnas(){
  if (columnasOp.value>30){
    columnas=columnasOp.value=30;
    tostada("¡El máximo de columnas es 30!","#f8d7da","#721c24");
  }
  else if (columnasOp.value<1){
    columnas=columnasOp.value=1;
    tostada("¡Las columnas tienen que ser números positivos!","#f8d7da","#721c24");
  }
  else if (columnasOp.value%1!==0){
    columnas=columnasOp.value=Math.floor(columnasOp.value);
    tostada("¡No se admiten fracciones de columnas!","#f8d7da","#721c24");
  }
  else{columnas=columnasOp.value;}
  if (filas>0&&columnas>0){
    if (bandera){artista();bandera=false;}
    else if (columnas-lastValuerC!=0){artista(columnas-lastValuerC,"C");}
  }else if (filas==0&&columnas==0){bandera=true;}
  lastValuerC=columnas;
}

//////////////////////////////////////////////////////////////////////////
//ACÁ SE DIBUJA TODO
//////////////////////////////////////////////////////////////////////////

function  artista(diferencia,filaOcol){
  switch (filaOcol) {
    case "C":{
      tablaTr=tablaButacas.querySelectorAll("tr");
      if (diferencia>0){
        for (let r=0;r<diferencia;r++){
          let j=tablaTr[0].childNodes.length;
          tablaTr.forEach(function(teibolRou){
            let butacaIcon=document.createElement("img");
            butacaIcon.setAttribute("src","/static/Media/ButacasGrid/butacaEditor.png");
            butacaIcon.setAttribute("class","butacaTD");
            butacaIcon.setAttribute("id",j+1);
            butacaIcon.setAttribute("title",j+1);
            butacaIcon.setAttribute("clase",true);
            butacaIcon.addEventListener("click",ev=>clickear(ev));
            let datoTd=document.createElement("td");
            datoTd.appendChild(butacaIcon);
            teibolRou.appendChild(datoTd);
          });
        }
      }else{
        diferencia=Math.abs(diferencia);
        for (let r=0;r<diferencia;r++){
          tablaTr.forEach(function(teibolRou){teibolRou.removeChild(teibolRou.lastChild);});
        }
      }
    }break;

    case "F":{
      if (diferencia>0){
        for (let i=Number(lastValuerF);i<filas;i++){
          let filaTr=document.createElement("tr");
          filaTr.setAttribute("id",numeroLetra(i));
          tablaButacas.appendChild(filaTr);

          for (let j=0;j<columnas;j++){
            let butacaIcon=document.createElement("img");

            butacaIcon.setAttribute("src","/static/Media/ButacasGrid/butacaEditor.png");
            butacaIcon.setAttribute("class","butacaTD");
            butacaIcon.setAttribute("id",j+1);
            butacaIcon.setAttribute("title",j+1);
            butacaIcon.setAttribute("clase",true);

            butacaIcon.addEventListener("click",ev=>clickear(ev));

            let datoTd=document.createElement("td");
            datoTd.appendChild(butacaIcon);
            filaTr.appendChild(datoTd);
          }
        }
      }else{
        diferencia=Math.abs(diferencia);
        for (let r=0;r<diferencia;r++){tablaButacas.removeChild(tablaButacas.lastChild);}
      }
    }break;

    default:{
      for (let i=0;i<filas;i++){

        let filaTr=document.createElement("tr");
        let letraFila=numeroLetra(i);
        filaTr.setAttribute("id",letraFila);
        tablaButacas.appendChild(filaTr);

        for (let j=0;j<columnas;j++){
          let butacaIcon=document.createElement("img");

          butacaIcon.setAttribute("src","/static/Media/ButacasGrid/butacaEditor.png");
          butacaIcon.setAttribute("class","butacaTD");
          butacaIcon.setAttribute("id",j+1);
          butacaIcon.setAttribute("title",j+1);
          butacaIcon.setAttribute("clase",true);

          butacaIcon.addEventListener("click",ev=>clickear(ev));

          let datoTd=document.createElement("td");
          datoTd.appendChild(butacaIcon);
          filaTr.appendChild(datoTd);
        }
      }
    }
  }
}

//////////////////////////////////////////////////////////////////////////
//EVENTOS
//////////////////////////////////////////////////////////////////////////

function clickear(ev){
  let iconoClick=ev.target;
  if (iconoClick.getAttribute("clase")==="false"){
    iconoClick.setAttribute("src","/static/Media/ButacasGrid/butacaEditor.png");
    iconoClick.setAttribute("clase",true);
    iconoClick.setAttribute("class","butacaTD");
  }
  else if(iconoClick.getAttribute("clase")==="true"){
    iconoClick.setAttribute("src","/static/Media/ButacasGrid/caminoEditor.png");
    iconoClick.setAttribute("clase",false);
    iconoClick.setAttribute("class","caminoTD");
  }
}

//////////////////////////////////////////////////////////////////////////
//EXTRAS
//////////////////////////////////////////////////////////////////////////

//transformador de número a letra, recordar que 65 es la letra A
function numeroLetra(numero){return String.fromCharCode(numero+65);}
function letraNumero(letra){return letra.charCodeAt(0)-65;}

//////////////////////////////////////////////////////////////////////////
//PERSISTENCIA
//////////////////////////////////////////////////////////////////////////

function ButacaClase(numero_asiento,fila,disponibilidad,clase){
  this.numero_asiento=numero_asiento;
  this.fila=fila;
  this.disponibilidad=disponibilidad;
  this.clase=clase;
}

function SalaClase(nombre,numero_sala,numero_asientos,numero_filas,numero_columnas,clase,boleteria){
  this.nombre=nombre;
  this.numero_sala=numero_sala;
  this.numero_asientos=numero_asientos;
  this.numero_filas=numero_filas;
  this.numero_columnas=numero_columnas;
  this.clase=clase;
  this.boleteria=boleteria;
}

function guardarSala(){
  /////////////creando les butacas
  let token = $('input[name=csrfmiddlewaretoken]').val();
  let numeroAsientos=0;
  let filaAsientos=-1;

  let butacas=[];
  let trButacas=tablaButacas.querySelectorAll("tr");

  trButacas.forEach(function(rowsT){
    let tdsT=rowsT.childNodes;
    let flage=0;
    let asientosRow=0;

    tdsT.forEach(function(casilla){if(casilla.firstChild.getAttribute("clase")=="true"){flage=1;}});

    if (flage==1){filaAsientos++;}

    tdsT.forEach(function(casilla){
      if(casilla.firstChild.getAttribute("clase")=="true"){
        numeroAsientos++;
        asientosRow++;
        butacas.push(new ButacaClase(asientosRow,numeroLetra(filaAsientos),true,true));
      }else{
        butacas.push(new ButacaClase(0,"-",true,false));
      }
    });
  });

  /////////////se crea la sala
  salaNueva=new SalaClase(
    document.getElementById("id_nombre").value,
    document.getElementById("id_numero_sala").value,
    numeroAsientos,
    document.getElementById("id_numero_filas").value,
    document.getElementById("id_numero_columnas").value,
    document.getElementById("id_clase").value,
    document.getElementById("id_boleteria").value
  );

  bootbox.dialog({
    centerVertical:"True",
    message: '<div class="text-center"><i class="fa fa-spin fa-spinner"></i> Guardando, por favor espere...</div>',
    closeButton: false
  });
  /////////////ahora se serializa
  mensaje1=JSON.stringify(salaNueva);
  mensaje2=JSON.stringify(butacas);

  $.ajax({
    url: a,
    type: "POST",
    data : {
      csrfmiddlewaretoken: token,
      mensaje1:mensaje1,
      mensaje2:mensaje2,
    },
    success: function (msg) {
      bootbox.hideAll();
      bootbox.alert({
        centerVertical:"True",
        closeButton: false,
        size: "small",
        title: "Notificación",
        message: "¡La sala ha sido guardada con éxito!",
        callback: function(){window.location.href=r}
      })
    },
    error: function (msg, textStatus, errorThrown) {alert("fail");console.log(msg);console.log(textStatus);console.log(errorThrown);}
  });

}
