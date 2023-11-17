import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// 创建 Vue 应用实例
const app = createApp(App);

// 使用路由器实例
app.use(router);

// 挂载 Vue 应用实例
app.mount('#app');
