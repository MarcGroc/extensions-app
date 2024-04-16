<template>
  <div>
    <login-form />
  </div>
</template>

<script>
import brand from '@/assets/text/brand';
import LoginForm from '@/components/Forms/Login';
import { defineNuxtComponent } from '#app';

export default defineNuxtComponent({
  components: {
    LoginForm,
  },
  head() {
    return {
      title: brand.saas.name + ' - Login',
    };
  },
});
</script>
