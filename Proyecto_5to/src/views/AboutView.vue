<script setup lang="ts">
import { ref } from 'vue'

const message = ref('')
async function say() {

  const query = await fetch("http://localhost:8080/otro")

  console.log("ola")
  if (query.ok)
    console.log(await query.json())

}

</script>

<template>
  <div class="moviestar">
    <input name = "ola" v-model= "message" placeholder="editme"/>

    <button id="generar" @click="say">Click to fetch</button>
</div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
