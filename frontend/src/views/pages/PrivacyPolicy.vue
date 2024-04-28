<template>
    <div class="main-container">
        <HeaderSection />

        <Breadcrumb>
            <template #breadcrumb>
                <div class="breadcrumb_box text-center">
                    <h2 class="breadcrumb-title">Polityka prywatności</h2>
                </div>
            </template>
        </Breadcrumb>

        <PrivacyPolicyContent />

        <FooterSection />

    </div>
</template>

<script>
    import HeaderSection from "@/components/HeaderSection.vue";
    import Breadcrumb from '@/components/Breadcrumb.vue'
    import PrivacyPolicyContent from '@/components/PrivacyPolicyContent.vue'
    import FooterSection from "@/components/FooterSection.vue";

    export default {
        name: 'PrivacyPolicy',
        components: {
          FooterSection,
            HeaderSection,
            Breadcrumb,
            PrivacyPolicyContent,
        }
    }
</script>
