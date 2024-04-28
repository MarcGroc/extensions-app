<template>
    <div class="main-container">
        <HeaderSection />

        <ContactForm />

        <FooterSection />

    </div>
</template>

<script>
    import HeaderSection from "@/components/HeaderSection.vue";
    import FooterSection from "@/components/FooterSection.vue";
    import ContactForm from "@/components/ContactForm.vue";

    export default {
        name: 'Contact',
        components: {
          ContactForm,
          FooterSection,
          HeaderSection,
        }
    }
</script>
