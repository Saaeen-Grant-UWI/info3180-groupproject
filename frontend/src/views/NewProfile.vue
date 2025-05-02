// src/views/NewProfile.vue
<template>
  <div>
    <h1>Add New Profile</h1>
    <form @submit.prevent="submitProfile">
      <input v-model="form.name" placeholder="Name" required />
      <input v-model="form.birth_year" placeholder="Birth Year" required type="number" />
      <input v-model="form.sex" placeholder="Sex" required />
      <input v-model="form.race" placeholder="Race" required />
      <input v-model="form.height" placeholder="Height" required type="number" />
      <input v-model="form.fav_colour" placeholder="Favourite Colour" />
      <input v-model="form.fav_cuisine" placeholder="Favourite Cuisine" />
      <input v-model="form.fav_school_subject" placeholder="School Subject" />
      <input v-model="form.political" placeholder="Political View" />
      <input v-model="form.religious" placeholder="Religious View" />
      <input v-model="form.family_oriented" placeholder="Family Oriented" />
      <button type="submit">Add Profile</button>
    </form>
  </div>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'NewProfile',
  data() {
    return {
      form: {
        name: '', birth_year: '', sex: '', race: '', height: '', fav_colour: '', fav_cuisine: '',
        fav_school_subject: '', political: '', religious: '', family_oriented: ''
      }
    };
  },
  methods: {
    async submitProfile() {
      await api.post('/profiles', this.form);
      alert('Profile added');
      this.$router.push('/');
    }
  }
};
</script>