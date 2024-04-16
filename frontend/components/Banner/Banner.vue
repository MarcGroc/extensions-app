<template>
  <div class="root">
    <v-dialog
      v-model="dialog"
      max-width="690"
    >
      <v-card class="video-popup">
        <v-card-title class="headline">
          <h2 class="text-h6">
            {{ $t('saasLanding.banner_title') }}
            <v-btn variant="flat" icon @click="handleVideoClose()">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </h2>
        </v-card-title>
        <div v-if="yt.use" class="text-center mx-auto py-4">
          <YouTube
            ref="youtube"
            :src="videoId"
            :vars="playerVars"
            :width="640"
            :height="360"
            class="youtube"
            @ready="onReady"
          />
        </div>
      </v-card>
    </v-dialog>
    <div class="decoration">
      <svg class="left-deco">
        <use xlink:href="/images/saas/deco-bg-left.svg#main" />
      </svg>
      <svg class="right-deco">
        <use xlink:href="/images/saas/deco-bg-right.svg#main" />
      </svg>
    </div>
    <v-container :class="{ fixed: isDesktop }">
      <div class="slider-wrap">
        <div class="text">
          <h3 class="use-text-title">
            {{ $t('saasLanding.banner_title') }}
            <strong>
              {{ $t('saasLanding.banner_titlestrong') }}
            </strong>
          </h3>
          <p class="use-text-subtitle">
            {{ $t('saasLanding.banner_subtitle') }}
          </p>
          <div class="btn-area">
            <v-btn
              variant="text"
              class="play-btn"
              size="large"
              @click="handleVideoOpen()"
            >
              <span class="icon">
                <i class="ion-ios-play-outline" />
              </span>
              {{ $t('saasLanding.banner_watchvideo') }}
            </v-btn>
            <v-btn
              :to="localePath(link.saas.register)"
              color="secondary"
              size="large"
            >
              {{ $t('saasLanding.getstarted') }}
            </v-btn>
          </div>
        </div>
        <div class="illustration">
          <img :src="imgAPI.saas[7]" alt="illustration">
        </div>
      </div>
    </v-container>
    <div class="deco">
      <hidden point="mdDown">
        <div :class="{ hide: hide }" class="deco-inner">
          <div class="wave wave-one" />
          <div class="wave wave-two" />
        </div>
      </hidden>
      <div class="wave wave-cover" />
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import './banner-style.scss';
</style>

<script>
import youtube from '@/config/youtube';
import imgAPI from '@/assets/images/imgAPI';
import link from '@/assets/text/link';
import { useLocalePath } from '#imports';
import Hidden from '../Hidden';

export default {
  setup() {
    const localePath = useLocalePath();
    return {
      localePath,
    };
  },
  components: {
    Hidden,
  },
  data() {
    return {
      videoId: 'KxZAdEGpYAw',
      hide: false,
      link,
      imgAPI,
      dialog: false,
      player: null,
      playerVars: {
        autoplay: 0,
        controls: 1,
        rel: 0,
        showinfo: 1,
        mute: 0,
        origin: 'https://localhost:8008',
      },
      yt: youtube,
    };
  },
  computed: {
    isDesktop() {
      const lgUp = this.$vuetify.display.lgAndUp;
      return lgUp;
    },
  },
  methods: {
    handleVideoOpen() {
      if (this.yt.use) {
        this.dialog = true;
      }
    },
    onReady() {
      this.$refs.youtube.playVideo();
    },
    handleVideoClose() {
      this.dialog = false;
      this.$refs.youtube.pauseVideo();
    },
  },
};
</script>
