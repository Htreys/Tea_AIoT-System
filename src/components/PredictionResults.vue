<template>
  <div class="prediction-results">
    <h3>预测结果</h3>
    <ul>
      <li v-for="(result, index) in results" :key="index" class="predicted-item">
        <span class="item-name">{{ result.class }}</span>
        <span class="confidence">: {{ (result.confidence * 100).toFixed(2) }}%</span>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  results: Array,
});
</script>

<style scoped>
.prediction-results {
  font-family: 'Arial', sans-serif; /* 选择合适的字体 */
  color: #333;
}

.predicted-item {
  margin-bottom: 10px;
}

.item-name {
  font-size: 1.2em;
  font-weight: bold;
  color: #4a90e2;
}

.confidence {
  font-size: 1em;
  color: #ff7f50;
  margin-left: 10px;
}
</style>
