<template>
  <div
    ref="wrapper"
    v-scroll="runCounter"
    class="counter-wrap"
  >
    <v-container>
      <v-row
        justify="center"
        align="center"
        class="counter-inner spacing6"
      >
        <v-col sm="4" cols="12" class="pa-6">
          <div class="counter-item">
            <div class="text">
              <h3 class="use-text-title">
                <span class="d-flex justify-center">
                  {{ !visible ? 0 : '' }}
                  <count-up
                    v-if="visible"
                    :start-val="0"
                    :end-val="10"
                  />
                  &nbsp;{{ $t('saasLanding.counter_credits') }}
                </span>
              </h3>
              <p class="use-text-subtitle">
                <v-icon>mdi-reply</v-icon>
                {{ $t('saasLanding.counter_free') }}
              </p>
            </div>
          </div>
        </v-col>
        <v-col sm="4" cols="12" class="pa-6">
          <div class="counter-item">
            <div class="text">
              <h3 class="use-text-title">
                <span>
                  {{ !visible ? 0 : '' }}
                  <count-up
                    v-if="visible"
                    :start-val="0"
                    :end-val="2137"
                    :options="{ prefix: '+', suffix: '' }"
                  />
                </span>
              </h3>
              <p class="use-text-subtitle">
                <v-icon>mdi-account-multiple</v-icon>
                {{ $t('saasLanding.counter_users') }}
              </p>
            </div>
          </div>
        </v-col>
        <v-col sm="4" cols="12" class="pa-6">
          <div class="counter-item">
            <div class="text">
              <h3 class="use-text-title">
                <span>
                  {{ !visible ? 0 : '' }}
                  <count-up
                    v-if="visible"
                    :start-val="0"
                    :end-val="18000"
                    :options="{ prefix: '+', suffix: '' }"
                  />
                </span>
              </h3>
              <p class="use-text-subtitle">
                <v-icon>mdi-layers</v-icon>
                {{ $t('saasLanding.counter_providers') }}
              </p>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<style lang="scss" scoped>
@import './counter-style.scss';
</style>

<script>
import CountUp from 'vue-countup-v3';
import { ref } from 'vue';

export default {
  components: {
    CountUp,
  },
  setup() {
    const visible = ref(false);
    const wrapper = ref(0);
    const offset = 500;
    function runCounter() {
      const scrollPosition = document.documentElement.scrollTop || document.body.scrollTop;
      const topPosition = scrollPosition + offset;

      if (topPosition > wrapper.value.offsetTop) {
        visible.value = true;
      }
    }

    return {
      visible,
      runCounter,
      wrapper,
    };
  },
  data() {
    return {
      loaded: false,
    };
  },
  mounted() {
    this.loaded = true;
  },
};
</script>
