<script lang="ts">
    import Header from '$/layout/header.svelte'
    import Aside from '$/layout/aside.svelte'
    import Footer from '$/layout/footer.svelte'
</script>

<Header>
    <slot name="header"/>
</Header>
<Aside>
    <slot name="aside"/>
</Aside>
    <main>
        <slot/>
    </main>
<Footer>
    <slot name="footer"/>
</Footer>

<style lang="postcss">
    :--body {
        $header: 60px;
        $footer: 20px;
        overflow-y: hidden;
        display: grid;
        grid-template:
            "header header" $header
            "aside main" calc(100vh - ($header + $footer))
            "footer footer" $footer
            / min-content 1fr
        ;
    }
    main {
        grid-area: main;
        height: 100vh;
        padding: 10px;
    }
</style>