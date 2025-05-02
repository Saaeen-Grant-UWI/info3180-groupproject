<template>
    <div class="p-6 max-w-3xl mx-auto">
      <h1 class="text-2xl font-bold mb-4">My Profile</h1>
      <div v-if="user" class="bg-white p-4 rounded shadow">
        <p><strong>Username:</strong> {{ user.username }}</p>
        <p><strong>Name:</strong> {{ user.name }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
      </div>
  
      <h2 class="text-xl font-semibold mt-6 mb-2">My Favourites</h2>
      <div v-if="favourites.length > 0" class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div
          v-for="fav in favourites"
          :key="fav.id"
          class="border p-4 rounded bg-gray-50"
        >
          <p><strong>Username:</strong> {{ fav.username }}</p>
          <router-link :to="{ name: 'UserProfile', params: { user_id: fav.id } }" class="text-blue-600 hover:underline">
            View Profile
          </router-link>
        </div>
      </div>
      <div v-else>
        <p>You haven't favourited anyone yet.</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'UserProfile',
    props: ['user_id'],
    data() {
      return {
        user: null,
        favourites: [],
      }
    },
    async created() {
      const token = localStorage.getItem('token')
      if (!token) {
        this.$router.push('/login')
        return
      }
  
      try {
        const headers = { Authorization: `Bearer ${token}` }
  
        const [userRes, favsRes] = await Promise.all([
          axios.get(`/api/users/${this.user_id}`, { headers }),
          axios.get(`/api/users/${this.user_id}/favourites`, { headers }),
        ])
  
        this.user = userRes.data.user
        this.favourites = favsRes.data.favourites
      } catch (err) {
        console.error(err)
        if (err.response && err.response.status === 401) {
          this.$router.push('/login')
        }
      }
    },
  }
  </script>
  
  <style scoped>
  p {
    margin-bottom: 0.5rem;
  }
  </style>
  