const crit=document.getElementById("criterio");
crit.value="";
crit.onkeyup=function () {filtro(this.value);}
crit.focus();

function filtro (criterio) {
  let filas=document.querySelectorAll("#tabla"+" tbody tr");
  for(let i=0;i<filas.length;i++){
    let mostrarFila=false;
    let fila=filas[i];
    fila.style.display="none";
    for (let j=0;j<fila.childElementCount;j++){
      if (fila.children[j].textContent.toLowerCase().indexOf(criterio.toLowerCase().trim())>-1){mostrarFila=true;break;}
    }
    if (mostrarFila){fila.style.display=null;}
  }
}
