<script setup>

import { ref } from 'vue'
import {paises,estado,token} from '../js/01.js'
import { revisar_email,validacion_nombre_apellido,clave } from '@/js/validaciones'; 

let valor = localStorage.getItem('recarga');

if(valor != 2){
    location.reload();
}

let password1 = ref('')
let password2 = ref('')
let email = ref('')
let nombre = ref('')
let apellido = ref('')
let pais =  ref('')
let state = ref('')
let cod_ced = ref()
let cedula = ref('')
let nacimiento = ref('')
let descripcion_persona = ref('')
let twitter = ref('')
let Instagram = ref('')
let Facebook = ref('')
let Tik_tok = ref('')

async function agregar_fruta() {
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

let Nombre = validacion_nombre_apellido(nombre.value);
let Apellido = validacion_nombre_apellido(apellido.value);
const random = Math.random().toString(36).substring(2,12)
let numero = 3
cedula.value = cod_ced.value+"-"+cedula.value

if(Email == true && Nombre == true && Apellido == true){
  const data = {
  
    "nombre": nombre.value,
    "apellido": apellido.value,
    "correo": email.value,
    "password": password1.value,
    "pais": pais.value,
    "estado": state.value,
    "rol": numero,
    "nacimiento": nacimiento.value,
    "token": random,
    "cedula": cedula.value,
    "descripcion_persona": descripcion_persona.value,
    "x": twitter.value,
    "instagram": Instagram.value,
    "facebook": Facebook.value,
    "Tik_tok": Tik_tok.value
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
      recuperacion: data.token,
      cedula: data.cedula,
      nacimiento: data.nacimiento,
      desc_per: data.descripcion_persona,
      x : data.x,
      instagram : data.instagram,
      facebook : data.facebook,
      tik_tok : data.Tik_tok// Include strings in the data object
    })


  });

  console.log(response)

  if (response.ok) {
    
    let respuesta = await response.json()
    

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
alert("correo invalido")
}
}
</script>

<template>


  <form>

  
  <div class = "about-form">
    Ingrese su nombre:
    
    <input type="text" v-model = "nombre" name="nombre" id="form2Example1" minlength="2" maxlength="20" class="form-control" required placeholder="Nombre:"/>
  </div>
  <div class = "about-form">
    Ingrese su apellido:
    
    <input type="text" v-model = "apellido" name="apellido" id="form2Example1" minlength="5"  maxlength="40" class="form-control" required placeholder="Apellido:"/>
  </div>
  <div class="about-form">

    Correo:
    <input type="email" v-model = "email" name="email" id="form2Example1" class="form-control" required placeholder="Email:"/>
    
  </div>

  <div class = "about-form">


            <template>Paises</template>
            Seleccione un Pais:
            <div id = "select_pais">
            <select id="paisSelect" v-on:change="populateEstados" v-model="pais">
                <option  value = "0" disabled>Ingrese una opcion:</option>
            </select>
            </div>
  
  </div>
  <div class = "about-form">
            Seleccione un Estado:
            <div id = "select_estado">
            <select id="estadoSelect" v-model="state">
                <option value = "0" disabled>Ingrese una opcion:</option>
            </select>
            </div>
    </div>

  <div class = "about-form">
    <h2 :class="clave(password1,password2) ? 'negative' : 'positive'">
        X
    </h2>
    Contraseña:
    <input type="password" v-model = "password1" name="password" id="form2Example1" class="form-control" minlength="8" required placeholder="Contraseña:"/>
    

    Revisar Contraseña
    <input type="password" v-model = "password2" v-on:change="clave" name="password" id="form2Example1" class="form-control" minlength="8" required placeholder="Contraseña:"/>
  </div>  


  <div class = "about-form">
    Cedula:
    <select v-model="cod_ced" required>
      <option value="V" selected>V</option>
      <option value="J">J</option>
      <option value="E">E</option>
      <option value="I">I</option>
    </select>
    <input type="number" v-model = "cedula" name="cedula" id="form2Example1" class="form-control" minlength="8" required placeholder="Cedula:"/>
  </div>
  <div class ="about-form">
    Fecha de nacimiento:   
    <input type="date" v-model = "nacimiento" name="nacimiento" id="form2Example1" class="form-control" min="1934-06-11" max="2014-12-31" required />
  </div>
  <div class= "about-form">
    <textarea required placeholder="Descripcion de tu persona" name="Descripcion persona" v-model="descripcion_persona" id="desc_per" cols="30" rows="10"></textarea>
  </div>
  <div class="about-form">
    <input type="text" v-model = "twitter" name="twitter" id="form2Example1" class="form-control" placeholder="X:"  />
    <input type="text" v-model = "Instagram" name="instagram" id="form2Example1" class="form-control" placeholder="Instagram:"  />
    <input type="text" v-model = "Facebook" name="Facebook" id="form2Example1" class="form-control" placeholder="Facebook:"  />
    <input type="text" v-model = "Tik_tok" name="Tik_tok" id="form2Example1" class="form-control" placeholder="Tik tok:" required />

  </div>
  <div class = "about-form">
    <button type="button" v-on:click="agregar_fruta">Cargar Países</button>
    <button type="button" v-on:click="enviar">Registro</button>
  </div>
  </form>

  
</template>

<style>
@media (min-width: 1024px) {
  .about {
    max-height: 3vh;
    display: flex;
    align-items: center;
  }
}
.about-form{
  max-height: 4vh;
}
.negative {
    color: red;
}

.positive {
    color: green;
}
</style>