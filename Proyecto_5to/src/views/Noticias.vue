<script setup>

import { ref } from 'vue';
import Menu from '../components/Menu.vue'

import Visualizacion from '../components/Noticias/visualizacion.vue'
import data from '../js/visualizacion.js'



let correo = localStorage.getItem('correo');

let jsonCorreo = JSON.stringify(correo)
let dato ={}
if (typeof correo === 'string') {
    console.log(correo)
    dato = { correo: correo };

}
let correo_api = await data(dato)
console.log(correo_api)
let prueba = ref(correo)

</script>

<template>
    <Menu/>

    <h1>{{ prueba }}</h1>

    <Visualizacion/>

</template>