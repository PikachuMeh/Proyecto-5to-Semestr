<script setup>
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
import { ref } from 'vue'

  var password = ref('')
  var email = ref('')
  var nombre = ref('')
  var apellido = ref('')
  
  async function revisar_email(email){
    var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}
  async function enviar() {

    let Email = revisar_email(email.value)

    if(await Email == true){
    const data = {
      
      "nombre": nombre.value,
      "apellido": apellido.value,
      "correo": email.value,
      "password": password.value
    }
    //CONSULTAR PAISES, me da paja meterlo en un js distinto asi que aja 
    try {
    const pais_token = await fetch('https://www.universal-tutorial.com/api/getaccesstoken', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'api-token': 'AuXnFjES43NqbdODZoc1anLtpO9op_9HsA7hqU56HJoxlbbNrMsUAzmsp6cqoZ0HhWQ',
        'user-email': 'abc@gmail.com'
      }
    });

    if (!pais_token.ok) {
      throw new Error(`HTTP error! status: ${pais_token.status}`);
    }else{
      const token = await pais_token.json()
      try {
        const pais = await fetch('https://www.universal-tutorial.com/api/countries/', {
          method: 'GET',
          headers: {
            "Authorization": token['auth_token'],
            "Accept": "application/json"
          }
        });

        if (!pais.ok) {
          throw new Error(`HTTP error! status: ${pais.status}`);
        }
      } catch (error) {
        console.error('Error fetching access token:', error);
        // Handle errors appropriately in your application
      }
    }
    
  } catch (error) {
    console.error('Error fetching access token:', error);
    // Handle errors appropriately in your application
  }
    //SACAR PAISES
    
    

    try {

      const response = await fetch(`http://localhost:8080/registro/`, {
        method: "POST", // Specify POST method for sending data
        headers: {
          "Content-Type": "application/json" // Set Content-Type for JSON data
        },
          body: JSON.stringify({
          nombre: data.nombre,
          apellido: data.apellido,
          correo: data.correo,
          password: data.password// Include strings in the data object
        
        })


      });

      console.log(response)

      if (response.ok) {
        let respuesta = await response.json()
        
        if(respuesta == null)
        {
          console.log("ola piter")
          
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
    
    <input type="text" v-model = "nombre" name="nombre" id="form2Example1" minlength="8" class="form-control" required placeholder="Nombre:"/>
    
  
    
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>Apellido</template>

    Ingrese su apellido:
    <input type="text" v-model = "apellido" name="apellido" id="form2Example1" minlength="8" class="form-control" required placeholder="Apellido:"/>
    
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
    <template #default?>Paises</template>

      Pais:
      <input type="Text" v-model = "pais" name="pais" id="form2Example1" class="form-control"  required placeholder="Pais:"/> 
  
  
    </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <SupportIcon />
    </template>
    <template #heading?>Enviar</template>

    <button type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-4" @click="enviar">Registro</button>
  </WelcomeItem>
</form>
</template>
