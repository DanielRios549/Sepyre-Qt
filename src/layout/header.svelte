<script lang="ts"></script>

<header>
    <h1>Sepyre</h1>
    <slot/>
</header>

<style lang="postcss">
    header {
        grid-area: header;
        background-color: var(--color1);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
    }
</style>
