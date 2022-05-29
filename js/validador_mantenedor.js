$('#formulario-1').validate({
    "rules": {
        "id": {
            required: true,
        },
        "categoria": {
            required: true,
        },
        "nombre": {
            required: true,
            minlength: 5,
            maxlength: 20
        },
        "descripcion": {
            required: true,
            maxlength: 100
        },
        "precio": {
            required: true,
        },
        "descuento": {
            required: true,
            maxlength: 2
        },
        "descuento2": {
            required: true,
            maxlength: 2 
        }
    },
    messages: {
        "id": {
            required: "Es necesario un id",
        },
        "categoria": {
            required: "Elegir categoria del producto",
        },
        "nombre": {
            required: "Ingresar nombre del producto",
            minlength: "El nombre debe tener un minimo de 5 caracteres",
            maxlength: "El nombre debe tener un maximo de 20 caracteres"
        },
        "descripcion": {
            required: "Ingresar descripcion del producto",
            maxlength: "La descripcion debe tener un maximo de 100 caracteres"
        },
        "precio": {
            required: "Ingresar precio del producto",
        },
        "descuento": {
            required: "Ingresar descuento de suscriptor",
            maxlength: "Maximo 2 digitos"
        },
        "descuento2": {
            required: "Ingresar oferta",
            maxlength: "Maximo 2 digitos" 
        }
    } ,
});