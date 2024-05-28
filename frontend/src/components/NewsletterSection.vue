<template>
    <div class="agency-newsletter-section section-space--ptb_120 bg-gray-3">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="digital-agency-section-title text-center section-space--mb_60">
                        <h3 class="section-title font-weight--light mb-15 wow move-up">{{text.title}}</h3>
                    </div>
                    <!-- newsletter form -->
                    <div class="newsletter-form--two section-space--mb_30 text-center wow move-up">
                        <form id="coming-soon-form" method="post" ref="form" @submit.prevent="handleSubmit">
                            <input name="name" type="text" :placeholder="text.name" required>
                            <input name="email" type="email" :placeholder="text.email" required>
                            <button type="submit" class="ht-btn ht-btn-md">{{ text.submit }}</button>
                        </form>
                        <p v-if="subscribed" class="subscribe-message">{{ subscribedmessage }}</p>
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
        name: 'NewsletterThree',
        data() {
            return {
              text:textData.newsletter,
              subscribed: false,
              subscribedmessage: ''
            }
        },
        methods: {
            async handleSubmit() {
                const formData = new FormData(this.$refs.form);
                try {
                    const response = await axios.post('/coming-soon/', formData);
                    if (response.status === 201) {
                        this.subscribedmessage = 'Zapisano do newslettera.'
                        this.subscribed = true;
                        console.log('Form submitted successfully');
                        this.$refs.form.reset();
                    }
                } catch (error) {
                    console.error(error);
                    console.log('Form submission failed');
                }
            },
        }
    }
</script>

<style>
.subscribe-message {
    color: green;
    font-size: 18px;
    padding-top: 5px;
}
</style>
