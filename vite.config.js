import { defineConfig } from 'vite'
import { sveltekit } from '@sveltejs/kit/vite'
import svg from '@poppanator/sveltekit-svg'
import { resolve } from 'path'

export default defineConfig({
    plugins: [sveltekit(), svg()],
    server: {
        port: 3000
    },
    build: {
        polyfillModulePreload: false
    },
    resolve: {
        alias: {
            $: resolve('./src')
        }
    }
})
