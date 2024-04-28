<template>
  <teleport to="body">
    <div v-if="!cookieConsent" class="cookie-consent">
      <p>{{text.title}}</p>
      <div class="button-container">
        <button class="ht-btn ht-btn-md" @click="acceptCookies">{{ text.accept }}</button>
        <button class="ht-btn ht-btn-md" @click="rejectCookies">{{text.decline}}</button>
      </div>
    </div>
  </teleport>
</template>

<script>
import textData from '../assets/text.json'
export default {
  data() {
    return {
      text: textData.cookies,
      cookieConsent: localStorage.getItem('cookieConsent') === 'true',
    };
  },
  methods: {
    acceptCookies() {
      localStorage.setItem('cookieConsent', 'true');
      this.cookieConsent = true;
    },
    rejectCookies() {
      localStorage.setItem('cookieConsent', 'false');
      this.cookieConsent = true;
    },
  },
};
</script>

<style scoped>
.cookie-consent {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #f0f0f0;
  padding: 20px;
  text-align: center;
}
.button-container {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-top: 10px;
}

</style>
