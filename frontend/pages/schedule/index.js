Page({
    data: {
      // 生成最近7天的日期数据
      dateList: [],
      selectedIndex: 3, // 默认选中中间日期
      currentDate: ''
    },
  
    onLoad() {
      this.generateDateList();
    },
  
    // 生成最近7天日期
    generateDateList() {
      const dateList = [];
      const today = new Date();
      
      for (let i = -3; i <= 3; i++) {
        const date = new Date(today);
        date.setDate(today.getDate() + i);
        
        dateList.push({
          day: date.getDate(),
          month: date.getMonth() + 1,
          dateText: date.getDate().toString(),
          isToday: i === 0
        });
      }
      
      this.setData({
        dateList,
        currentDate: `${today.getMonth() + 1}月${today.getDate()}日`
      });
    },
  
    // 选择日期
    onDateTap(e) {
      const index = e.currentTarget.dataset.index;
      this.setData({ selectedIndex: index });
    },
  
    // 重要性排序按钮
    onSortTap() {
      wx.showToast({ title: '切换重要性排序', icon: 'none' });
      // 这里可以添加排序逻辑
    },
  
    // 加号按钮点击
    onAddTap() {
      wx.showToast({ title: '添加新事项', icon: 'none' });
      // 这里可以添加跳转或弹窗逻辑
    }
  });
