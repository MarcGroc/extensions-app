<template>
    <div class="row mtn-30 fun-facts-container">
        <div class="col-lg-3 col-md-6 col-sm-6 wow move-up">
            <div class="fun-fact--one mt-30 text-center">
                <div class="fun-fact__count counter">
                    <span>{{ text.fact1value }}</span>
                </div>
                <span class="fun-fact__text">{{ text.fact1text }}</span>
            </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6 wow move-up">
            <div class="fun-fact--one mt-30 text-center">
                <div class="fun-fact__count counter">
                    <span>{{ text.fact2value }}</span>
                </div>
                <span class="fun-fact__text">{{ text.fact2text }}</span>
            </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6 wow move-up">
            <div class="fun-fact--one mt-30 text-center">
                <div class="fun-fact__count counter">
                    <span>{{ text.fact3value }}</span>
                </div>
                <span class="fun-fact__text">{{ text.fact3text }}</span>
            </div>
        </div>
    </div>
</template>

<script>
import textData from '../assets/text.json';

export default {
    data() {
        return {
            text : textData.funfacts
        }
    }
}
</script>

<style scoped>
.fun-facts-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 30px;
.fun-fact__count {
  color: #5945e6;
  }
}

</style>
