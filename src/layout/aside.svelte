<script lang="ts">
    import { page } from '$app/stores'

    const links = [
        ['/', 'Dashboard'],
        ['/profile', 'Profile']
    ]
</script>

<aside>
    <nav>
        <ul>
            {#each links as [link, name]}
                <li class:active={$page.url.pathname === link}>
                    <a href={link}>{name}</a>
                </li>
            {/each}
        </ul>
    </nav>
    <slot/>
</aside>

<style lang="scss">
    aside {
        grid-area: aside;
        background-color: var(--color1);

        nav {
            width: 300px;

            ul {
                display: flex;
                flex-direction: column;
                gap: 10px;

                li {
                    height: 40px;
                    text-indent: 40px;

                    &:not(.active) {
                        a:hover {
                            background-color: var(--color2);
                            color: var(--text);
                        }
                    }
                    &.active {
                        position: relative;

                        &::before {
                            content: '';
                            background-color: var(--text);
                            position: absolute;
                            width: 5px;
                            height: 100%;
                        }
                        a {
                            color: var(--text);
                            cursor: auto;
                        }
                    }
                    a {
                       display: flex;
                       align-items: center;
                       justify-content: flex-start;
                       color: var(--text2);
                    }
                }
            }
        }
    }
</style>