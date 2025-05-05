<template>
  <div class="container mt-4">
    <h2>My Favourite Profiles</h2>

    <div v-if="favourites.length === 0" class="alert alert-info">
      You have not added any favourites yet.
    </div>

    <div class="row row-cols-1 row-cols-md-2 g-4" v-else>
      <div v-for="fav in favourites" :key="fav.id" class="col">
        <div class="card shadow h-100">
          <div class="card-body">
            <h5 class="card-title">{{ fav.name }}</h5>
            <p class="card-text">{{ fav.description }}</p>
            <ul class="list-group list-group-flush">
              <li class="list-group-item"><strong>Birth Year:</strong> {{ fav.birth_year }}</li>
              <li class="list-group-item"><strong>Sex:</strong> {{ fav.sex }}</li>
              <li class="list-group-item"><strong>Race:</strong> {{ fav.race }}</li>
              <li class="list-group-item"><strong>Height:</strong> {{ fav.height }} inches</li>
              <li class="list-group-item"><strong>Parish:</strong> {{ fav.parish }}</li>
            </ul>
            <router-link
              :to="{ name: 'ProfileDetails', params: { profile_id: fav.id } }"
              class="btn btn-primary mt-3"
            >
              View Full Profile
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'FavouritesReport',
  data() {
    return {
      favourites: []
    }
  },
  methods: {
    fetchFavourites() {
      axios.get('/api/favourites', {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      })
      .then(response => {
        this.favourites = response.data.favourites;
      })
      .catch(err => {
        console.error(err);
        alert('Failed to load favourites.');
      });
    }
  },
  mounted() {
    this.fetchFavourites();
  }
}
</script>
