# 雏雁项目Flask后端配置文件
import os

# 基本配置
class Config:
    # 应用配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = True
    
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/chuyan_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # AI服务配置
    DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY') or 'your-deepseek-api-key'
    DEEPSEEK_API_URL = 'https://api.deepseek.com/v1/chat/completions'

# 开发环境配置
class DevelopmentConfig(Config):
    DEBUG = True

# 生产环境配置
class ProductionConfig(Config):
    DEBUG = False
    
# 测试环境配置
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/chuyan_test_db'

# 根据环境选择配置
env = os.environ.get('FLASK_ENV') or 'development'
if env == 'production':
    app_config = ProductionConfig()
elif env == 'testing':
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
