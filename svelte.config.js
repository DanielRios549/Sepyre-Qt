import adapter from '@sveltejs/adapter-static'
import preprocess from 'svelte-preprocess'
import Import from 'postcss-import'
import AutoPrefixer from 'autoprefixer'
import Nested from 'postcss-nested'
import SimpleVars from 'postcss-simple-vars'
import Extend from 'postcss-extend-rule'
import CustomMedia from 'postcss-custom-media'
import MediaMinMax from 'postcss-media-minmax'
import CustomSelector from 'postcss-custom-selectors'
import { join, resolve } from 'path'

const prepend = join(resolve('./styles'), '_custom.scss')

/** @type {import('@sveltejs/kit').Config} */
const config = {
    preprocess: preprocess({
        scss: {
            prependData: `@use "${prepend}";`
        },
        postcss: {
            prependData: `@import "${prepend}";`,
            plugins: [
                AutoPrefixer(), Nested(),
                SimpleVars(), Extend(),
                Import(), CustomMedia(),
                MediaMinMax(), CustomSelector()
            ]
        }
    }),
    kit: {
        adapter: adapter({
            pages: 'build'
        }),
        files: {
            assets: 'public',
            routes: 'pages'
        },
        prerender: {
            entries: ['*']
        }
    }
}

export default config
