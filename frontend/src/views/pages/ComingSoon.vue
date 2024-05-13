<template>
    <div class="main-container maintenance-wrapper">
        <div class="content-wrapper">
            <div class="container-fluid">
                <div class="row align-items-center">
                    <div class="col-lg-6 left-bg"></div>
                    <div class="col-lg-6 right-bg">
                        <div class="countdown-wrapper-maintenance section-space--ptb_60">
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="maintenance-logo text-center">
                                        <img src="../../assets/img/logo/logo-dark.png" alt="">
                                    </div>
                                </div>
                                <div class="col-lg-12">
                                    <div class="maintenance-title text-center">
                                        <h3 class="section-title font-weight--bold mb-15">{{ text.title}}</h3>
                                    </div>
                                </div>
                                <div class="col-sm-10 m-auto">
                                    <div class="timer text-center">
                                        <div class="countdown-deals counter-style--one">
                                            <Countdown deadline="june 31, 2024" />
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-8 col-sm-8 mx-auto">
                                    <div class="maintenance-newsletter">
                                        <div class="newsletter-form--two text-center">
                                            <p>{{ text.subtitle }}</p>
                                            <form id="coming-soon-form" ref="form" method="post" @submit.prevent="handleSubmit">
                                                <input name="name" type="text" :placeholder=text.name required>
                                                <input name="email" type="email" :placeholder=text.email required>
                                                <button class="ht-btn ht-btn-md">{{text.submit}}</button>
                                            </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "@/axios.js";
    import Countdown from "@/components/Countdown.vue"
    import textData from '../../assets/text.json'
    export default {
        name: 'ComingSoon',
        data() {
            return {
              text: textData.comingSoon
            }
        },
        components: {
            Countdown,
        },
      methods: {
          async handleSubmit() {
              const formData = new FormData(this.$refs.form);
              try {
                  const response = await axios.post('/coming-soon/', formData);
                  if (response.ok) {
                      console.log('Form submitted successfully');
                      this.$refs.form.reset();
                  }
              } catch (error) {
                  console.error(error);
                  console.log('Form submission failed');
              }
          }
      }
    }
</script>
