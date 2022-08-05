<script lang="ts">
    import { page } from '$app/stores'
    import Layout from '$/layout/__main.svelte'

    const path = $page.url.pathname.split('/').at(-1) || ''
</script>

<Layout>
    {#if path !== ''}
        {#await window.app.functions.getInfo(path)}
            <span>Loading</span>
        {:then info}
            {@const { name } = JSON.parse(info)}
            <h1>{name}</h1>
            <audio controls>
                <source src="audio:///{path}/drums.wav">
            </audio>
        {/await}
    {/if}
</Layout>

<style lang="postcss">

</style>