<template>

  <div class="v-movies">
    <div class="title">
      <router-link to="movies" style="color: black; text-decoration: none">Movies</router-link>
    </div>
    <div class="row row-cols-xxl-6 align-items-center">
      <div class="col" v-for="movie in this.movies" :key="movie.imdb_id">
        <router-link v-bind:to="`${movie.imdb_id}`" style="text-decoration: none">
          <div class="card">
            <img v-if="movie.poster_url === null" src="../../../static/images/default-movie.jpg">
            <img v-else :src="movie.poster_url">
            <div class="card-body" style="color: black">
              <h5 class="card-title">{{ movie.name }}</h5>
              <template v-for="movi in movie.movie_id">
                <template v-if="movi.job === 'director'">
                  <template v-for="directors in movi.person_id">
                    <h6 class="director">{{ directors }}</h6>
                  </template>
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
</template>

<script>
export default {
  name: "MoviesForm",
  data() {
    return {
      movie: [],
      movies: [],
      currentPage: 1,
      total_pages: null,
      showNext: false,
      showPrevious: false,
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
      const response = await fetch(`api/imdb/movies/?page=${this.currentPage}`)
      if (response.status === 200) {
        const data = await response.json()
        this.movies = data.results
        this.total_pages = data.total_pages
        console.log(data)
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
      }
    }
  }
}
</script>

<style scoped>

.card {
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
