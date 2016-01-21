$(function(){
    window.addEventListener('load', inicio, false);
    function inicio()
    {   document.getElementById("formulario").addEventListener('submit', validar, false);
    }
    function validar(evt)
    {   //Validacion de fecha de nacimiento
        var born = new Date(document.getElementById("datepicker").value);
        var today = new Date();
        var dd = today.getDate();
        var mm = today.getMonth()+1; //January is 0!
        var yyyy = today.getFullYear()-18;
        if(dd<10) dd='0'+dd;
        if(mm<10) mm='0'+mm;
        var menos18 = yyyy+'-'+mm+'-'+dd;
        var todayless18 = new Date(menos18);
        if (born>todayless18)
            {   document.getElementById("alerta").innerHTML = "¡Hay campos con datos erroneos!";
                document.getElementById("alerta").style.color = "red";
                document.getElementById("alertaBorn").innerHTML = "¡La fecha de nacimiento no puede ser mayor a la fecha actual y debe ser de hace 18 años antes de la fecha actual!";
                document.getElementById("alertaBorn").style.color = "red";
                evt.preventDefault();
            }
        else
            {   document.getElementById("alerta").innerHTML = "";
                document.getElementById("alertaBorn").innerHTML = "";
                //evt.initEvent();
            }
        }
});