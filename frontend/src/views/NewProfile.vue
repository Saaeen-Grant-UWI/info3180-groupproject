  <template>
    <div class="container mt-4">
      <h2>Create New Profile</h2>

      <form @submit.prevent="createProfile" class="card p-4 shadow">
        <div class="mb-3">
          <label class="form-label">Name</label>
          <input v-model="form.name" type="text" class="form-control" required />
        </div>

        <div class="mb-3">
          <label class="form-label">Description</label>
          <textarea v-model="form.description" class="form-control" rows="3" required></textarea>
        </div>

        <div class="mb-3">
          <label class="form-label">Parish</label>
          <input v-model="form.parish" type="text" class="form-control" required />
        </div>

        <div class="row">
          <div class="col-md-4 mb-3">
            <label class="form-label">Birth Year</label>
            <input v-model="form.birth_year" type="number" class="form-control" required />
          </div>

          <div class="col-md-4 mb-3">
            <label class="form-label">Sex</label>
            <select v-model="form.sex" class="form-select" required>
              <option disabled value="">Select sex</option>
              <option>Male</option>
              <option>Female</option>
            </select>
          </div>

          <div class="col-md-4 mb-3">
            <label class="form-label">Race</label>
            <input v-model="form.race" type="text" class="form-control" required />
          </div>
        </div>

        <div class="row">
          <div class="col-md-6 mb-3">
            <label class="form-label">Height (inches)</label>
            <input v-model="form.height" type="number" class="form-control" required />
          </div>
          <div class="col-md-6 mb-3">
            <label class="form-label">Favourite Colour</label>
            <input v-model="form.fav_colour" type="text" class="form-control" required />
          </div>
        </div>

        <div class="row">
          <div class="col-md-6 mb-3">
            <label class="form-label">Favourite Cuisine</label>
            <input v-model="form.fav_cuisine" type="text" class="form-control" required />
          </div>
          <div class="col-md-6 mb-3">
            <label class="form-label">Favourite School Subject</label>
            <input v-model="form.fav_school_subject" type="text" class="form-control" required />
          </div>
        </div>

        <div class="form-check mb-2">
          <input v-model="form.political" type="checkbox" class="form-check-input" id="politicalCheck" />
          <label class="form-check-label" for="politicalCheck">Political</label>
        </div>

        <div class="form-check mb-2">
          <input v-model="form.religious" type="checkbox" class="form-check-input" id="religiousCheck" />
          <label class="form-check-label" for="religiousCheck">Religious</label>
        </div>

        <div class="form-check mb-3">
          <input v-model="form.family_oriented" type="checkbox" class="form-check-input" id="familyCheck" />
          <label class="form-check-label" for="familyCheck">Family Oriented</label>
        </div>

        <button type="submit" class="btn btn-success">Create Profile</button>
      </form>
    </div>
  </template>

<script>
import api from '@/services/api'

export default {
  name: 'NewProfile',
  data() {
    return {
      form: {
        name: '',
        description: '',
        parish: '',
        birth_year: '',
        sex: '',
        race: '',
        height: '',
        fav_colour: '',
        fav_cuisine: '',
        fav_school_subject: '',
        political: false,
        religious: false,
        family_oriented: false
      }
    };
  },
  methods: {
  createProfile() {
    api.post('/profiles', this.form)
      .then(() => {
        alert('Profile created successfully!');
        this.$router.push({ name: 'Home' }); 
      })
      .catch(error => {
        console.error(error);
        alert(error.response?.data?.message || 'Error creating profile.');
      });
    }
  }
};
</script>
