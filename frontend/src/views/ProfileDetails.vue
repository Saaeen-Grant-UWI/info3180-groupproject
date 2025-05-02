// src/views/ProfileDetails.vue
<template>
  <div>
    <h1>Profile Details</h1>
    <div v-if="profile">
      <p>Name: {{ profile.name }}</p>
      <p>Birth Year: {{ profile.birth_year }}</p>
      <p>Sex: {{ profile.sex }}</p>
      <p>Race: {{ profile.race }}</p>
      <p>Height: {{ profile.height }}</p>
      <p>Favourite Colour: {{ profile.fav_colour }}</p>
      <button @click="addToFavourites">❤️ Favourite</button>
      <button>Email Profile</button>
      <button @click="matchProfile">Match Me</button>
      <div v-if="matches.length">
        <h2>Matches</h2>
        <ul>
          <li v-for="m in matches" :key="m.id">{{ m.name }} ({{ m.birth_year }})</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'ProfileDetails',
  props: ['profile_id'],
  data() {
    return { profile: null, matches: [] };
  },
  async mounted() {
    const res = await api.get(`/profiles/${this.profile_id}`);
    this.profile = res.data.profile;
  },
  methods: {
    async addToFavourites() {
      await api.post(`/profiles/${this.profile.user_id}/favourite`);
      alert('Added to favourites');
    },
    async matchProfile() {
      const res = await api.get(`/profiles/matches/${this.profile.id}`);
      this.matches = res.data.matches;
    }
  }
};
</script>
