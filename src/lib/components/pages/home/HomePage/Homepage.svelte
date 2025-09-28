<script lang="ts">
  import { onMount } from 'svelte';
  import styles from './Homepage.module.scss';
  import TopBar from '$lib/components/shared/topBar/TopBar.svelte';
  import ScriptEditor from '$lib/components/shared/scriptEditor/ScriptEditor.svelte';
  import ToolsPanel from '$lib/components/shared/toolsPanel/ToolsPanel.svelte';
  
</script>

<div class="{styles.pageContainer} {styles.dark}">
  <div class={styles.container}>
    <!-- Top Bar -->
    <TopBar />

    <!-- Content Container -->
    <div class={styles.contentContainer}>
      <!-- Left Column - Script Editor (3/4 width) -->
      <ScriptEditor />

      <!-- Right Column - Editing Tools (1/4 width) -->
      <ToolsPanel />
    </div>
  </div>
</div>
