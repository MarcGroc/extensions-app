<template>
    <div class="main-container">
        <HeaderSection />

        <Breadcrumb>
            <template #breadcrumb>
                <div class="breadcrumb_box text-center">
                    <h2 class="breadcrumb-title">Regulamin serwisu</h2>
                </div>
            </template>
        </Breadcrumb>

        <TermsOfUseContent />

        <FooterSection />
    </div>
</template>

<script>
    import Breadcrumb from '@/components/Breadcrumb.vue'
    import TermsOfUseContent from "@/components/TermsOfUseContent.vue";
    import HeaderSection from "@/components/HeaderSection.vue";
    import FooterSection from "@/components/FooterSection.vue";

    export default {
        name: 'ElementButtons',
        components: {
          FooterSection,
          HeaderSection,
          TermsOfUseContent,
          Breadcrumb
        }
    }
</script>
