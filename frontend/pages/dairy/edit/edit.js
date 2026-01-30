// 日记编辑页逻辑 - 团队模板适配版
Page({
  data: {
    selectDate: "", // 从日历页接收的日期
    mood: "",       // 选中的心情
    content: ""     // 日记内容
  },

  /**
   * 页面加载：接收日历页传递的日期
   */
  onLoad(options) {
    this.setData({
      selectDate: options.date
    });
  },

  /**
   * 选择心情标签
   */
  chooseMood(e) {
    this.setData({
      mood: e.currentTarget.dataset.mood
    });
  },

  /**
   * Markdown快捷按钮：自动添加语法（无需手动输入）
   */
  addMd(e) {
    const type = e.currentTarget.dataset.type;
    let newContent = this.data.content;
    switch (type) {
      case "bold": newContent += "** **"; break; // 加粗：**内容**
      case "italic": newContent += "* *"; break; // 斜体：*内容*
      case "list": newContent += "- "; break;    // 无序列表：- 内容
      case "line": newContent += "---\n"; break; // 分隔线：---
    }
    this.setData({ content: newContent });
  },

  /**
   * 获取输入框内容
   */
  getContent(e) {
    this.setData({
      content: e.detail.value
    });
  },

  /**
   * 提交日记：校验+跳转到详情页（传递所有参数）
   * 后续对接后端：在此处添加wx.request请求代码即可
   */
  submitDiary() {
    // 简单校验
    if (!this.data.mood) {
      wx.showToast({ title: "请选择今日心情~", icon: "none", duration: 1500 });
      return;
    }
    if (!this.data.content) {
      wx.showToast({ title: "请写下今日的内容吧~", icon: "none", duration: 1500 });
      return;
    }

    // 校验通过，提示并跳转到详情页
    wx.showToast({ title: "提交成功~", icon: "success", duration: 1000 });
    const { selectDate, mood, content } = this.data;
    wx.navigateTo({
      url: `/pages/diary/detail/detail?date=${selectDate}&mood=${mood}&content=${content}`,
    });
  }
});
