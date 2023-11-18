<template>
  <div id="app">
    <!-- 主内容区 -->
    <main>
      <top-bar></top-bar>
      <router-view></router-view>
      <video-stream @prediction-made="handlePrediction" />
      <prediction-results :results="predictionResults" />
    </main>

    <!-- 可选的页脚 -->
    <footer>
      <p>© 2023 Hangzhou City University</p>
    </footer>
  </div>
</template>

<script>
import { ref } from 'vue';
import VideoStream from "@/components/VideoStream.vue";
import PredictionResults from "@/components/PredictionResults.vue";
import TopBar from './components/TopBar.vue';

export default {
  name: 'App',
  components: {
    TopBar,
    PredictionResults,
    VideoStream
  },
  setup() {
    // 声明响应式数据
    const predictionResults = ref([]);

    // 事件处理函数
    const handlePrediction = (data) => {
      predictionResults.value = [data]; // 假设我们只处理最新的预测结果
    };

    // 暴露给模板的响应式数据和函数
    return {
      predictionResults,
      handlePrediction
    };
  },
};
</script>

<style>
/* 在这里编写全局 CSS */
#app {
  text-align: center;
}

/* 其他样式... */
</style>


