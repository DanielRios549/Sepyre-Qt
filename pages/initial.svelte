<script lang="ts">
    import { config } from '$/stores/config'
    import type { App } from '$/types/config'

    import Light from '$/icons/light.svg'
    import Dark from '$/icons/dark.svg'

    $: steps = 2
    $: step = 1
    $: first = step === 1
    $: last = step === steps

    const changeTheme = (theme: App['theme']) => {
        $config.app.theme = theme
    }
</script>

<main>
    <section class:hide={step !== 1}>
        <button on:click={() => changeTheme('light')}>
            <Light/>Light
        </button>
        <button on:click={() => changeTheme('dark')}>
            <Dark/>Dark
        </button>
    </section>
    <section class:hide={step !== 2}>
        123
    </section>
</main>
<footer>
    <button disabled={first} on:click={() => step--}>Previous</button>
    <button disabled={last} on:click={() => step++}>Next</button>
</footer>

<style lang="postcss">
    $footer: 100px;

    main {
        $space: 10px;
        display: flex;
        flex-direction: column;
        height: calc(100vh - $footer);
        width: 100vw;
        padding: $space;
        gap: $space;

        section {
            display: flex;
            height: 100%;

            &.hide {
                display: none;
            }
            button {
                @extend %center;
                background-color: var(--color1);
                cursor: pointer;
                width: 100%;
                font-size: 1.8rem;
                flex-direction: column;
                gap: 50px;

                &:--btn-hover {
                    background-color: var(--color2);
                }
                :--svg {
                    --size: 250px;
                }
            }

        }
    }
    footer {
        $space: 30px;
        height: $footer;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: $space;
        padding: 0 $space;

        button {
            background-color: var(--color2);
            border-width: 3px;
            border-style: solid;
            border-color: transparent;
            height: 50%;
            width: 200px;

            &:--btn-hover {
                border-color: var(--text3);
            }
            &:disabled {
                background-color: var(--color3);
                cursor: not-allowed;
            }
        }
    }
</style>
