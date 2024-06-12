<script setup>
import { ref } from 'vue'
import {RouterLink, RouterView } from 'vue-router'
import router from '../router';
import {revisar_email} from '../js/validaciones.js'



let email = ref('')
let password = ref('')
let opcion = true;
async function enviar() {

let Email = revisar_email(email.value)

if(Email == true){
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
          localStorage.setItem("correo",data.correo);
          router.push({ name: 'perfil' });
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
nav{
  display: contents;
}
 </style>
 
