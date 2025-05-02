// src/views/Logout.vue
<template>
  <div>Logging out...</div>
</template>

<script>
import api from '@/services/api';

export default {
  async mounted() {
    await api.post('/auth/logout');
    localStorage.removeItem('token');
    this.$router.push('/login');
  }
};
</script>
