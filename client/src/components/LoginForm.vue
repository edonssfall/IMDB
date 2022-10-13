<template>
  <form @submit="loginUser">
    <div class="alert alert-danger" v-if="error.detail" role="alert">
      {{ error.detail }}
    </div>
    <div class="mb-3 row">
      <div class="col-sm-10">
        <input type="email" class="form-control" v-model="data.email" required="required" placeholder="E-mail">
        {{ error.email }}
      </div>
    </div>
    <div class="mb-3 row">
      <div class="col-sm-10">
        <input type="password" class="form-control" v-model="data.password" required="required" placeholder="Password">
        {{ error.password }}
      </div>
    </div>
    <div class="header">
      <router-link class="lines" to="/register">Register</router-link>
      <a class="lines" href="#">Forgot Password!?</a>
      <button type="submit" class="btn btn-primary">Log in</button>
    </div>
    <div class="society">
      <h4>
        or use social media
      </h4>
    </div>
    <div class="society2">
      <img src=../assets/facebook_logo.png>
      <img src=../assets/google_logo.png>
      <img src=../assets/twitter_logo.png>
    </div>
  </form>
</template>

<script>
import {useUserStore} from "../stores/user";
import {apiFetch} from "../utils/api"
import {DjangoAPIHost} from "../constance";

export default {
  name: "LoginForm",
  data() {
    return {
      data: {
        email: '',
        password: ''
      },
      error: {}
    }
  },
  methods: {
    async loginUser(e) {
      e.preventDefault()
      e.stopPropagation()

      const response = await apiFetch(DjangoAPIHost + 'api/auth/login/',
          {
            method: 'POST',
            body: JSON.stringify(this.data)
          }
      )

      if (response.status !== 200) {
        this.error = await response.json()
        return
      } else {
        const data = await response.json()
        localStorage.setItem('userToken', data.access)
        await useUserStore().fetchUser();
        location.href = '/'
      }
    }
  }
}
</script>

<style scoped>

form {
  position: fixed;
  top: 38%;
  left: 38%;
  width: 420px;
}

.header {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  margin-left: 5px;
}

.header a {
  display: inline-block;
  padding: 10px;
}

.mb-3 {
  margin-left: 50px;
}

.society2 {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
}

.society2 img {
  display: inline-block;
  padding: 10px;
  height: 80px;
  width: 80px;
}
</style>