/* main */ 
/* integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"*/
/* integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1"*/
$(document).ready(function(){
    // Agrega el smooth a todos los botones de links
    $("a").on('click', function(event) {
  
      // Make sure this.hash has a value before overriding default behavior
      if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();
  
        // Store hash
        var hash = this.hash;
  
        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 800, function(){
  
          // Add hash (#) to URL when done scrolling (default click behavior)
          window.location.hash = hash;
        });
      } // End if
    });
});

function togglePasswordVisibility() {
  var passwordInput = document.getElementById('password');
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
  } else {
    passwordInput.type = "password";
  }
}

function validarFormulario() {
  // Obtener los valores de los campos de contraseña
  var password = document.getElementById("password").value;
  var confirm_password = document.getElementById("confirm_password").value;

  // Verificar si los valores son iguales
  if (password !== confirm_password) {
    // Mostrar un mensaje de error
    alert("Las contraseñas no coinciden");
    return false; // Evitar que se envíe el formulario
  }

  // Si llegamos aquí, las contraseñas coinciden
  return true; // Permitir que se envíe el formulario
}
