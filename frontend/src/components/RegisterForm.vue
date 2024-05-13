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
                        <span class="section-text_left wow move-up">{{text.subtitle}}</span>
                       <div class="col-md-6 text-center text-md-end">
                            <ul class="list ht-social-networks flat-round ">
                                <li class="item">
                                    <a href="https://localhost:8000/accounts/facebook/login" target="_blank" class="social-link"> <i class="fab fa-facebook social-link-icon"></i> </a>
                                </li>
                                <li class="item">
                                    <a href="https://localhost:8000/accounts/google/login" target="_blank" class="social-link"> <i class="fab fa-google social-link-icon"></i> </a>
                                </li>
                                <li class="item">
                                    <a href="https://localhost:8000/accounts/instagram/login" target="_blank" class="social-link"> <i class="fab fa-instagram social-link-icon"></i> </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <span class="section-text_left wow move-up register_or">{{text.register_or}}</span>
                    </div>
                    <div class="contact-from-wrapper wow move-up">
                        <form id="register-form" ref="form"  method="post" @submit.prevent="handleSubmit">
                            <div class="contact-page-form">
                                <div class="contact-input">
                                <div class="contact-inner">
                                    <input name="name" type="text" :placeholder="text.name + ' *'" required>
                                </div>
                                <div class="contact-inner">
                                    <input name="email" type="email" :placeholder="text.email + ' *'" required>
                                </div>
                                </div>
                                <div class="contact-inner">
                                    <input id="password" name="con_password" type="password" :placeholder="text.password + ' *'" required>
                                </div>
                                <div class="contact-inner">
                                    <input id="confirm_password" name="confirm_password" type="password" :placeholder="text.confirm + ' *'" required>
                                    <span id="password_error" class="error-message"></span>
                                </div>
                                <div class="checkbox">
                                    <input type="checkbox" id="terms" v-model="acceptTerms" required>
                                    <label for="terms">  Akceptuję <a href="/terms" target="_blank">regulamin</a> *</label>
                                </div>
                                <div class="contact-submit-btn">
                                    <button class="ht-btn ht-btn-md" type="submit">{{ text.submit }}</button>
                                </div>
                            </div>
                        </form>
                    </div>
                   <div class="row">
                    <div class="col-12">
                      <span class="section-text_left wow move-up">{{text.alreadyAccount}} <router-link class="nav-link hover-style-link hover-style-link--green" to="/login">{{text.login}} >>></router-link></span>
                    </div>
                  </div>
                </div>
                <div class="col-lg-5 order-1 order-lg-2">
                    <div class="peatures_image-wrap section-space--mb_40">
                        <div class="image text-center wow move-up">
                            <img class="img-fluid" src="../assets/img/forms/contact-form-image-01.png" alt="contact thumb">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import textData from '../assets/text.json'
    import axios from "@/axios.js";

    export default {
      name: 'RegisterForm',
      data() {
        return {
          text: textData.register,
          acceptTerms: false
        }
      },
      methods: {
        async handleSubmit() {
          const password = this.$refs.form.password.value;
          const confirm_password = this.$refs.form.confirm_password.value;
          if (password !== confirm_password) {
              password_error.textContent = "Hasło musi być identyczne.";
              return false;
          } else {
            if (this.$refs.form.checkValidity() && this.acceptTerms) {
              const formData = {
                name: this.$refs.form.name.value,
                email: this.$refs.form.email.value,
                password: this.$refs.form.password.value
              }
              try {
                const response = await axios.post('/dj-rest-auth/registration/', formData);
                if (response.ok) {
                  console.log('Form submitted successfully');
                  this.$refs.form.reset();
                  this.acceptTerms = false;
                }
              } catch (error) {
                console.error(error);
              }
            }
              password_error.textContent = "Na podany addres email został wysłany link do aktywacji konta.";
          }
          return true;
        }
      }
    }
</script>
<style scoped>
.error-message {
    color: red;
    font-size: 14px;
    padding-top: 5px;
.checkbox {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}
}
</style>
