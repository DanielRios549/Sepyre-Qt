/// <reference types="@sveltejs/kit" />

import { Separation } from '$/types/item'

declare namespace App {
    // interface Locals {}
    // interface Platform {}
    // interface Session {}
    // interface Stuff {}
}

export declare global {
    declare class Stringified<T> extends String {
        private ___object: T
    }

    interface JSON {
        stringify<T>(
            value: T,
            replacer?: (key: string, value: any) => any,
            space?: string | number
        ): string & Stringified<T>

        parse<T>(text: Stringified<T>, reviver?: (key: any, value: any) => any): T
        parse(text: string, reviver?: (key: any, value: any) => any): any
    }

    interface Window {
        app: {
            config: {
                set: (options: str) => Promise<void>
                get: (section: string, option: string, defaultValue?: string) => Promise<string>
                getAll: () => Promise<string>
            },
            pages: {
                initialSettings: () => Promise<void>
                mainWindow: () => Promise<void>
            },
            functions: {
                copy: (file: any) => Promise<void>
                getFiles: () => Promise<string[]>
                getInfo: (name: string) => Promise<Stringified<Separation>>
            }
        }
    }
}
