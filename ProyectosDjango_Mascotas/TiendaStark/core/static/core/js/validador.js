// objeto.metodo(json)

$('#formulario1').validate({ 
    "rules": {
        "txtEmail": {
            required: true,
            email: true,
        },
        "txtContrasena": {
            required: true,
            minlength: 5
        },
        "txtRepetirContrasena": {
            required: true,
            equalTo: '#id_txtContrasena'
        }
    }, // --> Fin de reglas
    messages: {
        "txtEmail": {
            required: 'El email es un campo requerido',
            email: 'El email no cumple el formato de un correo'
        },
        "txtContrasena": {
            required: 'La contraseña es una campo obligatorio',
            minlength: 'Mínimo 5 caracteres'
        },
        "txtRepetirContrasena": {
            required: 'Repita la contraseña anterior',
            equalTo: 'Debe ser igual al campo contraseña'
        }
    },
});