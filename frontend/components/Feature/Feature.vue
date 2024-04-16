<template>
  <div class="root">
    <div class="decoration">
      <svg class="wave">
        <use xlink:href="/images/saas/deco-bg.svg#main" />
      </svg>
    </div>
    <v-container :class="{ fixed: isDesktop }">
      <div class="item">
        <v-row>
          <v-col
            :order="isMobile ? 'last' : 'first'"
            cols="12"
            md="6"
          >
            <div class="illustration-left">
              <section v-if="loaded" class="parallax-wrap">
                <div class="viewport">
                  <figure class="figure screen">
                    <img :src="imgAPI.saas[0]" alt="screen">
                  </figure>
                </div>
              </section>
              <client-only>
                <section
                  v-if="loaded && !isMobile"
                  class="parallax-wrap"
                >
                  <scroll-parallax
                    :speed="isMobile ? 0 : 0.1"
                    direction="y"
                  >
                    <div class="viewport">
                      <figure class="figure graphic">
                        <img :src="imgAPI.saas[1]" alt="illustration">
                      </figure>
                    </div>
                  </scroll-parallax>
                </section>
              </client-only>
              <parallax-medium />
            </div>
          </v-col>
          <v-col
            :order="isMobile ? 'first' : 'last'"
            cols="12"
            md="6"
          >
            <div
              data-aos="fade-left"
              data-aos-offset="-100"
              data-aos-delay="500"
              data-aos-duration="500"
            >
              <div class="desc">
                <title-main :align="isMobile ? 'center' : 'left'">
                  <span>
                    {{ $t('saasLanding.feature_title1') }}
                    <strong>
                      {{ $t('saasLanding.feature_titlestrong1') }}
                    </strong>
                  </span>
                </title-main>
                <h6 class="use-text-subtitle2" :class="[isMobile ? 'text-center' : 'text-left']">
                  {{ $t('saasLanding.feature_desc1') }}
                </h6>
                <v-btn color="primary" size="large" class="btn" :to="localePath(link.saas.register)">
                  {{ $t('saasLanding.getstarted') }}
                </v-btn>
              </div>
            </div>
          </v-col>
        </v-row>
      </div>
      <div class="item">
        <v-row>
          <v-col md="6" cols="12">
            <div
              data-aos="fade-right"
              data-aos-offset="-100"
              data-aos-delay="500"
              data-aos-duration="500"
            >
              <div class="desc">
                <title-main :align="isMobile ? 'center' : 'right'">
                  <span>
                    {{ $t('saasLanding.feature_title1') }}
                    <strong>
                      {{ $t('saasLanding.feature_titlestrong2') }}
                    </strong>
                  </span>
                </title-main>
                <h6 class="use-text-subtitle2" :class="[isMobile ? 'text-center' : 'text-end']">
                  {{ $t('saasLanding.feature_desc2') }}
                </h6>
                <div :class="[isMobile ? 'text-center' : 'text-end']">
                  <v-btn color="primary" size="large" class="btn" :to="localePath(link.saas.register)">
                    {{ $t('saasLanding.getstarted') }}
                  </v-btn>
                </div>
              </div>
            </div>
          </v-col>
          <v-col md="6" cols="12">
            <div class="illustration-right">
              <section v-if="loaded" class="parallax-wrap">
                <div class="viewport">
                  <figure class="figure screen">
                    <img :src="imgAPI.saas[2]" alt="screen">
                  </figure>
                </div>
              </section>
              <section
                v-if="loaded && !isMobile"
                class="parallax-wrap"
              >
                <scroll-parallax
                  :speed="isMobile ? 0 : 0.1"
                  direction="y"
                >
                  <div class="viewport">
                    <figure class="graphic">
                      <img :src="imgAPI.saas[3]" alt="illustration">
                    </figure>
                  </div>
                </scroll-parallax>
              </section>
              <parallax-medium />
            </div>
          </v-col>
        </v-row>
      </div>
