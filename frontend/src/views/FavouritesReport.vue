// src/views/FavouritesReport.vue
<template>
  <div>
    <h1>Top Favourited Users</h1>
    <ul>
      <li v-for="user in topFavourites" :key="user.id">{{ user.username }}</li>
    </ul>
  </div>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'FavouritesReport',
  data() {
    return { topFavourites: [] };
  },
  async mounted() {
    const res = await api.get('/users/favourites/5');
    this.topFavourites = res.data.top_favourites;
  }
};
</script>