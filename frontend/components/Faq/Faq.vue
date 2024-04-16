<template>
  <div class="root">
    <v-container class="fixed-width">
      <v-row class="spacing6">
        <v-col md="6" class="pa-6">
          <title-main :align="isMobile ? 'center' : 'left'">
            <strong>
              Najczęściej zadawane pytania
            </strong>
          </title-main>
          <p
            class="text use-text-subtitle2"
            :class="[isMobile ? 'text-center' : 'text-left']"
          >
            {{ $t('saasLanding.faq_subtitle') }}
          </p>
          <hidden point="smDown">
            <div class="illustration">
              <parallax-medium />
              <img src="/images/saas/faq.png" alt="illustration">
            </div>
          </hidden>
        </v-col>
        <v-col md="6" cols="12" class="pa-6">
          <div class="accordion">
            <v-expansion-panels
              v-model="panel"
              variant="accordion"
              active-class="expanded"
            >
              <v-expansion-panel
                v-for="(item, index) in faqData"
                :key="index"
                class="paper"
              >
                <v-expansion-panel-title class="content">
                  <p class="heading">
                    {{ item.q }}
                  </p>
                </v-expansion-panel-title>
                <v-expansion-panel-text class="detail">
                  <p>
                    {{ item.a }}
                  </p>
                </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<style lang="scss" scoped>
@import 'faq-style.scss';
</style>

<script>
import Hidden from '../Hidden';
import ParallaxMedium from '../Parallax/Medium';
import Title from '../Title';

const faqData = [
  {
    q: 'How does it work?',
    a:
      "It's very easy just signup and ask your question.",
  },
  {
    q: 'How much does it cost?',
    a:
      'Pay as You go. No subscription, no hidden fees.',
  },
  {
    q: 'Will my results be saved?',
    a:
      'Yes, everything is saved in side panel. ',
  },
];

export default {
  components: {
    Hidden,
    ParallaxMedium,
    'title-main': Title,
  },
  data() {
    return {
      panel: 0,
      faqData,
    };
  },
  computed: {
    isMobile() {
      const smDown = this.$vuetify.display.smAndDown;
      return smDown;
    },
  },
};
</script>
