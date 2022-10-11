<template>

  <div v-show="isLoading" class="text-center">
    <div class="spinner-border" role="status">
    </div>
    <h3>Loading...</h3>
  </div>

  <div v-show="isLoading === false">
    <div class="block">
      <div class="detail_pic">
        <img v-if="this.movie.poster_url === null || this.movie.poster_url === ''"
             src="../../../static/images/default-movie.jpg">
        <img v-else :src="this.movie.poster_url">
      </div>
      <div class="detail_info">
        <div class="label">
          <h2>{{ this.movie.name }}</h2>
          <img v-if="userStore.UserIsStaff" src="../../../static/images/edit_logo.png"
               data-bs-toggle="modal" data-bs-target="#exampleModal">
        </div>

        <br>
        <br>
        <template class="genres" data-bs-toggle="tooltip" v-for="genre in movie.genres">
          <span class="badge rounded-pill bg-secondary">{{ genre }}</span>{{ ' ' }}
        </template>
        <template v-for="movi in this.movie.movie_id">
          <template v-if="movi.job === 'director'">
            <h5 class="director">{{ movi.person_id.name }}</h5>
          </template>
        </template>
        <h5 v-if="this.movie.year" class="year">{{ this.movie.year }}</h5>
        <h5 v-else>Unknown year</h5>
        <br>
        <br>
        <h3 v-if="this.movie.rating_imdb">Rating IMDB: {{ this.movie.rating_imdb }}</h3>
        <h3 v-else>No Rating</h3>
      </div>
    </div>

    <table class="table">
      <thead>
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Position</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="movi in this.movie.movie_id">
        <router-link v-bind:to="`/name/${movi.person_id.imdb_id}`" style="text-decoration: none; color: black"
                     :key="movi.imdb_id">
          <td scope="row">{{ movi.person_id.name }}</td>
        </router-link>
        <td>{{ movi.job }}</td>
      </tr>

      </tbody>
    </table>

    <div class="side_rec">
      <h1>Movies Like This</h1>
      <div class="col" v-for="rec_movie in this.rec_movies">
        <router-link v-bind:to="`/title/${rec_movie.imdb_id}`" style="text-decoration: none"
                     :key="`${rec_movie.imdb_id}`"
                     @click="RecMovie(rec_movie.imdb_id)">
          <div class="card mb-3">
            <div class="row g-0">
              <div class="col-md-4">
                <img v-if="rec_movie.poster_url === null || rec_movie.poster_url === ''"
                     src="../../../static/images/default-movie.jpg">
                <img v-else :src="rec_movie.poster_url">
              </div>
              <div class="col-md-8">
                <div class="card-body">
                  <h5 class="card-title">{{ rec_movie.name }}</h5>
                  <template class="genres" data-bs-toggle="tooltip" v-for="genre in rec_movie.genres">
                    <span class="badge rounded-pill bg-secondary">{{ genre }}</span>{{ ' ' }}
                  </template>
                </div>
              </div>
            </div>
          </div>
        </router-link>
      </div>
    </div>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Edit {{ this.movie.name }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit="MovieEdit">
              <div class="mb-3 row">
                <label class="col-sm-2 col-form-label">Name</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" v-model="movie_data.name">
                </div>
              </div>
              <div class="mb-3 row">
                <label class="col-sm-2 col-form-label">Release Date</label>
                <div class="col-sm-10">
                  <input type="date" class="form-control" v-model="movie_data.year">
                </div>
              </div>
              <div class="mb-3 row">
                <label class="col-sm-2 col-form-label">Rating IMDB</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" v-model="movie_data.rating_imdb">
                </div>
              </div>
              <div class="mb-3 row">
                <label class="col-sm-2 col-form-label">Rank</label>
                <div class="col-sm-10">
                  <input type="number" class="form-control" v-model="movie_data.rank">
                </div>
              </div>
              <div class="mb-3 row">
                <label for="inputPassword" class="col-sm-2 col-form-label">URL</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" v-model="movie_data.poster_url">
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
import {DjangoAPIHost} from "../constance"

export default {
  name: "MovieDetailsForm",
  setup() {
    const userStore = ref(useUserStore())
    return {
      userStore
    }
  },
  data() {
    return {
      movie: [],
      rec_movies: [],
      isLoading: false,
      movie_slug: this.$route.params['movie_slug'],
      movie_data: {
        rating_imdb: null,
        imdb_id: null,
        name: null,
        year: null,
        poster_url: null,
        rank: null
      },
      next_movie: null
    }
  },
  async beforeMount() {
    await this.MovieDetails(this.movie_slug)
    await this.MovieRec()
  },
  methods: {
    async RecMovie(movie_slug) {
      await this.MovieDetails(movie_slug)
      await this.MovieRec()
    },
    async MovieDetails(movie_slug) {
      this.isLoading = true
      const response = await fetch(DjangoAPIHost + `api/imdb/title/${movie_slug}`)
      if (response.status === 200) {
        this.movie = await response.json()
      }
      for (const [key, value] of Object.entries(this.movie_data)) {
        this.movie_data[key] = this.movie[key]
      }
    },
    async MovieRec() {
      let movie_genres = this.movie.genres
      let request_genres = ''
      for (const item of movie_genres) {
        request_genres += '&genres=' + item
      }
      const response = await fetch(DjangoAPIHost + `api/imdb/titles/?title=${this.movie.imdb_id}${request_genres}`)
      if (response.status === 200) {
        const data = await response.json()
        this.rec_movies = data.results
      }
      this.isLoading = false
    },
    async MovieEdit() {
      await fetch(DjangoAPIHost + `api/imdb/title/${this.movie.imdb_id}/edit`, {
        method: 'PUT',
        headers: {
          'X-CSRFToken': Cookies.get('csrftoken'),
          'content-type': 'application/json'
        },
        body: JSON.stringify(this.movie_data)
      })
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
  width: 350px;
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