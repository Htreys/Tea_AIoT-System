const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/predict': {
        target: 'http://127.0.0.1:5000', // Flask后端地址
        ws: true, // 如果您想要代理 websockets
        changeOrigin: true // 如果您的后端设置了验证头部信息中的host，这个参数会修改它
      },
      // 这里可以根据需要添加更多的代理规则
    }
  },
});

