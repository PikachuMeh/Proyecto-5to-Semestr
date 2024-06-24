<script setup>

import { ref } from 'vue';
import router from '../router';
import { RouterLink, RouterView } from 'vue-router'


let sesionS = localStorage.getItem('opcion');
let sesion = JSON.parse(sesionS)


async function login() {
    localStorage.setItem('token',false)
}


console.log(sesion) 

</script>
<template>

<h2 v-if="!sesion">Bienvenido a tu homepage</h2>
<nav v-if="!sesion">
    <RouterLink to="/Perfil">Perfil</RouterLink>
</nav>
<nav v-if="!sesion">
    <RouterLink to="/Inicio" @click="login">Salir</RouterLink>
</nav>

</template>