let camposBoleteria=document.getElementsByClassName("form-control");
let tamCampos=camposBoleteria.length;
let butacasDisponibles;
let boletosTotales=0;
let boletosPermitidos=10;

$.ajax({
  url: dispo,
  type: "POST",
  data : {
    csrfmiddlewaretoken: token,
    message1:func,
    message2:sa,
  },
  success: function(smg){
    butacasDisponibles=Number(smg);
  },
  error: function (msg, textStatus, errorThrown) {alert("fail");console.log(msg);console.log(textStatus);console.log(errorThrown);}
});

for(let i=0;i<tamCampos;i++){
  camposBoleteria[i].value=0;
  camposBoleteria[i].setAttribute("onchange","validar(this)");
}

function validar(wx){
  wxw=wx.value;
  boletosTotales=0;
  for (let u=0;u<tamCampos;u++){boletosTotales+=Number(camposBoleteria[u].value);}
  if (boletosTotales===0){document.getElementById("selectButaca").setAttribute("disabled","");}
  else{document.getElementById("selectButaca").removeAttribute("disabled");}
  if(wxw<0){
    wx.value=0;
    tostada("¡No es posible adquirir boletos negativos!","#f8d7da","#721c24");
  }
  else if(boletosTotales>butacasDisponibles){
    wx.value-=(boletosTotales-butacasDisponibles);
    tostada("¡No hay más butacas disponibles en la sala!","#f8d7da","#721c24");
  }else if (boletosTotales>boletosPermitidos){
    wx.value-=(boletosTotales-boletosPermitidos);
    tostada("¡No se permite comprar más de "+boletosPermitidos+" boletos!","#f8d7da","#721c24");
  }else if (wxw%1!==0){
    wx.value=Math.floor(wxw);
    tostada("¡No puedes comprar fracciones de boletos!","#f8d7da","#721c24");
    }
}
