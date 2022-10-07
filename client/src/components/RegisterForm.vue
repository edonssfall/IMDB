<template>
  <form @submit="registerUser">
    <div class="mb-3 row">
      <center>{{ error.detail }}</center>
      <label for="staticEmail" class="col-sm-2 col-form-label">First name</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" v-model="data.first_name">
      </div>
    </div>
    <div class="mb-3 row">
      <label for="staticEmail" class="col-sm-2 col-form-label">Last name</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" v-model="data.last_name">
      </div>
    </div>
    <div class="mb-3 row">
      <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
      <div class="col-sm-10">
        <input type="email" class="form-control" v-model="data.email" required="required">
        {{ error.email }}
      </div>
    </div>
    <div class="mb-3 row">
      <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" v-model="data.password" required="required">
        {{ error.password }}
      </div>
    </div>
    <div class="mb-3 row">
      <label for="inputPassword" class="col-sm-2 col-form-label">Repeat Password</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" v-model="data.password2" required="required">
        {{ error.password2 }}
      </div>
    </div>
    <div class="header">
      <a class="lines" href="/login">Have an account?!</a>
      <button type="submit" class="btn btn-primary">Register</button>
    </div>
  </form>
</template>

<script>
import {useUserStore} from "../stores/user";
import {apiFetch} from "../utils/api"
import {DjangoAPIHost} from "../constance";

export default {
  name: "RegisterForm",
  data() {
    return {
      data: {
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        password2: ''
      },
      error: {}
    }
  },
  methods: {
    async registerUser(e) {
      e.preventDefault()
      e.stopPropagation()
      const response = await apiFetch(DjangoAPIHost + '/api/auth/register/',
          {
            method: 'POST',
            body: JSON.stringify(this.data)
          })
      if (response.status !== 201) {
        this.error = await response.json()
      } else {
        const data = await response.json()
        localStorage.setItem('userToken', data.access)
        await useUserStore().fetchUser();
        location.href = '/login'
      }
    }
  }
}
</script>

<style scoped>

form {
  position: fixed;
  top: 30%;
  left: 35%;
  width: 650px;
}

.header {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
}

.header a {
  display: inline-block;
}

</style>