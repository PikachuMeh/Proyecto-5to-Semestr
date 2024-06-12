export function revisar_email(email){
    let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}


export function validacion_nombre_apellido(nombre){
    let re = /^[a-zA-Z]+$/;
    return re.test(nombre);
}

export function clave(clave1,clave2){
    if (clave1 === clave2) {
        return false
    }else
        return true
}