<script lang="ts">
  import styles from './+page.module.scss';
  import Editor from '$lib/ui/editor/editor.svelte';
  
</script>

<div class="{styles.pageContainer} {styles.dark}">
  <div class={styles.container}>

    <!-- Content Container -->
    <div class={styles.contentContainer}>
      <!-- Full Width Editor -->
      <Editor />
    </div>
  </div>
</div>
