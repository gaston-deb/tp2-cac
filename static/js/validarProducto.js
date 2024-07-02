document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
      if (!validarFormulario()) {
        event.preventDefault();
      }
    });
  });
  
  function validarFormulario() {
    let esValido = true;
  
    
    const tipo = document.getElementById("tipo");
    if (tipo.value === "") {
      alert("Por favor, seleccione un tipo de producto.");
      esValido = false;
    }
  
    
    const marca = document.getElementById("marca");
    if (marca.value.trim() === "") {
      alert("Por favor, ingrese la marca del producto.");
      esValido = false;
    }
  
    
    const modelo = document.getElementById("modelo");
    if (modelo.value.trim() === "") {
      alert("Por favor, ingrese el modelo del producto.");
      esValido = false;
    }
  
    
    const detalle = document.getElementById("detalle");
    if (detalle.value.trim() === "") {
      alert("Por favor, ingrese el detalle del producto.");
      esValido = false;
    }
  
   
    const precio = document.getElementById("precio");
    if (precio.value.trim() === "" || isNaN(precio.value) || Number(precio.value) <= 0) {
      alert("Por favor, ingrese un precio válido para el producto.");
      esValido = false;
    }
  
   
    const imagen = document.getElementById("imagen");
    if (imagen.value.trim() === "") {
      alert("Por favor, ingrese el nombre de la imagen del producto.");
      esValido = false;
    }
  
    
    const estado = document.getElementById("estado");
    if (estado.value === "") {
      alert("Por favor, seleccione un estado para el producto.");
      esValido = false;
    }
  
    return esValido;
  }
  