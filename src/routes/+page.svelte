<script lang="ts">
  import styles from './+page.module.scss';
  import TopBar from '$lib/ui/topBar/TopBar.svelte';
  import Ed from '$lib/ui/ed/Ed.svelte';
  import Widgets from '$lib/ui/widgets/Widgets.svelte';
  
</script>

<div class="{styles.pageContainer} {styles.dark}">
  <div class={styles.container}>
    <!-- Top Bar -->
    <TopBar />

    <!-- Content Container -->
    <div class={styles.contentContainer}>
      <!-- Left Column - Script Editor (3/4 width) -->
      <Ed />

      <!-- Right Column - Editing Tools (1/4 width) -->
      <Widgets />
    </div>
  </div>
</div>
