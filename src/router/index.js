import { createRouter, createWebHistory } from 'vue-router';

// 如果您以后添加了其他视图组件，可以在这里导入它们

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: [
        // 如果您没有其他页面，这里实际上可以是一个空数组
        // 例如，如果您的 App.vue 本身是主页面，您可能不需要在这里配置路由
    ],
});

export default router;
