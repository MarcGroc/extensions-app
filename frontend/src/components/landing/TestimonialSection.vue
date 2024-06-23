<template>
  <div
    class="testimonial-slider-area section-space--pb_120 section-space-custom-pt bg-gray"
    id="reviews"
  >
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="section-title-wrapper text-center section-space--mb_60">
            <h2 class="section-title font-weight--blod wow move-up">
              {{ text.title }}
            </h2>
          </div>
        </div>
      </div>
      <Testimonial />
    </div>
  </div>
</template>

<script>
import Testimonial from "@/components/landing/Testimonial.vue";
import textData from "../../assets/text_landing_pl.json";
export default {
  data() {
    return {
      text: textData.reviews,
    };
  },
  components: {
    Testimonial,
  },
};
</script>
