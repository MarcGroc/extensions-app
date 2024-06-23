<template>
  <div
    class="pricing-table-area section-space--ptb_120 theme_bg-2"
    id="pricing"
  >
    <div class="pricing-table-content-area">
      <div class="container-fluid container-fluid--cp-150">
        <div class="row">
          <div class="col-lg-3 col-md-12">
            <div class="price-plan-wrap mt-30 section-space--mb_60">
              <div class="price-plan-title mb-30 wow move-up">
                <h3 class="heading text-white">{{ text.title }}</h3>
              </div>
              <ul class="check-list price-plan-list mb-30 wow move-up">
                <li class="list-item">{{ text.subtitle2 }}</li>
                <li class="list-item">{{ text.subtitle3 }}</li>
                <li class="list-item">{{ text.subtitle4 }}</li>
              </ul>
              <h6 class="sub-heading wow move-up">{{ text.subtitle }}</h6>
            </div>
          </div>
          <div class="col-lg-9 col-md-12">
            <div class="row pricing-table-three">
              <div
                class="col-12 col-sm-6 col-md-6 col-lg-4 col-xl-4 pricing-table wow move-up"
              >
                <div class="pricing-table__inner">
                  <div class="pricing-table__header">
                    <div class="pricing-table__image">
                      <img
                        src="../../assets/img/pricing/pricing-image-01.png"
                        class="img-fluid"
                        alt=""
                      />
                    </div>
                    <h5 class="pricing-table__title">{{ text.price1title }}</h5>
                  </div>
                  <div class="pricing-table__body">
                    <p>{{ text.price1desc }}</p>
                    <p>{{ text.price1desc1 }}</p>
                    <p>{{ text.price1desc2 }}</p>
                  </div>
                  <div class="pricing-table__footer">
                    <a href="/register" class="ht-btn ht-btn-default">{{
                      text.ctabutton
                    }}</a>
                  </div>
                </div>
              </div>
              <div
                class="col-12 col-sm-6 col-md-6 col-lg-4 col-xl-4 pricing-table pricing-table--popular wow move-up"
              >
                <div class="pricing-table__inner">
                  <div class="pricing-table__feature-mark">
                    <span>{{ text.pricing_mark }}</span>
                  </div>
                  <div class="pricing-table__header">
                    <div class="pricing-table__image">
                      <img
                        src="../../assets/img/pricing/pricing-image-02.png"
                        class="img-fluid"
                        alt=""
                      />
                    </div>
                    <h5 class="pricing-table__title">{{ text.price2title }}</h5>
                  </div>
                  <div class="pricing-table__body">
                    <p>{{ text.price2desc }}</p>
                    <p>{{ text.price2desc1 }}</p>
                    <p>{{ text.price2desc2 }}</p>
                  </div>
                  <div class="pricing-table__footer">
                    <a href="/register" class="ht-btn ht-btn-default">{{
                      text.ctabutton
                    }}</a>
                  </div>
                </div>
              </div>
              <!--                            <div class="col-12 col-sm-6 col-md-6 col-lg-4 col-xl-4 pricing-table wow move-up">-->
              <!--                                <div class="pricing-table__inner">-->
              <!--                                    <div class="pricing-table__header">-->
              <!--                                        <div class="pricing-table__image">-->
              <!--                                            <img src="../assets/img/pricing/aeroland-pricing-image-07.png" class="img-fluid" alt="">-->
              <!--                                        </div>-->
              <!--                                        <h5 class="pricing-table__title">Group</h5>-->
              <!--                                    </div>-->
              <!--                                    <div class="pricing-table__body">-->
              <!--                                        <p>Lorem ipsum dolor sit amet, consectetur elit. Suspe ndisse suscipit sagittis leo sitea rem ipsum dolor sit amet, consectetu.</p>-->
              <!--                                    </div>-->
              <!--                                    <div class="pricing-table__footer">-->
              <!--                                        <a href="#" class="ht-btn ht-btn-default">Get started</a>-->
              <!--                                    </div>-->
              <!--                                </div>-->
              <!--                            </div>-->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import textData from "../../assets/text_landing_pl.json";
export default {
  name: "PricingSection",

  data() {
    return {
      text: textData.pricing,
    };
  },
};
</script>
