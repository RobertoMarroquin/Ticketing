if (getCookie("horaCarrito")!==""){
  let x=setInterval(function() {
    let tiempo =getCookie("horaCarrito");
    let ahora=new Date().getTime();
    let distancia=tiempo-ahora;
    let hora=formatear(Math.floor((distancia%(1000*60*60*24))/(1000*60*60)));
    let minuto=formatear(Math.floor((distancia%(1000*60*60))/(1000*60)));
    let segundo=formatear(Math.floor((distancia%(1000*60))/1000));

    if (document.getElementById("timer").hidden){
      document.getElementById("timer").removeAttribute("hidden");
      document.getElementById("temporizador").removeAttribute("hidden");
      document.getElementById("leSeparatorTime").removeAttribute("hidden");
    }

    if (hora!="00"){document.getElementById("timer").textContent=hora+":"+minuto+":"+segundo;}
    else {document.getElementById("timer").textContent=minuto+":"+segundo;}

    if (minuto!=="00"&&segundo==="00"){document.getElementById("timer").style.color="#c3c3c3";}
    else{document.getElementById("timer").style.color="";}

    if (minuto==="00"&&segundo<=30){
      if (segundo%2===0){document.getElementById("timer").style.color="";}
      else{document.getElementById("timer").style.color="#af4c4c";}
    }

    if (distancia<0){
      clearInterval(x);
      document.getElementById("timer").style.color="";
      document.getElementById("temporizador").setAttribute("hidden","");
      //document.getElementById("leSeparatorTime").setAttribute("hidden","");
      document.getElementById("carritoN").textContent=0;
      document.getElementById("timer").textContent="Carrito vaciado";
    }
  },1000);
}

function getCookie(cname) {
  let name = cname + "=";
  let ca = decodeURIComponent(document.cookie).split(';');
  for(let i=0;i<ca.length;i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {c = c.substring(1);}
    if (c.indexOf(name) == 0) {return c.substring(name.length, c.length);}
  }return "";
}

function setMinutos(tiempoEnMinutos) {
  let vencimiento=new Date();
  vencimiento.setTime(vencimiento.getTime()+tiempoEnMinutos*60*1000);
  let expira ="expires="+vencimiento.toUTCString();
  document.cookie="horaCarrito="+vencimiento.getTime()+";"+expira+";path=/";
}

function formatear(algo){
  if (algo<=9&&algo>=0){return "0"+algo;}
  else {return algo;}
}
