// 日记详情页逻辑 - 团队模板适配版
Page({
  data: {
    selectDate: "",
    mood: "",
    content: ""
  },

  /**
   * 页面加载：接收编辑页/日历页传递的参数
   */
  onLoad(options) {
    this.setData({
      selectDate: options.date,
      mood: options.mood || "",
      content: options.content || ""
    });
  },

  /**
   * 重新编辑日记：跳回编辑页并带回原有数据
   */
  goToEdit() {
    const { selectDate, mood, content } = this.data;
    wx.navigateTo({
      url: `/pages/diary/edit/edit?date=${selectDate}&mood=${mood}&content=${content}`,
    });
  }
});
