<script lang="ts">
    let log = 'log'
    let test: object = {}

    const handleClick = async () => {
        log = await window.app.config.get('app', 'theme')
    }
    const handleClick2 = async () => {
        test = await window.app.config.getAll()
    }
</script>

<header>
    <p>
        {log}
    </p>
    <p>{test}</p>
    <button on:click={handleClick}>Log</button>
    <button on:click={handleClick2}>Log2</button>
</header>
