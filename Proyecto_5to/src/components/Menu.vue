<script setup>
    import { RouterLink, RouterView } from 'vue-router'
    async function login() {
    localStorage.setItem('recarga',1);
    localStorage.setItem('token',false)
}


</script>

<template>

    <RouterLink to="/Perfil">Perfil</RouterLink>
    <RouterLink to="/About">Acerca de nosotros</RouterLink>
    
    <RouterLink to="/Noticias">Noticias</RouterLink>
    
    <RouterLink to="/Contactanos"></RouterLink>
    <RouterLink to="/Inicio" @click="login">Salir</RouterLink>
    
</template>