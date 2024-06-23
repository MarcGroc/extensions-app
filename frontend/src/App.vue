<template>
  <router-view />
</template>

<script>
import { useAuthStore } from "@/store/auth";

export default {
  /**
   * Initialize the authentication store on component mount.
   */
  async mounted() {
    const authStore = useAuthStore();
    await authStore.init();
  },
};
</script>

<style></style>
