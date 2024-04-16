<template>
  <div class="main-wrap" :class="{ 'dedicated-page': dedicated }">
    <main-header :invert="invert" />
    <div class="container-wrap" :class="{ 'scroll-nav-content' : navScroll }">
      <slot />
    </div>
    <main-footer invert v-if="invert" />
    <footer-with-deco v-else />
  </div>
</template>

<style lang="scss" scoped>
.main-wrap {
  position: relative;
  width: 100%;
  overflow: hidden;
  @include palette-text-primary;
  .v-theme--dark & {
    background-color: $dark-background-default;
  }
  .v-theme--light & {
    background-color: $light-background-paper;
  }
}

.container-wrap {
  margin-top: -40px;
  :deep(> section) {
    position: relative;
  }
}

.dedicated-page {
  background: $palette-primary-dark !important;
}
</style>

<script setup>
import MainHeader from '@/components/Header';
import FooterWithDeco from '@/components/Footer/FooterWithDeco';
import MainFooter from '@/components/Footer';

// eslint-disable-next-line vue/no-setup-props-destructure
const { invert, navScroll, dedicated } = defineProps({
  invert: {
    type: Boolean,
    default: false,
  },
  navScroll: {
    type: Boolean,
    default: false,
  },
  dedicated: {
    type: Boolean,
    default: false,
  },
});
</script>
