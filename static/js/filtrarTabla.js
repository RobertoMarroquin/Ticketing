function filtraTabla(n) {
  let fila;
  let i;
  let x;
  let y;
  let podriaCambiar;
  let bandera = true;
  let ascDesc = "asc";
  let cambiaCuenta = 0;
  let tabla = document.getElementById("tabla");
  let cabeceras=document.querySelectorAll("#tabla"+" thead th");
  let esFecha=false;

  if (cabeceras[n].textContent.slice(0,5).toLowerCase()=="fecha"){esFecha=true;}

  for (let w=0;w<cabeceras.length;w++)
  {cabeceras[w].innerHTML=cabeceras[w].textContent+"<span class='fas fa-sort'></span>"}

  while (bandera) {
    bandera = false;
    fila = tabla.rows;

    for (i = 1; i < (fila.length - 1); i++) {
      podriaCambiar = false;
      x = fila[i].getElementsByTagName("TD")[n].innerHTML.toLowerCase();
      y = fila[i + 1].getElementsByTagName("TD")[n].innerHTML.toLowerCase();

      if (esFecha){
        let indix=x.indexOf("/");
        let di=x.slice(0,indix);
        let me=x.slice(indix+1,x.lastIndexOf("/")); indix=x.lastIndexOf("/");
        let an=x.slice(indix+1);
        x=new Date(an,me-1,di,0,0,0,0);

        indix=y.indexOf("/");
        di=y.slice(0,indix);
        me=y.slice(indix+1,y.lastIndexOf("/")); indix=y.lastIndexOf("/");
        an=y.slice(indix+1);
        y=new Date(an,me-1,di,0,0,0,0);
      }

      if (ascDesc == "asc") {
        if (x > y) {
          podriaCambiar= true;
          break;
        }
      } else if (ascDesc == "desc") {
        if (x < y) {
          podriaCambiar = true;
          break;
        }
      }
    }

    if (ascDesc=="asc"){
      cabeceras[n].innerHTML=cabeceras[n].textContent+"<span class='fas fa-sort-down'></span>";
    }
    else{
      cabeceras[n].innerHTML=cabeceras[n].textContent+"<span class='fas fa-sort-up'></span>";
    }

    if (podriaCambiar) {
      fila[i].parentNode.insertBefore(fila[i + 1], fila[i]);
      bandera = true;
      cambiaCuenta++;
    } else if (cambiaCuenta == 0 && ascDesc == "asc") {ascDesc = "desc";bandera = true;}
  }
}
