<script setup>
import { ref } from 'vue';
import router from '../router';


let item = ref(''),
    sesion; // Define item within setup

const salir = () => {
    localStorage.setItem('token',false);
    router.push({ name: 'inicio' });

};

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