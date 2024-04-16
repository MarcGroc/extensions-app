<template>
  <div>
    <contact />
  </div>
</template>

<script>
import Contact from '@/components/Forms/Contact';
import brand from '@/assets/text/brand';
import { defineNuxtComponent } from '#app';

export default defineNuxtComponent({
  components: {
    Contact,
  },
  head() {
    return {
      title: brand.saas.name + ' - Contact',
    };
  },
});
</script>
