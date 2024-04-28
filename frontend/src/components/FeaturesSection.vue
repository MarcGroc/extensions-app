<template>
    <div class="ebook-feature section-space--pt_120 section-space--pb_60" id="feature">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="section-title-wrapper text-center section-space--mb_60">
                        <h2 class="section-title font-weight--blod wow move-up">{{ text.title}}</h2>
                    </div>
                </div>
            </div>
            <Feature />
        </div>
    </div>
</template>

<script>
    import Feature from '@/components/Feature.vue'
    import textData from '../assets/text.json';

    export default {
        data() {
            return {
                text: textData.feature
            }
        },
        name: 'EbookIntro',
        components: {
            Feature
        }
    };
</script>
