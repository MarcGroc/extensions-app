import { createRouter, createWebHistory } from "vue-router";
import middlewarePipeline from "../middleware/middlewarePipeline";
import routes from "./route";
import { useAuthStore } from "@/store/auth";
// import { makeServer } from "../server";
// import { useAuthStore } from "../store/auth";

const router = createRouter({
  history: createWebHistory(import.meta.BASE_URL),
  base: import.meta.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  },
});
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  if (authStore.isAuthenticated) {
    const isUserGroupOnly =
      authStore.group.length === 1 && authStore.group.includes(3);
    if (isUserGroupOnly && to.path !== "chat") {
      next({ name: "chat" });
    } else {
      next();
    }
  } else {
    next();
  }
  const titleText = to.name;
  const words = titleText.split(" ");
  const wordslength = words.length;
  for (let i = 0; i < wordslength; i++) {
    words[i] = words[i][0].toUpperCase() + words[i].substr(1);
  }
  document.title = "DjaVue  - " + words;

  const middleware = to.meta.middleware;
  const context = { to, from, next };
  return middleware[0]({
    ...context,
    next: middlewarePipeline(context, middleware, 1),
  });
});

router.afterEach(() => {
  // Remove initial loading
  const appLoading = document.getElementById("loading-bg");
  if (appLoading) {
    appLoading.style.display = "none";
  }
  // makeServer();
});

export default router;
