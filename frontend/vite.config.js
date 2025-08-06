import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  base: '/Resume-Screening-App/',
  plugins: [react()],
  server: {
    port: 5173,
    host: true
  },
  resolve: {
    alias: {
      '@': '/src'
    }
  },
  optimizeDeps: {
    include: ['@popperjs/core']
  }
})