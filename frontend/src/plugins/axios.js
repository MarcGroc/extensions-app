import axios from "axios";
import { useAuthStore } from "@/store/auth.js";
const instance = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});
const token = localStorage.getItem("token");
if (token) {
  instance.defaults.headers.common["Authorization"] = `Token ${token}`;
}
instance.interceptors.request.use(
  (response) => response,
  async (error) => {
    if (error.response.status === 401) {
      const auth = useAuthStore();
      await auth.localLogout();
      await auth.logout();
    }
    return Promise.reject(error);
  }
);

export default instance;

export const getProducts = async () => {
  const response = await instance.get("/products");

  return response.data;
};
export const getProductById = async (id) => {
  const response = await instance.get(`/products/${id}`);

  return response.data;
};
