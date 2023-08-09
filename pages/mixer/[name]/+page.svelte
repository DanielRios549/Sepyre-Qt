<script lang="ts">
    import { page } from '$app/stores'
    import { calculateTime } from '$/lib/utils'
    import Layout from '$/layout/__main.svelte'
    import Play from '$/icons/play.svg'
    import Pause from '$/icons/pause.svg'

    const path = $page.url.pathname.split('/').at(-1) || ''

    const parts = [
        ['vocals', '#00c9e4'],
        ['drums', '#63fb97'],
        ['bass', '#00dae8'],
        ['piano', '#31eac0'],
        ['other', '#00b4cc']
    ]

    $: range = 0
    $: current = 0

    $: paused = true
    $: icon = paused ? Play : Pause
    $: time = '0:00'
    $: total = '0:00'

    const PlayPause = () => {
        paused = !paused
    }

    const setTotalTime = (event: any) => {
        if (total === '0:00') {
            range = event.target.duration || 0
            total = calculateTime(range)
        }
    }

    const setSeekTime = (event: any) => {
        const parts = document.getElementsByTagName('audio')

        Array.prototype.slice.call(parts).forEach((audio) => {
            audio.currentTime = event.target.value
        })

        current = event.target.value || 0
        time = calculateTime(current)
    }

    const changeVolume = (event: any) => {
        const name = (event.target.id as string).split('-')[1].trim()
        const element = document.getElementById(`part-${name}`) as HTMLMediaElement

        element.volume = event.target.value / 100
    }

    const updateTime = (event: any) => {
        current = event.target.currentTime || 0
        time = calculateTime(current)
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
                <input
                    type="range"
                    name="progress"
                    id="progress"
                    max={range}
                    bind:value={current}
                    on:input={setSeekTime}
                />
                {#each parts as [part, color], index}
                    {@const audio = `audio:///${path}/${part}.wav`}
                    <article style="--color: {color};">
                        <header>
                            <h2>{part}</h2>
                            <input
                                type="range"
                                name="volume-{part}"
                                id="volume-{part}"
                                class="volume"
                                max="100"
                                value={100}
                                on:input={changeVolume}
                            >
                        </header>
                        {#if index === 0}
                            <audio
                                id="part-{part}"
                                class="part"
                                bind:paused
                                on:timeupdate={updateTime}
                                on:loadedmetadata={setTotalTime}
                            >
                                <source src={audio}>
                            </audio>
                        {:else}
                            <audio
                                id="part-{part}"
                                class="part"
                                bind:paused
                            >
                                <source src={audio}>
                            </audio>
                        {/if}
                        <section>
                            <!-- <img src="audio:///{path}/__PEAKS__/{part}.png" alt="{part} peak"> -->
                        </section>
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
        display: flex;
        flex-direction: column;
        gap: 5px;

        #progress {
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
                height: 540px; /* TODO: Make thumnb height dynamic */
                width: 8px;
            }
        }
        article {
            display: flex;
            height: 100px;
            z-index: 11;
            overflow: hidden;

            &:nth-of-type(1) {
                border-radius: 5px 5px 0 0;
            }
            &:last-child {
                border-radius: 0 0 5px 5px;
            }
            header {
                position: relative;
                background-color: var(--color2);
                width: $left;
                padding: 5px;
                display: flex;
                justify-content: space-between;

                h2 {
                    text-transform: capitalize;
                }
                .volume {
                    $height: 15px;
                    $width: 120px;
                    outline: none;
                    -webkit-appearance: none;
                    background-color: transparent;
                    position: absolute;
                    top: 35px;
                    left: 25px;
                    width: $width;
                    height: $height;
                    transform: rotate(-90deg);

                    &::-webkit-slider-runnable-track {
                        border-radius: 20px;
                        -webkit-appearance: none;
                        background-color: var(--color1);
                    }
                    &::-webkit-slider-thumb {
                        -webkit-appearance: none;
                        border-radius: 8px;
                        border: 2px solid var(--color1);
                        background-color: var(--highlight);
                        height: $height;
                        width: 15px;
                    }
                }
            }
            section {
                background-color: var(--color);
                flex-grow: 1;

                img {
                    height: 100%;
                    width: 100%;
                }
            }
        }
    }
</style>