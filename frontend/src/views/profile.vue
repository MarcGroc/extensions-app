<template>
  <div class="space-y-5 profile-page">
    <div
      class="profiel-wrap px-[35px] pb-10 md:pt-[84px] pt-10 rounded-lg bg-white dark:bg-slate-800 lg:flex lg:space-y-0 space-y-6 justify-between items-end relative z-[1]"
    >
      <div
        class="bg-slate-900 dark:bg-slate-700 absolute left-0 top-0 md:h-1/2 h-[150px] w-full z-[-1] rounded-t-lg"
      ></div>
      <div class="profile-box flex-none md:text-start text-center">
        <div class="md:flex items-end md:space-x-6 rtl:space-x-reverse">
          <div class="flex-none">
            <div
              class="md:h-[186px] md:w-[186px] h-[140px] w-[140px] md:ml-0 md:mr-0 ml-auto mr-auto md:mb-0 mb-4 rounded-full ring-4 ring-slate-100 relative"
            >
              <img
                :src="profileImg"
                alt=""
                class="w-full h-full object-cover rounded-full"
              />
              <!--              <router-link-->
              <!--                to="/app/profile-setting"-->
              <!--                class="absolute right-2 h-8 w-8 bg-slate-50 text-slate-600 rounded-full shadow-sm flex flex-col items-center justify-center md:top-[140px] top-[100px]"-->
              <!--                ><Icon icon="heroicons:pencil-square" />-->
              <!--              </router-link>-->
            </div>
          </div>
          <div class="flex-1">
            <div
              class="text-2xl font-medium text-slate-900 dark:text-slate-200 mb-[3px]"
            >
              {{ user?.username.toUpperCase() }}
            </div>
            <!--            <div class="text-sm font-light text-slate-600 dark:text-slate-400">-->
            <!--              Front End Developer-->
            <!--            </div>-->
          </div>
        </div>
      </div>
      <!-- end profile box -->
      <div
        class="profile-info-500 md:flex md:text-start text-center flex-1 max-w-[516px] md:space-y-0 space-y-4"
      >
        <div class="flex-1">
          <div
            class="text-base text-slate-900 dark:text-slate-300 font-medium mb-1"
          >
            ${{ user?.balance }}
          </div>
          <div class="text-sm text-slate-600 font-light dark:text-slate-300">
            Total Balance
          </div>
        </div>
        <!-- end single -->
        <div class="flex-1">
          <div
            class="text-base text-slate-900 dark:text-slate-300 font-medium mb-1"
          >
            200
          </div>
          <div class="text-sm text-slate-600 font-light dark:text-slate-300">
            Change this for metric
          </div>
        </div>
        <!-- end single -->
        <div class="flex-1">
          <div
            class="text-base text-slate-900 dark:text-slate-300 font-medium mb-1"
          >
            3200
          </div>
          <div class="text-sm text-slate-600 font-light dark:text-slate-300">
            Change this for metric
          </div>
        </div>
        <!-- end single -->
      </div>
      <!-- profile info-500 -->
    </div>
    <div class="grid grid-cols-12 gap-6">
      <div class="lg:col-span-4 col-span-12">
        <Card title="Info">
          <ul class="list space-y-8">
            <li class="flex space-x-3 rtl:space-x-reverse">
              <div
                class="flex-none text-2xl text-slate-600 dark:text-slate-300"
              >
                <!--                <Icon icon="heroicons:envelope" />-->
              </div>
              <div class="flex-1">
                <div
                  class="uppercase text-xs text-slate-500 dark:text-slate-300 mb-1 leading-[12px]"
                >
                  Email
                </div>
                <p class="text-base text-slate-600 dark:text-slate-50">
                  {{ user?.email }}
                </p>
              </div>
            </li>
            <!-- end single list -->
            <li class="flex space-x-3 rtl:space-x-reverse">
              <div
                class="flex-none text-2xl text-slate-600 dark:text-slate-300"
              >
                <!--                <Icon icon="heroicons:phone-arrow-up-right" />-->
              </div>
              <div class="flex-1">
                <div
                  class="uppercase text-xs text-slate-500 dark:text-slate-300 mb-1 leading-[12px]"
                >
                  Change Password
                </div>
                <p class="text-base text-slate-600 dark:text-slate-50">
                  Password button
                </p>
              </div>
            </li>
            <!-- end single list -->
            <li class="flex space-x-3 rtl:space-x-reverse">
              <div
                class="flex-none text-2xl text-slate-600 dark:text-slate-300"
              >
                <!--                <Icon icon="heroicons:map" />-->
              </div>
              <div class="flex-1">
                <div
                  class="uppercase text-xs text-slate-500 dark:text-slate-300 mb-1 leading-[12px]"
                >
                  Other action
                </div>
                <div class="text-base text-slate-600 dark:text-slate-50">
                  Action button
                </div>
              </div>
            </li>
            <!-- end single list -->
          </ul>
        </Card>
      </div>
      <div class="lg:col-span-8 col-span-12">
        <Card title="Change for some kind of activity tracker">
          <apexchart
            type="area"
            height="250"
            :options="
              themeSettingsStore.isDark
                ? basicAreaDark.chartOptions
                : basicArea.chartOptions
            "
            :series="basicArea.series"
          />
        </Card>
      </div>
    </div>
  </div>
</template>
<script>
import { ref, onMounted } from "vue";
import Card from "@/components/Card";
import Icon from "@/components/Icon";
import { basicArea, basicAreaDark } from "@/constant/appex-chart.js";
import { useAuthStore } from "@/store/auth.js";
import profileImg from "@/assets/images/all-img/djavue_logo.jpg";
import { useThemeSettingsStore } from "@/store/themeSettings";
export default {
  components: {
    Card,
    Icon,
  },
  data() {
    /**
     * A function that returns the data object containing basicArea, basicAreaDark, and profileImg.
     *
     * @return {Object} The data object with basicArea, basicAreaDark, and profileImg.
     */
    return {
      basicArea,
      basicAreaDark,
      profileImg,
    };
  },
  setup() {
    /**
     * Initializes the setup of the component by setting up the necessary stores and retrieving the user data.
     *
     * @return {Object} An object containing the user data and the theme settings store.
     */
    const themeSettingsStore = useThemeSettingsStore();
    const authStore = useAuthStore();
    const user = ref(authStore.user);

    onMounted(() => {
      if (!authStore.isAuthenticated) {
        authStore.localLogout();
        authStore.logout();
      }
    });

    return {
      user,
      themeSettingsStore,
    };
  },
};
</script>
<style lang="scss" scoped></style>
