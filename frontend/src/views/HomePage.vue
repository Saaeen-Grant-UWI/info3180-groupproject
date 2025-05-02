// src/views/HomePage.vue
<template>
  <div>
    <h1>Home</h1>
    <div v-if="profiles.length">
      <h2>Latest Profiles</h2>
      <div v-for="profile in profiles" :key="profile.id">
        <p>{{ profile.name }} ({{ profile.birth_year }})</p>
        <router-link :to="`/profiles/${profile.id}`">View More Details</router-link>
      </div>
    </div>
    <div>
      <h2>Search Profiles</h2>
      <input v-model="search.name" placeholder="Name" />
      <input v-model="search.birth_year" placeholder="Birth Year" />
      <input v-model="search.sex" placeholder="Sex" />
      <input v-model="search.race" placeholder="Race" />
      <button @click="searchProfiles">Search</button>
      <div v-if="results.length">
        <h3>Search Results</h3>
        <div v-for="result in results" :key="result.id">
          <p>{{ result.name }}</p>
          <router-link :to="`/profiles/${result.id}`">View</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'HomePage',
  data() {
    return {
      profiles: [],
      search: { name: '', birth_year: '', sex: '', race: '' },
      results: []
    };
  },
  async mounted() {
    const res = await api.get('/profiles');
    this.profiles = res.data.profiles;
  },
  methods: {
    async searchProfiles() {
      const params = new URLSearchParams(this.search).toString();
      const res = await api.get(`/search?${params}`);
      this.results = res.data.results;
    }
  }
};
</script>