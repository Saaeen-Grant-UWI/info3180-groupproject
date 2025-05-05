<template>
  <div class="container mt-4">
    <div v-if="profile" class="card">
      <div class="card-body">
        <h3 class="card-title">{{ profile.name }}</h3>
        <p class="card-text">{{ profile.description }}</p>
        <p><strong>Parish:</strong> {{ profile.parish }}</p>
        <p><strong>Sex:</strong> {{ profile.sex }}</p>
        <p><strong>Race:</strong> {{ profile.race }}</p>
        <p><strong>Birth Year:</strong> {{ profile.birth_year }}</p>
        <p><strong>Height:</strong> {{ profile.height }} inches</p>
        <p><strong>Favourite Cuisine:</strong> {{ profile.fav_cuisine }}</p>
        <p><strong>Favourite Colour:</strong> {{ profile.fav_colour }}</p>
        <p><strong>Favourite School Subject:</strong> {{ profile.fav_school_subject }}</p>
        <p><strong>Political:</strong> {{ profile.political ? 'Yes' : 'No' }}</p>
        <p><strong>Religious:</strong> {{ profile.religious ? 'Yes' : 'No' }}</p>
        <p><strong>Family Oriented:</strong> {{ profile.family_oriented ? 'Yes' : 'No' }}</p>

        <div class="mt-3">
          <button class="btn btn-outline-primary" @click="addToFavourites(profile.user_id)">
            ❤️ Add to Favourites
          </button>
          <button class="btn btn-outline-secondary ms-2" @click="getMatchingProfiles">
            Match Me
          </button>
        </div>
        
        <div v-if="matches.length > 0" class="mt-4">
          <h4>Matching Profiles</h4>
          <div class="row row-cols-1 row-cols-md-2 g-4">
            <div v-for="match in matches" :key="match.id" class="col">
              <div class="card h-100 shadow">
                <div class="card-body">
                  <h5 class="card-title">{{ match.name }}</h5>
                  <p class="card-text">{{ match.description }}</p>
                  <p><strong>Sex:</strong> {{ match.sex }}</p>
                  <p><strong>Race:</strong> {{ match.race }}</p>
                  <router-link :to="{ name: 'ProfileDetails', params: { profile_id: match.id } }" class="btn btn-outline-primary me-2">
                    View Details
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProfileDetails',
  data() {
    return {
      profile: null,
      matches: []
    };
  },
  methods: {
    fetchProfile() {
      const profileId = this.$route.params.profile_id;
      axios.get(`/api/profiles/${profileId}`, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      })
      .then(response => {
        this.profile = response.data.profile;
      })
      .catch(error => {
        console.error(error);
      });
    },
    addToFavourites(userId) {
      axios.post(`/api/profiles/${userId}/favourite`, {}, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      })
      .then(() => {
        alert('Profile added to favourites!');
      })
      .catch(err => {
        alert(err.response?.data?.message || 'Error adding to favourites.');
      });
    },
    getMatchingProfiles() {
      const profileId = this.$route.params.profile_id;
      axios.get(`/api/profiles/matches/${profileId}`, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      })
      .then(response => {
        this.matches = response.data.matches;
      })
      .catch(error => {
        console.error(error);
      });
    }
  },
  mounted() {
    this.fetchProfile();
  }
};
</script>
