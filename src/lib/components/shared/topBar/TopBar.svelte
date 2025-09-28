<script lang="ts">
  import styles from './TopBar.module.scss';
  
  let { isDarkMode, onToggleDarkMode } = $props();
</script>

<div class={styles.topBar}>
  <h1>🎭</h1>
  <div class={styles.topBarActions}>
    <button class={styles.btn}>💾</button>
    <button class={styles.btn}>📤</button>
    <button class={styles.btn} on:click={onToggleDarkMode}>
      {isDarkMode ? '💡' : '🌙'}
    </button>
  </div>
</div>
