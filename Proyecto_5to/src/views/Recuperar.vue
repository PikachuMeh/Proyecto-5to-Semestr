<script setup>
import {revisar_email} from '../js/validaciones.js'
import { ref } from 'vue'
let email = ref('')


async function enviar(){
    let Email = revisar_email(email.value)

    if(Email == true){
  const data = {
    "correo": email.value
  }



  try {

    const response = await fetch(`http://localhost:9000/recuperacion/`, {
      method: "POST", // Specify POST method for sending data
      headers: {
        "Content-Type": "application/json" // Set Content-Type for JSON data
      },
        body: JSON.stringify({
        correo: data.correo,// Include strings in the data object
      
      })


    });

    let respuesta = await response.json()
    if (response.ok) {

        if( respuesta["Falso"] == false){
          alert("error, correo o contraseña invalida")
        }else{
          console.log("Data sent successfully:", respuesta);
        }
    } else{
      alert("Error sending data: error" + respuesta);

    }
  } catch (error) {
    console.log("Error:", error);
  }

  }else{
  alert("Correo invalido")
  }
}
</script>
<template> 
    <form>
        
        <div data-mdb-input-init class="form-outline mb-4">
            Recuperacion de contraseña
            <br>
        <input type="email" v-model = "email" name="email" id="form2Example1" class="form-control" placeholder="Correo:" required/>
        <label class="form-label" for="form2Example1">Email address</label>

        </div>
        <button type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-4" v-on:click= "enviar">Inicia sesion</button>
    </form>
</template>