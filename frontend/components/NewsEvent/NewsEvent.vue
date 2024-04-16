<template>
  <div class="root">
    <div v-if="loaded" class="carousel">
      <splide :options="settings">
        <splide-slide
          v-for="(item, index) in newsContent"
          :key="index"
        >
          <div class="item">
            <news-card
              :img="item.img"
              :text="item.text"
              :type="item.type"
            />
          </div>
        </splide-slide>
      </splide>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import './news-event-style.scss';
</style>

<script>
import { Splide, SplideSlide } from '@splidejs/vue-splide';
import imgAPI from '@/assets/images/imgAPI';
import NewsCard from '../Cards/News';

const newsContent = [
  {
    text:
      'Sed imperdiet enim ligula, vitae viverra justo porta vel. Duis eget felis bibendum, pretium mi sed, placerat ante.',
    img: imgAPI.photo[1],
    type: 'caption_news',
  },
  {
    text:
      'Sed imperdiet enim ligula, vitae viverra justo porta vel. Duis eget felis bibendum, pretium mi sed, placerat ante.',
    img: imgAPI.photo[2],
    type: 'caption_news',
  },
  {
    text:
      'Sed imperdiet enim ligula, vitae viverra justo porta vel. Duis eget felis bibendum, pretium mi sed, placerat ante.',
    img: imgAPI.photo[3],
    type: 'caption_event',
  },
  {
    text:
      'Sed imperdiet enim ligula, vitae viverra justo porta vel. Duis eget felis bibendum, pretium mi sed, placerat ante.',
    img: imgAPI.photo[4],
    type: 'caption_news',
  },
  {
    text:
      'Sed imperdiet enim ligula, vitae viverra justo porta vel. Duis eget felis bibendum, pretium mi sed, placerat ante.',
    img: imgAPI.photo[5],
    type: 'caption_event',
  },
  {
    text:
      'Sed imperdiet enim ligula, vitae viverra justo porta vel. Duis eget felis bibendum, pretium mi sed, placerat ante.',
    img: imgAPI.photo[6],
    type: 'caption_news',
  },
];

export default {
  components: {
    NewsCard,
    Splide,
    SplideSlide,
  },
  data() {
    return {
      loaded: false,
      newsContent,
      settings: {
        pagination: true,
        type: 'loop',
        speed: 500,
        perPage: 2,
        perMove: 1,
        arrows: false,
        autoplay: true,
        interval: 5000,
        direction: 'ltr',
        reducedMotion: {
          speed: 500,
          rewindSpeed: 1000,
          autoplay: true,
        },
        breakpoints: {
          700: {
            perPage: 1,
          },
        },
      },
    };
  },
  mounted() {
    this.loaded = true;
    setTimeout(() => {
      if (this.$vuetify.locale.isRtl) {
        this.settings.direction = 'rtl';
      } else {
        this.settings.direction = 'ltr';
      }
    }, 100);
  },
};
</script>
