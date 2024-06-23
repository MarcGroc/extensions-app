<template>
  <div class="loginwrapper">
    <div class="lg-inner-column">
      <div class="left-column relative z-[1]">
        <div class="max-w-[520px] pt-20 ltr:pl-20 rtl:pr-20">
          <router-link to="/">
            <img
              :src="logo"
              width="100"
              height="100"
              alt=""
              class="mb-10"
              v-if="!themeSettingsStore.isDark"
            />
            <img :src="logoWhite" alt="" class="mb-10" v-else />
          </router-link>

          <h4>
            <span class="text-slate-800 dark:text-slate-400 font-bold">{{ text.title }}</span>
          </h4>
        </div>
        <div
          class="absolute left-0 2xl:bottom-[-160px] bottom-[-130px] h-full w-full z-[-1]"
        >
          <img :src="logo" alt="" class="h-full w-full object-contain" />
        </div>
      </div>
      <div class="right-column relative">
        <div
          class="inner-content h-full flex flex-col bg-white dark:bg-slate-800"
        >
          <div class="auth-box h-full flex flex-col justify-center">
            <div class="mobile-logo text-center mb-6 lg:hidden block">
              <router-link to="/">
                <img
                  :src="logo"
                  alt=""
                  class="mx-auto"
                  v-if="!themeSettingsStore.isDark"
                />
                <img :src="logoWhite" alt="" class="mx-auto" v-else />
              </router-link>
            </div>
            <div class="text-center 2xl:mb-10 mb-4">
              <h4 class="font-medium">{{ text.signIn }}</h4>
<!--              <div class="text-slate-500 text-base">-->
<!--                {{ text.login_or }}-->
<!--              </div>-->
            </div>
            <Signin />
            <div
              class="relative border-b-[#9AA2AF] border-opacity-[16%] border-b pt-6"
            >
              <div
                class="absolute inline-block bg-white dark:bg-slate-800 dark:text-slate-400 left-1/2 top-1/2 transform -translate-x-1/2 px-4 min-w-max text-sm text-slate-500 font-normal"
              >
                {{ text.subtitle }}
              </div>
            </div>
            <div class="max-w-[242px] mx-auto mt-8 w-full">
              <Social />
            </div>
            <div
              class="md:max-w-[345px] mx-auto font-normal text-slate-500 dark:text-slate-400 mt-12 uppercase text-sm"
            >
              {{ text.notAccount }}
              <router-link
                to="/register"
                class="text-slate-900 dark:text-white font-medium hover:underline"
              >
                {{ text.register }}
              </router-link>
            </div>
          </div>
          <div class="auth-footer text-center">
            Copyright {{ new Date().getFullYear() }},
            {{ brand.projectName }} All Rights Reserved.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { useThemeSettingsStore } from "@/store/themeSettings";
import Signin from "../common/Signin";
import Social from "../common/Social";
import brand from "@/assets/brand/brand";
import textData from "@/assets/text_landing_pl.json";


// Image Import
import logoWhite from "@/assets/images/logo/logo-white.svg";
import logo from "@/assets/img/logo/djavue_logo.jpg";
import sideImg from "@/assets/images/auth/ils1.svg";

export default {
  setup() {
    const themeSettingsStore = useThemeSettingsStore();
    return {
      themeSettingsStore,
    };
  },
  data() {
    return {
      logoWhite,
      logo,
      sideImg,
      brand,
      text: textData.login,
    };
  },
  components: {
    Social,
    Signin,
  },
};
</script>
<style lang="scss"></style>
