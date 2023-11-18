<template>
  <div class="video-container">
    <video ref="videoElement" autoplay muted playsinline></video>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import axios from 'axios';

import { defineEmits } from 'vue';
const emit = defineEmits(['prediction-made']);


const videoElement = ref(null);
let intervalId = null; // 用于存储定时器的ID

const captureAndSendFrame = () => {
  const video = videoElement.value;
  if (video) {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(blob => {
      const formData = new FormData();
      formData.append('frame', blob);
      axios.post('http://127.0.0.1:5000/api/predict', formData)
          .then(response => {
            // 触发自定义事件并传递结果数据
            emit('prediction-made', response.data);
          })
          .catch(error => {
            console.error('发送帧时出错:', error);
          });
    });
  }
};

onMounted(() => {
  // 获取摄像头视频流
  navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        if (videoElement.value) {
          videoElement.value.srcObject = stream;
        }
        // 设置定时器，例如每5秒发送一次视频帧
        intervalId = setInterval(captureAndSendFrame, 5000);
      })
      .catch(error => {
        console.error('访问媒体设备时出错:', error);
      });
});

onUnmounted(() => {
  // 清除定时器
  if (intervalId) {
    clearInterval(intervalId);
  }
  // 关闭摄像头视频流
  const stream = videoElement.value.srcObject;
  const tracks = stream.getTracks();
  tracks.forEach(track => track.stop());
});
</script>

<style scoped>
.video-container {
  width: 100%;
  height: auto;
  background: black;
}

video {
  width: 100%;
  height: auto;
}
</style>

