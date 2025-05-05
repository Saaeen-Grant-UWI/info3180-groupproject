<template>
  <div>
    <NavBar />
    <router-view />
  </div>
</template>

<script>
import { provide, reactive } from 'vue'
import NavBar from './components/NavBar.vue'

export default {
  name: 'App',
  components: { NavBar },
  setup() {
    const authState = reactive({
      isAuthenticated: !!localStorage.getItem('token'),
      userId: null,
      username: ''
    })

    if (authState.isAuthenticated) {
      const token = localStorage.getItem('token')
      const decoded = jwtDecode(token)
      authState.userId = decoded.user_id
      authState.username = decoded.username
    }

    provide('authState', authState)

    return { authState }
  }
}
</script>
