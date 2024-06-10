<script>
    import {ref} from 'vue'

    let email = ref('')

    async function revisar_email(email){
        let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    }
    async function recupera(){
        console.log(email)
        let Email = revisar_email(email.value)
        if(await Email == true){
        
        }else{
            alert("Ingresa Bien el correo")
        }
    }

</script>
<template>
    <form>
        Correo:
        <input type="email" v-model ="email" name="email" id="form2Example1" class="form-control" required placeholder="Email:"/>
        <br><br>
        <button type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-4" @click="recupera">Registro</button>
    </form>

</template>