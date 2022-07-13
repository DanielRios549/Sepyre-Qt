<script lang="ts">
    import { onMount } from 'svelte'
    import { config } from '$/stores/config'
    import type { Config } from '$/types/config'

    let ready = false

    onMount(async() => {
        const options: Config = JSON.parse(await window.app.config.getAll())
        let section: keyof Config

        // TODO: Fix Types
        for (section in options) {
            for (const option in options[section] as any) {
                $config[section][option] = options[section][option]
            }
        }

        ready = true
    })
</script>

{#if ready}
    <slot/>
{/if}

<style lang="scss" global>
    @use "../styles/app.scss";
</style>