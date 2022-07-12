<script lang="ts">
    import { onMount } from 'svelte'
    import { config } from '$/stores/config'

    onMount(async () => {
        $config = await window.app.config.getAll()
    })
</script>

<header>
    <p>
        {$config}
    </p>
</header>
