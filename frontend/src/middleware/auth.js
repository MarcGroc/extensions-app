import { useAuthStore } from "@/store/auth";
export default function auth({ next, store }) {
  const authStore = useAuthStore();
  if (authStore.isAuthenticated) {
    next();
  }
  return next({ name: "Login" });
}
