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
                        <form method="post" @submit.prevent="handleSubmit">
                            <input type="text" :placeholder="text.name" required>
                            <input type="email" :placeholder="text.email" required>
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
            handleSubmit() {
                this.subscribed = true;
                this.subscribedmessage = 'Zapisano do newslettera.'
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
