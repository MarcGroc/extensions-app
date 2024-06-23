<template>
  <Dropdown classMenuItems=" w-[180px] top-[58px] ">
    <div class="flex items-center">
      <div class="flex-1 ltr:mr-[10px] rtl:ml-[10px]">
        <div class="lg:h-8 lg:w-8 h-7 w-7 rounded-full">
          <img
            :src="profileImg"
            alt="{{ user?.username }}"
            class="block w-full h-full object-cover rounded-full"
          />
        </div>
      </div>
      <div
        class="flex-none text-slate-600 dark:text-white text-sm font-normal items-center lg:flex hidden overflow-hidden text-ellipsis whitespace-nowrap"
      >
        <span
          class="overflow-hidden text-ellipsis whitespace-nowrap w-[85px] block"
          >{{ user?.username }}</span
        >
        <span class="text-base inline-block ltr:ml-[10px] rtl:mr-[10px]"
          ><Icon icon="heroicons-outline:chevron-down"></Icon
        ></span>
      </div>
    </div>
    <template #menus>
      <MenuItem v-slot="{ active }" v-for="(item, i) in ProfileMenu" :key="i">
        <div
          type="button"
          :class="`${
            active
              ? 'bg-slate-100 dark:bg-slate-700 dark:bg-opacity-70 text-slate-900 dark:text-slate-300'
              : 'text-slate-600 dark:text-slate-300'
          } `"
          class="inline-flex items-center space-x-2 rtl:space-x-reverse w-full px-4 py-2 first:rounded-t last:rounded-b font-normal cursor-pointer"
          @click="item.link()"
        >
          <div class="flex-none text-lg">
            <Icon :icon="item.icon" />
          </div>
          <div class="flex-1 text-sm">
            {{ item.label }}
          </div>
        </div>
      </MenuItem>
    </template>
  </Dropdown>
</template>
<script>
import { useAuthStore } from "@/store/auth";
import { MenuItem } from "@headlessui/vue";
import Dropdown from "@/components/Dropdown";
import Icon from "@/components/Icon";
import profileImg from "@/assets/images/all-img/djavue_logo.jpg";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
export default {
  components: {
    Icon,
    Dropdown,
    MenuItem,
  },
  data() {
    return {
      profileImg,
      ProfileMenu: [
        {
          label: "Profile",
          icon: "heroicons-outline:user",
          link: () => {
            this.$router.push("profile");
          },
        },

        // {
        //   label: "Settings",
        //   icon: "heroicons-outline:cog",
        //   link: () => {
        //     this.$router.push("settings");
        //   },
        // },

        {
          label: "Logout",
          icon: "heroicons-outline:login",
          link: () => {
            this.$router.push("/");
            useAuthStore().logout();
          },
        },
      ],
    };
  },
  setup() {
    const authStore = useAuthStore();
    const user = ref(authStore.user);
    const router = useRouter();

    onMounted(() => {
      if (!authStore.isAuthenticated) {
        console.error("User not authenticated");
        router.push({ name: "Login" }); // Redirect to login page if user is not authenticated, disable for dev
      }
    });
    return {
      user,
    };
  },
};
</script>
<style lang=""></style>
