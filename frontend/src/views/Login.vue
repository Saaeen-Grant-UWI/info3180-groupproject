<template>
  <div class="container mt-5">
    <h2 class="mb-4">Login</h2>
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input v-model="username" type="text" class="form-control" id="username" required />
      </div>

      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <div class="input-group">
          <input :type="showPassword ? 'text' : 'password'" v-model="password" class="form-control" id="password" required />
          <button type="button" class="btn btn-outline-secondary" @click="showPassword = !showPassword">
            <i :class="showPassword ? 'bi bi-eye-slash' : 'bi bi-eye'"></i>
          </button>
        </div>
      </div>

      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script>
import { inject } from 'vue'
import { jwtDecode } from 'jwt-decode'
import api from '@/services/api'

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      showPassword: false,
      error: ''
    }
  },
  setup() {
    const authState = inject('authState')
    return { authState }
  },
  methods: {
    async login() {
      try {
        const response = await api.post('/auth/login', {
          username: this.username,
          password: this.password
        })

        const { token } = response.data
        const decoded = jwtDecode(token)

        // Update the provided authState
        localStorage.setItem('token', token)
        localStorage.setItem('user', JSON.stringify({
          id: decoded.user_id,
          username: decoded.username
        }))
        
        this.authState.isAuthenticated = true
        this.authState.userId = decoded.user_id
        this.authState.username = decoded.username

        this.$router.push('/')
      } catch (err) {
        this.error = err.response?.data?.error || 'Login failed'
      }
    }
  }
}
</script>

<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css";
</style>
