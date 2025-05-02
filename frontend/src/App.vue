
<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<script setup>
import NavBar from './components/NavBar.vue'

defineExpose({
  name: 'App',
  components: {
    NavBar
  }
});
</script>

