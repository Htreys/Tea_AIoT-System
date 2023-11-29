<template>
  <div class="top-bar">
    <div class="logo-container">
      <img src="../../public/top.svg" alt="Logo" class="logo"/>
    </div>
    <div class="controls-container">
      <!-- 控件按钮，如设置等 -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'TopBar'
  // 如果需要，可以添加逻辑
};
</script>

<style scoped>
.top-bar {
  display: flow;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #003366; /* 深蓝色背景 */
  color: white; /* 白色文本 */
}

.logo-container {
  /* 如果需要，可以添加样式 */
}

.logo {
  height: 50px; /* 根据实际情况调整 */
}

.title-container h1 {
  margin: 0;
  font-size: 24px; /* 根据实际情况调整 */
  font-weight: bold; /* 加粗字体 */
}

.controls-container {
  /* 如果需要，可以添加样式 */
}
</style>
