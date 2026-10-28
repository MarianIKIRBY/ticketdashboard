import { defineConfig } from 'vite'
import { resolve } from 'node:path'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        index: resolve(import.meta.dirname, 'index.html'),
        dashboard: resolve(import.meta.dirname, 'dashboard.html'),
        login: resolve(import.meta.dirname, 'src/pages/login/login.html'),
        gestion: resolve(import.meta.dirname, 'src/pages/gestion/gestion.html'),
        reportes: resolve(import.meta.dirname, 'src/pages/gestion/reportes.html'),
      },
    },
  },
})