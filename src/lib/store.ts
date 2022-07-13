import { writable } from 'svelte/store'
import { browser } from '$app/env'

export function savable<T>(key: string, initial: T | string | [] | Record<string, never> | boolean, save = true) {
    let data: any = initial

    if (save) {
        const persist = browser && sessionStorage.getItem(key)
        data = persist ? JSON.parse(persist) : initial
    }

    const store = writable<T>(data, () => {
        const unsubscribe: any = store.subscribe((value) => {
            if (save) {
                browser && sessionStorage.setItem(key, JSON.stringify(value))
            }
        })

        return unsubscribe
    })

    return store
}
