<script lang="ts">
    import { page } from '$app/stores'
    import Layout from '$/layout/__main.svelte'

    const name = $page.url.pathname.split('/').at(-1) || ''
</script>

<Layout>
    {#if name !== ''}
        {#await window.app.functions.getInfo(name)}
            <span>Loading</span>
        {:then info}
            {@const { name } = JSON.parse(info)}
            <span>{name}</span>
        {/await}
    {/if}
</Layout>

<style lang="postcss">

</style>