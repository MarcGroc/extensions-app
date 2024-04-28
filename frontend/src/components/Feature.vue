<template>
    <div class="row">
        <div v-for="feat in features" :key="feat.id" class="col-lg-4 col-md-6 wow move-up">
            <div class="service-grid">
                <div class="ht-service-box--two text-center">
                        <div class="image mb-20">
                            <img :src="feat.icon" class="img-fluid" :alt="feat.alt">
                        </div>
                        <div class="content">
                            <h6 class="sub-heading">{{ feat.subheading }}</h6>
                            <h6 class="ht-heading mb-15">{{ feat.heading }}</h6>
                            <div class="service_text">{{ feat.text }}</div>
                        </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import textData from '../assets/text.json'
export default {
    name: 'Feature',
    data (){
        return {
            features: [
                {
                    icon: 'src/assets/icons/icon-feature-03.png',
                    heading: '',
                    subheading:'',
                    text: '',
                },
                {
                    icon: 'src/assets/icons/icon-feature-02.png',
                    heading:'',
                    subheading:'',
                    text:''
                },
                {
                    icon: 'src/assets/icons/icon-feature-01.png',
                    heading:'',
                    subheading:'',
                    text:''
                },
            ]
        }
    },
    mounted() {
        for (let i = 0; i < 3; i++) {
        this.features[i].heading = textData.feature[`step${i + 1}heading`];
        this.features[i].subheading = textData.feature[`step${i + 1}subheading`];
        this.features[i].text = textData.feature[`step${i + 1}text`];
    }
    }
}
</script>
