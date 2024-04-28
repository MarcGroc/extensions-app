<template>
    <div class="main-container">

        <RegisterForm />

        <FooterSection />

    </div>
</template>

<script>
    import FooterSection from "@/components/FooterSection.vue";
    import RegisterForm from "@/components/RegisterForm.vue";
    export default {
        name: 'Contact',

        components: {
          RegisterForm,
          FooterSection,
        }
    }
</script>
