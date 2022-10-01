<template>
  <div class="text">
    <ul>
      <li v-for="person in this.persons">{{ person.name }}</li>
    </ul>
  </div>
  <ul class="pagination justify-content-center">
    <li class="page-item disabled" v-if="disablePrevious">
      <a class="page-link">Previous</a>
    </li>
    <li class="page-item" v-if="showPrevious">
      <a class="page-link" @click="loadPrevious">Previous</a>
    </li>
    <li class="page-item active">
      <a class="page-link" href="#">1</a>
    </li>
    <li class="page-item" aria-current="page">
      <a class="page-link" href="#">2</a>
    </li>
    <li class="page-item">
      <a class="page-link" href="#">3</a>
    </li>
    <li class="page-item">
      <a class="page-link" href="#">4</a>
    </li>
    <li class="page-item disabled" v-if="disableNext">
      <a class="page-link">Next</a>
    </li>
    <li class="page-item" v-if="showNext">
      <a class="page-link" @click="loadNext">
        Next
      </a>
    </li>
  </ul>
</template>

<script>
export default {
  name: "PersonForm",
  data() {
    return {
      persons: [],
      images: [],
      currentPage: 1,
      showNext: false,
      disableNext: false,
      showPrevious: false,
      disablePrevious: false,
      previous: false
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
    async loadPrevious(){
      this.currentPage -= 1
      await this.PersonsList()
    },
    async PersonsList() {
      const response = await fetch('/api/imdb/persons/?page=' + this.currentPage)
      if (response.status === 200) {
        const data = await response.json()
        this.persons = data.results
        // const resp = await fetch('https://imdb-api.com/API/FullCast/k_o57coyq8/tt1375666')
        // const dt = await resp.json()
        // console.log(dt)
        if (data.next) {
          this.showNext = true
          this.disableNext = false
        }
        else {
          this.disableNext = true
          this.showNext = false
        }
        if (data.previous) {
          this.showPrevious = true
          this.disablePrevious = false
        }
        else {
          this.showPrevious = false
          this.disablePrevious = true
        }
        return this.persons
      }
    }
  }
}

</script>

<style scoped>

</style>