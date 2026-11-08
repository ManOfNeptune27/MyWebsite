import adapter from '@sveltejs/adapter-static';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

const basePath = process.env.BASE_PATH?.replace(/^\/+|\/+$/g, '') ?? '';

export default defineConfig({
  plugins: [
    sveltekit({
      adapter: adapter(),
      paths: {
        base: basePath ? `/${basePath}` : ''
      },
      prerender: {
        entries: ['*']
      }
    })
  ]
});
