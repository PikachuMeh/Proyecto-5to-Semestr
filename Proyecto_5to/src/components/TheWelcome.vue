<script setup>
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
import { ref } from 'vue'
import {paises,estado,token} from './js/pais.js'



  let password = ref('')
  let email = ref('')
  let nombre = ref('')
  let apellido = ref('')
  let pais =  ref('')
  let state = ref('')


  async function revisar_email(email){
    let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}
 //CONSULTAR PAISES

        
        async function cargarPaises() {
            let tok = await token()
            let paisData = await paises(tok['auth_token']); // Replace with your actual country data
            
            let paisSelect = document.getElementById('paisSelect');
            paisSelect.innerHTML = '';
            paisData.forEach(function(paiss,index) {
              let op = document.createElement("option")
              op.value = paisData[index]['country_name']
              op.id = index
              op.innerText = paisData[index]['country_name']
              paisSelect.appendChild(op)  

            })
            
        }
        
        async function populateEstados() {

            let tok = await token()
            let estadoSelect = document.getElementById('estadoSelect');
            estadoSelect.innerHTML = ''; // Clear existing options
            
            let states = await estado(pais.value,tok['auth_token'])
            states.forEach(function(paiss,index) {
              let op = document.createElement("option");
              op.value = states[index]['state_name']; // Assuming estado has a 'nombre' property
              op.innerText = states[index]['state_name'];
              estadoSelect.appendChild(op);
            });
        }

  async function enviar() {

    let Email = revisar_email(email.value)
    const random = Math.random().toString(36).substring(2,12)
    console.log(random)
    let numero = 3
    if(await Email == true){
    const data = {
      
      "nombre": nombre.value,
      "apellido": apellido.value,
      "correo": email.value,
      "password": password.value,
      "pais": pais.value,
      "estado": state.value,
      "rol": numero,
      "token": random
    }
    console.log(data)
    //SACAR PAISES
    
   
    
    try {

      const response = await fetch(`http://localhost:9000/registro/`, {
        method: "POST", // Specify POST method for sending data
        headers: {
          "Content-Type": "application/json" // Set Content-Type for JSON data
        }, 
          body: JSON.stringify({
          nombre: data.nombre,
          apellido: data.apellido,
          correo: data.correo,
          clave: data.password,
          pais: data.pais,
          estado: data.estado,
          roles_idroles: data.rol,
          token_idtoken: 0,
          recuperacion: data.token,// Include strings in the data object
        })


      });

      console.log(response)

      if (response.ok) {
        
        let respuesta = await response.json()
        alert(respuesta);
        

        if(respuesta == null)
        {
          console.log("si")
          
        }else if(respuesta['falso'] == false){
          alert("Error, Correo ya registrado")
        }
        
      } else {
        console.error("Error sending data:", await response.text());
      }
    } catch (error) {
      console.error("Error:", error);
    }

    }else{
    alert("La tasca mano correo invalido")
    }

}




</script>

<template>
  <h1>Bienvenido, llene la informacion a continuacion para trabajar</h1>
  <form>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Nombre:</template>
    Ingrese su nombre:
    
    <input type="text" v-model = "nombre" name="nombre" id="form2Example1" minlength="2" maxlength="20" class="form-control" required placeholder="Nombre:"/>
    
  
    
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>Apellido</template>

    Ingrese su apellido:
    <input type="text" v-model = "apellido" name="apellido" id="form2Example1" minlength="5"  maxlength="40" class="form-control" required placeholder="Apellido:"/>
    
    <br />
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <EcosystemIcon />
    </template>
    <template #heading>Correo</template>

    Correo:
    <input type="email" v-model = "email" name="email" id="form2Example1" class="form-control" required placeholder="Email:"/>
    
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading>Contraseña</template>

    Contraseña:
    <input type="password" v-model = "password" name="password" id="form2Example1" class="form-control" minlength="8" required placeholder="Contraseña:"/>
    
    
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <EcosystemIcon />
    </template>
    <template #heading>Paises</template>

    Seleccione un Pais:
    <div id = "select_pais">
      <select id="paisSelect" v-model="pais">
        <option  value = "0" disabled>Ingrese una opcion:</option>
      </select>
    </div>
    Seleccione un Estado:
    <div id = "select_estado">
      <select id="estadoSelect"v-model="state">
        <option value = "0" disabled>Ingrese una opcion:</option>
      </select>
    </div>
    <button @click="cargarPaises">Cargar Países</button>
    <button @click="populateEstados">Cargar Estados</button>

      
    </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <SupportIcon />
    </template>
    <template #heading?>Enviar</template>

    <button type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-4" @click="enviar">Registro</button>

  </WelcomeItem>
</form>
</template>./js/token
