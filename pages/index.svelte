<script lang="ts">
    import Layout from '$/layout/__main.svelte'
    import SeparationForm from '$/forms/separation.svelte'
</script>

<Layout>
    <input type="text" slot="header" placeholder="Search" name="search"/>
    {#await window.app.functions.getFiles()}
        <span>Loading...</span>
    {:then items}
        {#if items.length <= 0}
            <SeparationForm/>
        {:else}
            <ul>
                {#each items as item}
                    {@const name = item.replaceAll('-', ' ')}
                    <li><a href="/mixer/{item}">{name}</a></li>
                {/each}
            </ul>
        {/if}
    {/await}
</Layout>

<style lang="postcss">
    input {
        background-color: var(--color2);
        transition: none;
    }
</style>
