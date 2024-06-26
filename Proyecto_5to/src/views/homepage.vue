<script setup>

import { ref } from 'vue';
import router from '../router';
import { RouterLink, RouterView } from 'vue-router'
import Noticias from '../components/Noticias.vue';
import Menu from '../components/Menu.vue'

let sesionS = localStorage.getItem('token');
let sesion = JSON.parse(sesionS);
let valor = localStorage.getItem('recarga');

if(valor != 2){
    localStorage.setItem('recarga',2);
    location.reload();
}



</script>
<template>

<h2 v-if="sesion">Bienvenido a tu homepage</h2>

<nav v-if="sesion">
    
    <Menu/>

</nav>

</template>