<template>
  <AuthFrame
    :title="$t('common.login_title')"
    :subtitle="$t('common.login_subtitle')"
  >
    <div>
      <div class="head">
        <title-secondary :align="isMobile ? 'center' : 'left'">
          {{ $t('common.login') }}
        </title-secondary>
        <v-btn
          :to="localePath(routerLink.saas.register)"
          class="button-link"
          variant="text"
          size="small"
        >
          <v-icon class="icon signArrow">
            mdi-arrow-right
          </v-icon>
          {{ $t('common.login_create') }}
        </v-btn>
      </div>
      <social-auth />
      <div class="separator">
        <p>
          {{ $t('common.login_or') }}
        </p>
      </div>
      <v-form
        ref="form"
        v-model="valid"
      >
        <v-row class="spacing3">
          <v-col cols="12" sm="12" class="py-1 px-3">
            <v-text-field
              v-model="email"
              :label="$t('common.login_email')"
              :rules="emailRules"
              color="secondary"
              class="input"
              name="email"
              filled
              required
            />
          </v-col>
          <v-col cols="12" sm="12" class="py-1 px-3">
            <v-text-field
              v-model="password"
              :label="$t('common.login_password')"
              :rules="requiredRules"
              color="secondary"
              type="password"
              class="input"
              name="password"
              filled
              required
            />
          </v-col>
        </v-row>
        <div class="form-helper">
          <div class="form-control-label">
            <v-checkbox
              v-model="checkbox"
              :label="$t('common.login_remember')"
              color="secondary"
            />
          </div>
          <v-btn
            size="small"
            class="button-link"
            variant="text"
            href="#"
          >
            {{ $t('common.login_forgot') }}
          </v-btn>
        </div>
        <div class="btn-area">
          <v-btn
            size="large"
            block
            color="secondary"
            @click="handleSubmit"
            @touchstart.prevent="handleSubmit"
          >
            {{ $t('common.continue') }}
          </v-btn>
        </div>
      </v-form>
    </div>
  </AuthFrame>
</template>

<style lang="scss" scoped>
@import './form-style';
</style>

<script>
import routerLink from '@/assets/text/link';
import { useLocalePath } from '#imports';
import TitleSecondary from '../Title/TitleSecondary';
import SocialAuth from './SocialAuth';
import AuthFrame from './AuthFrame';

export default {
  components: {
    SocialAuth,
    TitleSecondary,
    AuthFrame,
  },
  setup() {
    const localePath = useLocalePath();
    return {
      localePath,
    };
  },
  data() {
    return {
      routerLink,
      valid: true,
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      password: '',
      requiredRules: [v => !!v || 'This field is required'],
      checkbox: false,
    };
  },
  computed: {
    isMobile() {
      const smDown = this.$vuetify.display.smAndDown;
      return smDown;
    },
  },
  methods: {
    async handleSubmit() {
      if (this.$refs.form.validate()) {
        try {
          const formData = {
            email: this.email,
            password: this.password,
          };
          const response = await fetch('http://localhost:8000/api/dj-rest-auth/login/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
          });
          if (response.ok) {
            this.$router.push('/');
          }
        } catch (error) {
          if (error.response) {
            console.log('Error status:', error.response.status);
            console.log('Error message:', error.response.statusText);
          } else {
            console.error('Error during fetch:', error.message);
          }
        }
      } else {
        console.log('Form validation failed');
      }
    },
  },
};
</script>
