# 社区模块API路由
from flask import Blueprint, jsonify, request

# 创建蓝图对象
community_bp = Blueprint('community', __name__)

# 社区模块API路由示例

@community_bp.route('/posts')
def get_post_list():
    """获取帖子列表"""
    # 实际开发中，这里应该从数据库查询帖子列表
    return jsonify({
        "code": 200,
        "message": "获取帖子列表成功",
        "data": {
            "posts": [
                {
                    "id": 1,
                    "title": "如何学习Flask",
                    "content": "分享一下学习Flask的经验...",
                    "author": "张三",
                    "create_time": "2026-01-19 10:00:00",
                    "like_count": 12,
                    "comment_count": 5
                },
                {
                    "id": 2,
                    "title": "小程序开发心得",
                    "content": "小程序开发的一些心得体会...",
                    "author": "李四",
                    "create_time": "2026-01-18 15:30:00",
                    "like_count": 8,
                    "comment_count": 3
                }
            ]
        }
    })

@community_bp.route('/posts/<int:post_id>')
def get_post_detail(post_id):
    """获取帖子详情"""
    # 实际开发中，这里应该从数据库查询指定ID的帖子
    return jsonify({
        "code": 200,
        "message": "获取帖子详情成功",
        "data": {
            "id": post_id,
            "title": "帖子标题",
            "content": "帖子内容...",
            "author": "作者名",
            "create_time": "2026-01-19 10:00:00",
            "like_count": 10,
            "comment_count": 5,
            "comments": [
                {
                    "id": 1,
                    "author": "王五",
                    "content": "这个帖子很有用",
                    "create_time": "2026-01-19 11:00:00"
                }
            ]
        }
    })

@community_bp.route('/posts', methods=['POST'])
def create_post():
    """发布帖子"""
    # 实际开发中，这里应该解析请求数据并保存到数据库
    data = request.get_json()
    return jsonify({
        "code": 201,
        "message": "发布帖子成功",
        "data": {
            "id": 3,  # 实际应该是数据库返回的ID
            "title": data.get('title'),
            "content": data.get('content'),
            "author": "当前用户",
            "create_time": "2026-01-19 16:00:00",
            "like_count": 0,
            "comment_count": 0
        }
    })

@community_bp.route('/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    """点赞帖子"""
    # 实际开发中，这里应该处理帖子点赞逻辑
    return jsonify({
        "code": 200,
        "message": "点赞成功",
        "data": {
            "post_id": post_id,
            "like_count": 11  # 实际应该是更新后的点赞数
        }
    })
