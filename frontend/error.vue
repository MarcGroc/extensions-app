<template>
  <theme-wrapper theme="violeta">
    <v-app>
      <main-container invert dedicated>
        <Error
          error-code="errObj.statusCode"
          :text="$t('common.404')"
        />
      </main-container>
    </v-app>
  </theme-wrapper>
</template>

<style lang="scss" scoped>
  div {}
</style>

<script>
import brand from './assets/text/brand';
import ThemeWrapper from './components/ThemeWrapper';
import MainContainer from './components/MainContainer';
import Error from './components/Error';
import { useHead, useError, defineNuxtComponent } from '#app';

export default defineNuxtComponent({
  components: {
    MainContainer,
    ThemeWrapper,
    Error,
  },
  setup() {
    const error = useError();
    const errObj = error._object.error;
    useHead({
      title: errObj.statusCode === 404
        ? `${brand.saas.name} - Not Found`
        : `${brand.saas.name} - An error occurred`,
    });
  },
});
</script>
