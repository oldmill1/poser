<script lang="ts">
  import styles from './+page.module.scss';
  import Ed from '$lib/ui/ed/ed.svelte';
  
</script>

<div class="{styles.pageContainer} {styles.dark}">
  <div class={styles.container}>

    <!-- Content Container -->
    <div class={styles.contentContainer}>
      <!-- Full Width Editor -->
      <Ed />
    </div>
  </div>
</div>
