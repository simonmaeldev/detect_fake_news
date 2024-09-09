<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const inputText = ref('')
const result = ref(null)
const inputRef = ref(null)
const errorMessage = ref('')

const submitText = async () => {
  try {
    errorMessage.value = ''
    const response = await fetch('/api/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: inputText.value }),
    })
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    result.value = await response.json()
  } catch (error) {
    console.error('Error:', error)
    errorMessage.value = `Error: ${error.message}`
    result.value = null
  }
}

const handleKeyDown = (event: KeyboardEvent) => {
  if (event.ctrlKey && event.key === 'i') {
    event.preventDefault()
    inputRef.value.focus()
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeyDown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeyDown)
})
</script>

<template>
  <div class="container">
    <h1>Fake or True Info Predictor</h1>
    <input
      ref="inputRef"
      v-model="inputText"
      @keyup.enter="submitText"
      placeholder="Paste text or URL (Ctrl + I to focus)"
      type="text"
    />
    <button @click="submitText">Predict</button>
    <div v-if="result" class="result">
      <p>
        This information is likely
        <span :class="{ 'true': result.real, 'fake': !result.real }">
          {{ result.real ? 'TRUE' : 'FAKE' }}
        </span>
      </p>
      <p>Confidence: {{ result.confidence.toFixed(2) }}%</p>
    </div>
    <div v-if="errorMessage" class="error">
      {{ errorMessage }}
    </div>
  </div>
</template>

<style scoped>

:global(#app) {
  /* Your styles for #app */
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

body {
  background-color: #1a1a1a;
  color: #ffffff;
  font-family: Arial, sans-serif;
}

.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

h1 {
  margin-bottom: 2rem;
}

input {
  width: 100%;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  border: none;
  border-radius: 25px;
  background-color: #333;
  color: #fff;
  margin-bottom: 1rem;
}

button {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  border: none;
  border-radius: 25px;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.result {
  margin-top: 2rem;
  padding: 1rem;
  border-radius: 15px;
  background-color: #333;
}

.true {
  color: #4CAF50;
}

.fake {
  color: #f44336;
}

.error {
  margin-top: 1rem;
  color: #f44336;
  font-weight: bold;
}
</style>
