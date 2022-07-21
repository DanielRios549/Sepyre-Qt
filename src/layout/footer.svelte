<script lang="ts"></script>

<footer>
    <slot/>
    <span>Footer</span>
</footer>

<style lang="postcss">
    footer {
        grid-area: footer;
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }
</style>