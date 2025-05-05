<template>
  <div class="container mt-4">
    <h2>My Profiles</h2>

    <div v-if="profiles.length === 0" class="text-muted">You have no profiles yet.</div>

    <div class="row row-cols-1 row-cols-md-2 g-4">
      <div v-for="profile in profiles" :key="profile.id" class="col">
        <div class="card shadow h-100">
          <div class="card-body">
            <h5 class="card-title">{{ profile.name }}</h5>
            <p class="card-text">{{ profile.description }}</p>
            <p><strong>Birth Year:</strong> {{ profile.birth_year }}</p>
            <p><strong>Sex:</strong> {{ profile.sex }}</p>
            <p><strong>Race:</strong> {{ profile.race }}</p>
            <p><strong>Height:</strong> {{ profile.height }} inches</p>
            <p><strong>Parish:</strong> {{ profile.parish }}</p>

            <p><strong>Favourites:</strong></p>
            <ul v-if="profile.favourites && profile.favourites.length">
              <li v-for="fav in profile.favourites" :key="fav.id">
                {{ fav.name }} ({{ fav.sex }}, {{ fav.race }})
              </li>
            </ul>
            <p v-else class="text-muted">No favourites for this profile.</p>

            <button class="btn btn-outline-success mt-2" @click="matchMe(profile.id)">Match Me</button>

            <div v-if="matches[profile.id]" class="mt-3">
              <h6>Matches:</h6>
              <ul>
                <li v-for="match in matches[profile.id]" :key="match.id">
                  {{ match.name }} ({{ match.sex }}, {{ match.race }}, Age: {{ getAge(match.birth_year) }})
                </li>
              </ul>
            </div>

          </div>
        </div>
      </div>
    </div>

    <router-link to="/profiles/new" class="btn btn-primary">
      <i class="bi bi-plus-lg"></i> Create New Profile
    </router-link>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserProfile',
  data() {
    return {
      profiles: [],
      matches: {}
    }
  },
  methods: {
    fetchUserProfiles() {
      axios.get('/api/user/profiles', {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      })
      .then(res => {
        this.profiles = res.data.profiles || []; // fallback to empty array
      })
      .catch(err => {
        console.error(err);
        this.profiles = []; // ensure it's at least an empty array
        alert('Failed to load profiles.');
      });
    },
    matchMe(profileId) {
      axios.get(`/api/profiles/${profileId}/match`, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      })
      .then(res => {
        this.$set(this.matches, profileId, res.data.matches);
      })
      .catch(err => {
        console.error(err);
        alert('Failed to get matches.');
      });
    },
    getAge(birthYear) {
      const currentYear = new Date().getFullYear();
      return currentYear - birthYear;
    }
  },
  mounted() {
    this.fetchUserProfiles();
  }
}
</script>
