<template>
  <div class="container mt-4">
    <h2>Welcome to JamDate</h2>

    <div class="card my-4">
      <div class="card-body">
        <form @submit.prevent="searchProfiles">
          <div class="row g-2">
            <div class="col-md">
              <input v-model="search.name" type="text" class="form-control" placeholder="Search by Name" />
            </div>
            <div class="col-md">
              <input v-model="search.birth_year" type="number" class="form-control" placeholder="Birth Year" />
            </div>
            <div class="col-md">
              <select v-model="search.sex" class="form-select">
                <option value="">Sex</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>
            <div class="col-md">
              <input v-model="search.race" type="text" class="form-control" placeholder="Race" />
            </div>
            <div class="col-md-auto">
              <button type="submit" class="btn btn-primary">Search</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <div v-if="loading" class="text-center text-muted">Loading profiles...</div>

    <div v-else-if="Array.isArray(profiles) && profiles.length === 0" class="text-muted">
      No profiles found. Try adjusting your search filters.
    </div>

    <div v-else class="row row-cols-1 row-cols-md-2 g-4">
      <div v-for="profile in profiles" :key="profile.id" class="col">
        <div class="card h-100 shadow">
          <div class="card-body">
            <h5 class="card-title">{{ profile.name }}</h5>
            <p class="card-text">{{ profile.description }}</p>
            <p class="mb-1"><strong>Parish:</strong> {{ profile.parish }}</p>
            <p class="mb-1"><strong>Sex:</strong> {{ profile.sex }}</p>
            <p class="mb-1"><strong>Race:</strong> {{ profile.race }}</p>
            <router-link
              v-if="profile.id"
              :to="{ name: 'ProfileDetails', params: { profile_id: profile.id } }"
              class="btn btn-outline-primary me-2"
            >
              View Details
            </router-link>
            <button
              v-if="profile.user_id"
              class="btn btn-outline-danger"
              @click="addToFavourites(profile.user_id)"
            >
              ❤️
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomePage',
  data() {
    return {
      profiles: null,
      loading: false,
      search: {
        name: '',
        birth_year: '',
        sex: '',
        race: ''
      }
    }
  },
  methods: {
    fetchProfiles() {
      this.loading = true;
      axios.get('/api/profiles', {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      })
      .then(response => {
        console.log('Fetched profiles:', response.data);
        this.profiles = response.data.profiles || [];
      })
      .catch(error => {
        console.error('Error fetching profiles:', error);
        this.profiles = [];
      })
      .finally(() => {
        this.loading = false;
      });
    },
    searchProfiles() {
      this.loading = true;
      const params = new URLSearchParams(this.search).toString();
      axios.get(`/api/search?${params}`, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      })
      .then(response => {
        console.log('Search results:', response.data);
        this.profiles = response.data.results || [];
      })
      .catch(error => {
        console.error('Search error:', error);
        this.profiles = [];
      })
      .finally(() => {
        this.loading = false;
      });
    },
    addToFavourites(userId) {
      if (!userId) {
        alert('Invalid user ID.');
        return;
      }

      axios.post(`/api/profiles/${userId}/favourite`, {}, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      })
      .then(() => {
        alert('Profile added to favourites!');
      })
      .catch(err => {
        alert(err.response?.data?.message || 'Error adding to favourites.');
      });
    }
  },
  mounted() {
    this.fetchProfiles();
  }
}
</script>
