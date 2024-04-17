<template>
  <div class="page-wrap">
    <v-snackbar
      v-model="snackbar"
      :timeout="4000"
      location="top right"
      class="notification"
    >
      <div class="action">
        Message Sent
      </div>
      <template #actions>
        <v-btn
          variant="text"
          icon
          @click="snackbar = false"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </template>
    </v-snackbar>
    <hidden point="mdUp">
      <div class="logo logo-header">
        <nuxt-link :to="localePath(routeLink.saas.home)">
          <img :src="logo" alt="logo">
          <span class="use-text-title">
            {{ brand.saas.projectName }}
          </span>
        </nuxt-link>
      </div>
    </hidden>
    <v-container class="inner-wrap max-md">
      <v-btn
        :to="localePath(routeLink.saas.home)"
        icon
        variant="text"
        class="backtohome"
      >
        <i class="ion-ios-home-outline" />
        <i class="ion-ios-arrow-round-back-outline" />
      </v-btn>
      <div class="decoration">
        <svg class="left-deco">
          <use xlink:href="/images/saas/deco-bg-left.svg#main" />
        </svg>
        <svg class="right-deco">
          <use xlink:href="/images/saas/deco-bg-right.svg#main" />
        </svg>
      </div>
      <v-card class="form-box fragment-fadeUp">
        <div class="full-form-wrap">
          <h3 class="use-text-title title-contact pb-3 text-center">
            {{ $t('common.contact_title2') }}
          </h3>
          <p class="desc use-text-subtitle2 text-center">
            {{ $t('common.contact_subtitle') }}
          </p>
          <div class="form">
            <v-form
              ref="form"
              v-model="valid"
            >
              <v-row class="spacing6">
                <v-col cols="12" sm="6" class="py-1 px-6">
                  <v-text-field
                    v-model="name"
                    :rules="nameRules"
                    :label="$t('common.form_name')"
                    color="white"
                    class="input light"
                    filled
                    required
                  />
                </v-col>
                <v-col cols="12" sm="6" class="py-1 px-6">
                  <v-text-field
                    v-model="email"
                    :rules="emailRules"
                    :label="$t('common.form_email')"
                    class="input light"
                    color="white"
                    filled
                    required
                  />
                </v-col>
                <v-col cols="12" class="py-1 px-6">
                  <v-textarea
                    v-model="message"
                    rows="6"
                    color="white"
                    class="input light"
                    filled
                    :label="$t('common.form_message')"
                  />
                </v-col>
              </v-row>
              <div class="btn-area flex">
                <div class="form-control-label">
                  <v-checkbox
                    v-model="checkbox"
                    :rules="[v => !!v || 'You must agree to continue!']"
                    :label="$t('common.form_terms')"
                    :hide-details="hideDetail"
                    color="secondary"
                    class="white-label"
                    required
                  />
                  <span class="mx-3">
                    <a href="/privacy" class="link">
                      {{ $t('common.form_privacy') }}
                    </a>
                  </span>
                </div>
                <v-btn
                  :block="isMobile"
                  color="secondary"
                  size="large"
                  @click="validate"
                >
                  {{ $t('common.form_send') }}
                </v-btn>
              </div>
            </v-form>
          </div>
        </div>
      </v-card>
    </v-container>
  </div>
</template>

<style lang="scss" scoped>
@import './form-style.scss';
@import '../Title/title-style.scss';
</style>

<script>
import logo from '@/assets/images/saas-logo.svg';
import brand from '@/assets/text/brand';
import link from '@/assets/text/link';
import Hidden from '../Hidden';
import { useLocalePath } from '#imports';

export default {
  setup() {
    const localePath = useLocalePath();
    return {
      localePath,
    };
  },
  components: {
    Hidden,
  },
  data() {
    return {
      valid: true,
      snackbar: false,
      hideDetail: true,
      name: '',
      nameRules: [v => !!v || 'Name is required'],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      message: '',
      checkbox: false,
      logo,
      brand,
      routeLink: link,
    };
  },
  computed: {
    isMobile() {
      const smDown = this.$vuetify.display.smAndDown;
      return smDown;
    },
  },
  methods: {
    async validate() {
      const { valid } = await this.$refs.form.validate();

      if (valid) {
        try {
          const formData = {
            name: this.name,
            email: this.email,
            message: this.message,
          };
          const response = await fetch('http://localhost:8000/api/contact/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
          });
          if (response.ok) {
            this.snackbar = true;
            this.hideDetail = true;
          } else {
            this.snackbar = true;
          }
        } catch (error) {
          console.error('Error during fetch:', error.message);
        }
      } else {
        this.hideDetail = false;
      }
    },
  },
};
</script>
