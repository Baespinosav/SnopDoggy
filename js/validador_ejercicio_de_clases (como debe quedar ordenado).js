// objeto.metodo(json)

$('#formulario1').validate(
    { 
        "rules": 
            {
                "txtEmail": 
                    {
                        required: true,
                        email: true,
                    },
            }, // --> Fin de reglas
        messages: 
            {
                "txtEmail": 
                    {
                        required: 'El email es un campo requerido',
                        email: 'El email no cumple el formato de un correo'
                    },
            },
    }
);