<template>
  <header
    class="header-area header-ebook navbar-light"
    :class="{ 'is-sticky': isSticky }"
  >
    <div class="container-fluid container-fluid--cp-150">
      <nav class="navbar navbar-expand-lg" id="navbar-example2">
        <router-link to="/">
          <img
            src="../../assets/img/logo/djavue_logo.jpg"
            class="resaized d-none d-lg-block"
            alt="logo"
          />
        </router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="header-config-wrapper btn-group">
          <!--          <router-link-->
          <!--            v-if="!authStore.isAuthenticated"-->
          <!--            to="/login"-->
          <!--            class="ht-btn ht-btn&#45;&#45;outline hire-btn d-sm-block loginbtn"-->
          <!--            >{{ text.login }}-->
          <!--          </router-link>-->
          <!--          <router-link-->
          <!--            v-else-->
          <!--            to="/logout"-->
          <!--            class="ht-btn ht-btn&#45;&#45;outline hire-btn d-sm-block loginbtn"-->
          <!--          >-->
          <!--            Logout-->
          <!--          </router-link>-->
          <router-link
            v-if="!authStore.isAuthenticated"
            to="/login"
            class="ht-btn ht-btn--outline hire-btn d-sm-block registerbtn"
          >
            {{ text.login }}
          </router-link>
          <router-link
            v-else
            to="/app/profile"
            class="ht-btn ht-btn--outline hire-btn d-sm-block registerbtn"
          >
            Profile
          </router-link>
        </div>

        <div
          class="collapse navbar-collapse justify-content-center"
          id="navbarSupportedContent"
        >
          <ul class="nav main-menu">
            <li class="nav-item">
              <a class="nav-link" href="/" @click="menuCollapseOnLinkClick">
                <span>{{ text.home }}</span>
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link"
                href="#feature"
                @click="menuCollapseOnLinkClick"
              >
                <span>{{ text.feature }}</span>
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link"
                href="#reviews"
                @click="menuCollapseOnLinkClick"
              >
                <span>{{ text.reviews }}</span>
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link"
                href="#pricing"
                @click="menuCollapseOnLinkClick"
              >
                <span>{{ text.pricing }}</span>
              </a>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  </header>
</template>

<script>
import { useAuthStore } from "@/store/auth.js";
import textData from "../../assets/text_landing_pl.json";

export default {
  data() {
    return {
      isSticky: false,
      text: textData.header,
    };
  },
  mounted() {
    window.addEventListener("scroll", () => {
      let scroll = window.scrollY;
      this.isSticky = scroll >= 200;
    });
  },

  methods: {
    menuCollapseOnLinkClick() {
      if (this.$route.path === "/") {
        document
          .getElementById("navbarSupportedContent")
          .classList.remove("show");
      } else {
        this.$router.push({ path: "/", force: true }).finally(() => {
          document
            .getElementById("navbarSupportedContent")
            .classList.remove("show");
        });
      }
    },
  },
  setup() {
    const authStore = useAuthStore();

    return {
      authStore,
    };
  },
};
</script>

<style lang="scss" scoped>
.header-ebook {
  &.is-sticky {
    top: 0;
    left: 0;
    position: fixed;
    width: 100%;
  }
}

.nav-item {
  color: #5945e6;
}

.registerbtn {
  background-color: #c60d29;
  color: #fff;
}

.loginbtn {
  background-color: #26a12c;
  color: #fff;
}

.resaized {
  width: 100px;
  height: 100px;
}
</style>
