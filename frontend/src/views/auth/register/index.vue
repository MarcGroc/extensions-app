<template>
  <div class="loginwrapper">
    <div class="lg-inner-column">
      <div class="left-column relative z-[1]">
        <div class="max-w-[520px] pt-20 ltr:pl-20 rtl:pr-20">
          <router-link to="/">
            <img
              src="@/assets/img/logo/djavue_logo.jpg"
              alt=""
              width="100"
              height="100"
              class="mb-10"
              v-if="!themeSettingsStore.isDark"
            />
            <img
              src="@/assets/img/logo/djavue_logo.jpg"
              alt=""
              class="mb-10"
              v-else
            />
          </router-link>

          <h4>
            <span class="text-slate-800 dark:text-slate-400 font-bold">{{
              text.title
            }}</span>
          </h4>
        </div>
        <div class="absolute left-0 bottom-[-130px] h-full w-full z-[-1]">
          <img
            src="@/assets/img/logo/djavue_logo.jpg"
            alt=""
            class="h-full w-full object-contain"
          />
        </div>
      </div>
      <div class="right-column relative bg-white dark:bg-slate-800">
        <div
          class="inner-content h-full flex flex-col bg-white dark:bg-slate-800"
        >
          <div class="auth-box h-full flex flex-col justify-center">
            <div class="mobile-logo text-center mb-6 lg:hidden block">
              <router-link to="/"
                ><img
                  src="@/assets/images/logo/logo.svg"
                  alt=""
                  class="mx-auto"
              /></router-link>
            </div>
            <div class="text-center 2xl:mb-10 mb-5">
              <h4 class="font-medium">{{ text.subtitle }}</h4>
              <!--              <div class="text-slate-500 dark:text-slate-400 text-base">-->
              <!--                Create an account to start using Dashcode-->
              <!--              </div>-->
            </div>
            <Signup />
            <div
              class="relative border-b-[#9AA2AF] border-opacity-[16%] border-b pt-6"
            >
              <div
                class="absolute inline-block bg-white dark:bg-slate-800 left-1/2 top-1/2 transform -translate-x-1/2 px-4 min-w-max text-sm text-slate-500 dark:text-slate-400font-normal"
              >
                {{ text.register_or }}
              </div>
            </div>
            <div class="max-w-[242px] mx-auto mt-8 w-full">
              <Social />
            </div>
            <div
              class="max-w-[215px] mx-auto font-normal text-slate-500 dark:text-slate-400 2xl:mt-12 mt-6 uppercase text-sm"
            >
              {{ text.alreadyAccount }}
              <router-link
                to="/"
                class="text-slate-900 dark:text-white font-medium hover:underline"
              >
                {{ text.login }}</router-link
              >
            </div>
          </div>
          <div class="auth-footer text-center">
            Copyright {{ new Date().getFullYear() }} &copy; ,
            {{ brand.projectName }} All Rights Reserved.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Signup from "../common/Signup";
import Social from "../common/Social";
import { useThemeSettingsStore } from "@/store/themeSettings";
import textData from "@/assets/text_landing_pl.json";
import brand from "@/assets/brand/brand";
export default {
  setup() {
    const themeSettingsStore = useThemeSettingsStore();
    return { themeSettingsStore };
  },
  components: {
    Social,
    Signup,
  },
  data() {
    return {
      text: textData.register,
      brand,
    };
  },
};
</script>
<style lang="scss"></style>
