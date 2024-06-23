<template>
  <section class="section-space--ptb_90">
    <div class="container">
      <div class="mb-4">
        <h5 class="mb-2">1.</h5>
        <p>{{ text.userRequirements }}</p>
      </div>
      <div class="mb-4">
        <h5 class="mb-2">2.</h5>
        <p>{{ text.useLicense }}</p>
      </div>
      <div class="mb-4">
        <h5 class="mb-2">3.</h5>
        <p>{{ text.userResponsibilities }}</p>
      </div>
      <div class="mb-4">
        <h5 class="mb-2">4.</h5>
        <p>{{ text.privacyPolicy }}</p>
      </div>
      <div class="mb-4">
        <h5 class="mb-2">5.</h5>
        <p>{{ text.changesToTerms }}</p>
      </div>
      <div class="mb-4">
        <h5 class="mb-2">6.</h5>
        <p>{{ text.finalProvisions }}</p>
      </div>
    </div>
  </section>
</template>

<script>
import textData from "../../assets/text_landing_pl.json";
export default {
  name: "PrivacyPolicyContent",
  data() {
    return {
      text: textData.terms,
    };
  },
};
</script>
