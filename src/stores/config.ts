import { savable } from '$/lib/store'
import type { Config } from '$/types/config'

export const config = savable<Config>('config', {
    app: {
        theme: 'light'
    }
}, false)
