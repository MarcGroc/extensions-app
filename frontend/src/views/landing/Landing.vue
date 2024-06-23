<template>
  <div class="main-container box-page">
    <div class="site-wrapper-box">
      <div class="site-wrapper">
        <HeaderSection />
        <HeroSection />
        <FunFactSection />
        <FeaturesSection id="feature" />
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
import HeaderSection from "@/components/landing/HeaderSection.vue";
import HeroSection from "@/components/landing/HeroSection.vue";
import FunFactSection from "@/components/landing/FunFactSection.vue";
import FeaturesSection from "@/components/landing/FeaturesSection.vue";
import TestimonialSection from "@/components/landing/TestimonialSection.vue";
import PricingSection from "@/components/landing/PricingSection.vue";
import NewsletterSection from "@/components/landing/NewsletterSection.vue";
import FooterSection from "@/components/landing/FooterSection.vue";
import CookieConsent from "@/components/landing/CookieConsent.vue";
export default {
  name: "Home",
  components: {
    NewsletterSection,
    PricingSection,
    FunFactSection,
    HeaderSection,
    HeroSection,
    FeaturesSection,
    TestimonialSection,
    FooterSection,
    CookieConsent,
  },
};
</script>
