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
        <UserBadge/>
      </div>
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

</style>