<script lang="ts">
  import styles from './Widgets.module.scss';
  
</script>

<div class="{styles.rightColumn} {styles.dark}">
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
