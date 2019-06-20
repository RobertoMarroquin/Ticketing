function tostada(texto,colorFondo,colorTexto,tiempo) {
  var x = document.getElementById("snackbar");
  x.textContent=texto;
  x.style.backgroundColor=colorFondo||"#cce5ff";
  x.style.color=colorTexto||"#394085";
  x.className = "show";
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, tiempo||3000);
}
