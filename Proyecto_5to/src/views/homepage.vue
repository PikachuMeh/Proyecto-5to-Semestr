<script setup>

import { ref } from 'vue';
import router from '../router';
import { RouterLink, RouterView } from 'vue-router'


let sesionS = localStorage.getItem('token');
let sesion = JSON.parse(sesionS);
let valor = localStorage.getItem('recarga');

if(valor != 2){
    localStorage.setItem('recarga',2);
    location.reload();
}

async function login() {
    localStorage.setItem('recarga',1);
    localStorage.setItem('token',false)
}



</script>
<template>

<h2 v-if="sesion">Bienvenido a tu homepage</h2>
<nav v-if="sesion">
    <RouterLink to="/Perfil">Perfil</RouterLink>
    <RouterLink to="/About">Acerca de nosotros</RouterLink>
    <RouterLink to="/Noticias">Noticias</RouterLink>
    <RouterLink to="/Contactanos"></RouterLink>
    <RouterLink to="/Inicio" @click="login">Salir</RouterLink>
    
</nav>

</template>