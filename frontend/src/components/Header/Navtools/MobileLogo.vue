<template>
  <router-link :to="{ name: 'home' }">
    <img
      src="@/assets/images/logo/logo-c.svg"
      alt=""
      v-if="!themeSettingsStore.isDark"
    />

    <img
      src="@/assets/images/logo/logo-c-white.svg"
      alt=""
      v-if="themeSettingsStore.isDark"
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
