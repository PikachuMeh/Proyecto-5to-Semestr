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
    console.log("Data sent successfully:", await response.json());
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
  <form>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Bienvenido, llene la informacion a continuacion para trabajar</template>
    Ingrese su nombre:
    
    <input type="text" v-model = "nombre" name="nombre" id="form2Example1" class="form-control" required placeholder="Nombre:"/>
    
  
    
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>Apellido</template>

    Ingrese su apellido:
    <input type="text" v-model = "apellido" name="apellido" id="form2Example1" class="form-control" required placeholder="Apellido:"/>
    
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
    <input type="password" v-model = "password" name="password" id="form2Example1" class="form-control" required placeholder="Contraseña:"/>
    
    
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <SupportIcon />
    </template>
    <template #heading>Enviar</template>

    <button type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-4" @click="enviar">Registro</button>
  </WelcomeItem>
</form>
</template>
