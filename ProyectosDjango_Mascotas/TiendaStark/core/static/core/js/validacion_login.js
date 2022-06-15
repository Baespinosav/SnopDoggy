$('#login').validate({
    "rules": {
        "correo":{
            required: true,
        },
        "constraseña":{
            required: true
        },
    },
    messages: {
        "correo":{
            required: "Correo es un campo obligatorio",
        },
        "constraseña":{
            required: "Contraseña es un campo obligatorio"
        }
    },
});

function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

$.validator.addMethod(
    "validateemail",
    function(value, element, validate) {
        debugger
        if (validate) {
            return validateEmail(value);
        }
    },
    "Formato de correo incorrecto"
);

$.validator.addMethod(
    "onenumber",
    function(value, element, validate) {
        if (validate) {
            var re = new RegExp('.*[0-9].*');
            resp = re.test(value);
            return resp;
        }
    },
    "La contraseña debe contener al menos un número"
);

$.validator.addMethod(
    "onemayus",
    function(value, element, validate) {
        if (validate) {
            var re = new RegExp('.*[A-Z].*');
            resp = re.test(value);
            return resp;
        }
    },
    "La contraseña debe contener al menos una mayúscula"
);

$("#correo").rules("add", { validateemail: true });
$("#password").rules("add", { onenumber: true });
$("#password").rules("add", { onemayus: true });

/*
let btn = document.getElementById("validacion");
btn.addEventListener("click", function() {
    let correo = document.getElementById("correo");
    let constraseña = document.getElementById("contraseña");
})
*/