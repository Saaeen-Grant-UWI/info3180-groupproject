<template>
  <div class="container mt-5">
    <h2 class="mb-4">Register</h2>
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <form @submit.prevent="register">
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input v-model="username" type="text" class="form-control" id="username" required />
      </div>
      <div class="mb-3">
        <label for="name" class="form-label">Full Name</label>
        <input v-model="name" type="text" class="form-control" id="name" required />
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email address</label>
        <input v-model="email" type="email" class="form-control" id="email" required />
      </div>

      <!-- Password with visibility toggle -->
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <div class="input-group">
          <input :type="showPassword ? 'text' : 'password'" v-model="password" class="form-control" id="password" required />
          <button type="button" class="btn btn-outline-secondary" @click="showPassword = !showPassword">
            <i :class="showPassword ? 'bi bi-eye-slash' : 'bi bi-eye'"></i>
          </button>
        </div>
      </div>

      <!-- Confirm Password with visibility toggle -->
      <div class="mb-3">
        <label for="confirmPassword" class="form-label">Confirm Password</label>
        <div class="input-group">
          <input :type="showConfirmPassword ? 'text' : 'password'" v-model="confirmPassword" class="form-control" id="confirmPassword" required />
          <button type="button" class="btn btn-outline-secondary" @click="showConfirmPassword = !showConfirmPassword">
            <i :class="showConfirmPassword ? 'bi bi-eye-slash' : 'bi bi-eye'"></i>
          </button>
        </div>
      </div>

      <button type="submit" class="btn btn-success">Register</button>
    </form>
  </div>
</template>

<script>
import api from '@/services/api'

export default {
  name: 'Register',
  data() {
    return {
      username: '',
      name: '',
      email: '',
      password: '',
      confirmPassword: '',
      photo: '', 
      showPassword: false,
      showConfirmPassword: false,
      error: '',
      success: ''
    }
  },
  methods: {
    async register() {
      this.error = ''
      this.success = ''

      if (this.password !== this.confirmPassword) {
        this.error = "Passwords do not match"
        return
      }

      try {
        const response = await api.post('/register', {
          username: this.username,
          name: this.name,
          email: this.email,
          password: this.password,
          photo: this.photo || ''
        })

        this.success = response.data.message || 'Registration successful!'
        setTimeout(() => {
          this.$router.push('/login')
        }, 1500)
      } catch (err) {
        console.error('Registration error:', err.response || err)
        this.error = err.response?.data?.error || 'Registration failed'
      }
    }
  }
}
</script>

<style>
/* Optional: Use Bootstrap Icons CDN if not already installed */
@import "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css";
</style>
