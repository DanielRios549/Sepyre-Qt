import { savable } from '$/lib/store'
import type { Config } from '$/types/config'

export const defaults: Config = {
    app: {
        theme: 'light'
    }
}

export const config = savable<Config>('config', 'set', null)

export async function getConfig() {
    config.set(JSON.parse(await window.app.config.getAll()))
}
