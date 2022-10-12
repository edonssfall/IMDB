<template>
  <div class=container>
    <div v-show="isLoading" class="text-center">
      <LoadingView/>
    </div>

    <div v-show="isLoading === false">
      <div class="row row-cols-lg-6 align-items-center">
        <div class="col" v-for="person in this.persons">
          <router-link v-bind:to="`name/${person.imdb_id}`" :key="person.imdb_id" style="text-decoration: none">
            <div class="card">
              <img v-if="person.image_url === null || person.image_url === ''"
                   src="../../../static/images/default-person.jpg">
              <img v-else :src="person.image_url">
              <div class="card-body" style="color: black">
                <h5 class="card-title">{{ person.name }}</h5>
                <p class="year">{{ person.birth_year }}</p>
              </div>
            </div>
          </router-link>
        </div>
      </div>
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
  </div>
</template>

<script>


import {DjangoAPIHost} from "../constance";
import LoadingView from "../views/LoadingView.vue";

export default {
  name: "PersonsForm",
  components: {LoadingView},
  data() {
    return {
      persons: [],
      currentPage: 1,
      total_pages: null,
      showNext: false,
      showPrevious: false,
      isLoading: false
    }
  },
  async beforeMount() {
    await this.PersonsList()
  },
  methods: {
    async loadNext() {
      this.currentPage += 1
      await this.PersonsList()
    },
    async loadPrevious() {
      this.currentPage -= 1
      await this.PersonsList()
    },
    async PersonsList() {
      this.isLoading = true
      const response = await fetch(DjangoAPIHost + `api/imdb/persons/?page=${this.currentPage}`)
      if (response.status === 200) {
        const data = await response.json()
        this.persons = data.results
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

.container {
  width: 1920px;
}

.card {
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
