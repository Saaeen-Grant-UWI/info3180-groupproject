<template>
  <div class="container mt-5 text-center">
    <h4>You have been logged out.</h4>
    <router-link to="/login" class="btn btn-secondary mt-3">Go to Login</router-link>
  </div>
</template>

<script>
export default {
  created() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');

    this.$router.replace('/login');
  }
};
</script>
