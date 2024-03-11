

<script>
import axios from 'axios';

export default {
  data() {
    return {
      exampleText: '',
    };
  },
  mounted() {
    axios.get('/api/example/')
      .then(response => {
        this.exampleText = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
}
</script>

<template>
  <div>{{ exampleText }}</div>
</template>
