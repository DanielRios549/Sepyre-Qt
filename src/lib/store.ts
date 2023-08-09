import { writable } from 'svelte/store'
import { browser } from '$app/environment'

type Key = keyof Window['app']
type Method = string

export function savable<T>(key: Key, update: Method, initial: any) {
    const store = writable<T>(initial, () => {
        const unsubscribe: any = store.subscribe((value) => {
            if (browser && update) {
                window.app[key][update](JSON.stringify(value))
            }
        })

        return unsubscribe
    })

    return store
}
