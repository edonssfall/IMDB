<script setup>
import RegisterForm from "../components/RegisterForm.vue";
import {useUserStore} from "../stores/user";
import {onBeforeMount} from "vue";

const userStore = useUserStore();

onBeforeMount(() => {
  if (userStore.getUserId) {
    location.href = '/';
  }
})

</script>

<template>
  <title>Registration</title>
  <main>
    <RegisterForm/>
  </main>
</template>
