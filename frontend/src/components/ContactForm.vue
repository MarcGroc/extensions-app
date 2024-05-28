<template>
  <div class="contact-form-section section-space--ptb_120" id="contact">
    <div class="container">
      <div class="row">
        <div class="col-lg-7 order-2 order-lg-1">
          <div class="section-title text-left section-space--mb_60">
            <h2 class="font-weight--bold mb-15 wow move-up">{{ text.title }}</h2>
            <span class="section-text_left wow move-up">{{ text.subtitle }}</span>
          </div>
          <div class="contact-from-wrapper wow move-up">
            <form id="contact-form" ref="form" method="post" @submit.prevent="handleSubmit">
              <div class="contact-page-form">
                <div class="contact-input">
                  <div class="contact-inner">
                    <input name="name" type="text" :placeholder="text.name + ' *'" required>
                  </div>
                  <div class="contact-inner">
                    <input name="email" type="email" id="email" :placeholder="text.email + ' *'" required>
                  </div>
                </div>
                <div class="contact-inner contact-message">
                  <textarea name="message" :placeholder="text.message + ' *'" required></textarea>
                </div>
                <div class="contact-inner">
                  <span id="confirmation" class="confirmation"></span>
                </div>
                <div class="checkbox">
                  <input type="checkbox" id="terms" v-model="acceptTerms" required>
                  <label for="terms">Akceptuję <a href="/terms" target="_blank">regulamin</a> *</label>
                </div>

                <div class="contact-submit-btn">
                  <button class="ht-btn ht-btn-md" type="submit">{{ text.submit }}</button>
                </div>
              </div>
            </form>
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
import axios from "@/axios.js";
import textData from '../assets/text.json'

export default {
  name: 'ContactForm',
  data() {
    return {
      text: textData.contact,
      acceptTerms: false
    };
  },
  methods: {
    async handleSubmit() {
      if (this.$refs.form.checkValidity() && this.acceptTerms) {
        const formData = {
          name: this.$refs.form.name.value,
          email: this.$refs.form.email.value,
          message: this.$refs.form.message.value
        };
        try {
          const response = await axios.post('/contact/', formData);
          if (response.status === 201) {
            console.log('Form submitted successfully');
            confirmation.textContent = "Otrzymaliśmy od Ciebie wiadomość.";
            this.$refs.form.reset();
            this.acceptTerms = false;
          } else {
            console.log('Unexpected status:', response.status);
          }
        } catch (error) {
          console.error(error);
        }
      }
    }
  }
}
</script>

<style scoped>
.checkbox {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.confirmation {
  color: red;
  font-size: 14px;
  padding-top: 5px;
}
</style>
