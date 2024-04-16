<template>
  <div>
    <main-container nav-scroll>
      <section id="home">
        <banner />
      </section>
<!--      <section>-->
<!--        <company-logo />-->
<!--      </section>-->
      <section :class="!isMobile && 'space-top-short'">
        <counter />
      </section>
      <section id="feature" :class="isMobile ? 'space-top-short' : 'space-top'">
        <feature />
      </section>
      <section id="testimonials" class="space-bottom-testi">
        <testimonials />
      </section>
      <section id="pricing" class="space-top">
        <pricing-plan />
      </section>
<!--      <section id="faq" class="space-top-short">-->
<!--        <faq />-->
<!--      </section>-->
<!--      <section class="space-top-short space-bottom-short">-->
<!--        <news-event />-->
<!--      </section>-->
      <hidden point="mdDown">
        <page-nav />
      </hidden>
      <hidden point="mdDown">
<!--        <notification />-->
      </hidden>
    </main-container>
  </div>
</template>

<style scoped lang="scss">
@function section-margin($margin) {
  @return $margin * 20;
}
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
.space-bottom {
  margin-bottom: section-margin($spacing1);
  @include breakpoints-down(sm) {
    margin-bottom: section-margin(6px);
  }
}
.space-bottom-testi {
  @include breakpoints-up(md) {
    margin-bottom: section-margin($spacing1);
  }
}
.space-bottom-short {
  margin-bottom: section-margin($spacing1 * 0.5);
}
.space-top {
  margin-top: section-margin($spacing1);
  @include breakpoints-down(sm) {
    margin-top: section-margin(6px);
  }
}
.space-top-short {
  margin-top: section-margin($spacing1 * 0.5);
}
.container-wrap {
  margin-top: -40px;
  > section {
    position: relative;
  }
}
</style>

<script>
import { onMounted } from 'vue';
import { useI18n } from 'vue-i18n';
import MainContainer from '@/components/MainContainer';
import Banner from '@/components/Banner';
import CompanyLogo from '@/components/CompanyLogo';
import Counter from '@/components/Counter';
import Feature from '@/components/Feature';
import Testimonials from '@/components/Testimonials';
import PricingPlan from '@/components/PricingPlan';
import Faq from '@/components/Faq';
import NewsEvent from '@/components/NewsEvent';
import Hidden from '@/components/Hidden';
import PageNav from '@/components/PageNav';
import Notification from '@/components/Notification';
import brand from '@/assets/text/brand';
import { defineNuxtComponent, useRouter, useCookie } from '#app';

export default defineNuxtComponent({
  components: {
    MainContainer,
    Banner,
    CompanyLogo,
    Counter,
    Feature,
    Testimonials,
    PricingPlan,
    Faq,
    NewsEvent,
    PageNav,
    Hidden,
    Notification,
  },
  setup() {
    // push route to the stored cookie languages only for index page
    const router = useRouter();
    const storedLang = useCookie('i18n_redirected');
    const i18nLocale = useI18n();

    const defaultLocale = '/' + i18nLocale.fallbackLocale.value;
    onMounted(() => {
      const rootUrl = document.location.pathname === '/' || document.location.pathname === defaultLocale;
      if (storedLang.value && rootUrl) {
        router.push({ path: `/${storedLang.value}` });
      }
    });
  },
  head() {
    return {
      title: brand.saas.name + ' - Home Page',
    };
  },
  computed: {
    isTablet() {
      const mdDown = this.$vuetify.display.mdAndDown;
      return mdDown;
    },
    isMobile() {
      const smDown = this.$vuetify.display.smAndDown;
      return smDown;
    },
  },
});
</script>
