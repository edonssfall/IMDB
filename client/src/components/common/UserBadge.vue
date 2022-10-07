<template>
  <div>
    <div v-if="userStore.user" style="color: white">

      {{ userStore.getUserName }}

      <RouterLink class="logo" to="/">
        <img @click="logOut" src=../../../../static/images/user_logo.png height="30" width="30">
      </RouterLink>
    </div>
    <div v-else>
      <RouterLink to="/login" style="text-decoration: none; color: white">
        Log In
      </RouterLink>
    </div>
  </div>
</template>

<script>
import {useUserStore} from "../../stores/user";

export default {
  name: "UserBadge",
  setup() {
    const userStore = useUserStore();
    return {
      userStore
    }
  },
  data() {
    return {
      user: this.userStore.user
    }
  },
  methods: {
    logOut() {
      this.userStore.logOut()
    }
  }
}
</script>

<style scoped>

.logo img {
  width: 30px;
  margin: 1em auto;
  background: white;
  border-radius: 50%;
}
</style>