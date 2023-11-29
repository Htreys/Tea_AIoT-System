<template>
  <div id="app">
    <!-- 主内容区 -->
    <main>
      <top-bar></top-bar>
      <router-view></router-view>

      <current-time class="timestamp"></current-time>
      <video-stream @prediction-made="handlePrediction"></video-stream>
      <historical-data-chart/>
      <prediction-results :results="predictionResults" />
    </main>

    <!-- 可选的页脚 -->
<!--    <footer>-->
<!--      <p>© 2023 Hangzhou City University</p>-->
<!--    </footer>-->
  </div>
</template>

<script>
import { ref } from 'vue';
import CurrentTime from '@/components/CurrentTime.vue';
import VideoStream from "@/components/VideoStream.vue";
import PredictionResults from "@/components/PredictionResults.vue";
import TopBar from './components/TopBar.vue';
import HistoricalDataChart from "@/components/HistoricalDataChart.vue";

export default {
  name: 'App',
  components: {
    HistoricalDataChart,
    CurrentTime,
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


body::before {
  content: ""; /* 伪元素需要content属性来显示 */
  position: fixed; /* 固定位置，不随滚动条滚动 */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url('https://img.js.design/assets/img/61dfc457b7aade6258558905.png') no-repeat center center;
  background-size: cover;
  opacity: 0.6; /* 设置不透明度 */
  pointer-events: none; /* 防止伪元素阻挡鼠标事件 */
  z-index: -1; /* 确保背景在最底层 */
}

prediction-results {
  background: none; /* 或者使用具体的透明背景颜色 */
}


/* 其他样式... */
</style>


