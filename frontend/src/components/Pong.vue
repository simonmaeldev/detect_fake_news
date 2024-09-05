<template>
  <div class="pong-container">
    <button @click="pingServer" :disabled="loading">Ping</button>
    <p v-if="loading">Loading...</p>
    <p v-else-if="result">{{ result }}</p>
    <p v-else-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import axios from 'axios'

export default defineComponent({
  name: 'Pong',
  setup() {
    const result = ref('')
    const error = ref('')
    const loading = ref(false)

    const pingServer = async () => {
      loading.value = true
      result.value = ''
      error.value = ''

      try {
        const response = await axios.get('/api/ping')
        result.value = response.data.text
      } catch (err) {
        error.value = 'Error: Unable to reach the server'
        console.error(err)
      } finally {
        loading.value = false
      }
    }

    return {
      result,
      error,
      loading,
      pingServer
    }
  }
})
</script>

<style scoped>
.pong-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

p {
  margin-top: 20px;
  white-space: pre-wrap;
}

.error {
  color: red;
}
</style>
