<script lang="ts">
    import { page } from '$app/stores'
    import Layout from '$/layout/__main.svelte'

    const name = $page.url.pathname.split('/').at(-1)
</script>

<Layout>
    <span>Mixer of {name}</span>
</Layout>

<style lang="postcss">
    
</style>