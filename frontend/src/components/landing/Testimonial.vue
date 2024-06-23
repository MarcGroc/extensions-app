<template>
  <div class="row">
    <div class="col-lg-12">
      <div class="testimonial-slider">
        <div class="testimonial-slider__container">
          <div class="testimonial-slider__wrapper">
            <swiper
              :speed="800"
              :loop="true"
              :slidesPerView="2"
              :spaceBetween="30"
              :pagination="swiperOptions.pagination"
              :breakpoints="swiperOptions.breakpoints"
            >
              <swiper-slide class="testimonial-slider__three wow move-up">
                <div class="testimonial-slider__media">
                  <img
                    src="../../assets/img/avatar/avatar-01-120x120.png"
                    class="img-fluid"
                    alt=""
                  />
                </div>
                <div class="testimonial-slider__text">
                  {{ text.review1Text }}
                </div>
                <div class="testimonial-slider__author">
                  <h6 class="name">{{ text.review1Name }}</h6>
                </div>
              </swiper-slide>
              <swiper-slide class="testimonial-slider__three wow move-up">
                <div class="testimonial-slider__media">
                  <img
                    src="../../assets/img/avatar/avatar-02-120x120.png"
                    class="img-fluid"
                    alt=""
                  />
                </div>
                <div class="testimonial-slider__text">
                  {{ text.review2Text }}
                </div>
                <div class="testimonial-slider__author">
                  <h6 class="name">{{ text.review2Name }}</h6>
                </div>
              </swiper-slide>
              <swiper-slide class="testimonial-slider__three wow move-up">
                <div class="testimonial-slider__media">
                  <img
                    src="../../assets/img/avatar/avatar-03-120x120.png"
                    class="img-fluid"
                    alt=""
                  />
                </div>
                <div class="testimonial-slider__text">
                  {{ text.review3Text }}
                </div>
                <div class="testimonial-slider__author">
                  <h6 class="name">{{ text.review3Name }}</h6>
                </div>
              </swiper-slide>
              <swiper-slide class="testimonial-slider__three wow move-up">
                <div class="testimonial-slider__media">
                  <img
                    src="../../assets/img/avatar/avatar-07-120x120.png"
                    class="img-fluid"
                    alt=""
                  />
                </div>
                <div class="testimonial-slider__text">
                  {{ text.review4Text }}
                </div>
                <div class="testimonial-slider__author">
                  <h6 class="name">{{ text.review4Name }}</h6>
                </div>
              </swiper-slide>
            </swiper>
          </div>
        </div>
        <div
          class="swiper-pagination swiper-pagination-1 section-space--mt_60 text-center"
        ></div>
      </div>
    </div>
  </div>
</template>

<script>
import SwiperCore from "swiper/core";
import { Swiper, SwiperSlide } from "swiper/vue";
import textData from "../../assets/text_landing_pl.json";
import { Pagination } from "swiper/modules";
SwiperCore.use([Pagination]);

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      text: textData.reviews,
      swiperOptions: {
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
        breakpoints: {
          1499: {
            slidesPerView: 3,
          },

          991: {
            slidesPerView: 2,
          },

          767: {
            slidesPerView: 1,
          },
        },
      },
    };
  },
};
</script>
