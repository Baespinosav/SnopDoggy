$('#registro').validate({ 
    "rules": {
        "rut": {
            required: true,
        },
        "nombres": {
            required: true,
        },
        "apellidos": {
            required: true,
        },
        "correo": {
            required: true,
            email: true,
        },
        "direccion": {
            required: true,
        },
        "password": {
            required: true,
            minlength : 10,
        },
        "password2": {
            required: true,
            minlength : 10,
            equalTo : "#password",
        },
    },
    messages: {
        "rut": {
            required: 'Debe ingresar un RUT válido',
        },
        "nombres": {
            required: 'Debe ingresar sus nombres',
        },
        "apellidos": {
            required: 'Debe ingresar sus apellidos',
        },
        "correo": {
            required: 'Debe ingresar su correo electrónico',
            email: 'Formato de correo incorrecto'
        },
        "direccion": {
            required: 'Debe ingresar su dirección',
        },
        "password": {
            required: 'Debe ingresar una password',
            minlength: 'La mínima cantidad de caracteres de la contraseña es 10',
        },
        "password2": {
            required: 'Debe repetir la misma password',
            minlength: 'La mínima cantidad de caracteres de la contraseña es 10',
            equalTo: 'La repetición de contraseña debe coincidir con la contraseña original',
        },
    }
});

function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

// Valida el rut con su cadena completa "XXXXXXXX-X"
function validateRut(rutCompleto) {
    if (!/^[0-9]+-[0-9kK]{1}$/.test(rutCompleto))
        return false;
    var tmp = rutCompleto.split('-');
    var rut = tmp[0];
    var digv = tmp[1]; 
    if (digv == 'k') digv = 'K' ;
    return (dv(rut) == digv );
}

function dv(T) {
    var M=0,S=1;
    for(; T; T = Math.floor(T/10))
        S=(S + T % 10 * (9 - M++ %6))%11;
    return S?S-1:'k';
}

// Uso de la función validateRut
// alert( Fn.validateRut('16560241-2') ? 'válido' : 'inválido');

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

$.validator.addMethod(
    "rut",
    function(value, element, validate) {
        if (validate) {
            return validateRut(value);
        }
    },
    "El formato del rut no es válido"
);

$("#rut").rules("add", { rut: true });
$("#correo").rules("add", { validateemail: true });
$("#password").rules("add", { onenumber: true });
$("#password").rules("add", { onemayus: true });

$('#buscarfoto').on('change', function(e) {
    let file = '../images/' + e.target.files[0].name;
    $('#fotoperfil').attr('src', file);
});