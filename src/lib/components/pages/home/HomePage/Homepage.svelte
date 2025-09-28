<script lang="ts">
  import { onMount } from 'svelte';
  import styles from './Homepage.module.scss';
  import TopBar from '$lib/components/shared/topBar/TopBar.svelte';
  import ScriptEditor from '$lib/components/shared/scriptEditor/ScriptEditor.svelte';
  import ToolsPanel from '$lib/components/shared/toolsPanel/ToolsPanel.svelte';
  
  let isDarkMode = true;

  // Cookie utility functions
  function setCookie(name: string, value: string, days: number = 365) {
    const expires = new Date();
    expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
  }

  function getCookie(name: string): string | null {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) === ' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }

  function toggleDarkMode() {
    isDarkMode = !isDarkMode;
    setCookie('darkMode', isDarkMode.toString());
  }

  function updateBodyClass() {
    // No longer needed since we're using reactive classes
  }

  onMount(() => {
    // Check for saved dark mode preference
    const savedDarkMode = getCookie('darkMode');
    if (savedDarkMode === 'false') {
      isDarkMode = false;
    }
  });
</script>

<div class="{styles.pageContainer} {isDarkMode ? styles.dark : ''}">
  <div class={styles.container}>
    <!-- Top Bar -->
    <TopBar {isDarkMode} onToggleDarkMode={toggleDarkMode} />

    <!-- Content Container -->
    <div class={styles.contentContainer}>
      <!-- Left Column - Script Editor (3/4 width) -->
      <ScriptEditor {isDarkMode} />

      <!-- Right Column - Editing Tools (1/4 width) -->
      <ToolsPanel {isDarkMode} />
    </div>
  </div>
</div>
