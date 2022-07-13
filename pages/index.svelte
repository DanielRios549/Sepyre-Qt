<script lang="ts">
    import { onMount } from 'svelte'
    import { config } from '$/stores/config'

    onMount(async() => {
        config.set(JSON.parse(await window.app.config.getAll()))
    })

    // const change = (section: string, value: string) => {
    //     window.app.config.set(section, value)
    // }
</script>

<header>
    <p>
        Config:
        {$config}
    </p>
    <!-- <button on:click={change}>Change</button> -->
</header>

<style lang="postcss">
    p {
        color: var(--text);
    }
</style>
