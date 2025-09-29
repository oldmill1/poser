<script lang="ts">
  import styles from './editor.module.scss';
  import { getRandomQuote } from '$lib/quotes';
  
  let text = $state(getRandomQuote());
  let wordCount = $state(0);
  let sentenceCount = $state(0);
  let isLoading = $state(false);
  
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

  async function handleEdit() {
    if (!text.trim() || isLoading) {
      console.log('No text to edit or already loading');
      return;
    }

    isLoading = true;

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: text,
          isEdit: true
        })
      });

      if (!response.ok) {
        throw new Error('Failed to get edit response');
      }

      const data = await response.json();
      
      // Log the full response for debugging
      console.log('Edit response:', data);
      
      if (data.text) {
        // New structured response format
        text = data.text;
        console.log('Analysis:', data.analysis);
        console.log('Diff:', data.diff);
        updateCounts();
      } else if (data.response) {
        // Fallback to old format
        text = data.response;
        updateCounts();
      }
    } catch (error) {
      console.error('Error editing text:', error);
    } finally {
      isLoading = false;
    }
  }
</script>

<div class="{styles.leftColumn} {styles.dark}">
  <div class={styles.scriptEditor}>
    <div class={styles.textareaContainer}>
      <textarea 
        id="script-controller"
        name="script-controller"
        class="{styles.scriptController} {isLoading ? styles.loading : ''}"
        placeholder="Start writing, then press ⏎ when done..."
        rows="8"
        bind:value={text}
        oninput={updateCounts}
        onkeydown={handleKeydown}
        disabled={isLoading}
      ></textarea>
      <button class={styles.quickEdit} onclick={handleEdit} type="button" aria-label="Edit text with AI" disabled={isLoading}>
        <div class={styles.editIcon}>✏️</div>
      </button>
    </div>
  </div>
</div>
