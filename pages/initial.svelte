<script lang="ts">
    import { config } from '$/stores/config'
    import type { App } from '$/types/config'

    const changeTheme = (theme: App['theme']) => {
        $config.app.theme = theme
    }
</script>

<main>
    <section on:click={() => changeTheme('light')}><span>Light</span></section>
    <section on:click={() => changeTheme('dark')}><span>Dark</span></section>
</main>

<style lang="postcss">
    main {
        $space: 10px;
        display: flex;
        justify-content: space-between;
        height: 100vh;
        padding: $space;
        gap: $space;

        section {
            @extend %center;
            width: 100%;
            cursor: pointer;

            &:hover {
                background-color: var(--color2);
            }
        }
    }
</style>
