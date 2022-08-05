<script lang="ts">
    import { page } from '$app/stores'
    import Layout from '$/layout/__main.svelte'

    const parts = [
        ['vocals', '#00c9e4'],
        ['drums', '#00dae8'],
        ['bass', '#63fb97'],
        ['piano', '#31eac0'],
        ['other', '#00b4cc']
    ]

    $: paused = true
    $: buttonName = paused ? 'Play' : 'Pause'

    const path = $page.url.pathname.split('/').at(-1) || ''

    const PlayPause = () => {
        paused = !paused
    }
</script>

<Layout>
    {#if path !== ''}
        {#await window.app.functions.getInfo(path)}
            <span>Loading</span>
        {:then info}
            {@const { name } = JSON.parse(info)}
            <h1>{name}</h1>
            <button on:click={PlayPause}>{buttonName}</button>
            <section>
                {#each parts as [part, color]}
                    {@const audio = `audio:///${path}/${part}.wav`}
                    <article style="--color: {color};">
                        <header><h2>{part}</h2></header>
                        <audio id="part-{part}" class="part" bind:paused>
                            <source src={audio}>
                        </audio>
                        <section></section>
                    </article>
                {/each}
            </section>
        {/await}
    {/if}
</Layout>

<style lang="postcss">
    button {
        background-color: var(--color2);
        color: var(--text);
    }
    section {
        border-radius: 5px;
        display: flex;
        flex-direction: column;
        gap: 5px;
        overflow: hidden;

        article {
            display: flex;
            height: 100px;

            header {
                background-color: var(--color2);
                width: 100px;

                h2 {
                    text-transform: capitalize;
                }
            }
            section {
                background-color: var(--color);
                flex-grow: 1;
            }
        }
    }
</style>