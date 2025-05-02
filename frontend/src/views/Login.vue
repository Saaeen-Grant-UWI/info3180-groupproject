// src/views/Login.vue
<template>
  <div class="p-4 max-w-md mx-auto">
    <h2 class="text-2xl font-bold mb-4">Login</h2>
    <form @submit.prevent="login">
      <input v-model="form.username" placeholder="Username" class="input" required />
      <input type="password" v-model="form.password" placeholder="Password" class="input" required />
      <button type="submit" class="btn">Login</button>
    </form>
    <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const form = ref({ username: '', password: '' })
const error = ref('')

const login = async () => {
  try {
    const res = await axios.post('/api/auth/login', form.value)
    localStorage.setItem('token', res.data.token)
    router.push('/')
  } catch (err) {
    error.value = err.response?.data?.error || 'Login failed.'
  }
}
</script>

<style scoped>
.input { display: block; margin-bottom: 1rem; padding: 0.5rem; width: 100%; }
.btn { background-color: #3490dc; color: white; padding: 0.5rem 1rem; border-radius: 0.25rem; }
</style>