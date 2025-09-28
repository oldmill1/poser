<script lang="ts">
  import styles from './Ed.module.scss';
  
</script>

<div class="{styles.leftColumn} {styles.dark}">
  <div class={styles.scriptEditor}>
    <textarea 
      id="script-controller"
      name="script-controller"
      class={styles.scriptController}
      placeholder="Start writing, then press ⏎ when done..."
      rows="8"
    ></textarea>
  </div>
</div>
