# 雏雁项目Flask后端入口文件
from flask import Flask, jsonify
from flask_cors import CORS
import os

# 创建Flask应用实例
app = Flask(__name__)

# 配置CORS支持跨域请求
CORS(app, resources={r"/api/*": {"origins": "*"}})

# 加载配置文件
app.config.from_object('config')

# API路由注册
# 注意：实际开发中，这些路由应该放在各自的模块文件中
# 这里只是为了展示基础框架的结构

@app.route('/api')
def api_root():
    return jsonify({"message": "雏雁项目API服务正常运行"})

# AI日记模块API路由
from modules.diary.routes import diary_bp
app.register_blueprint(diary_bp, url_prefix='/api/diary')

# AI视频模块API路由
from modules.video.routes import video_bp
app.register_blueprint(video_bp, url_prefix='/api/video')

# 日程管理模块API路由
from modules.schedule.routes import schedule_bp
app.register_blueprint(schedule_bp, url_prefix='/api/schedule')

# 社区模块API路由
from modules.community.routes import community_bp
app.register_blueprint(community_bp, url_prefix='/api/community')

# 错误处理
@app.errorhandler(404)
def not_found(error):
    return jsonify({"code": 404, "message": "接口不存在"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"code": 500, "message": "服务器内部错误"}), 500

if __name__ == '__main__':
    # 启动Flask开发服务器
    app.run(host='0.0.0.0', port=5000, debug=True)
