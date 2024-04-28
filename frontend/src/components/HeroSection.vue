<template>
    <div class="hero-ebook hero-swiper-btn" id="home">
        <div class="container_f1">
            <div class="swiper-wrapper">
              <div class="hero-item" :style="bgImg">
                            <div class="hero-content">
                                <h6 class="hero-content-subtitle">{{ text.contentsubtitleh6 }}</h6>
                                <h2 class="h1 hero-content-title">{{text.contentsubtitleh2}}</h2>
                                <router-link to="/register" class="btn btn--black">{{ text.ctabutton }}</router-link>
                            </div>
                            <div class="hero-thumb">
                                <img src="../assets/img/logo/djavue_logo.jpg" class="img-fluid" alt="hero thumb">
                            </div>
                        </div>
<!--                <swiper-->
<!--                    :speed="1000"-->
<!--                    :loop="true"-->
<!--                    :navigation="swiperOptions.navigation"-->
<!--                >-->
<!--                    <swiper-slide class="swiper-slide" :style="bgImg">-->
<!--                        -->
<!--                    </swiper-slide>-->
<!--                    <swiper-slide class="swiper-slide" :style="bgImg">-->
<!--                        <div class="hero-item">-->
<!--                            <div class="hero-content">-->
<!--                                <h6 class="hero-content-subtitle">{{ text.contentsubtitleh6 }}</h6>-->
<!--                                <h2 class="h1 hero-content-title">{{text.contentsubtitleh2}}</h2>-->
<!--                                <router-link to="/register" class="btn btn&#45;&#45;black">{{ text.ctabutton }}</router-link>-->
<!--                            </div>-->
<!--                            <div class="hero-thumb">-->
<!--                                <img src="../assets/img/hero/hero-thumb1.png" class="img-fluid" alt="hero thumb">-->
<!--                            </div>-->
<!--                        </div>-->
<!--                    </swiper-slide>-->
<!--                    <swiper-slide class="swiper-slide" :style="bgImg">-->
<!--                        <div class="hero-item">-->
<!--                            <div class="hero-content">-->
<!--                                <h6 class="hero-content-subtitle">it's time to change something</h6>-->
<!--                                <h2 class="h1 hero-content-title">Learn to Design Beautiful & Simple Websites</h2>-->
<!--                                <router-link to="" class="btn btn&#45;&#45;black">Get the book your way</router-link>-->
<!--                            </div>-->
<!--                            <div class="hero-thumb">-->
<!--                                <img src="../assets/img/hero/ebook/ebook-hero-thumb1.png" class="img-fluid" alt="hero thumb">-->
<!--                            </div>-->
<!--                        </div>-->
<!--                    </swiper-slide>-->
<!--                </swiper>-->
            </div>
        </div>
    </div>
</template>

<script>
    import { Swiper, SwiperSlide } from "swiper/vue"
    // import SwiperCore, { Navigation } from 'swiper/core'
    // SwiperCore.use([Navigation])

    import "swiper/css"
    import textData from '../assets/text.json'


    export default {
        components: {
            // Swiper,
            // SwiperSlide
        },

        data() {
            return {
                text: textData.hero,
                bgImg: {
                    // backgroundImage: `url(${require("../assets/img/hero/hero-bg.jpg")})`
                    backgroundImage: "src/assets/img/hero/hero-bg.jpg"
                },
                // swiperOptions: {
                //     navigation: {
                //         nextEl: '.swiper-button-next',
                //         prevEl: '.swiper-button-prev'
                //     },
                // }
            };
        }
    };
</script>

<style scoped>

</style>
