<template>
  <nav class="navbar navbar-expand bg-dark">
    <div class="container-fluid">
      <div class="collapse navbar-collapse" id="navbarScroll">
        <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
          <li class="nav-item">
            <router-link to="/movies" class="nav-link active" aria-current="page" style="color: white">Movies
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/persons" class="nav-link active" aria-current="page" style="color: white">Persons
            </router-link>
          </li>
        </ul>
      </div>
        <form class="collapse navbar-collapse d-lg-flex justify-content-center" role="search" method="get" action="/search">
          <input class="form-control me-2" type="search" placeholder="What are you looking at?" aria-label="Search"
                 name="query">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
        <UserBadge/>
      </div>
  </nav>
</template>

<script>
import UserBadge from "./UserBadge.vue";

export default {
  name: "Navbar",
  components: {UserBadge}
}
</script>

<style scoped>

form {
  margin-right: 50px;
  max-width: 400px;
}
.navbar {
  height: 78px;
}
</style>