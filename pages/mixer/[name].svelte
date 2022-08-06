<script lang="ts">
    import { page } from '$app/stores'
    import { calculateTime } from '$/lib/utils'
    import Layout from '$/layout/__main.svelte'
    import Play from '$/icons/play.svg'
    import Pause from '$/icons/pause.svg'

    const parts = [
        ['vocals', '#00c9e4'],
        ['drums', '#00dae8'],
        ['bass', '#63fb97'],
        ['piano', '#31eac0'],
        ['other', '#00b4cc']
    ]

    $: length = 0
    $: paused = true
    $: icon = paused ? Play : Pause
    $: time = '0:00'
    $: total = '0:00'

    const path = $page.url.pathname.split('/').at(-1) || ''

    const PlayPause = () => {
        paused = !paused
    }

    const setTotalTime = (event: any) => {
        if (total === '0:00') {
            const seconds = event.target.duration || 0
            total = calculateTime(seconds)
            length = seconds
        }
    }

    const setSeekTime = (event: any) => {
        console.log(event.target.value)
    }
</script>

<Layout>
    {#if path !== ''}
        {#await window.app.functions.getInfo(path)}
            <span>Loading</span>
        {:then info}
            {@const { name } = JSON.parse(info)}
            <section id="info">
                <header>
                    <h1>{name}</h1>
                </header>
                <button on:click={PlayPause}>
                    <svelte:component this={icon}/>
                </button>
            </section>
            <section id="time">
                <span>{time}</span>
                <span>{total}</span>
            </section>
            <section id="mixer">
                <input type="range" name="progress" id="progress" max={length} value="0" on:input={setSeekTime}/>
                {#each parts as [part, color]}
                    {@const audio = `audio:///${path}/${part}.wav`}
                    <article style="--color: {color};">
                        <header>
                            <h2>{part}</h2>
                        </header>
                        <audio
                            id="part-{part}"
                            class="part"
                            bind:paused
                            on:loadedmetadata={setTotalTime}>
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
    $left: 100px;
    #info {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        gap: 10px;

        header {
            order: 2;
        }
        button {
            @extend %center;
            $size: 50px;
            border-radius: 50%;
            background-color: var(--color2);
            color: var(--text);
            height: $size;
            width: $size;
            order: 1;

            :global {
                svg path {
                    fill: var(--text) !important;
                }
            }
        }
    }
    #time {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    #mixer {
        position: relative;
        border-radius: 5px;
        display: flex;
        flex-direction: column;
        gap: 5px;

        input[type="range"] {
            position: absolute;
            outline: none;
            -webkit-appearance: none;
            background-color: transparent;
            margin-left: $left;
            width: calc(100% - $left);
            height: 100%;
            z-index: 12;
            cursor: pointer;

            &::-webkit-slider-thumb {
                -webkit-appearance: none;
                border-radius: 8px;
                border: 2px solid var(--color1);
                background-color: var(--highlight);
                height: 540px; /* TODO: Make thumnb height dinamic */
                width: 8px;
            }
        }
        article {
            display: flex;
            height: 100px;
            z-index: 11;

            header {
                background-color: var(--color2);
                width: $left;

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