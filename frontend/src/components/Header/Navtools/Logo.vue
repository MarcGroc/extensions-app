<template>
  <router-link :to="{ name: 'home' }">
    <img
      src="@/assets/img/logo/djavue_logo.jpg"
      alt=""
      v-if="!themeSettingsStore.isDark"
      style="height: 100px; width: 100px"
    />

    <img
      src="@/assets/img/logo/djavue_logo.jpg"
      alt=""
      v-if="themeSettingsStore.isDark"
      style="height: 100px; width: 100px"
    />
  </router-link>
</template>
<script>
import { useThemeSettingsStore } from "@/store/themeSettings";

export default {
  setup() {
    const themeSettingsStore = useThemeSettingsStore();
    return {
      themeSettingsStore,
    };
  },
};
</script>
