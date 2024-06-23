import { useAuthStore } from "@/store/auth";
export default function auth({ next, store }) {
  const authStore = useAuthStore();
  if (authStore.isAuthenticated) {
    return next();
  }
  // return next({ name: "Login" });
}
