<template>
    <div class="contact-form-section section-space--ptb_120" id="contact">
        <div class="container">

             <div class="row">
                <div class="col-12">
                  <span class="section-text_left wow move-up"><router-link class="nav-link hover-style-link hover-style-link--green" to="/"><<< Strona główna</router-link></span>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-7 order-2 order-lg-1">
                    <div class="section-title text-left section-space--mb_60">
                        <h2 class="font-weight--bold mb-15 wow move-up">{{ text.title }}</h2>
                        <p class="wow move-up">{{ text.subtitle }}</p>
                        <div class="col-md-6 text-center text-md-end">
                            <ul class="list ht-social-networks flat-round ">
                                <li class="item">
                                    <a href="http://localhost:8000/accounts/facebook/login/" target="_blank" class="social-link"> <i class="fab fa-facebook-f social-link-icon"></i> </a>
                                </li>
                                <li class="item">
                                    <a href="http://localhost:8000/accounts/google/login/" target="_blank" class="social-link"> <i class="fab fa-google social-link-icon"></i> </a>
                                </li>
<!--                                <li class="item">-->
<!--                                    <a href="http://localhost:8000/accounts/instagram/login/" target="_blank" class="social-link"> <i class="fab fa-instagram social-link-icon"></i> </a>-->
<!--                                </li>-->
                            </ul>
                        </div>
                    </div>
                    <div>
                        <span class="section-text_left wow move-up">{{text.login_or}}</span>
                    </div>
                    <div class="contact-from-wrapper wow move-up">
                        <form id="login-form" ref="form" method="post" @submit.prevent="handleSubmit">
                            <div class="contact-page-form">
                                <div class="contact-input">
                                    <div class="contact-inner">
                                        <input name="email" type="email" :placeholder="text.email" required>
                                    </div>
                                    <div class="contact-inner">
                                        <input name="password" type="password" :placeholder="text.password" required>
                                    </div>
                                </div>
                                <div class="contact-submit-btn">
                                    <button class="ht-btn ht-btn-md" type="submit">{{ text.submit }}</button>
                                </div>
                            </div>
                        </form>
                    </div>
                  <div class="row">
                    <div class="col-12">
                      <span class="section-text_left wow move-up">{{text.notAccount}} <router-link class="nav-link hover-style-link hover-style-link--green" to="/register">{{text.register}} >>></router-link></span>
                    </div>
                    <div class="col-12">
                      <span class="section-text_left wow move-up"> <router-link to="/password-reset" class="nav-link hover-style-link hover-style-link--green">{{text.forgot}} >>></router-link></span>
                    </div>
                  </div>
                </div>
                <div class="col-lg-5 order-1 order-lg-2">
                    <div class="peatures_image-wrap section-space--mb_40">
                        <div class="image text-center wow move-up">
                            <img class="img-fluid" src="../assets/img/forms/contact-form-image-01.png" alt="login thumb">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "@/axios.js";

    import textData from '../assets/text.json'

    export default {
      name: 'LoginForm',
      data() {
          return {
            text: textData.login
          }
        },

        methods: {
            async handleSubmit() {
              if (this.$refs.form.checkValidity()) {
                const formData = {
                  email: this.$refs.form.email.value,
                  password: this.$refs.form.password.value,
                };
                try {
                  const response = await axios.post('/dj-rest-auth/login/', formData);
                  if (response.status === 200) {
                    this.$router.push('/');
                    this.$refs.form.reset();
                  }
                } catch (error) {
                  if (error.response) {
                    console.log('Error status:', error.response.status);
                    console.log('Error message:', error.response.statusText);
                  } else {
                    console.error('Error during fetch:', error.message);
                  }
                }
              }
            }
        }
    }
</script>
