function chuck() {
  const settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random",
    "method": "GET",
    "headers": {
      "accept": "application/json",
      "x-rapidapi-key": "SIGN-UP-FOR-KEY",
      "x-rapidapi-host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }
  };

  $.ajax(settings).done(function (response) {
    console.log(response);

  });

}

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

const Installer = function(root) {
  let promptEvent;

  const install = function(e) {
    if(promptEvent) {
      promptEvent.prompt();
      promptEvent.userChoice
        .then(function(choiceResult) {
          // The user actioned the prompt (good or bad).
          // good is handled in
          promptEvent = null;
          ga('send', 'event', 'install', choiceResult);
          root.classList.remove('available');
        })
        .catch(function(installError) {
          // Boo. update the UI.
          promptEvent = null;
          ga('send', 'event', 'install', 'errored');
          root.classList.remove('available');
        });
    }
  };

  const installed = function(e) {
    promptEvent = null;
    // This fires after onbeforinstallprompt OR after manual add to homescreen.
    ga('send', 'event', 'install', 'installed');
    root.classList.remove('available');
  };

  const beforeinstallprompt = function(e) {
    promptEvent = e;
    promptEvent.preventDefault();
    ga('send', 'event', 'install', 'available');
    root.classList.add('available');
    return false;
  };

  window.addEventListener('beforeinstallprompt', beforeinstallprompt);
  window.addEventListener('appinstalled', installed);

  root.addEventListener('click', install.bind(this));
  root.addEventListener('touchend', install.bind(this));
};
