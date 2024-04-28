<template>
    <div class="main-container box-page">
        <div class="site-wrapper-box">
            <div class="site-wrapper">
              <HeaderSection />
              <HeroSection />
              <FunFactSection />
              <FeaturesSection id="feature"/>
              <TestimonialSection />
              <PricingSection id="pricing" />
              <NewsletterSection />
              <FooterSection />
              <cookie-consent></cookie-consent>
            </div>
        </div>
    </div>
</template>

<script>
    import HeaderSection from '@/components/HeaderSection.vue'
    import HeroSection from '@/components/HeroSection.vue'
    import FunFactSection from "@/components/FunFactSection.vue";
    import FeaturesSection from '@/components/FeaturesSection.vue'
    import TestimonialSection from '@/components/TestimonialSection.vue'
    import PricingSection from "@/components/PricingSection.vue";
    import NewsletterSection from "@/components/NewsletterSection.vue";
    import FooterSection from '@/components/FooterSection.vue'
    import CookieConsent from "@/components/CookieConsent.vue";
    export default {
        name: 'Home',
        components: {
          NewsletterSection,
          PricingSection,
          FunFactSection,
          HeaderSection,
          HeroSection,
          FeaturesSection,
          TestimonialSection,
          FooterSection,
          CookieConsent
        }
    }
</script>
