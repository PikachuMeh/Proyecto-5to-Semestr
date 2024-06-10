<script setup lang="ts">
import { ref } from 'vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle'
import router from '../router';

const password = ref('') 
const email = ref('')


async function enviar() {

  let Email = revisar_email(email.value)

  if(await Email == true){
  const data = {
    "correo": email.value,
    "password": password.value
  }

  

  try {

    const response = await fetch(`http://localhost:9000/login/`, {
      method: "POST", // Specify POST method for sending data
      headers: {
        "Content-Type": "application/json" // Set Content-Type for JSON data
      },
        body: JSON.stringify({
        correo: data.correo,
        password: data.password// Include strings in the data object
       
      })


    });

    let respuesta = await response.json()
    if (response.ok) {

        if( respuesta["Falso"] == false){
          alert("error, correo o contraseña invalida")
        }else{
          router.push({ name: 'perfil' });
          console.log("Data sent successfully:", respuesta);
        }
    } else{
      alert("Error sending data:", respuesta);

    }
  } catch (error) {
    console.log("Error:", error);
  }
  
}else{
  alert("La tasca mano correo invalido")
}
}

async function revisar_email(email){
    var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

</script>
<!-- Prueba
  
  <div class="moviestar">
    <input type="text" name="ola" v-model="message" placeholder="editme" />
    <input type="number" name="item_id" v-model="itemId" placeholder="Item ID" />
    <button id="generar" @click="say">Click to fetch</button>
  </div>
-->
<template>
 <!-- FORMULARIO -->
  <form class = "si">
  <!-- Email input -->
  <div data-mdb-input-init class="form-outline mb-4">

    <input type="email" v-model = "email" name="email" id="form2Example1" class="form-control" required/>
    <label class="form-label" for="form2Example1">Email address</label>
  
  </div>

  <!-- Password input -->
  <div data-mdb-input-init class="form-outline mb-4">
    <input type="password" v-model = "password" id="form2Example2" required class="form-control" />
    <label class="form-label" for="form2Example2">Password</label>
  </div>

  <!-- 2 column grid layout for inline styling -->
  <div class="row mb-4">
    <div class="col d-flex justify-content-center">
      <!-- Checkbox -->

    </div>

    <div class="col">
      <!-- Simple link -->
  


    </div>
  </div>

  <!-- Submit button -->
  <button type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-4" @click="enviar">Inicia sesion</button>
  <!-- Register buttons -->
</form>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

