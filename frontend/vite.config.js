import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';
import {configDefaults} from "vitest/config";

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    }
  },
  server: {
    host: '0.0.0.0',
    port: 8008,
    watch: {
      usePolling: true,
    port: 8008
  },
  test: {
    environment: 'jsdom',
    exclude: [...configDefaults.exclude, 'e2e/*']
  }
}
});
