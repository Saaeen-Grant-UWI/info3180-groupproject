// src/views/Register.vue
<template>
  <div class="p-4 max-w-md mx-auto">
    <h2 class="text-2xl font-bold mb-4">Register</h2>
    <form @submit.prevent="register">
      <input v-model="form.username" placeholder="Username" class="input" required />
      <input v-model="form.email" type="email" placeholder="Email" class="input" required />
      <input v-model="form.name" placeholder="Full Name" class="input" required />
      <input v-model="form.photo" placeholder="Photo URL" class="input" />
      <input v-model="form.password" type="password" placeholder="Password" class="input" required />
      <button type="submit" class="btn">Register</button>
    </form>
    <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const form = ref({ username: '', email: '', name: '', photo: '', password: '' })
const error = ref('')

const register = async () => {
  try {
    await axios.post('/api/register', form.value)
    router.push('/login')
  } catch (err) {
    error.value = err.response?.data?.error || 'Registration failed.'
  }
}
</script>

<style scoped>
.input { display: block; margin-bottom: 1rem; padding: 0.5rem; width: 100%; }
.btn { background-color: #38c172; color: white; padding: 0.5rem 1rem; border-radius: 0.25rem; }
</style>