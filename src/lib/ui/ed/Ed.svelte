<script lang="ts">
  import styles from './Ed.module.scss';
  import { getRandomQuote } from '$lib/quotes';
  
  let text = $state(getRandomQuote());
  let wordCount = $state(0);
  let sentenceCount = $state(0);
  
  // Initialize counts when component loads
  updateCounts();
  
  function updateCounts() {
    const trimmedText = text.trim();
    
    // Word count - split by whitespace and filter out empty strings
    wordCount = trimmedText ? trimmedText.split(/\s+/).length : 0;
    
    // Sentence count - split by sentence endings and filter out empty strings
    sentenceCount = trimmedText ? trimmedText.split(/[.!?]+/).filter(sentence => sentence.trim().length > 0).length : 0;
  }
  
  function handleKeydown(event: KeyboardEvent) {
    if (event.key === 'Enter') {
      console.log(`📊 Words: ${wordCount} | Sentences: ${sentenceCount} | Text: "${text.trim()}"`);
    }
  }
</script>

<div class="{styles.leftColumn} {styles.dark}">
  <div class={styles.scriptEditor}>
    <textarea 
      id="script-controller"
      name="script-controller"
      class={styles.scriptController}
      placeholder="Start writing, then press ⏎ when done..."
      rows="8"
      bind:value={text}
      oninput={updateCounts}
      onkeydown={handleKeydown}
    ></textarea>
  </div>
</div>
