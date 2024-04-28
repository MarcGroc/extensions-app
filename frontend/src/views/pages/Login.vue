<template>
    <div class="main-container">

        <LoginForm />

        <FooterSection />

    </div>
</template>

<script>
    import FooterSection from "@/components/FooterSection.vue";
    import LoginForm from "@/components/LoginForm.vue";
    export default {
        name: 'Contact',

        components: {
          LoginForm,
          FooterSection,
        }
    }
</script>
