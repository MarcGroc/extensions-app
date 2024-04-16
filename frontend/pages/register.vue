<template>
  <div>
    <register-form />
  </div>
</template>

<script>
import brand from '@/assets/text/brand';
import RegisterForm from '@/components/Forms/Register';
import { defineNuxtComponent } from '#app';

export default defineNuxtComponent({
  components: {
    RegisterForm,
  },
  head() {
    return {
      title: brand.saas.name + ' - Register',
    };
  },
});
</script>
