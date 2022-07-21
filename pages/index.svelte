<script lang="ts">
    import { config } from '$/stores/config'
    import Layout from '$/layout/__main.svelte'
</script>

<Layout>
    <span>{$config.app.theme}</span>
    <input type="text" slot="header" placeholder="Search"/>
</Layout>

<style lang="postcss">
    input {
        background-color: var(--color2);
        transition: none;
    }
</style>
