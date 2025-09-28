<script lang="ts">
  import { onMount } from 'svelte';
  import styles from './Homepage.module.scss';
  
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
    <div class={styles.topBar}>
      <h1>🎭</h1>
      <div class={styles.topBarActions}>
        <button class={styles.btn}>💾</button>
        <button class={styles.btn}>📤</button>
        <button class={styles.btn} on:click={toggleDarkMode}>
          {isDarkMode ? '💡' : '🌙'}
        </button>
      </div>
    </div>

    <!-- Content Container -->
    <div class={styles.contentContainer}>
      <!-- Left Column - Script Editor (3/4 width) -->
      <div class={styles.leftColumn}>
        <div class={styles.scriptEditor}>
          <textarea 
            class={styles.textarea}
            placeholder="Write your script here..."
            rows="20"
          ></textarea>
        </div>
      </div>

      <!-- Right Column - Editing Tools (1/4 width) -->
      <div class={styles.rightColumn}>
        <div class={styles.toolsPanel}>
          <div class={styles.toolSection}>
            <h4>Actions</h4>
            <button class={styles.toolBtn}>Add Character</button>
            <button class={styles.toolBtn}>Add Scene</button>
            <button class={styles.toolBtn}>Add Dialogue</button>
          </div>

          <div class={styles.toolSection}>
            <h4>Formatting</h4>
            <button class={styles.toolBtn}>Bold</button>
            <button class={styles.toolBtn}>Italic</button>
            <button class={styles.toolBtn}>Underline</button>
          </div>

          <div class={styles.toolSection}>
            <h4>Export Options</h4>
            <button class={styles.toolBtn}>PDF</button>
            <button class={styles.toolBtn}>Word</button>
            <button class={styles.toolBtn}>HTML</button>
          </div>

          <div class={styles.toolSection}>
            <h4>Settings</h4>
            <button class={styles.toolBtn}>Preferences</button>
            <button class={styles.toolBtn}>Themes</button>
            <button class={styles.toolBtn}>Help</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
