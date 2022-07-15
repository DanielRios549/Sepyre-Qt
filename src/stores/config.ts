import { savable } from '$/lib/store'
import type { Config } from '$/types/config'

export const defaults: Config = {
    app: {
        theme: 'light'
    }
}

export const config = savable<Config>('config', 'set', null)

export async function getConfig() {
    const get = JSON.parse(await window.app.config.getAll())
    const configs = Object.keys(get).length > 0 ? get : defaults

    config.set(configs)
}
