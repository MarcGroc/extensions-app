import { defineStore } from "pinia";
import axios from "@/plugins/axios.js";
import { useToast } from "vue-toastification";

const toast = useToast();

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem("token") || null,
    user: null,
    isAuthenticated: false,
    group: [],
  }),
  actions: {
    async init() {
      const token = localStorage.getItem("token");
      if (token) {
        this.token = token;
        this.isAuthenticated = true;
        axios.defaults.headers.common["Authorization"] = `Token ${token}`;
        try {
          await this.getUser();
        } catch (error) {
          this.localLogout();
          toast.error("Somthing went wrong, please try again later", {
            timeout: 3000,
          });
        }
      }
    },
    async login(credentials) {
      const response = await axios.post("api/dj-rest-auth/login/", credentials);
      if (response.status === 200) {
        this.token = response.data.key;
        this.isAuthenticated = true;
        localStorage.setItem("token", this.token);
        axios.defaults.headers.common["Authorization"] = ` Token ${this.token}`;
      }
    },

    async logout() {
      try {
        await axios.post("api/dj-rest-auth/logout/");
      } catch (error) {
        localStorage.removeItem("token");
        delete axios.defaults.headers.common["Authorization"];
      } finally {
        this.token = null;
        this.isAuthenticated = false;
        this.user = null;
        this.group = null;
        localStorage.removeItem("token");
        delete axios.defaults.headers.common["Authorization"];
      }
    },
    localLogout() {
      this.token = null;
      this.isAuthenticated = false;
      this.user = null;
      this.group = null;
      localStorage.removeItem("token");
      delete axios.defaults.headers.common["Authorization"];
    },

    async getUser() {
      try {
        const response = await axios.get("users/api/user");
        this.user = response.data;
        this.group = response.data.groups[0];
      } catch (error) {
        console.log(error.status);
        if (error.response && error.response.status === 401) {
          await this.localLogout();
          try {
            await this.logout();
          } catch (error) {
            toast.error("Somthing went wrong, please try again later", {
              timeout: 3000,
            });
          }
        }
      }
    },
  },
});
