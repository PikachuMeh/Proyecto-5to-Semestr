<script setup>
import { ref } from 'vue';
import router from '../router';

localStorage.setItem('recarga',1);
let item = ref(''),
    sesion; // Define item within setup
    let valor = localStorage.getItem('recarga');
if(valor != 2){
    localStorage.setItem('recarga',2);
    location.reload();
}

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