<!--      <div class="item last">-->
<!--        <title-main align="center">-->
<!--          <span>-->
<!--            {{ $t('saasLanding.feature_title3') }}-->
<!--            <strong>-->
<!--              {{ $t('saasLanding.feature_titlestrong3') }}-->
<!--            </strong>-->
<!--          </span>-->
<!--        </title-main>-->
<!--        <div class="tab">-->
<!--          <v-row class="spacing6">-->
<!--            <v-col-->
<!--              v-if="!isMobile"-->
<!--              class="pa-6"-->
<!--              md="1"-->
<!--              cols="12"-->
<!--            />-->
<!--            <v-col lg="10" cols="12" class="pa-6">-->
<!--              <v-tabs-->
<!--                v-model="tab"-->
<!--                class="tabs"-->
<!--                color="primary"-->
<!--                align-tabs="center"-->
<!--              >-->
<!--                <v-tab value="tab-1" class="tab-label">-->
<!--                  Pellentesque-->
<!--                </v-tab>-->
<!--                <v-tab value="tab-2" class="tab-label">-->
<!--                  Donec-->
<!--                </v-tab>-->
<!--                <v-tab value="tab-3" class="tab-label">-->
<!--                  Vestibulum-->
<!--                </v-tab>-->
<!--              </v-tabs>-->
<!--              <v-window v-model="tab">-->
<!--                <v-window-item value="tab-1">-->
<!--                  <div class="tab-content">-->
<!--                    <section>-->
<!--                      <h6 class="text-center use-text-subtitle2">-->
<!--                        {{ $t('saasLanding.feature_desc3') }}-->
<!--                      </h6>-->
<!--                      <div class="illustration-center">-->
<!--                        <figure class="figure screen">-->
<!--                          <img :src="imgAPI.saas[4]" alt="screen">-->
<!--                        </figure>-->
<!--                      </div>-->
<!--                    </section>-->
<!--                  </div>-->
<!--                </v-window-item>-->
<!--                <v-window-item value="tab-2">-->
<!--                  <div class="tab-content">-->
<!--                    <section>-->
<!--                      <h6 class="text-center use-text-subtitle2">-->
<!--                        {{ $t('saasLanding.feature_desc3') }}-->
<!--                      </h6>-->
<!--                      <div class="illustration-center">-->
<!--                        <figure class="figure screen">-->
<!--                          <img :src="imgAPI.saas[8]" alt="screen">-->
<!--                        </figure>-->
<!--                      </div>-->
<!--                    </section>-->
<!--                  </div>-->
<!--                </v-window-item>-->
<!--                <v-window-item value="tab-3">-->
<!--                  <div class="tab-content">-->
<!--                    <section>-->
<!--                      <h6 class="text-center use-text-subtitle2">-->
<!--                        {{ $t('saasLanding.feature_desc3') }}-->
<!--                      </h6>-->
<!--                      <div class="illustration-center">-->
<!--                        <figure class="figure screen">-->
<!--                          <img :src="imgAPI.saas[6]" alt="screen">-->
<!--                        </figure>-->
<!--                      </div>-->
<!--                    </section>-->
<!--                  </div>-->
<!--                </v-window-item>-->
<!--              </v-window>-->
<!--              <parallax-large />-->
<!--            </v-col>-->
<!--          </v-row>-->
<!--        </div>-->
<!--      </div>-->
    </v-container>
  </div>
</template>

<style lang="scss" scoped>
@import './feature-style.scss';
</style>

<script>
import AOS from 'aos';
import imgAPI from '@/assets/images/imgAPI';
import ParallaxMedium from '../Parallax/Medium';
import ParallaxLarge from '../Parallax/Large';
import Title from '../Title';
import link from "@/assets/text/link";

export default {
  components: {
    ParallaxMedium,
    ParallaxLarge,
    'title-main': Title,
  },
  data() {
    return {
      tab: null,
      imgAPI,
      loaded: false,
      link,
    };
  },
  computed: {
    isDesktop() {
      const lgUp = this.$vuetify.display.lgAndUp;
      return lgUp;
    },
    isMobile() {
      const smDown = this.$vuetify.display.smAndDown;
      return smDown;
    },
  },
  mounted() {
    this.loaded = true;
    AOS.init({
      once: true,
    });
  },
};
</script>
