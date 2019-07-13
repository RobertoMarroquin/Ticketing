function actualOpcion(){
  let direccion=window.location.pathname.slice( 0,-1);
  direccion=direccion.slice(direccion.lastIndexOf("/")+1);
  let elemento=document.getElementById(direccion);
  if (elemento){elemento.style="color:#0066cc;"}
  else {
    elemento=document.title;
    limpiaNavBar(elemento);
  }
}

function limpiaNavBar(texto){
  let navBar=document.getElementById("navBar");
  while (navBar.firstChild) {navBar.removeChild(navBar.firstChild);}

  let nuevoLi=document.createElement("li");
  let textoH=document.createElement("h2");
  nuevoLi.setAttribute("class","navbar-nav");
  textoH.textContent=texto;
  nuevoLi.appendChild(textoH);
  navBar.appendChild(nuevoLi);
}
