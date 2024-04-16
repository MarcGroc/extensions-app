<template>
  <div class="parallax-wrap">
    <div v-if="loaded" class="inner-parallax medium">
      <scroll-parallax
        :speed="0.15"
        down
        direction="y"
      >
        <div class="figure">
          <div>
            <svg class="plus">
              <use xlink:href="/images/decoration/plus.svg#main" />
            </svg>
          </div>
        </div>
      </scroll-parallax>
      <scroll-parallax
        :speed="0.12"
        down
        direction="y"
      >
        <div class="figure">
          <div>
            <svg class="circle">
              <use xlink:href="/images/decoration/circle.svg#main" />
            </svg>
          </div>
        </div>
      </scroll-parallax>
      <scroll-parallax
        :speed="0.14"
        down
        direction="y"
      >
        <div class="figure">
          <div>
            <svg class="zigzag">
              <use xlink:href="/images/decoration/zigzag.svg#main" />
            </svg>
          </div>
        </div>
      </scroll-parallax>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import './parallax-style.scss';
</style>

<script>
export default {
  data() {
    return {
      loaded: false,
    };
  },
  mounted() {
    this.loaded = true;
  },
};
</script>
