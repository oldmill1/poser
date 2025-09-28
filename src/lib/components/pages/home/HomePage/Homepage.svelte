<script lang="ts">
  import styles from './Homepage.module.scss';
  // Component logic here
</script>

<div class={styles.pageContainer}>
  <div class={styles.container}>
    <!-- Top Bar -->
    <div class={styles.topBar}>
      <h1>Poser</h1>
      <div class={styles.topBarActions}>
        <button class={styles.btn}>Save</button>
        <button class={styles.btn}>Export</button>
      </div>
    </div>

    <!-- Content Container -->
    <div class={styles.contentContainer}>
      <!-- Left Column - Script Editor (3/4 width) -->
      <div class={styles.leftColumn}>
        <div class={styles.scriptEditor}>
          <h2>Script Editor</h2>
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
          <h3>Editing Tools</h3>
          
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
