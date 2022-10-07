<template>

  <div v-show="isLoading" class="text-center">
    <div class="spinner-border" role="status">
    </div>
    <h3>Loading...</h3>
  </div>

  <div v-show="isLoading === false">
    <div class="row row-cols-xxl-6 align-items-center">
      <div class="col" v-for="movie in this.movies">
        <router-link v-bind:to="`/title/${movie.imdb_id}`" :key="movie.imdb_id" style="text-decoration: none">
          <div class="card">
            <img v-if="movie.poster_url === null || movie.poster_url === ''" src="../../../static/images/default-movie.jpg">
            <img v-else :src="movie.poster_url">
            <div class="card-body" style="color: black">
              <h5 class="card-title">{{ movie.name }}</h5>
              <template v-for="movi in movie.movie_id">
                <template v-if="movi.job === 'director'">
                    <h6 class="director">{{ movi.person_id.name }}</h6>
                </template>
              </template>
              <p class="year">{{ movie.year }}</p>
              <template class="genres" data-bs-toggle="tooltip" v-for="genre in movie.genres">
                <span class="badge rounded-pill bg-secondary">{{ genre }}</span>{{ ' ' }}
              </template>
            </div>
          </div>
        </router-link>
      </div>
    </div>
    <br>
    <div class="pagination justify-content-center">
      <li class="page-item previous" v-if="showPrevious">
        <a class="page-link" @click="loadPrevious">Previous</a>
      </li>
      <li class="my_pagination">Current page is {{ this.currentPage }} of {{ this.total_pages }}</li>
      <li class="page-item next" v-if="showNext">
        <a class="page-link" @click="loadNext">Next</a>
      </li>
    </div>
  </div>

</template>

<script>


import {DjangoAPIHost} from "../constance";

export default {
  name: "MoviesForm",
  data() {
    return {
      movies: [],
      currentPage: 1,
      total_pages: null,
      showNext: false,
      showPrevious: false,
      isLoading: false
    }
  },
  async beforeMount() {
    await this.MoviesList()
  },
  methods: {
    async loadNext() {
      this.currentPage += 1
      await this.MoviesList()
    },
    async loadPrevious() {
      this.currentPage -= 1
      await this.MoviesList()
    },
    async MoviesList() {
      this.isLoading = true
      const response = await fetch(DjangoAPIHost + `api/imdb/movies/?page=${this.currentPage}`)
      if (response.status === 200) {
        const data = await response.json()
        this.movies = data.results
        this.total_pages = data.total_pages
        if (data.next) {
          this.showNext = true
        } else {
          this.showNext = false
        }
        if (data.previous) {
          this.showPrevious = true
        } else {
          this.showPrevious = false
        }
        this.isLoading = false
      }
    }
  }
}
</script>

<style scoped>

.spinner-border {
  margin-top: 100px;
}

.card {
  margin: 20px;
  hight: 250px;
  width: 220px;
}

.title {
  font-size: 50px;
}

.disabled {
  background: #cccccc;
}

.my_pagination {
  margin: 5px;
}

.my_pagination li {
  cursor: pointer;
}
</style>
