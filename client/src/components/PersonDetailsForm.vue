<template>

  <div v-show="isLoading" class="text-center">
    <div class="spinner-border" role="status">
    </div>
    <h3>Loading...</h3>
  </div>

  <div v-show="isLoading === false">
    <div class="block">
      <div class="detail_pic">
        <img v-if="this.person.image_url === null || this.person.image === ''"
             src="../../../static/images/default-person.jpg">
        <img v-else :src="this.person.image_url">
      </div>
      <div class="detail_info">
        <div class="label">
          <h2>{{ this.person.name }}</h2>
          <img v-if="userStore.UserIsStaff" src="../../../static/images/edit_logo.png"
               data-bs-toggle="modal" data-bs-target="#exampleModal">
        </div>

        <br>
        <br>

        <h5 v-if="this.person.birth_year" class="year">{{ this.person.birth_year }}</h5>
        <h5 v-else>Unknown year</h5>
        <br>
        <br>
        <h3 v-if="this.person.birth_place">Birth Place: {{ this.person.birth_place }}</h3>
        <h3 v-else>Unknown Birth Place</h3>
      </div>
    </div>

    <div class="side_rec">
      <router-link v-bind:to="`/title/${this.title.imdb_id}`" :key="this.title.imdb_id"
                   style="text-decoration: none; color: black">
        <h1>Persons in This Movie:
          <br>
          {{ this.title.name }}</h1>
      </router-link>
      <div class="col" v-for="rec_person in this.rec_persons">
        <div class="card mb-3" v-if="rec_person.person_id.imdb_id !== this.person.imdb_id">
          <router-link v-bind:to="`/name/${rec_person.person_id.imdb_id}`" style="text-decoration: none"
                       :key="rec_person.person_id.imdb_id" @click="RecPerson">
            <div class="row g-0">
              <div class="col-md-4">
                <img v-if="rec_person.person_id.image_url === null || rec_person.person_id.image_url === ''"
                     src="../../../static/images/default-person.jpg">
                <img v-else :src="rec_person.person_id.image_url">
              </div>
              <div class="col-md-8">
                <div class="card-body">
                  <h3 class="card-title">{{ rec_person.person_id.name }}</h3>
                  <h5 v-if="rec_person.birth_place">Rating IMDB: {{ rec_person.birth_place }}</h5>
                  <h5 v-else>Unknown Birth Place</h5>
                </div>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </div>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Edit {{ this.person.name }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit="PersonEdit">
              <div class="mb-3 row">
                <label class="col-sm-2 col-form-label">Name</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" v-model="person_data.name">
                </div>
              </div>
              <div class="mb-3 row">
                <label class="col-sm-2 col-form-label">Birth Date</label>
                <div class="col-sm-10">
                  <input type="date" class="form-control" v-model="person_data.birth_year">
                </div>
              </div>
              <div class="mb-3 row">
                <label class="col-sm-2 col-form-label">Death Date</label>
                <div class="col-sm-10">
                  <input type="date" class="form-control" v-model="person_data.death_year">
                </div>
              </div>
              <div class="mb-3 row">
                <label class="col-sm-2 col-form-label">Birth Place</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" v-model="person_data.birth_place">
                </div>
              </div>
              <div class="mb-3 row">
                <label for="inputPassword" class="col-sm-2 col-form-label">URL</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" v-model="person_data.image_url">
                </div>
              </div>
              <button type="submit" class="btn btn-primary" style="float: right">PUT</button>
            </form>
          </div>
        </div>
      </div>
    </div>

  </div>

</template>

<script>
import {useUserStore} from "../stores/user";
import Cookies from 'js-cookie';
import {ref} from "vue";
import {DjangoAPIHost} from "../global";

export default {
  name: "PersonDetailsForm",
  setup() {
    const userStore = ref(useUserStore())
    return {
      userStore
    }
  },
  data() {
    return {
      person: [],
      title: [],
      rec_persons: [],
      error: null,
      isLoading: false,
      person_data: {
        imdb_id: null,
        name: null,
        birth_year: null,
        death_year: null,
        image_url: null,
        birth_place: null
      },
    }
  },
  async beforeMount() {
    await this.PersonDetails()
    await this.PersonsRec()
  },
  methods: {
    async RecPerson() {
      await this.PersonDetails()
      await this.PersonsRec()
    },
    async PersonDetails() {
      this.isLoading = true
      const response = await fetch(DjangoAPIHost + `api/imdb/name/${this.$route.params['person_slug']}`)
      if (response.status === 200) {
        this.person = await response.json()
      }
      for (const [key, value] of Object.entries(this.person_data)) {
        this.person_data[key] = this.person[key]
      }
      console.log(this.person)
    },
    async PersonsRec() {
      if (this.person['person_id']['0']) {
        this.title = this.person['person_id']['0']['movie_id']
        const response = await fetch(DjangoAPIHost + `api/imdb/title/${this.title['imdb_id']}`)
        const data = await response.json()
        this.rec_persons = data['movie_id']
      }
      this.isLoading = false
    },
    async PersonEdit(e) {
      e.preventDefault()

      const response = await fetch(DjangoAPIHost + `api/imdb/name/${this.person.imdb_id}/edit/`, {
        method: 'PUT',
        headers: {
          'X-CSRFToken': Cookies.get('csrftoken'),
          'content-type': 'application/json'
        },
        body: JSON.stringify(this.person_data)
      })
      if (response.status !== 201) {
        this.error = await response.json()
      }
    }
  }
}

</script>

<style scoped>

.spinner-border {
  margin-top: 100px;
}

.label img {
  width: 40px;
  height: 40px;
  cursor: pointer;
}

.detail_pic img {
  float: left;
  margin-top: 90px;
  margin-left: 50px;
  width: 430px;
  height: 600px;
}

.detail_info {
  float: left;
  margin-top: 90px;
  margin-left: 60px;
  width: 350px;
  height: 310px;
}

.table {
  margin-left: 40px;
  float: left;
  margin-top: 140px;
  width: 460px;
  height: 263px;
}

.side_rec {
  float: right;
  margin-right: 50px;
  margin-top: 60px;
  width: 450px;
  height: 550px;
}

.card img {
  height: 100px;
  width: 100px;
}

.card-body {
  text-decoration: none;
  color: black;
}

</style>