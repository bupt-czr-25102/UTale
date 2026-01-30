// AI日记日历首页逻辑 - 团队模板改造版
Page({
  data: {},

  /**
   * 点击日期跳【日记编辑页】（未写日记）
   * 传递选中的日期参数到编辑页
   */
  goToEdit(e) {
    const selectDate = e.currentTarget.dataset.date;
    wx.navigateTo({
      url: `/pages/diary/edit/edit?date=${selectDate}`,
    });
  },

  /**
   * 点击日期跳【日记详情页】（已写日记）
   * 传递选中的日期参数到详情页
   */
  goToDetail(e) {
    const selectDate = e.currentTarget.dataset.date;
    wx.navigateTo({
      url: `/pages/diary/detail/detail?date=${selectDate}`,
    });
  }
});
