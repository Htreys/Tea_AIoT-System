<template>
  <div class="prediction-results">
    <h3>预测结果</h3>
    <ul>
      <li v-for="(result, index) in results" :key="index">
        {{ result.class }}: {{ (result.confidence * 100).toFixed(2) }}%
      </li>
    </ul>
  </div>
</template>


<script setup>
import { defineProps } from 'vue';

// 定义 props
defineProps({
  results: Array,
});
</script>

