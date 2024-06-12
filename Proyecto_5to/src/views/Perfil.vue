<script>

import { ref } from 'vue';
import router from '../router';

let sesion = localStorage.getItem('correo');

let item = ref(sesion || '');

const salir = () =>{
    router.push({ name: 'inicio' });
}


</script>

<template>


    <h1>{{ item }}</h1>
    <button id="salir" v-on:click="salir">Salir</button>

</template>
<style>
nav{
    display: none; 
}
#salir{
    margin-left: 90%;
    width: 50px;
    height: auto;

}
</style>