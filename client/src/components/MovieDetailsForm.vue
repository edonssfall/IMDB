<template>
  <div class="title">
    <router-link to="movies" style="color: black; text-decoration: none">Movies</router-link>
    >
    <router-link v-bind:to="`${movie.imdb_id}`" style="text-decoration: none; color: black">{{ movie.name }}
    </router-link>
  </div>
  <div class="block">
    <div class="detail_pic">
      <img v-if="this.movie.poster_url === null" src="../../../static/images/default-movie.jpg">
      <img v-else :src="this.movie.poster_url">
    </div>
    <div class="detail_info">
      <div class="label" style="height: 28px; width: 187px; font-size: 20px">
        <h4>{{ this.movie.name }}</h4>
      </div>
      <br>
      <template class="genres" data-bs-toggle="tooltip" v-for="genre in movie.genres">
        <span class="badge rounded-pill bg-secondary">{{ genre }}</span>{{ ' ' }}
      </template>
      <template v-for="movi in this.movie.movie_id">
        <template v-if="movi.job === 'director'">
          <template v-for="directors in movi.person_id">
            <h5 class="director">{{ directors }}</h5>
          </template>
        </template>
      </template>
      <h5 v-if="this.movie.year !== null" class="year">{{ this.movie.year }}</h5>
      <h5 v-else>Unknown year</h5>
      <br>
      <h3 v-if="this.movie.rating_imdb !== null">{{ this.movie.rating_imdb }}</h3>
      <h3 v-else>No Rating</h3>
    </div>
  </div>

  <table class="table">
    <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Position</th>
      <th scope="col">Role</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="movi in this.movie.movie_id">
      <template v-for="nami in movi.person_id">
        <td scope="row">{{ nami }}</td>
        <td>{{ movi.job }}</td>
        <td></td>
      </template>
    </tr>
    </tbody>
  </table>

  <div v-for="rec_movi in rec_movies">
    <div v-for="rec_movie in rec_movi">{{rec_movies}}</div>
  </div>

</template>

<script>
import {useRoute} from 'vue-router';


export default {
  name: "MovieDetailsForm",
  data() {
    return {
      movie: [],
      rec_movies: []
    }
  },
  async mounted() {
    await this.MovieDetails()
    await this.MovieRec()
  },
  methods: {
    async MovieDetails() {
      this.isLoading = true
      const movie_slug = useRoute().params.movie_slug
      this.isLoading = true
      const response = await fetch(`api/imdb/title/${movie_slug}`)
      if (response.status === 200) {
        this.movie = await response.json()
      }
    },
    async MovieRec() {
      const movie_genre = this.movie.genres
      const response = await fetch(`api/imdb/title/${movie_genre}`)
      if (response.status === 200) {
        const data = await response.json()
        this.rec_movies = data.results
        console.log(data.results)
      }
    }
  }
}

</script>

<style scoped>

.title {
  font-size: 50px;
}

.detail_pic img {
  position: absolute;
  left: 75px;
  top: 172px;
  width: 190px;
  height: 310px;
}

.detail_info {
  position: absolute;
  left: 278px;
  top: 172px;
  width: 350px;
  height: 310px;
}

.table {
  position: absolute;
  left: 73px;
  top: 480px;
  width: 460px;
  height: 263px;
}

</style>