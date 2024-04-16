<template>
  <div class="root">
    <div class="decoration">
      <svg fill="#cccccc">
        <use xlink:href="/images/saas/deco-med-bg.svg#main" />
      </svg>
    </div>
    <v-container :class="{ fixed: isDesktop }">
      <title-main align="center">
        <strong>
          {{ $t('saasLanding.pricing_title') }}
        </strong>
      </title-main>
      <p class="subtitle use-text-subtitle2 text-center">
        {{ $t('saasLanding.pricing_subtitle') }}
      </p>
      <div class="pricing-wrap">
        <section>
          <div
            data-aos="fade-up"
            data-aos-offset="500"
            data-aos-delay="200"
            data-aos-duration="400"
            class="item"
          >
            <pricing-card
              :price="0"
              :feature-list="feature.trial"
              title="Trial"
              desc="10 Darmowych kredytów."
              type="basic"
            />
          </div>
          <div
            data-aos="fade-up"
            data-aos-offset="500"
            data-aos-delay="400"
            data-aos-duration="400"
            class="item best"
          >
            <pricing-card
              :price="0"
              :feature-list="feature.best"
              title="Basic"
              desc="Doładuj konto i odkryj nieznane odpowiedzi."
              type="value"
            />
          </div>
          <div
            data-aos="fade-up"
            data-aos-offset="500"
            data-aos-delay="600"
            data-aos-duration="400"
            class="item"
          >
            <pricing-card
              :price="54"
              :feature-list="feature.premium"
              title="Premium"
              desc="Doładuj konto i odkryj nieznane odpowiedzi."
            />
          </div>
          <div
            data-aos="fade-in"
            data-aos-offset="500"
            data-aos-delay="800"
            data-aos-duration="400"
            class="item"
          >
            <pricing-card
              :price="99"
              :feature-list="feature.enterprise"
              title="Premium +"
              desc="Potrzbujesz usługi dopasowanej do twoich potrzeb?"
            />
          </div>
        </section>
      </div>
    </v-container>
  </div>
</template>

<style lang="scss" scoped>
@import './pricing-plan-style.scss';
</style>

<script>
import AOS from 'aos';
import Title from '../Title';
import PricingCard from '../Cards/Pricing';

const featureList = {
  trial: [
    'Pełna wersja',
    'Darmowe kredyty',
    'Bez subskrypcji',
  ],
  best: [
    'Doładuj konto i korzystaj',
    'Bez ukrytych opłat, bez subskrypcji',
    '30 dniowa historia',
    '5 pytań uzupełniających',
  ],
  premium: [
    'Zamień odpowiedź w ilustrację',
    'Bez ukrytych opłat, bez subskrypcji',
    '360 dniowa historia',
    '15 pytań uzupełniających',
  ],
  enterprise: [
    'Szukasz personalizowanej usługi?',
    'Porozmawiajmy',
    'Wyślij pytanie przez formularz',
  ],
};

export default {
  components: {
    'title-main': Title,
    PricingCard,
  },
  data() {
    return {
      feature: featureList,
    };
  },
  computed: {
    isDesktop() {
      const lgUp = this.$vuetify.display.lgAndUp;
      return lgUp;
    },
  },
  mounted() {
    AOS.init({
      once: true,
    });
  },
};
</script>
