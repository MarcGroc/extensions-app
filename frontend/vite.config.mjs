import { defineConfig } from "vite";
import path from "path";
import Vue from "@vitejs/plugin-vue";
import ViteImages from "vite-plugin-vue-images";
import dotenv from "dotenv";

dotenv.config({ path: "../.env" });
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    Vue(),
    ViteImages({
      dirs: ["src/assets/images"],
    }),
  ],
  define: {
    "process.env": process.env,
  },
  build: {
    chunkSizeWarningLimit: 80000,
  },
  resolve: {
    extensions: [".mjs", ".js", ".ts", ".jsx", ".tsx", ".json", ".vue", ".css"],
    alias: {
      "@": path.resolve(__dirname, "./src"),
      "#": path.resolve(__dirname, "../"), // monorepo root
    },
  },
  server: {
    host: "0.0.0.0",
    port: 8008,
    watch: {
      usePolling: true,
    },
    test: {
      globals: true,
      environment: "jsdom",
      setupFiles: "./tests/setup.js",
      coverage: {
        provider: "istanbul",
        reporter: ["text", "json", "html"],
      },
      exclude: ["tests/e2e/*"],
    },
  },
});
