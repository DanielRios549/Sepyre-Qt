<script lang="ts">
    import * as yup from 'yup'
    import { createForm } from 'svelte-forms-lib'

    const { form, errors, handleChange, handleSubmit } = createForm({
        initialValues: {
            uploadFile: null
        },
        validationSchema: yup.object().shape({
            uploadFile: yup.string().nullable().required('Choose a MP3 file, please.')
        }),
        onSubmit: (values: any) => {
            console.log(values)
            // window.app.functions.copy(JSON.stringify(values))
        }
})
</script>

<form action="" method="post" on:submit|preventDefault={handleSubmit}>
    <label class="file" for="uploadFile">Select MP3 File</label>
    <input
        hidden
        accept="audio/mp3"
        type="file"
        name="uploadFile"
        id="uploadFile"
        class:error={$errors.uploadFile.length > 0}
        on:change={handleChange}
        bind:value={$form.uploadFile}
    />
    {#if $errors.uploadFile}
        <span>{$errors.uploadFile}</span>
    {/if}
    <input type="submit" value="Start"/>
</form>

<style lang="postcss">
    form {
        display: flex;
        flex-direction: column;

        label {
            &.file {
                $size: 100px;
                @extend %center;
                border: 1px solid red;
                height: $size;
                width: $size;
            }
        }
    }
</style>