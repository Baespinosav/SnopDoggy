// objeto.metodo(json)

$('#formulario1').validate({ 
    "rules": {
        "txtEmail": 
         required: true,
            email: true,
        },
    }, // --> Fin de reglas
    messages: {
        "txtEmail": {
    
    },
});