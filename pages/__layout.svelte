<script lang="ts">
    import { browser } from '$app/env'
    import { onMount } from 'svelte'
    import { config, defaults, getConfig } from '$/stores/config'

    let ready = !import.meta.env.DEV

    $: addBodyId = () => {
        if (browser && ready) {
            document.body.id = $config.app.theme
        }
    }

    onMount(async () => {
        await getConfig()
        ready = true
    })

    $: addBodyId()

    $: if (!browser) {
        config.set(defaults)
    }
</script>

{#if ready}
    <slot/>
{/if}

<style lang="scss" global>
    @use "../styles/app.scss";
</style>