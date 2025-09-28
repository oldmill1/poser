<script lang="ts">
  import styles from './ScriptEditor.module.scss';
  
  let { isDarkMode } = $props();
</script>

<div class="{styles.leftColumn} {isDarkMode ? styles.dark : ''}">
  <div class={styles.scriptEditor}>
    <textarea 
      class={styles.textarea}
      placeholder="Write your script here..."
      rows="20"
    ></textarea>
  </div>
</div>
