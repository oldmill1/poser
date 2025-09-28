<script lang="ts">
  import styles from './ScriptEditor.module.scss';
  
</script>

<div class="{styles.leftColumn} {styles.dark}">
  <div class={styles.scriptEditor}>
    <textarea 
      class={styles.textarea}
      placeholder="Start writing, then press Enter when done..."
      rows="8"
    ></textarea>
  </div>
</div>
