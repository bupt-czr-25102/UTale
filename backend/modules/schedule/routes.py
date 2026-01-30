# 日程管理模块API路由
from flask import Blueprint, jsonify, request

# 创建蓝图对象
schedule_bp = Blueprint('schedule', __name__)

# 日程管理模块API路由示例

@schedule_bp.route('/')
def get_schedule_list():
    """获取日程列表"""
    # 实际开发中，这里应该从数据库查询日程列表
    return jsonify({
        "code": 200,
        "message": "获取日程列表成功",
        "data": {
            "schedules": [
                {
                    "id": 1,
                    "title": "项目会议",
                    "start_time": "2026-01-20 10:00:00",
                    "end_time": "2026-01-20 11:30:00",
                    "location": "会议室A",
                    "description": "讨论项目进度",
                    "reminder": 30  # 提前30分钟提醒
                },
                {
                    "id": 2,
                    "title": "学习Flask",
                    "start_time": "2026-01-20 14:00:00",
                    "end_time": "2026-01-20 16:00:00",
                    "location": "家中",
                    "description": "学习Flask后端开发",
                    "reminder": 15  # 提前15分钟提醒
                }
            ]
        }
    })

@schedule_bp.route('/<int:schedule_id>')
def get_schedule_detail(schedule_id):
    """获取日程详情"""
    # 实际开发中，这里应该从数据库查询指定ID的日程
    return jsonify({
        "code": 200,
        "message": "获取日程详情成功",
        "data": {
            "id": schedule_id,
            "title": "日程标题",
            "start_time": "2026-01-19 10:00:00",
            "end_time": "2026-01-19 11:00:00",
            "location": "地点",
            "description": "日程描述...",
            "reminder": 30
        }
    })

@schedule_bp.route('/', methods=['POST'])
def create_schedule():
    """创建新日程"""
    # 实际开发中，这里应该解析请求数据并保存到数据库
    data = request.get_json()
    return jsonify({
        "code": 201,
        "message": "创建日程成功",
        "data": {
            "id": 3,  # 实际应该是数据库返回的ID
            "title": data.get('title'),
            "start_time": data.get('start_time'),
            "end_time": data.get('end_time'),
            "location": data.get('location'),
            "description": data.get('description'),
            "reminder": data.get('reminder')
        }
    })

@schedule_bp.route('/<int:schedule_id>', methods=['PUT'])
def update_schedule(schedule_id):
    """更新日程"""
    # 实际开发中，这里应该更新数据库中的日程信息
    data = request.get_json()
    return jsonify({
        "code": 200,
        "message": "更新日程成功",
        "data": {
            "id": schedule_id,
            "title": data.get('title'),
            "start_time": data.get('start_time'),
            "end_time": data.get('end_time'),
            "location": data.get('location'),
            "description": data.get('description'),
            "reminder": data.get('reminder')
        }
    })
