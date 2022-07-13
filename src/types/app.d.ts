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
                set: (self, section: str, key: str, value: str) => Promise<any>
                get: (section: string, option: string, defaultValue?: string) => Promise<string>
                getAll: () => Promise<string>
            }
        }
    }
}
