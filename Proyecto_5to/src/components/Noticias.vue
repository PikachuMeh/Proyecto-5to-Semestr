<script setup>

import { ref } from 'vue';


let correo = localStorage.getItem('correo');
let prueba = ref(correo)

</script>

<template>

    <h1>{{ prueba }}</h1>

</template>