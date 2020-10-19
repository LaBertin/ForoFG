$(function() {

	$.validator.setDefaults({
  	errorClass:'error-label',
    highlight: function(element){
    	$(element).addClass('error-control');
    },
    unhighlight: function(element){
    $(element).removeClass('error-control');
    }
  });

$("#registro").validate({
    rules: {
        nombrecuenta: "required",
        codigo: "required",

        email: {
            required: true,
            email: true
        },
        contraseña: "required",
        ccontraseña: {
            required: true,
            equalTo: "#contraseña"
        }

    },
    messages: {
        nombrecuenta: {
          required: 'Ingrese nombre',
          minlength: 'Ingrese 6 o mas caracteres',
          maxlength: 'Ingrese 20 o menos caracteres'
        },
        codigo: {
          required: 'Ingresa código de FallGuys',
          minlength: 'Ingrese 4 dígitos',
          maxlength: 'Ingrese 4 dígitos',
        },
        email: {
            required: 'Ingresa tu correo electrónico',
            email: 'Formato de correo no válido'
        },
        contraseña: {
            required: 'Ingresa una contraseña',
            minlength: 'Largo insuficiente'
        },
        ccontraseña: {
            required: 'Reingresa la contraseña',
            equalTo: 'Las contraseñas ingresadas no coinciden',
            minlength: 'Ingrese 8 o mas caracteres'

      }
    }
  }); 
});