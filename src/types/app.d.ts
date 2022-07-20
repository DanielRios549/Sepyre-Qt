/// <reference types="@sveltejs/kit" />

declare namespace App {
    // interface Locals {}
    // interface Platform {}
    // interface Session {}
    // interface Stuff {}
}

export declare global {
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
            }
        }
    }
}
