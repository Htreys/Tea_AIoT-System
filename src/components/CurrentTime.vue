<template>
  <div class="timestamp">当前时间：{{ currentTime }}</div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';

export default {
  name: 'CurrentTime',
  setup() {
    const currentTime = ref(new Date().toLocaleTimeString());

    // 更新时间的函数
    const updateCurrentTime = () => {
      currentTime.value = new Date().toLocaleTimeString();
    };

    // 设置定时器
    let intervalId = null;
    onMounted(() => {
      intervalId = setInterval(updateCurrentTime, 1000);
    });

    // 清除定时器
    onUnmounted(() => {
      if (intervalId) {
        clearInterval(intervalId);
      }
    });

    return { currentTime };
  },
};
</script>

<style scoped>
.timestamp {
  //position: absolute;
  top: 16px;
  right: 16px;
  background: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 30px;
  border-radius: 4px;
  font-size: 0.9em;
}

</style>
