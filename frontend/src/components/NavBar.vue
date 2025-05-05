<template>
  <nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand">Navbar</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" v-if="authState.isAuthenticated" :to="'/users/' + authState.userId">My Profile</router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Reports</a>
          </li>
        </ul>
        <div class="d-flex">
          <router-link v-if="!authState.isAuthenticated" class="btn btn-link" style="text-decoration: none;" to="/login">Login</router-link>
          <router-link v-if="authState.isAuthenticated" class="btn btn-link" style="text-decoration: none;" to="/logout">Logout</router-link>
          <router-link v-if="!authState.isAuthenticated" class="btn btn-warning" to="/register">Register</router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { inject } from 'vue'

export default {
  name: 'NavBar',
  setup() {
    const authState = inject('authState')
    return { authState }
  }
}
</script>
