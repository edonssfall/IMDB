<template>
  <div class="container">
    <div v-show="isLoading" class="text-center">
      <LoadingView/>
    </div>

    <div v-show="isLoading === false">
      <h2 class="is-size-5 has-text-grey">Search term: {{ query }}</h2>
      <h2 class="is-size-5 has-text-grey">Found {{ size }} items</h2>
      <div class="row row-cols">
        <div class="col" v-for="movie in this.movies">
          <router-link v-bind:to="`/title/${movie.imdb_id}`" :key="movie.imdb_id" style="text-decoration: none">
            <div class="card">
              <img v-if="movie.poster_url === null || movie.poster_url === ''"
                   src="../assets/default-movie.jpg">
              <img v-else :src="movie.poster_url">
              <div class="card-body" style="color: black">
                <h5 class="card-title">{{ movie.name }}</h5>
                <p class="year">{{ movie.year }}</p>
                <template class="genres" data-bs-toggle="tooltip" v-for="genre in movie.genres">
                  <span class="badge rounded-pill bg-secondary">{{ genre }}</span>{{ ' ' }}
                </template>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {DjangoAPIHost} from "../constance";
import Cookies from 'js-cookie';

export default {
  name: "SearchForm",
  data() {
    return {
      movies: [],
      query: '',
      isLoading: false,
      size: null,
    }
  },
  async mounted() {
    await this.SearchProduct()
  },
  methods: {
    async SearchProduct() {
      this.isLoading = true
      let item_search = window.location.search.substring(1)
      let params = new URLSearchParams(item_search)
      if (params.get('query')) {
        this.query = params.get('query')
      }
      const response = await fetch(DjangoAPIHost + `api/imdb/movies/search`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': Cookies.get('csrftoken'),
          'content-type': 'application/json'
        },
        body: JSON.stringify({'query': this.query})
      })
      this.movies = await response.json()
      this.size = Object.keys(this.movies).length
      this.isLoading = false
    }
  }
}
</script>

<style scoped>
.card {
  height: 480px;
  width: 220px;
}

.card img {
  height: 280px;
  width: 218px;
}

.col {
  margin: 20px;
  padding: 0;
}

.col a {
  height: 480px;
  width: 220px;
}
</style>