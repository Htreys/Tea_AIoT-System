import { createRouter, createWebHistory } from 'vue-router';
import DashboardView from '@/views/DashboardView.vue';

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: [
        {
            path: '/', // 将 DashboardView 设置为根路径的视图
            name: 'Home', // 通常首页会被命名为 'Home'
            component: DashboardView,
        },
        // ...其他路由规则...
    ],
});

export default router;
