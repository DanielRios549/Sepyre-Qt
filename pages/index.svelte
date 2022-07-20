<script lang="ts">
    import { config } from '$/stores/config'
    import Header from '$/layout/header.svelte'
    import Aside from '$/layout/aside.svelte'
    import Footer from '$/layout/footer.svelte'
</script>

<Header/>
<Aside/>
<main>
    <span>{$config.app.theme}</span>
</main>
<Footer/>

<style lang="postcss">
    main {
        grid-area: main;
        height: 100vh;
    }
</style>
