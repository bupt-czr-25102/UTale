// 雏雁项目小程序入口文件
App({
  // 小程序初始化时执行
  onLaunch: function() {
    console.log('雏雁小程序启动');
    // 可以在这里初始化全局数据或执行一些启动逻辑
  },
  
  // 全局数据
  globalData: {
    userInfo: null,
    apiBaseUrl: 'http://localhost:5000/api' // 后端API基础地址
  }
});
