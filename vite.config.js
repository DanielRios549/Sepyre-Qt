import { sveltekit } from '@sveltejs/kit/vite'
import svg from '@poppanator/sveltekit-svg'
import { resolve } from 'path'

/** @type {import('vite').UserConfig} */
const config = {
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
}

export default config
