document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        let valid = true;

        
        const nombre = document.getElementById('nombre').value.trim();
        const email = document.getElementById('email').value.trim();
        const telefono = document.getElementById('telefono').value.trim();

        
        if (nombre === "") {
            valid = false;
            alert('Por favor, ingresa tu nombre.');
        }

        
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        if (!emailPattern.test(email)) {
            valid = false;
            alert('Por favor, ingresa un email válido.');
        }

        
        const telefonoPattern = /^[0-9]{10}$/;
        if (!telefonoPattern.test(telefono)) {
            valid = false;
            alert('Por favor, ingresa un número de teléfono válido (10 dígitos).');
        }

        if (!valid) {
            event.preventDefault(); 
        }
    });
});
