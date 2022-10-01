<template>
  <form @submit="loginUser">
    <center>{{ error.detail }}</center>
    <div class="mb-3 row">
      <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
      <div class="col-sm-10">
        <input type="email" class="form-control" placeholder="email" v-model="data.email" required="required">
        {{ error.email }}
      </div>
    </div>
    <div class="mb-3 row">
      <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" placeholder="password" v-model="data.password" required="required">
        {{ error.password }}
      </div>
    </div>
    <div class="header">
      <a class="lines" href="/register">Register</a>
      <a class="lines" href="#">Forgot Password!?</a>
      <button type="submit" class="btn btn-primary">Log in</button>
    </div>
    <div class="society">
      <h4>
        or use social media
      </h4>
    </div>
    <div class="society2">
      <img src=../../../static/images/facebook_logo.png height="100" width="100">
      <img src=../../../static/images/google_logo.png height="100" width="100">
      <img src=../../../static/images/twitter_logo.png height="100" width="100">
    </div>
  </form>
</template>

<script>
import {useUserStore} from "../stores/user";
import {apiFetch} from "../utils/api"

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

      const response = await apiFetch('/api/auth/login/',
          {
            method: 'POST',
            body: JSON.stringify(this.data)
          }
      )

      if (response.status !== 200) {
        this.error = await response.json()
        console.log(this.error(data.email))
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
  margin-right: 10px;
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
}
</style>